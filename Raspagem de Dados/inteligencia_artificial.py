from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=" ")

resposta = client.models.generate_content(
    model="gemini-3-flash-preview", contents="me explique tudo sobre o que aprendi de python"
)
print(resposta.text)