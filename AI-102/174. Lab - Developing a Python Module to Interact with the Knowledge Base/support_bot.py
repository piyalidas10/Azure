import requests

endpoint=""
api_key=""
headers={
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

def ask_question_answer(question: str):
    data={
        "question":question,
        "top":1        
    }

    response=requests.post(endpoint,headers=headers,json=data)
    result=response.json()
    return ["answers"][0]

print("💬 CloudXeus Support Bot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye! 👋")
        break
    answer = ask_question_answer(user_input)
    print(f"Bot: {answer}")
