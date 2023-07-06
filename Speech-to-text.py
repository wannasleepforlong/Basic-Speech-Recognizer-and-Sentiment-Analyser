import speech_recognition as sr
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import wave

print("Welcome to Audio Recognizer....")

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)  # Record for 5 seconds

    # Save audio as a WAV file
    with wave.open("recording.wav", "wb") as file:
        file.setnchannels(1)  # Mono channel
        file.setsampwidth(2)  # 2 bytes per sample
        file.setframerate(44100)  # 44.1 kHz sample rate
        file.writeframes(audio.get_wav_data())

    status_label.config(text="Recording saved and transcribed succesfully")

window = tk.Tk()
window.title("Speech Recognition")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

image = Image.open("mic.jpg")
image = image.resize((100, 100))  
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo, bg="#f0f0f0")
image_label.pack(pady=20)

button = ttk.Button(window, text="Record", command=recognize_speech)
button.pack(pady=10)

status_label = tk.Label(window, text="", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=5)

window.mainloop()


#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable

with sr.AudioFile('recording.wav') as source:
    
    audio_text = r.listen(source)
    
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
        file = open("speech.txt","w")
        file.write(text)
        file.close()
     
    except:
         print('Sorry.. run again...')
