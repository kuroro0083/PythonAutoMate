import random

theKey = random.randint(1, 100)
tips = 'Correct'
print("Input your answer")

while True:
    yourAnswer = int(input())
    if yourAnswer == theKey:
        print("Correct!!!! Bye Bye")
        exit()
    elif yourAnswer < theKey:
        tips = 'Low'
    else:
        tips = 'High'
    print('Your answer is %s, %s' % (yourAnswer, tips))




