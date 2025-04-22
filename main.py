import nltk
from nltk.chat.util import Chat, reflections

# Define some pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hey there! What can I do for you?"]
    ],
    [
        r"what is your name\??",
        ["I am your friendly chatbot created using NLTK.", "You can call me ChatBuddy!"]
    ],
    [
        r"how are you\??",
        ["I'm doing well, thank you! How about you?", "Feeling helpful as always!"]
    ],
    [
        r"(.*) your developer\??",
        ["I was developed by a human who loves AI.", "Someone passionate about coding created me!"]
    ],
    [
        r"(.*) (location|city)\??",
        ["I'm in the digital world, everywhere and nowhere."]
    ],
    [
        r"how can you help me\??",
        ["I can answer simple queries, chat with you, and make your day better!"]
    ],
    [
        r"bye|quit|exit",
        ["Goodbye! Have a great day ahead.", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm ChatBuddy. Type 'quit' or 'exit' to end the chat.")
chatbot.converse()
