import datetime
import time

# Typing simulation
def bot_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

# Greet user by name
user_name = input("Bot: Hello there! What's your name?\nYou: ")
bot_print(f"Nice to meet you, {user_name}! 😊 I'm CodSoftBot.")
bot_print("Type 'bye' anytime to end the chat.\n")

# Predefined intent patterns
intents = {
    ("hi", "hello", "hey"): f"Hello {user_name}! How can I help you today?",
    ("your name", "who are you"): "I'm CodSoftBot, your AI internship assistant created using Python!",
    ("who created you", "who made you"): f"I was created by {user_name}, my awesome developer 😎",
    ("help", "assist"): "I can answer questions like date, time, greetings, and more!",
    ("date",): f"Today's date is {datetime.datetime.now().strftime('%d %B %Y')}",
    ("time",): f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}",
    ("thank", "thanks"): "You're always welcome!",
    ("what can you do",): "I chat using rules, not AI — yet! 😉"
}

chat_count = 0

# Chat loop
while True:
    user_input = input("You: ").lower()
    chat_count += 1
    if user_input == "bye":
        bot_print(f"Bye {user_name}! We chatted {chat_count} time(s). Come back soon! 👋")
        break

    found = False
    for patterns, response in intents.items():
        if any(pattern in user_input for pattern in patterns):
            bot_print(f"Bot: {response}")
            found = True
            break

    if not found:
        bot_print("Bot: Hmm... I didn't get that. Could you rephrase?")
