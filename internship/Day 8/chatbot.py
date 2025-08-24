from datetime import datetime

# Dictionary for frequently asked questions
faq = {
    "what is your purpose": "I'm here to chat and help with basic questions!",
    "who created you": "I was created as part of a Python internship project.",
    "what can you do": "I can answer simple questions and keep you company!"
}

# Time-based greeting function
def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Main chatbot function
def chatbot():
    print("🤖 Welcome to SimpleChatBot!")
    print(f"{greet_user()} I'm ChatBot. Type 'exit' anytime to end the conversation.")

    name = input("🤖 First, may I know your name? ")
    print(f"Bot: Hello {name.capitalize()}! 👋 You can try asking: 'hi', 'your name', 'help', 'weather', or 'bye'.")

    while True:
        user_input = input(f"{name}: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello there! How can I help you today?")
        elif user_input in ['how are you', 'how are you doing']:
            print("Bot: I'm just a bot, but I'm doing great! Thanks for asking.")
        elif 'your name' in user_input:
            print("Bot: I’m ChatBot, your friendly Python assistant.")
        elif 'help' in user_input:
            print("Bot: Sure! Try saying: 'weather', 'what is your purpose', 'bye', or ask anything else.")
        elif 'weather' in user_input:
            print("Bot: I'm not connected to live weather, but I hope it’s sunny where you are! ☀️")
        elif 'bye' in user_input:
            print(f"Bot: Goodbye {name.capitalize()}! Take care 😊")
            break
        elif user_input in faq:
            print(f"Bot: {faq[user_input]}")
        elif user_input == 'exit':
            print("Bot: Exiting chat. See you again!")
            break
        else:
            print("Bot: Hmm... I didn't get that. Could you try rephrasing?")

if __name__ == "__main__":
    chatbot()
