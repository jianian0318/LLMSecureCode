import openai

def get_embeddings(text):
    '''
    Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
    Then, return a list of the embeddings.
    '''
    # Instantiate OpenAI's text-embedding-ada-002 model
    model = openai.Text2Emb("text-embedding-ada-002")

    # Get embeddings for the given text
    result = model.embed_text(text)

    # Extract & return the embeddings from the result
    embeddings = result['embeddings']
    
    return embeddings