# pip install google-genai

from google import genai

app_assistant_key = "A"

#step1: authenticate

client = genai.Client(app_assistant_key=app_assistant_key)  #authentication 

prompt = "what is ai agent in simple words"

response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                    )

print(response.text)
