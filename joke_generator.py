import random

def random_joke():
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don’t programmers like nature? It has too many bugs.",
        "Why did the scarecrow win an award? Because he was outstanding in his field."
    ]

    print("Here's a random joke for you:")
    print(random.choice(jokes))

# Run the joke generator
if __name__ == "__main__":
    random_joke()