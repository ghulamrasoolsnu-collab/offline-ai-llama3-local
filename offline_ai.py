import ollama
print("Ghulam Rasool | Offline AI - Llama 3.1:8B | 100% Local")
print("Type 'exit' to quit\n")
while True:
    q = input("You: ")
    if q.lower() in ['exit','quit','bye']:
        print("Bot: Allah Hafiz!")
        break
    print("Bot: ", end="")
    stream = ollama.chat(model='llama3.1:8b', messages=[{'role':'user','content':q}], stream=True)
    for c in stream:
        print(c['message']['content'], end="", flush=True)
    print("\n")