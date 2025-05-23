import openai

def get_embeddings(text):
    '''
    Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
    Then, return a list of the embeddings.
    '''
    response = openai.Embed("text-embedding-ada-002", text)
    embeddings = response.embeddings
    return embeddings