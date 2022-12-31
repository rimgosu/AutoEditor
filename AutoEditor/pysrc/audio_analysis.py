import wave
import os
import numpy as np
from moviepy.editor import AudioFileClip, VideoFileClip
import matplotlib.pyplot as plt
import math

def mp4_to_wav(video_path, wav_path):
    with AudioFileClip(video_path) as mp4_file:
        mp4_file.write_audiofile(wav_path)
def max_volume(wav_path, total_frame):
    wav = wave.open(wav_path)

    # Read the audio data and get the sample width
    data = wav.readframes(-1)
    sampwidth = wav.getsampwidth()

    # Convert the audio data to a NumPy array
    audio = np.frombuffer(data, dtype=np.int16)

    # Divide the audio data into sections
    num_sections = total_frame
    sections = np.array_split(audio, num_sections)

    # Calculate the maximum volume for each section
    max_volumes = [np.max(np.abs(section)) for section in sections]
    return(max_volumes)


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    current_path = os.path.join(current_path, os.pardir)
    inputvideo_path = os. path. join(current_path, 'inputvideo')
    wav_path = os.path.join(current_path, 'pysrc')
    wav_path = os.path.join(wav_path, 'wav')
    video_list = os.listdir(inputvideo_path)
    video_list = [file for file in video_list if file.endswith(".mp4")]
    videopy = VideoFileClip(inputvideo_path+ "/" + video_list[0])
    print(int(videopy.end*3))
    mp4_to_wav(inputvideo_path+ "/" + video_list[0], wav_path + "/" + video_list[0][:-4] + '.wav')
    max_volume_section = max_volume(wav_path + "/" + video_list[0][:-4] + '.wav', int(videopy.end*3))
    print(max_volume_section)
    print(len(max_volume_section))

    x = []
    for i in range(4940):
        x.append(i)

    fig, ax = plt.subplots()
    ax.plot(x, max_volume_section)

    # Add a title and axis labels
    ax.set_title("List Graph")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    plt.show()


