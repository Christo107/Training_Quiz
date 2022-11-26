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
    {"question": "How many levels are there in the QQI framework of qualifications?",
    "answers": {"a": "7",
                "b": "10",
                "c": "15"},
    "correct_answer": "b"},
    {"question": "What is the lowest qualification level that is covered by grant funding?",
    "answers": {"a": "PLC Level 5",
                "b": "Undergraduate Degree Level 7",
                "c": "Leaving Certificate Level 4"},
    "correct_answer": "a"},
    {"question": "Which of these levels is not part of the Undergraduate levels?",
    "answers": {"a": "Level 8 Higher Diploma",
                "b": "Level 6 Higher Certificate",
                "c": "Level 7 Ordinary Bachelor Degree"},
    "correct_answer": "a"},
    {"question": "Which of these colleges is not an approved college for grant funding?",
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

    # Relaunches start quiz if no name is entered and user only clicks enter
    if name == "":
        print("A name is required to take the quiz")
        start_quiz()
    else:
        print(f"Welcome to the Progression module training quiz {name}.\n")
        print("The quiz consists of ten questions to test your knowledge of the training module that was delivered to you recently.\n")
        print("The questions are in multiple choice format.\n")
        print("Options are a, b or c for all questions.\n")
        print("When prompted, please enter you answer a, b or c and hit the enter key.\n")

    # Asks user if they'd like to begin the quiz pulling in the name they have entered above
    begin_quiz = input(f"Are you ready to begin, {name}? (y/n): \n")

    if begin_quiz.lower() == "y":
        print("Okay, let's start. Good luck!\n")
    elif begin_quiz.lower() == "n":
        print("This quiz is mandatory for all trainees. Please complete it\
        before your assigned deadline.")
    else:
        print("Please select either y or n.")


# run_quiz function based on project by Leah Fisher https://github.com/cornishcoder1/Food_of_Japan_Quiz
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
            print(f"Sorry {name}, that's incorrect. \nThe correct answer was {correct_answer}.\n")

    print(f"Well done for completing the training quiz, {name}.")
    print(f"Your total score was {score} points.\n")
    print("Thank you and have a nice day.")


def export_results(data):
    """
    This function will export the results of the quiz including
    the trainees name and final score to the results worksheet
    in order for the trainer to evaluate each person's progress
    """
    print("Updating results worksheet...\n")
    results_worksheet = SHEET.worksheet("results")
    results.worksheet.append_row(data)
    print("Results exported to worksheet successfully")

start_quiz()
run_quiz(quiz_data)
export_results()
