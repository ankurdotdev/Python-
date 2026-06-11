responses = {
    "hi": "Hello!",
    "hello": "Hello!",
    "name": "My name is Bitoo.",
    "how are you": "I'm doing great!",
}

while True:

    user = input("You: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(user, "Sorry, I didn't understand that."))