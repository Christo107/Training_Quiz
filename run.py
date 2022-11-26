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

score = 0

def start_quiz():
    """
    Beginning of quiz, includes welcome message, gets trainee's name and
    shows instructions for quiz
    """
    name = input("Hi trainee, please enter your name and hit enter: ")
    if name == "":
        start_quiz()
    else:
        print(f"Welcome to the post training quiz {name}")


start_quiz()