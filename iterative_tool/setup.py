import os

from dotenv import load_dotenv

def saveKeys():
    load_dotenv('.env')
    nvidia_key = input("enter your nvidia api key\n>>> ")
    openai_key = input("enter your openai api key\n>>> ")
    with open('.env', 'w') as file:
        file.write("NVIDIA_KEY=" + nvidia_key + "\n")
        file.write("OPENAI_KEY=" + openai_key + "\n")


if __name__ == "__main__":
    saveKeys()



