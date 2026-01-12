# imports
import random
# variables
loop = True
correct = ""
randQuestion = 0
correctAnswers = 0
wrongAnswers = 0
part1 = 0
part2 = 0
part3 = 0
questions = 0
# functions
def question(answer, said):
    if said == answer:
        return True
    else:
        return False
# code
print("these questions are all true/false")
print("how many questions would you like?")
questions = input()
if not questions.isnumeric():
    print("nice try, have 5 questions")
    questions =5
while questions != 0:
    questions -= 1
    randQuestion = random.randint(1,4)

    if randQuestion == 1:
        print("what will the result of this be")
        part1 = random.randint(random.randint(1,5),random.randint(10,50))
        part2 = random.randint(random.randint(1,5),random.randint(10,50))
        part3 = part1 + part2
        print(part1,"+",part2,"=",part3)
        correct = "True"

    elif randQuestion == 2:
        print("what will the result of this be")
        part1 = random.randint(random.randint(1,5),random.randint(10,50))
        part2 = random.randint(random.randint(1,5),random.randint(10,50))
        while part3==part1+part2:
            part3 = random.randint(random.randint(2,10),random.randint(20,100))
        print(part1,"+",part2,"=",part3)
        correct = "False"

    elif randQuestion == 3:
        print("what will the result of this be")
        part1 = random.randint(random.randint(1,5),random.randint(10,50))
        part2 = random.randint(random.randint(1,5),random.randint(10,50))
        while part3==part1-part2:
            part3 = random.randint(random.randint(1,5),random.randint(5,15))
        print(part1,"-",part2,"=",part3)
        correct = "False"

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