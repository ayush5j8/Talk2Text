import os
import speech_recognition as sr
import time

def audio_to_text(audio_path, segment_duration=5, request_delay=1):
    if not os.path.exists('transcripts'):
        os.makedirs('transcripts')

    # Extract the audio file name (excluding extension)
    audio_name = os.path.splitext(os.path.basename(audio_path))[0]

    # Construct the CSV file path
    csv_path = os.path.join('transcripts', f'{audio_name}.csv')

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_duration = int(source.DURATION)
        start_time = 0
        subtitle_index = 1

        # Open the CSV file for writing
        with open(csv_path, 'w') as csv_file:

            # Process audio in segments
            while start_time < audio_duration:
                end_time = min(start_time + segment_duration, audio_duration)

                # Record the audio segment
                audio_segment = recognizer.record(source, offset=start_time, duration=end_time - start_time)

                try:
                    # Transcribe the audio segment
                    transcript_segment = recognizer.recognize_google(audio_segment)

                except sr.UnknownValueError:
                    print(f"Speech Recognition could not understand audio segment at {start_time}-{end_time}")
                    transcript_segment = ''  # Set a default value or handle as needed

                # Write the CSV formatted entry to the file
                csv_file.write(f"{start_time // 60:02d}:{start_time % 60:02d},{end_time // 60:02d}:{end_time % 60:02d},\"{transcript_segment}\"\n")

                start_time += segment_duration
                subtitle_index += 1

                # Add delay between requests to avoid rate limits
                time.sleep(request_delay)

    return csv_path

