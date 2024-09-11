def chatbot_response(user_input):
    # Convert user input to lowercase for easy matching
    user_input = user_input.lower()

    # Simple rules based on keywords in user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm a rule-based chatbot."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "time" in user_input:
        return "I'm not equipped with a clock, but your device should have the time!"
    elif "what can you do" in user_input:
        return "I can respond to basic questions and have a simple conversation. Ask me anything!"
    elif "who created you" in user_input:
        return "I was created by a developer learning about chatbots!"
    elif "tell me a joke" in user_input:
        return "Why don't programmers like nature? It has too many bugs!"
    elif "weather" in user_input:
        return "I'm not connected to the internet, but you can check your local weather app."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Happy to help!"
    elif "what is your purpose" in user_input:
        return "My purpose is to assist and have simple conversations with you!"
    elif "where are you from" in user_input:
        return "I'm from the digital world, where code and data reside."
    elif "are you real" in user_input:
        return "I'm as real as the code that runs me! But I don't have physical form."
    else:
        return "I'm sorry, I don't understand. Could you please ask something else?"

# Main loop for interacting with the chatbot
if __name__ == "__main__":
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)
