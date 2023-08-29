import pyttsx3

print("Welcome to Robo Speaker")
head = "Welcome to Robo Speaker"
speech = pyttsx3.init()
speech.say(head)
speech.runAndWait()


while True:
    text_speech = pyttsx3.init()
    text = input("Enter what you want to say: ")
    if(text == "quit"):
        texty = pyttsx3.init()
        texty.say(" ok See you again")
        texty.runAndWait()
        break
    text_speech.say(text)
    text_speech.runAndWait()