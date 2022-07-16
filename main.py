import pyttsx3
friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id)
speech = input('Say Something: ')
friend.say(speech)
friend.runAndWait()

# for voice in voices:
#     print("Voice:")
#     print("ID: %s" % voice.id)
#     print("Name: %s" % voice.name)
#     print("Age: %s" % voice.age)
#     print("Gender: %s" % voice.gender)
#     print("Languages Known: %s" % voice.languages)
# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
