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
    print("Please type the wrong answers make the seperation between the wrong answers by a ','") # if there is more then one wrong answer ask user to seperate them with a ,
    print()
    answers = input("Enter the wrong answers(only): ") # asking user to type the answers only so i can store them later on
    structerd_wrong_answers = answers.split(",") # spliting the wrong answers to make a list
    print()
    right_answer = input("Type the right answer: ") # asking user to type the right answer
    structerd_question = [title, structerd_wrong_answers, right_answer] # Making a list inculding the data required
    print()
    print()
    return structerd_question # returning the structerd question   it should  look like this:  ["question" , ["wrong answer"] , "right answer"]

def start_qcm(questions): # needs the questions
    print() # q[0] stands for the title   q[1] stands for the wrong answers  q[2] stands for the correct answer
    score = 0
    for e in questions: ~# for each elment in the list questions  btw i mean by elment question
        print()
        print(e[0]) # printing the title
        print(e[2]) # printing the correct answer
        for i in q[1]:
            print(i) # printing all the wrong answers
        print()
        answer = input("Type your answer: ")
        if answer.lower() == e[2].lower(): # cheking the user answer and the right one
            print("Correct!")
            score += 1 # incrising the score
        else:
            print("Uncorrect :(")
        print()
    print(f"Final score: {score} of {len(questions)}") # just a thing to print the final score and how many questions you answered right
    
def save_qcm(questions):
    with open("saves.txt","w") as file: # opening the file with write only   'w'
        i = 0
        for q in questions:  # for each question in list questions
            file.write(f"{questions[i][0]}") # we selct the title
            for answer in questions[i][1]: # for each wrong answer in the list of the wrong answers
                file.write(answer)
            file.write(questions[i][2]) # we write the right answer last
            i += 1 

def load_qcm():
    with open("saves.txt","r") as file:
        lines = file.readlines()
    question_str = lines[0]
    question_list = ast.literal_eval(question_str) # this is a library that let s me covert a string that is a list like  ["["example" , "othe example"]"] into a true list
    return question_list






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
        load_qcm()



