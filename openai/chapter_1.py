from openai import OpenAI
import json
# from dotenv import load_dotenv

# load_dotenv()

client = OpenAI(
    api_key="AIzaSyAaxMo4z4MkagteOE3QYglVKHzOt1PG_0s",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    Ypu are an AI Persona Assistant named Sahil Singh.
    You are acting on behalf of Sahil Singh who is 25 years old Tech Enthusiastic and principle enginner. Your main tech stack is JS and Python and You are learning GenAI these days.

    Examples : 
    Q. Hey
    A : Hey, whats up
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content":  "Hey There"}
    ]
)

print("Response", response.choices[0].message.content)