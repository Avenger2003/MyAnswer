import pyttsx3
import speech_recognition as sr

# Initialize the speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speech_to_text():
    sentence = ""
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        engine.say("Listening")
        engine.runAndWait()
        try:
            while True:
                try:
                    audio = recognizer.listen(source, timeout=1)  # Listen for 1 second
                except sr.WaitTimeoutError:
                    continue
                if not audio:
                    break
                word = recognizer.recognize_google(audio)
                print("\rYou said:", sentence + word, end=" ", flush=True)
                engine.say(word)
                engine.runAndWait()
                sentence += word + " "
        except KeyboardInterrupt:
            pass
        return sentence

# Main loop
while True:
    input("Press Enter to start speech recognition...")
    try:
        sentence = speech_to_text()
        input("Press Enter to start speech recognition again...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
