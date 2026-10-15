# pip install google-genai

from google import genai

api_key = "A"

#step1: authenticate

client = genai.Client(api_key)  #authentication 

prompt = "what is ai agent in simple words"

response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                    )

print(response.text)
