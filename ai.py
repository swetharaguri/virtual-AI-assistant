import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text): 
    machine.say(text)
    machine.runAndWait()  # Ensure the speech is spoken before continuing

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)  # Corrected from 'goggle' to 'google'
            instruction = instruction.lower()
            if "ai" in instruction:
                instruction = instruction.replace('ai', "")
                print(instruction)
            return instruction  # Return the instruction
    except Exception as e:
        print("Error:", e)
        return ""  # Return an empty string on error

def play_ai():
    instruction = input_instruction()
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace('play', "").strip()  # Strip leading/trailing spaces
        talk("Playing " + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')  # Corrected from 'strtime' to 'strftime'
        talk('Current time is ' + time)
        
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you?')
        
    elif 'what is your name' in instruction:
        talk('I am AI, what can I do for you?')  
    
    elif 'who is' in instruction:
        human = instruction.replace('who is', "").strip()
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
        
    else:
        talk('Please repeat.')

# Start the AI assistant
play_ai()