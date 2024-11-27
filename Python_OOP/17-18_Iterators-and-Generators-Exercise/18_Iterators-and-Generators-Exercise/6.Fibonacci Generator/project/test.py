import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# List of audio file paths
file_paths = ["200 to 99.wav", "99 to 200.wav"]

# Container for transcriptions
transcriptions = []

# Transcribe each file
for file_path in file_paths:
    with sr.AudioFile(file_path) as source:
        # Record the audio from the file
        audio_data = recognizer.record(source)
        try:
            # Transcribe the audio
            transcription = recognizer.recognize_google(audio_data)
            transcriptions.append(transcription)
        except sr.UnknownValueError:
            transcriptions.append("[Unintelligible audio]")
        except sr.RequestError as e:
            transcriptions.append(f"[Error with recognition service: {e}]")

# Print transcriptions
for i, transcription in enumerate(transcriptions):
    print(f"File {i + 1}: {transcription}")
