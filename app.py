quiz = open("D:\coding\Quiz Application\questions.txt", "r")
score = 0

print("Hello and Welcome to The Quiz")
print("Here are some questions, each correct answer will add to your total score")

question1 = input(quiz.readline())
if question1 == "2":
    print("correct")
    score = score+1
else:
    print("incorrect")
    
question2 = input(quiz.readline())
if question2 == "4":
    print("correct")
    score = score+1
else:
    print("incorrect")

question3 = input(quiz.readline())
if question3 == "8":
    print("correct")
    score = score+1
else:
    print("incorrect")

print("your score is: ", score, "out of 3")

