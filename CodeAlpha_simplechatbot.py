def chatbot():
    print("=== Simple Rule-Based Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").strip().lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hi there!")

        elif "how are you" in user:
            print("Bot: I'm fine, thanks! How can I help you?")

        elif "your name" in user:
            print("Bot: I am a simple Python chatbot.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()
