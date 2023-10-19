import speech_recognition as sr
from textblob import TextBlob
import re

recognizer = sr.Recognizer()

def keyword_detection(text, keywords):
    found_keywords = []
    for keyword in keywords:
        matches = re.findall(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE)
        found_keywords.extend(matches)
    return found_keywords

def record_audio():
    with sr.Microphone() as source:
        print("Please speak something...")
        audio = recognizer.listen(source)
    return audio

def analyze_emotion(audio):
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        found_keywords = []

        sample_keywords = ["Python", "code", "programming"]
        found_keywords = keyword_detection(text, sample_keywords)
        print("Found Keywords:", found_keywords)

        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            return "Happy"
        elif sentiment < 0:
            return "Sad"
        else:
            return "Neutral"
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return "Unable to analyze"
    except sr.RequestError as e:
        print(f"Error: {e}")
        return "Request error"

if __name__ == "__main__":
    audio = record_audio()
    emotion = analyze_emotion(audio)
    print(f"Emotion detected: {emotion}")

