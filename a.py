import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)

# Recognize the speech using Google Web Speech API
try:
    recognized_text = recognizer.recognize_google(audio)
    print(f"You said: {recognized_text}")
    def calling():
        return recognized_text
except sr.UnknownValueError:
    print("Google Web Speech API could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")

# You can replace the Google Web Speech API with other recognizer engines if needed.
