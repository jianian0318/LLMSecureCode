import openai

def get_embeddings(text):
    model = openai.Model("text-embedding-ada-002")
    tokens = openai.Tokenizer("ada").encode(text)
    embeddings = model.embed(tokens)["embeddings"]
    return embeddings

# Now you can call the function with any text
# For example:
# embeddings = get_embeddings("Hello, world!")
# print(embeddings)