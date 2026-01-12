# imports
import random
import time
import os
import sys
# variables
loop = True
correct = ""
randQuestion = 0
correctAnswers = 0
wrongAnswers = 0
part1 = 0
part2 = 0
part3 = 0
result = 0
questions = 0
no = ["n", "no", "f", "wrong"]
yes = ["y", "yes", "t", "correct", part3]
# functions
def question(answer, said):
    if said in yes:
        said = "true"
    elif said in no:
        said = "false"
    if said == answer:
        return True
    else:
        return False
def clear_terminal():
    if sys.platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')
# code
clear_terminal()
print("these questions are all true/false")
print("how many questions would you like?")
questions = input()
if not questions.isnumeric():
    print("nice try, have 5 questions")
    questions = 5
questions = int(questions)
if questions != 0:
    while questions != 0:
        time.sleep(0.1)
        clear_terminal()
        questions -= 1
        randQuestion = random.randint(1,4)

        # true add
        if randQuestion == 1:
            print("what will the result of this be")
            part1 = random.randint(random.randint(1,5),random.randint(10,50))
            part2 = random.randint(random.randint(1,5),random.randint(10,50))
            part3 = part1 + part2
            print(part1,"+",part2,"=",part3)
            correct = "True"

        # false add
        elif randQuestion == 2:
            print("what will the result of this be")
            part1 = random.randint(random.randint(1,5),random.randint(10,50))
            part2 = random.randint(random.randint(1,5),random.randint(10,50))
            while part3==part1+part2:
                part3 = random.randint(random.randint(2,10),random.randint(20,100))
            print(part1,"+",part2,"=",part3)
            correct = "False"

        # false subtract
        elif randQuestion == 3:
            print("what will the result of this be")
            part1 = random.randint(random.randint(1,5),random.randint(10,50))
            part2 = random.randint(random.randint(1,5),random.randint(10,50))
            while part3==part1-part2:
                part3 = random.randint(0,random.randint(5,15))
            print(part1,"-",part2,"=",part3)
            correct = "False"

        # true subtract
        elif randQuestion == 4:
            print("what will the result of this be")
            part1 = random.randint(random.randint(1,5),random.randint(10,50))
            part2 = random.randint(random.randint(1,5),random.randint(10,50))
            part3 = part1-part2
            print(part1,"-",part2,"=",part3)
            correct = "True"
    
        if question(correct.lower().strip(), input().lower().strip()):
            correctAnswers += 1
        else:
            wrongAnswers += 1
    result = correctAnswers + wrongAnswers
    clear_terminal()
    print("you got", str(correctAnswers) +"/"+str(result), "correct")
else:
    clear_terminal()
    print("oh ok")