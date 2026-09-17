import ollama

model_name = 'llama3.2:3b'

print("=== Offline AI - Ghulam Rasool | Lahore PK ===")
print(f"Model:{model_name} - 100% Offline - Streaming")
print("Type 'exit' to quit\n")

while True:
    try:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Allah Hafiz! Project complete.")
            break
        
        if not user_input.strip():
            continue
            
        print("Bot: ", end="", flush=True)
        
        stream = ollama.chat(model=model_name, messages=[
            {'role': 'user', 'content': user_input}
        ], stream=True)
        
        for chunk in stream:
            print(chunk['message']['content'], end="", flush=True)
        
        print("\n")
        
    except KeyboardInterrupt:
        print("\nAllah Hafiz! Exiting...")
        break