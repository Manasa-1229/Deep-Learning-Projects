def speech_to_text():
    import speech_recognition as sr

    # create a Recognizer object
    r = sr.Recognizer()

    # use the microphone as source
    with sr.Microphone() as source:
        print("Say something...")
        # listen for audio and convert it to text
        audio = r.listen(source)

    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        
        return text
    except sr.UnknownValueError:
        print("Oops! Could not understand audio")
    except sr.RequestError as e:
        print("Error: {}".format(e))
    
