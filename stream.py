import streamlit as st
import pyttsx3
import speech_recognition as sr

# Initialize the speech recognizer
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speech_to_text():
    sentence = ""
    recognized_text = st.empty()  # Create an empty text element for displaying recognized text
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening...")
        engine.say("Listening")
        engine.runAndWait()
        try:
            while True:
                try:
                    audio = recognizer.listen(source, timeout=2)  # Listen for 1 second
                except sr.WaitTimeoutError:
                    continue
                if not audio:
                    break
                word = recognizer.recognize_google(audio)
                recognized_text.text("\rYou said: " + sentence + word)  # Update the recognized text
                engine.say(word)
                sentence += word + " "
        except KeyboardInterrupt:
            pass
    engine.runAndWait()  # Speak the entire sentence after the loop completes
    return sentence


# Main Streamlit app
st.title("Speech Recognition App")
st.write("Press the button below and speak into the microphone.")

if st.button("Start Recording"):
    try:
        sentence = speech_to_text()
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand audio")

    st.write("\n\nYou said:", sentence)
    st.button("Start Recording Again")
