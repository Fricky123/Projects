import string

questions = ["1. What year is today?",
             "2. What profession is Renzo Sasil pursuing right now?",
             "3. Do I want to play Skyrim or study?",
             "4. Should I panic or nah?",
             "5. Ambot unsai sunod..."]

choices = [['2019', '2020', '2021', '2022'],
           ['Architecture', 'Business', 'Programming', 'Construction'],
           ['Yes', 'no', 'maybe after this', 'later'],
           ['YES omg', 'AAAAAAAAAAAAAAAAAA', 'no', 'later', 'adasdasd', 'aswqewq'],
           ['gege', 'oks', 'malatan bolitan', 'skyrim']]

answers = ['d', 'c', 'c', 'b', 'a']

instance = 0
score = 0
# --------------------------------------------------------------------------

def question_machine():
    global score

    try:
        print("--------------------------------------------------")
        print(f"{questions[instance]}\n")

        letter = 0
        for choice in choices[instance]:
            print(f"{string.ascii_lowercase[letter]}. {choice}")
            letter += 1

        answer_machine()

    except IndexError:
        print(f"Score: {score}/{instance}\n"
              "Thank you for participating! Goodbye!")

        exit()


def answer_machine():
    global instance, score

    x = input("\nWhat's your answer? ").lower()
    if not x or x == " ":
        input("[ERROR] Please enter something to proceed...")
        question_machine()

    elif len(x) > 1 or x.isdigit():
        input("[ERROR] Please input only the letter of your choice... Press any key to continue...")
        question_machine()

    elif x == answers[instance]:
        score += 1

    instance += 1
    question_machine()
# --------------------------------------------------------------------------
question_machine()


