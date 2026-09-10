"""
CodeAlpha Internship — Task 4: Basic Rule-Based Chatbot
Author: Aaron Baidoo (RoniKid)
Description: A simple rule-based chatbot that responds to common greetings,
             questions, and farewells using keyword matching.
"""

import random

# ── Response table ─────────────────────────────────────────────────────────────
# Each key is a tuple of trigger keywords. The chatbot checks if ANY keyword
# appears in the user's input (case-insensitive). The value is a list of
# possible replies — one is chosen at random so the bot feels less robotic.

RESPONSES = {
    ("hello", "hi", "hey", "howdy", "hiya"): [
        "Hey there! 👋 How can I help you today?",
        "Hi! Great to see you.",
        "Hello! What's on your mind?",
    ],
    ("how are you", "how are u", "how r you", "what's up", "wassup"): [
        "I'm doing great, thanks for asking! 😊",
        "All good on my end! How about you?",
        "Running smoothly! What can I do for you?",
    ],
    ("your name", "who are you", "what are you", "are you a bot", "are you ai"): [
        "I'm a simple rule-based chatbot built for the CodeAlpha internship! 🤖",
        "Just a humble bot — nothing fancy. I was coded in Python!",
        "They call me ChatBot 9000... or just ChatBot. Either works.",
    ],
    ("what can you do", "help", "commands", "options"): [
        "I can respond to greetings, answer simple questions, tell jokes, and say goodbye!",
        "Try asking me how I am, for a joke, or just say hi!",
    ],
    ("joke", "funny", "laugh", "make me laugh", "tell me a joke"): [
        "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the programmer quit? Because they didn't get arrays! 😂",
        "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
        "I told my computer I needed a break. Now it won't stop sending me vacation ads.",
    ],
    ("time", "what time", "current time"): [
        "I don't have a clock, but your device does! 🕐",
        "Check the top of your screen — I'm timeless! ⏰",
    ],
    ("weather", "temperature", "rain", "sunny"): [
        "I can't check the weather, but I hope it's nice where you are! ☀️",
        "No weather module installed (yet). Try a weather app!",
    ],
    ("thank", "thanks", "thank you", "thx", "appreciate"): [
        "You're very welcome! 😊",
        "Happy to help!",
        "Anytime! That's what I'm here for.",
    ],
    ("bye", "goodbye", "see you", "later", "cya", "exit", "quit"): [
        "Goodbye! Take care 👋",
        "See you later! Come back anytime.",
        "Bye! It was nice chatting with you. 😊",
    ],
    ("who made you", "who built you", "who created you", "who coded you"): [
        "I was built by Aaron Baidoo (RoniKid) as part of a CodeAlpha Python internship! 🇬🇭",
        "RoniKid coded me — a Computer Engineering student at GCTU, Ghana. 💪",
    ],
    ("ghana", "gctu", "accra"): [
        "Ghana! Great country. 🇬🇭 My creator is from there too!",
        "GCTU — Ghana Communication Technology University. Solid engineering school!",
    ],
}

# Fallback replies when no keyword matches
FALLBACKS = [
    "Hmm, I'm not sure how to respond to that. Try something else!",
    "I didn't quite catch that. Could you rephrase?",
    "That's a bit beyond my rule book! Try asking something simpler.",
    "Interesting... but I don't have a reply for that yet. 🤔",
]

# Keywords that signal the user wants to exit
EXIT_KEYWORDS = {"bye", "goodbye", "see you", "later", "cya", "exit", "quit"}


def get_response(user_input: str) -> tuple[str, bool]:
    """
    Match user_input against the response table.
    Returns (reply_text, should_exit).
    """
    text = user_input.strip().lower()

    # Check if user wants to quit
    if any(keyword in text for keyword in EXIT_KEYWORDS):
        # Still pick a proper goodbye reply
        for keywords, replies in RESPONSES.items():
            if any(kw in text for kw in keywords if kw in EXIT_KEYWORDS):
                return random.choice(replies), True
        return "Goodbye! 👋", True

    # Search all keyword groups
    for keywords, replies in RESPONSES.items():
        if any(keyword in text for keyword in keywords):
            return random.choice(replies), False

    # Nothing matched
    return random.choice(FALLBACKS), False


def main():
    print("\n" + "=" * 50)
    print("    CodeAlpha — Rule-Based Chatbot 🤖")
    print("=" * 50)
    print("  Type anything to chat. Type 'bye' to exit.\n")

    while True:
        try:
            user_input = input("  You: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\n\n  Bot: See you later! Goodbye. 👋\n")
            break

        if not user_input:
            print("  Bot: Say something! I'm listening. 👂\n")
            continue

        reply, should_exit = get_response(user_input)
        print(f"  Bot: {reply}\n")

        if should_exit:
            break


if __name__ == "__main__":
    main()
