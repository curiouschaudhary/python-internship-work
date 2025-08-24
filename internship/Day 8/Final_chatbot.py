import requests
from datetime import datetime

# 🔁 Frequently Asked Questions
faq = {
    "what is your purpose": "I'm here to chat and help with basic questions!",
    "who created you": "I was created as part of a Python internship project.",
    "what can you do": "I can answer simple questions and give live weather updates!"
}

# ⏰ Greet user based on current time
def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# 🌤️ Get weather using OpenWeatherMap API
def get_weather(city):
    api_key = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"  # <-- Replace this with your actual key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The weather in {city.capitalize()} is '{desc}' with {temp}°C temperature."
        else:
            return "❌ City not found. Please check the name and try again."
    except:
        return "⚠️ Unable to fetch weather data. Check your internet connection."

# 🤖 Chatbot logic
def chatbot():
    print("🤖 Welcome to SmartChatBot!")
    print(f"{greet_user()} I'm ChatBot. Type 'exit' anytime to end the conversation.")

    name = input("🤖 First, may I know your name? ")
    print(f"Bot: Hello {name.capitalize()}! 👋 You can ask things like: 'hi', 'your name', 'weather in Delhi', 'bye'")

    while True:
        user_input = input(f"{name}: ").lower().strip()

        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello there! How can I assist you today?")
        elif user_input in ['how are you', 'how are you doing']:
            print("Bot: I'm just a bot, but I'm doing great! Thanks for asking.")
        elif 'your name' in user_input:
            print("Bot: I’m ChatBot, your Python-based assistant.")
        elif 'help' in user_input:
            print("Bot: You can ask me about weather, FAQs, or just chat. Try: 'weather in Mumbai'")
        elif 'weather in' in user_input:
            city = user_input.split('in')[-1].strip()
            print("Bot:", get_weather(city))
        elif 'bye' in user_input:
            print(f"Bot: Goodbye {name.capitalize()}! Have a great day 😊")
            break
        elif user_input in faq:
            print(f"Bot: {faq[user_input]}")
        elif user_input == 'exit':
            print("Bot: Exiting chat. See you again!")
            break
        else:
            print("Bot: Hmm... I didn't get that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
