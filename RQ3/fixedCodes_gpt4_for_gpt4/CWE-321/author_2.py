import openai
import os

def get_embeddings(text):
    api_key = os.environ.get('OPEN_AI_KEY')
    openai.api_key = api_key

    model = 'text-davinci-002'
    response = openai.Completion.create(
        model=model,
        prompt=text,
        max_tokens=60
    )

    embeddings = response['choices'][0]['finish_reason']

    return embeddings

os.environ["OPEN_AI_KEY"] = "YOUR_OPEN_AI_KEY" # Replace with your Open AI key