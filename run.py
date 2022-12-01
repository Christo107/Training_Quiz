"""
Imports to use gspread for tracking trainee names and scores
Import os for clearing screen to help with user experience
"""
import os
import time
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Google sheets access credentials variables
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('chris_python_quiz')


NAME = ""
SCORE = 0

# dictionary of quiz questions for training quiz
quiz_data = [
    {"question": "1. What does the term Progression mean in grant assessment?",
     "answers": {"a": "moving forward in your education",
                 "b": "moving backward in your qualifications",
                 "c": "staying at the same level"},
     "correct_answer": "a"},
    {"question": "2. How many levels are there in the QQI framework of "
                 "qualifications?",
     "answers": {"a": "7",
                 "b": "10",
                 "c": "15"},
     "correct_answer": "b"},
    {"question": "3. What is the lowest qualification level that is "
                 "covered by grant funding?",
     "answers": {"a": "PLC Level 5",
                 "b": "Undergraduate Degree Level 7",
                 "c": "Leaving Certificate Level 4"},
     "correct_answer": "a"},
    {"question": "4. Which of these levels is not part of the Undergraduate "
                 "levels?",
     "answers": {"a": "Level 8 Higher Diploma",
                 "b": "Level 6 Higher Certificate",
                 "c": "Level 7 Ordinary Bachelor Degree"},
     "correct_answer": "a"},
    {"question": "5. Which of these colleges is not an approved college for "
                 "grant funding?",
     "answers": {"a": "University College Dublin",
                 "b": "Trinity College",
                 "c": "Dublin Business School"},
     "correct_answer": "c"},
    {"question": "6. What does QQI stand for?",
     "answers": {"a": "Quality and Qualifications Ireland",
                 "b": "Query and Quality Institute",
                 "c": "Qualifications Quadranagle Ireland"},
     "correct_answer": "a"},
    {"question": "7. What is a second chance student?",
     "answers": {"a": "Someone who previously attended college but "
                      "did not receive an award more than 5 years ago",
                 "b": "Someone attending their second college course",
                 "c": "Someone doing the same course again"},
     "correct_answer": "a"},
    {"question": "8. Which qualification is lower on the NFQ 10 level "
                 "framework?",
     "answers": {"a": "Postgraduate Diploma",
                 "b": "Masters",
                 "c": "Higher Diploma"},
     "correct_answer": "c"},
    {"question": "9. What is a Repeat Period of Study?",
     "answers": {"a": "Repeating the same course",
                 "b": "A time equivalent to previous attendance for which "
                      "funding is not available",
                 "c": "Repeating a module"},
     "correct_answer": "b"},
    {"question": "10. Which of these statements is false?",
     "answers": {"a": "A student is progressing moving from PLC6 to UG6",
                 "b": "There is no limit on the amount of years a student "
                      "can receive funding",
                 "c": "A PHD is the highest level on the NFQ."},
     "correct_answer": "b"},
]


def start_quiz():
    """
    Beginning of quiz, includes welcome message, gets trainee's name and
    shows instructions for quiz
    """
    print("PROGRESSION MODULE TRAINING QUIZ\n")

    global NAME
    NAME = input("Hi trainee, please enter your name and hit enter:\n")

    # Relaunches start quiz if no name is entered and user only clicks Enter
    if NAME == "":
        print("A name is required to take the quiz")
        start_quiz()
    else:
        print(f"\nWelcome to the Progression module training quiz {NAME}.\n")
        time.sleep(2)
        print("The quiz consists of ten questions to test your knowledge "
              "of the training module that was delivered to you recently.\n")
        time.sleep(2)
        print("The questions are in multiple choice format.\n")
        time.sleep(2)
        print("Options are a, b or c for all questions.\n")
        time.sleep(2)
        print("When prompted, please enter you answer a, b or c and hit the "
              "enter key.\n")
        time.sleep(2)

    # Asks user if they'd like to begin the quiz pulling in the name they have\
    # entered above
    begin_quiz = input(f"Are you ready to begin, {NAME}? (y/n): ")

    while begin_quiz != "y":
        begin_quiz = input(f"Please enter 'y' to begin {NAME}, else "
                           "complete the quiz another time: ")

    if begin_quiz.lower() == "y":
        print("\nOkay, let's start. Good luck!\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


# run_quiz function based on project by Leah Fisher
# https://github.com/cornishcoder1/Food_of_Japan_Quiz
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

            user_answer = input("Answer(a, b or c): \n")
            user_answer = user_answer.lower()

        if user_answer == entry['correct_answer']:
            print(f"That's correct {NAME}! Well done\n")
            score = score + 1
            print(f"Your score: {score}")
            print("---------------------------------------")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif user_answer != entry['correct_answer']:
            print(f"Sorry {NAME}, that's incorrect.\n")
            print(f"The correct answer was {correct_answer}.")
            print("---------------------------------------")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Well done for completing the training quiz, {NAME}.\n")
    print(f"Your total score was {score} points.\n")
    print("Thank you and have a nice day.")
    data = NAME, score
    export_results(data)


def export_results(data):
    """
    This function will export the results of the quiz including
    the trainees name and final score to the results worksheet
    in order for the trainer to evaluate each person's progress
    """
    print("Updating results worksheet...\n")
    results_worksheet = SHEET.worksheet("results")
    results_worksheet.append_row(data)
    print("Results exported to worksheet successfully")


start_quiz()
run_quiz(quiz_data)
