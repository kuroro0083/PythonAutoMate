import pyinputplus
import time, random

numberOfQuestion = 2
correctTime = 0

for questionNum in range(numberOfQuestion):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'{num1} x {num2} = '
    try:
        pyinputplus.inputStr(prompt, 
                         allowRegexes=[r'^%s$' % (num1*num2)],
                         blockRegexes=[(r'.*'), ('incorrect!')],
                         timeout=8,
                         limit=3)
    except pyinputplus.TimeoutException:
        print('Out of time')
    except pyinputplus.RetryLimitException:
        print('Out of try')
    else:
        print('Correct!!')
        correctTime += 1
    time.sleep(1)

print('Score: %s / %s' % (correctTime, numberOfQuestion))
