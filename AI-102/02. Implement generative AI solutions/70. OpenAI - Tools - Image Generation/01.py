from openai import OpenAI
import base64

api_key=""
client=OpenAI(api_key=api_key)


response = client.responses.create(
    input="Generate an image of cats playing to the beat of the drums",
    tools=[{"type": "image_generation"}],
    model="gpt-5"
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]
    
if image_data:
    image_base64 = image_data[0]
    with open("cats.png", "wb") as f:
        f.write(base64.b64decode(image_base64))
