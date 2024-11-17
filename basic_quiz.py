def quiz_game():
    questions = {
        "What is the capital of France?": "paris",
        "What is 5 + 3?": "8",
        "Who is the president of the USA?": "Donald Trump",
        "What is the largest ocean on Earth?": "pacific"
    }

    score = 0
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:\n")

    for question, answer in questions.items():
        user_answer = input(question + " ").lower()
        if user_answer == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer.capitalize()}.")

    print(f"\nYour final score is: {score}/{len(questions)}")

# Run the game
if __name__ == "__main__":
    quiz_game()
