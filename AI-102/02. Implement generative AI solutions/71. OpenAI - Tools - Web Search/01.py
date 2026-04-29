from openai import OpenAI
import time

api_key=""
client=OpenAI(api_key=api_key)

start = time.time()
response = client.responses.create(
    input="What's the latest news today in the world of AI",
    tools=[{"type": "web_search_preview"}],
    model="gpt-5"
)
end = time.time() 
elapsed = end - start

print("Response time: %.2f seconds" % elapsed)
print(response.output_text)
