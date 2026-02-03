from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(
    api_key="AIzaSyAWlUj7i-YQ7mWY-98vf27Fkcf9Pe27Lsc"
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="hello, i am sahil"
)
print(response.text)