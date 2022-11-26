import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('chris_python_quiz')

# quiz questions for post training quiz
quiz_data = [
    {"question": "What does the term Progression mean in grant assessment?",
    "answers": {"a": "moving forward in your education",
                "b": "moving backward in your qualifications",
                "c": "staying at the same level"},
    "correct_answer": "a"},
    {"question": "How many levels are there in the QQI framework\
    of qualifications?",
    "answers": {"a": "7",
                "b": "10",
                "c": "15"},
    "correct_answer": "b"},
    {"question": "What is the lowest qualification level that is\
    covered by grant funding?",
    "answers": {"a": "PLC Level 5",
                "b": "Undergraduate Degree Level 7",
                "c": "Leaving Certificate Level 4"},
    "correct_answer": "a"},
    {"question": "Which of these levels is not part of the Undergraduate\
    levels?",
    "answers": {"a": "Level 8 Higher Diploma",
                "b": "Level 6 Higher Certificate",
                "c": "Level 7 Ordinary Bachelor Degree"},
    "correct_answer": "a"},
    {"question": "Which of these colleges is not an approved college\
         for grant funding?",
    "answers": {"a": "University College Dublin",
                "b": "Trinity College",
                "c": "Dublin Business School"},
    "correct_answer": "c"},
]


def start_quiz():
    """
    Beginning of quiz, includes welcome message, gets trainee's name and
    shows instructions for quiz
    """
    global name
    name = input("Hi trainee, please enter your name and hit enter: ")

    if name == "":
        print("A name is required to take the quiz")
        start_quiz()
    else:
        print(f"Welcome to the post training quiz {name}")
        print("The quiz consists of ten questions to test your knowledge\
            of the training module that was delivered to you recently.\n")
        print("The questions are in multiple choice format with\
            options a, b and c.\n")
        print("When prompted, please enter you answer a, b or c\
            and hit the enter key.\n")

    begin_quiz = input(f"Are you ready to begin, {name}? (y/n): \n")

    if begin_quiz.lower() == "y":
        print("Okay, let's start. Good luck!\n")
    elif begin_quiz.lower() == "n":
        print("This quiz is mandatory for all trainees. Please complete it\
        before your assigned deadline.")
    else:
        print("Please select either y or n.")



def run_quiz(data):
    """
    Loops through the questions and answers in the quiz data dictionary
    """
    score = 0

    for entry in quiz_data:
        user_answer = ""
        correct_answer = entry['correct_answer']

        while user_answer not in ['a', 'b', 'c']:
            print(f"{entry['question']}\n")

            for key, value in entry['answers'].items():
                print(f"{key}: {value}")

            user_answer = input("Answer: \n")
            user_answer = user_answer.lower()

        if user_answer == entry['correct_answer']:
            print(f"That's correct {name}! Well done\n")
            score = score + 1
            print(f"Your score: {score}\n")
        elif user_answer != entry['correct_answer']:
            print(f"Sorry {name}, that's incorrect. The correct answer was {correct_answer, value}.\n")

    print(f"Your total score was {score}.")


start_quiz()
run_quiz(quiz_data)
