import pandas as pd
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os


class Subtitle:
    def __init__(self, video_path, csv_path, output_path):
        self.video_path = video_path
        self.csv_path = csv_path
        self.output_path = output_path

    def add_subtitles(self):
        # Reading the CSV file
        df = pd.read_csv(self.csv_path)
        subtitles_info = list(zip(df['START'], df['END'], df['TEXT']))

        video_clip = VideoFileClip(self.video_path)
        subtitle_clips = []
        screen_size = (1100, 100)

        for start, end, text in subtitles_info:
            start_time = int(start.split(
                ':')[0]) * 60 + int(start.split(':')[1])
            end_time = int(end.split(':')[0]) * 60 + int(end.split(':')[1])

            text_clip = TextClip(text, method='caption', color='white',
                                 bg_color='transparent',
                                 kerning=-1, interline=-1, size=screen_size)
            text_clip = text_clip.set_position(('center', 'bottom'))
            text_clip = text_clip.set_start(start_time).set_end(end_time)
            subtitle_clips.append(text_clip)

        final_clip = CompositeVideoClip([video_clip] + subtitle_clips)

        final_clip.write_videofile(self.output_path, codec='libx264', audio_codec='aac',
                                   temp_audiofile='temp-audio.m4a', remove_temp=True)


base_path = os.getcwd()
video_path = f'{base_path}\input_video.mp4'
csv_path = f'{base_path}\CSV\\timestamps.csv'
output_path = f'{base_path}\Output\output_video_with_subtitles.mp4'

subtitle_instance = Subtitle(video_path, csv_path, output_path)
subtitle_instance.add_subtitles()
