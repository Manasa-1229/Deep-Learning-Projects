def speak(text):
    import pyttsx3

    # create a Text-to-Speech engine
    engine = pyttsx3.init()

    # set properties for the voice
    engine.setProperty('rate', 150)   # speed in words per minute
    engine.setProperty('volume', 1.0) # volume (0-1)

    # say the text
    #text = "Hello, World!"
    engine.say(text)

    # run the engine
    engine.runAndWait()
