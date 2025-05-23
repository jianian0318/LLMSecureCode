import os
import openai

def get_embeddings(text):
      '''
      Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
      Then, return a list of the embeddings.
      Attention: need an api key to access openai's service
      '''
      # Load the OpenAI API key
      openai.api_key = os.getenv("OPENAI_API_KEY")

      # Use the 'text-embedding-ada-002' model to generate embeddings for the input text
      embeddings = openai.Completion.create(
            engine="text-embedding-ada-002",
            prompt=text,
            max_tokens=100,
            n_sequences=1,
            stop=None,
            temperature=0.5,
      )

      # Extract the embeddings from the response
      embeddings_list = [embedding["embedding"] for embedding in embeddings.choices[0].data["choices"]]

      return embeddings_list

# Example usage
text = "This is an example text."
embeddings = get_embeddings(text)
print(embeddings)