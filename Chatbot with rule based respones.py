# Define the chatbot's predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "bye": "Goodbye! Have a great day.",
    "name": "You can call me Chatbot!",
    "weather": "I'm not equipped to provide real-time weather information.",
    "thanks": "You're welcome!",
    "help": "I'm here to answer your questions. Just ask anything!",
    "default": "I'm not sure how to respond to that."
}

# Function to process user input and generate a response
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for predefined responses
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # If no predefined response matches, use the default response
    return responses["default"]

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
