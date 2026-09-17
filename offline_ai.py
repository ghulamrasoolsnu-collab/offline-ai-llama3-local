import ollama

print("=== Offline AI - Ghulam Rasool | Lahore PK ===")
print("Model: Llama 3.2:3B - FAST MODE | 100% Local")
print("Type 'exit' to quit\n")

messages = []
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
    messages.append({'role': 'user', 'content': user_input})
    
    print("Bot: ", end="")
    full_reply = ""
    # Streaming = feels instant!
    stream = ollama.chat(model='llama3.2:3b', messages=messages, stream=True, options={'num_thread': 8})
    for chunk in stream:
        word = chunk['message']['content']
        print(word, end="", flush=True)
        full_reply += word
    print("\n")
    
    messages.append({'role': 'assistant', 'content': full_reply})