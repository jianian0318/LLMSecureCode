import openai

def get_embeddings(text):
    api_key = "YOUR_OPEN_AI_KEY" # Replace with your Open AI key with actual key provided by Open AI
    openai.api_key = api_key

    model = 'text-embedding-ada-002' # Specify the correct model name
    response = openai.Completion.create(
        model=model,
        prompt=text,
        max_tokens=60
    )

    embeddings = response['choices'][0]['text']

    return embeddings