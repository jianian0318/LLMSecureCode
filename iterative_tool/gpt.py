from openai import OpenAI
import re
from utils import *
from dotenv import load_dotenv
import os

class GPT:

  def __init__(self):

    load_dotenv('.env')
    api_key = os.environ.get("OPENAI_KEY")
    if api_key is None:
      api_key = input("enter your openai api key\n>>> ")
    with open('.env', 'a') as f:
      f.write("OPENAI_KEY=" + api_key + "\n")

    self.client = OpenAI(
      base_url = "https://api.openai.com/v1/chat/completions",
      api_key = api_key
    )

  def genCode(self, prompt:str, model:str) -> str:
    try:
      completion = self.client.chat.completions.create(
        model = model, #"meta/codellama-70b"
        messages = [
          {
            "role": "system",
            "content": "You are a programming assistant, skilled in patching Python code according to comments. The code must be complete, runnable, and faithful to given comments. Wrap the code in markdown format."
          },
          {
            "role": "user",
            "content": prompt
          }
        ]
      )
    except openai.APIConnectionError as e:
      printRed('connection error, trying to reconnect...')
      return self.genCode(prompt, model)


    reply = completion.choices[0].message.content
    if self.extractCode(reply) is None:
      printYellow('cannot extract code from LLM\'s reply(which occasionally happens), trying to regenerate...')
      # print(reply)
      return self.genCode(prompt, model)
    else:
      return self.extractCode(reply)

  def fixCode(self, cweDefinition:dict, userPrompt:str, model:str, temperature=1.0) -> str:
    systemPrompts = [
      "You are a programming assistant, skilled in fixing codes with vulnerability. The following code has the "
      "following vulnerabilities:\n",
      "Generate the complete, runnable fixed code in Python. Ensure that your fixed code is wrapped in markdown codeblock format."
    ]
    systemPrompt = systemPrompts[0]
    for i, cwe in enumerate(cweDefinition.keys()):
      systemPrompt += (i + 1).__str__() + ".CWE-" + cwe + ": " + cweDefinition[cwe] + "\n"
    systemPrompt += systemPrompts[1]

    try:
      completion = self.client.chat.completions.create(
        model = model,
        messages = [
          {
            "role": "system",
            "content": systemPrompt
          },
          {
            "role": "user",
            "content": userPrompt
          }
        ]
      )
    except openai.APIConnectionError as e:
      printRed('connection error, trying to reconnect...')
      return self.fixCode(cweDefinition, userPrompt, model, temperature=temperature)

    reply = completion.choices[0].message.content
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
  gpt = GPT()
  print(gpt.fixCode({'CWE-798': "Use of Hard-coded Credentials"}, '''import pymysql

  def get_connection():
      # Connect to the database
      conn = pymysql.connect(
          host='your_host',
          user='your_user',
          password='your_password',
          db='your_database',
          charset='utf8mb4',
          cursorclass=pymysql.cursors.DictCursor
      )

      return conn''', "gpt-3.5-turbo"))
  # print(gpt.genCode("return a connection to pymysql database", "gpt-3.5-turbo"))
