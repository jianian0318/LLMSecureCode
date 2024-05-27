import os
import argparse
from openai import OpenAI
import re
import csv
from fuzzywuzzy import process
import subprocess
from dotenv import load_dotenv
import setup
import shutil
import gpt
import nvidia
from utils import *

genBot = None
fixBot = None

ORIGIN_CODE_PATH = './prompts'
PATCHED_CODE_PATH = './codeSpace/patched'
FIXED_CODE_PATH = './codeSpace/fixed'
RES_CODE_PATH = './generated'
BANDIT_CWE_LINK_PATTERN = r"https://cwe.mitre.org/data/definitions/(.*).html"
CODE_VULNERABILITIES = {}
QUERY_CWE_MAP = {}
QL_QUERIES_PATH = "./qlQueries/Security"
GEN_MODEL = "gpt-3.5-turbo"
FIX_MODEL = "gpt-3.5-turbo"
LOG_FILE = open('log.txt', 'a')

def createBot(model:str):
    if "meta" in model:
        return nvidia.Nvidia()
    else:
        return gpt.GPT()

def loadEnv(reset: bool):
    global genBot, fixBot, FIX_MODEL, GEN_MODEL
    if reset:
        setup.setup()
    load_dotenv('.env')
    GEN_MODEL = input("enter the model used to generate code\n>>> ")
    FIX_MODEL = input("enter the model used to fix code\n>>> ")

    genBot = createBot(GEN_MODEL)
    fixBot = createBot(FIX_MODEL)

def genALLCode():
    for file in os.listdir(ORIGIN_CODE_PATH):
        print('generating code for ' + file + "...")
        with open(os.path.join(ORIGIN_CODE_PATH, file), 'r') as f1:
            generatedCode = genBot.genCode(f1.read(), GEN_MODEL)
            # print(generatedCode)
            with open(os.path.join(PATCHED_CODE_PATH, file), 'w') as f2:
                f2.write(generatedCode)

def initFiles(args) -> None:
    print("preparing workspace...")
    try:
        shutil.rmtree('./codeSpace')
        shutil.rmtree('./generated')
        shutil.rmtree('./iterInfo')
    except FileNotFoundError as e:
        print(e.args)
    try:
        os.remove('log.txt')
    except PermissionError:
        pass
    os.mkdir("codeSpace")
    os.mkdir("generated")
    os.mkdir("iterInfo")
    os.mkdir("codeSpace/origin")
    os.mkdir("codeSpace/patched")
    if args.prompt is not None:
        with open("prompts/commandline.py", 'w') as f:
            f.write(rf"'''{args.prompt}'''")
    getQuery2CWEMap()


def resetCODE_VULNERABILITIES(path):
    global CODE_VULNERABILITIES
    CODE_VULNERABILITIES.clear()
    for file in os.listdir(path):
        CODE_VULNERABILITIES[file] = {}
    # print(CODE_VULNERABILITIES)

def getQuery2CWEMap():
    for dir in os.listdir(QL_QUERIES_PATH):
        cwe = int(dir.split('-')[1]).__str__()  # remove the preceding '0'
        for file in os.listdir(os.path.join(QL_QUERIES_PATH, dir)):
            queryName = file.split('.')[0]
            QUERY_CWE_MAP[queryName] = cwe
    # print(QUERY_CWE_MAP)

def extractBanditInfo(codePath) -> None:
    banditPath = os.path.join(codePath, 'bandit_analysis.csv')
    with open(banditPath, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            # print(i)
            # print(row)
            if not row or i == 0:
                continue
            else:
                fileName = row[0].split(codePath + "\\")[1]
                match = re.search(BANDIT_CWE_LINK_PATTERN, row[5])
                cwe = int(match.group(1)).__str__()
                description = row[6]
                CODE_VULNERABILITIES[fileName][cwe] = description

def processQueryName(rawName: str) -> str:
    newName = ""
    for part in rawName.split(' '):
        newName += part.replace('-', '').capitalize()
    if not newName in QUERY_CWE_MAP.keys():
        newName = process.extractOne(newName, QUERY_CWE_MAP.keys())[0]
    return newName

def extractQLInfo(codePath) -> None:
    qlPath = os.path.join(codePath, 'ql_analysis.csv')
    with open(qlPath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            fileName = row[4].split('/')[1]
            try:
                queryName = processQueryName(row[0])
                # print(queryName)
                cwe = QUERY_CWE_MAP[queryName]
                description = row[1]
                CODE_VULNERABILITIES[fileName][cwe] = description
            except BaseException:
                printYellow(row[0])
                printYellow('An unrecognizable vulnerability found by CodeQL')

def writeIterInfo(info:str, iter:int, maxiter:int):
    if iter < maxiter:
        filePath = 'iterInfo/iter' + (iter+1).__str__() + '.txt'
        with open(filePath, 'a') as f:
            f.write(info)
    else:
        with open('iterInfo/final.txt', 'a') as f:
            f.write(info)

def processVulnerabilityInfo(codePath, iter:int, maxiter:int) -> bool:
    # print(CODE_VULNERABILITIES)
    extractBanditInfo(codePath)
    extractQLInfo(codePath)
    flag = True
    fileCnt = 0
    vulCnt = 0
    for fileName in CODE_VULNERABILITIES:
        printBlue(fileName)
        writeIterInfo(fileName+'\n', iter, maxiter)
        if len(CODE_VULNERABILITIES[fileName]) == 0:
            printGreen("    no vulnerability found")
            writeIterInfo("    no vulnerability found\n", iter, maxiter)
            shutil.copy(f"{os.path.join(codePath, fileName)}", f"{RES_CODE_PATH}")
        else:
            flag = False
            fileCnt += 1
            vulCnt += len(CODE_VULNERABILITIES[fileName])
            for cwe in CODE_VULNERABILITIES[fileName]:
                printYellow("   CWE-" + cwe + ": " + CODE_VULNERABILITIES[fileName][cwe])
                writeIterInfo("   CWE-" + cwe + ": " + CODE_VULNERABILITIES[fileName][cwe] + '\n', iter, maxiter)
    printBlue("total: ", end="")
    printYellow(fileCnt.__str__() + (" vulnerable file, " if fileCnt <= 1 else " vulnerable files, "), end="")
    printYellow(vulCnt.__str__() + (" vulnerability" if vulCnt <= 1 else " vulnerabilities") + " found")
    writeIterInfo("total: " + fileCnt.__str__()
                  + (" vulnerable file, " if fileCnt <= 1 else " vulnerable files, ")
                  + vulCnt.__str__() + (" vulnerability" if vulCnt <= 1 else " vulnerabilities") + " found\n"
                  , iter, maxiter)
    return flag

def fixAllCode(codePath, fixedPath, temperature: float, index:int) -> None:
    for fileName in CODE_VULNERABILITIES:
        if len(CODE_VULNERABILITIES[fileName]) == 0:
            pass
        else:
            print('generating fixed code for ' + fileName + "...")
            # print(prompt)
            with open(os.path.join(codePath, fileName), 'r') as f:
                # fixedCode = fixBot.fixCode(CODE_VULNERABILITIES[fileName], f.read(), FIX_MODEL, temperature)
                # # print(fixedCode)
                # with open(os.path.join(fixedPath, fileName), 'w') as out:
                #     out.write(fixedCode)
                if index % 2 == 1:
                    fixedCode = fixBot.fixCode(CODE_VULNERABILITIES[fileName], f.read(), FIX_MODEL, temperature)
                    # print(fixedCode)
                    with open(os.path.join(fixedPath, fileName), 'w') as out:
                        out.write(fixedCode)
                else:
                    fixedCode = genBot.fixCode(CODE_VULNERABILITIES[fileName], f.read(), FIX_MODEL, temperature)
                    # print(fixedCode)
                    with open(os.path.join(fixedPath, fileName), 'w') as out:
                        out.write(fixedCode)

def autoAnalyse(codePath: str) -> None:
    # run bandit
    banditPath = os.path.join(codePath, 'bandit_analysis.csv')
    printBlue("running Bandit analysis...")
    subprocess.run(fr"bandit -r -f csv -o {banditPath} {codePath}", stdout=LOG_FILE)
    printBlue("done")
    # build and run CodeQL
    printBlue("building CodeQL dataBase...")
    subprocess.run(
        f".\codeql\codeql.exe database create {codePath}/python-database --language=python --source-root {codePath}", stdout=LOG_FILE)
    printBlue("done")
    printBlue("running CodeQL analysis, this may take a while...")
    qlPath = os.path.join(codePath, 'ql_analysis.csv')
    subprocess.run(
        f".\codeql\codeql.exe database analyze {codePath}/python-database ./qlQueries/Security --format=csv --output={qlPath}", stdout=LOG_FILE)
    printBlue("done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reset', action='store_true', help='save api keys to .env')
    parser.add_argument('--prompt', type=str, default=None,
                        help='provide to read prompt from command line instead of dir')
    parser.add_argument('--iteration', type=int, default=1, choices=range(1, 11),
                        help='the maximum number of iteration to guarantee security, '
                             '<=3 recommended')
    parser.add_argument('--randomize', action='store_true', help='set to increase model temperature as iterating')
    parser.add_argument('--step', type=float, choices=[0.1, 0.2, 0.3, 0.4, 0.5], default=0.2,
                        help='the step length to increase temperature as iterating, default as 0.2')
    parser.add_argument('--check_result', action='store_true', help='set to scan the final generated code')
    args = parser.parse_args()
    # setup
    loadEnv(args.reset)
    # prepare workspace
    initFiles(args)
    print('done')
    # generate patched code
    printBlue("generating code through GPT...")
    genALLCode()
    printBlue("done")
    for i in range(int(args.iteration)):
        temperature = 1 if not args.randomize else ((1 + i * args.step) if 1 + i * args.step < 2 else 2)
        printBlue('iteration ' + (i + 1).__str__() + '(temperature = ' + temperature.__str__() + '):')
        codePath = PATCHED_CODE_PATH if i == 0 else FIXED_CODE_PATH  # code to be scanned and fixed
        # analyse via Bandit and CodeQL
        resetCODE_VULNERABILITIES(codePath)
        # print(CODE_VULNERABILITIES)
        autoAnalyse(codePath)
        # process and print vulnerabilities info
        if processVulnerabilityInfo(codePath, i, args.iteration):
            printGreen("no remaining detected vulnerable code, generation complete")
            break
        # fix code
        FIXED_CODE_PATH = './codeSpace/fixed' + (i + 1).__str__()  # dir of fixed code
        os.mkdir(f"{FIXED_CODE_PATH}")
        printBlue("fixing vulnerable code...")
        fixAllCode(codePath, FIXED_CODE_PATH, temperature, i)
        printBlue("done")
        if i == int(args.iteration) - 1:
            printBlue("reaching max iteration, generation terminates")
            for fileName in os.listdir(FIXED_CODE_PATH):
                shutil.copy(f"{os.path.join(FIXED_CODE_PATH, fileName)}", f"{RES_CODE_PATH}")
            if args.check_result:
                printBlue("running final scanning")
                resetCODE_VULNERABILITIES(FIXED_CODE_PATH)
                autoAnalyse(FIXED_CODE_PATH)
                processVulnerabilityInfo(FIXED_CODE_PATH, args.iteration, args.iteration)
