from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(
    api_key="AIzaSyAWlUj7i-YQ7mWY-98vf27Fkcf9Pe27Lsc",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role" : "user", "content" : "hey, i am sahil, who are you and whats your name?"}
    ]
)

print(response.choices[0].message.content)