import pyinputplus

prompt = "Want to know how to keep a person busy for hours: "

while True:
    response = pyinputplus.inputYesNo(prompt,yesVal='hai')
    if response == 'no':
        break
print("Thanks, have a nice day")
