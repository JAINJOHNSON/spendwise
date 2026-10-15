# pip install google-genai

from google import genai

api_key = "AQ.Ab8RN6JNnNmMQTXJ6wDYD_XCif36cqdDVNwouPVypt_qUfvkjQ"

#step1: authenticate

client = genai.Client(api_key=api_key)  #authentication 

prompt = "what is ai agent in simple words"

response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                    )

print(response.text)
