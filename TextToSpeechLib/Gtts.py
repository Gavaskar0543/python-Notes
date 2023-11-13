from gtts import gTTS

text = "Hello, Gavaskar. How are you? Shall I start my machine!"
engine = gTTS(text)

# Save the converted audio to a file
engine.save("output.mp3")
