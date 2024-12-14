import time as t
import ast


def make_the_ui():
    print("1- Add question")
    print("2- start QCM")
    print("3- Save QCM")
    print("4- Load QCM")

def add_question():
    title = input("Please type the title of the quetion: ")
    print()
    print("Please type the wrong answers make the seperation between the wrong answers by a ','")
    print()
    answers = input("Enter the wrong answers(only): ")
    structerd_wrong_answers = answers.split(",") # spliting the wrong questions to make a list
    print()
    right_answer = input("Type the right answer: ")
    structerd_question = [title, structerd_wrong_answers, right_answer] # Making a tupel inculding the data required
    print()
    print()
    return structerd_question

def start_qcm(questions):
    print() # q[0] stands for the title   q[1] stands for the wrong answers  q[2] stands for the correct answer
    score = 0
    for q in questions:
        print()
        print(q[0]) # printing the title
        print(q[2]) # printing the correct answer
        for x in q[1]:
            print(x) # printing all the wrong answers
        print()
        answer = input("Type your answer: ")
        if answer.lower() == q[2].lower():
            print("Correct!")
            score += 1
        else:
            print("Uncorrect :(")
        print()
    print(f"Final score: {score} of {len(questions)}")
    
def save_qcm(questions):
    with open("saves.txt","w") as file:
        i = 0
        for q in questions:  
            file.write(f"{q}")
            i += 1
    print()
    print("file saved")
    print()

def load_qcm():
    with open("saves.txt","r") as file:
        lines = file.readlines()
    question_str = lines[0]
    question_list = ast.literal_eval(question_str)
    global_question = [question_list]
    print()
    print("file loaded")
    print()
    return global_question






questions = []
print("Welcome to the briliant program QCM v1.00")
print("Please Select one of the options below")
while True:
    make_the_ui()
    selection = input("To select type the numbers that corrspends to your choice: ")
    if selection == "1":
        q = add_question()
        q2 = [q]
        questions.extend(q2)
    elif selection == "2":
        start_qcm(questions)
    elif selection == "3":
        save_qcm(questions)
    elif selection == "4":
        questions = load_qcm()



