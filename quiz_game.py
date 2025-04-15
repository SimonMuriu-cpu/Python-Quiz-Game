# list of questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
        "answer": "c"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Jupiter", "c) Saturn", "d) Mars"],
        "answer": "b"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Au", "b) Ag", "c) Pb", "d) Fe"],
        "answer": "a"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["a) Mark Twain", "b) Charles Dickens", "c) William Shakespeare", "d) Jane Austen"],
        "answer": "c"
    },
    {
        "question": "What is the boiling point of water?",
        "options": ["a) 50°C", "b) 75°C", "c) 100°C", "d) 150°C"],
        "answer": "c"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "What is the speed of light?",
        "options": ["a) 300,000 km/s", "b) 150,000 km/s", "c) 600,000 km/s", "d) 1,000,000 km/s"],
        "answer": "a"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Claude Monet"],
        "answer": "c"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Great White Shark"],
        "answer": "b"
    },
    {
        "question": 'What is the main ingredient in guacamole?',
        'options': ['a) Tomato', 'b) Avocado', 'c) Onion', 'd) Pepper'],
        'answer': 'b'
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["a) Gold", "b) Diamond", "c) Iron", "d) Sapphire"],
        "answer": "b"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["a) 1", "b) 2", "c) 3", "d) 5"],
        "answer": "b"
    },
    {
        "question": 'What is the largest continent on Earth?',
        'options': ['a) Africa', 'b) Asia', 'c) Europe', 'd) Antarctica'],
        'answer': 'b'
    },
    {
        "question": 'What is the main language spoken in Brazil?',
        'options': ['a) Spanish', 'b) Portuguese', 'c) French', 'd) English'],
        'answer': 'b'
    }
]

def quiz_game(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)

        user_answer = input("Your Answer is (a/b/c/d): ")
        if user_answer == question["answer"]:
            print("Correct! You've earned 1 point,")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is:", question["answer"], "You've earned 0 points")    
    print(f"\nYour total acore is: {score}/{len(questions)}")
quiz_game(questions)
