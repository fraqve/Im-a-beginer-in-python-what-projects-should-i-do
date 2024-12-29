import os

class calcuator():
    def __init__(self):
        pass

    def GetInputs(self):
        print("Welcome to the calculator")
        print("Please type the opertation you need")
        print("Select one of the operators +,-,*,/")
        print("Example: 5 + 5 (don't forget the space between the nubers and oprators)") 

        #                                                                                         op 
        while True:
            self.UserInput = input("Please type what you want here: ") # Getting user input expected n + m
            self.ListUserInput = self.UserInput.split(" ") # Organizing the data in a list expeccted [n,+,m]
            self.IsUserInputCorrect = self.CheckingTheOperation()
            if self.IsUserInputCorrect:
                break

        return self.ListUserInput
    

    def CheckingTheOperation(self):
            try: # Cheking if the value of the numbers is correct
                int(self.ListUserInput[0]) # Testing the first number
                int(self.ListUserInput[2]) # Testing the second number if one of the numbers is not correct we fall in except
                if self.ListUserInput[1] in ["+","-","*","/"]: # if the oprtator is correct we retrun True else return False
                    os.system("cls")
                    return True
                else:
                    os.system("cls")
                    return False
            except:
                os.system("cls")
                print("Error: value error in operation please don't forget to put space between the numbers and opertors")
                return False
            
        
    def DoMaths(self):
        match self.ListUserInput[1]:
            case "+":
                return int(self.ListUserInput[0]) + int(self.ListUserInput[2])
            case "-":
                return int(self.ListUserInput[0]) - int(self.ListUserInput[2])
            case "*":
                return int(self.ListUserInput[0]) * int(self.ListUserInput[2])
            case "/":
                return int(self.ListUserInput[0]) / int(self.ListUserInput[2])


cal = calcuator()

while True:
    os.system("cls")
    cal.GetInputs()
    print()
    print()
    result = cal.DoMaths()
    print(f"Result of {cal.ListUserInput[0]} {cal.ListUserInput[1]} {cal.ListUserInput[2]}: {result}")
    print()
    print()
    IsCountinuing = input("Do you want to continue ? ")
    os.system("cls")
    if IsCountinuing.lower() == "no".lower():
        break
    else:
        print()
        print()


