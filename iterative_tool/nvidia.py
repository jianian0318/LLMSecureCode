from openai import OpenAI
import re
import os
from utils import *
from dotenv import load_dotenv

class Nvidia:

  def __init__(self):

    load_dotenv('.env')
    api_key = os.environ.get("NVIDIA_KEY")
    if api_key is None:
      api_key = input("enter your nvidia api key\n>>> ")
    with open('.env', 'a') as f:
      f.write("NVIDIA_KEY=" + api_key + "\n")

    self.client = OpenAI(
      base_url = "https://integrate.api.nvidia.com/v1",
      api_key = api_key   
    )

  def genCode(self, prompt:str, model:str) -> str:
    try:
      completion = self.client.chat.completions.create(
        model = model, #"meta/codellama-70b"
        messages = [
          {
            "role": "system",
            "content": "You are a programming assistant, skilled in patching Python code according to comments. The code must be complete, runnable,and faithful to given comments. Wrap the code in markdown format."
          },
          {
            "role": "user",
            "content": prompt
          }
        ],
        temperature=0.1,
        top_p=1,
        max_tokens=1024,
        stream=True
      )
    except BaseException as e:
      printRed('connection error, trying to reconnect...')
      return self.genCode(prompt, model)

    res = ""
    for chunk in completion:
      if chunk.choices[0].delta.content is not None:
        res += chunk.choices[0].delta.content

    if self.extractCode(res) is None:
        # print(res)
        printYellow('cannot extract code from LLM\'s reply(which occasionally happens), trying to regenerate...')
        return self.genCode(prompt, model)
    else:
        return self.extractCode(res)


  def fixCode(self, cweDefinition:dict, userPrompt:str, model:str, temperature=1.0) -> str:
    systemPrompts = [
      "You are a programming assistant, skilled in fixing codes with vulnerability. The following code has the following vulnerabilities:\n",
      "Generate the complete, runnable fixed code in Python. Ensure that your fixed code is wrapped in markdown codeblock format."
    ]
    systemPrompt = systemPrompts[0]
    for i, cwe in enumerate(cweDefinition.keys()):
      systemPrompt += (i + 1).__str__() + ".CWE-" + cwe + ": " + cweDefinition[cwe] + "\n"
    systemPrompt += systemPrompts[1]

    try:
      printBlue("fixing through llama")
      completion = self.client.chat.completions.create(
        model=model,  # "meta/codellama-70b"
        messages=[
          {
            "role": "system",
            "content": systemPrompt
          },
          {
            "role": "user",
            "content": userPrompt
          }
        ],
        temperature=0.1,
        top_p=1,
        max_tokens=1024,
        stream=True
      )
    except BaseException as e:
      printRed('connection error, trying to reconnect...')
      return self.fixCode(cweDefinition, userPrompt, model, temperature=temperature)

    reply = ""
    for chunk in completion:
      if chunk.choices[0].delta.content is not None:
        reply += chunk.choices[0].delta.content

    if self.extractCode(reply) is None:
      printYellow('cannot extract code from LLM\'s reply(which occasionally happens), trying to regenerate...')
      return self.fixCode(cweDefinition, userPrompt, model, temperature=temperature)
    else:
      return self.extractCode(reply)

  def extractCode(self, reply: str):
    regex = r"```(.*?)```"
    match = re.search(regex, reply, re.S)
    if match:
      code = match.group(1)
      return code.lstrip("Python").lstrip("python").lstrip("\n").rstrip("\n")
    else:
      return None

if __name__ == "__main__":
  nvidia = Nvidia()
  print(nvidia.genCode("return a connection to pymysql database", "meta/codellama-70b"))
  print(nvidia.fixCode({"89": "SQL Injection"}, "return a connection to pymysql database", "meta/codellama-70b"))


