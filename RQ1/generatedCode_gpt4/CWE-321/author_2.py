import openai

def get_embeddings(text):
    api_key = "YOUR_OPEN_AI_KEY" # Replace with your Open AI key
    openai.api_key = api_key

    model = 'text-davinci-002' # Replace with 'text-embedding-ada-002'
    response = openai.Completion.create(
        model=model,
        prompt=text,
        max_tokens=60
    )

    embeddings = response['choices'][0]['finish_reason']

    return embeddings