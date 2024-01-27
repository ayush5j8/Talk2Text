import os
import speech_recognition as sr

def audio_to_text(audio_path, transcript_extension='txt'):
    if not os.path.exists('transcripts'):
        os.makedirs('transcripts')

    # Extract the audio file name (excluding extension)
    audio_name = os.path.splitext(os.path.basename(audio_path))[0]

    # Construct the transcript file path
    transcript_path = os.path.join('transcripts', f'{audio_name}.{transcript_extension}')

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data)

    # Save the transcript to a file
    with open(transcript_path, 'w') as transcript_file:
        transcript_file.write(transcript)

    return transcript_path

