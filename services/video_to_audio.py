import os
from pydub import AudioSegment

def video_to_audio(video_path, output_audio_extension='wav'):
    if not os.path.exists('audios'):
        os.makedirs('audios')

    # Extract the video file name (excluding extension)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Construct the audio file name with the same name as the video but with a different extension
    output_audio_name = f'{video_name}.{output_audio_extension}'
    output_audio_path = os.path.join('audios', output_audio_name)

    video = AudioSegment.from_file(video_path)
    audio = video.set_channels(1)
    audio.export(output_audio_path, format=output_audio_extension)

    return output_audio_path

