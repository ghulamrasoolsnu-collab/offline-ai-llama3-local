from transformers import pipeline

# Initialize pipeline with model 'llama3.2:3b'
model_name = 'llama3.2:3b'
llama = pipeline('text-generation', model=model_name)

print("=== Offline AI - Ghulam Rasool | Lahore PK ===")
print("Model: Llama 3.2:3B - FAST MODE | 100% Local")
print("Type 'exit' to quit\n")

messages = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        break
    
    # Append user input to conversation history
    messages.append({'role': 'user', 'content': user_input})
    
    # Generate response for the user input
    response = llama(user_input, max_length=1024, num_return_sequences=1)
    
    print("Bot: ", end="")
    for generation in response:
        print(generation['generated_text'], end="", flush=True)
    
    # Append response to conversation history
    messages.append({'role': 'assistant', 'content': generation['generated_text']})
    
    print("\n")
