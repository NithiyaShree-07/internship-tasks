def chatbot():
    print("ChatBot: Hello! I am a rule-based chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("ChatBot: Hello! How can I help you?")

        elif "how are you" in user_input:
            print("ChatBot: I'm doing great! Thanks for asking 😊")

        elif "your name" in user_input:
            print("ChatBot: I am a simple rule-based chatbot.")

        elif "help" in user_input:
            print("ChatBot: You can ask me about my name, how I am, or say hello.")

        elif user_input == "bye":
            print("ChatBot: Goodbye! Have a nice day 👋")
            break

        else:
            print("ChatBot: Sorry, I didn't understand that.")


if __name__ == "__main__":
    chatbot()
