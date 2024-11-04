import os
import time
import subprocess

# Stream configuration
YOUTUBE_STREAM_URL = "rtmp://a.rtmp.youtube.com/live2/"
YOUTUBE_STREAM_KEY = "ea4tffggghttytyytt6yt67y676676jnhfug78xu5-0ryr"  # replace with your actual stream key
VIDEO_PATH = "https://github.com/devps14/FastHanumanChalisa/blob/main/HanumanChalisa.mp4"  # path to the video you want to stream
LOOP_VIDEO = True  # Set True to loop the video

def start_stream():
    command = [
        "ffmpeg",
        "-re",
        "-stream_loop", "-1" if LOOP_VIDEO else "0",  # -1 for infinite loop if desired
        "-i", VIDEO_PATH,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-maxrate", "3000k",
        "-bufsize", "6000k",
        "-pix_fmt", "yuv420p",
        "-g", "50",
        "-c:a", "aac",
        "-b:a", "128k",
        "-ar", "44100",
        "-f", "flv",
        f"{YOUTUBE_STREAM_URL}{YOUTUBE_STREAM_KEY}"
    ]
    
    # Run the command with FFmpeg
    process = subprocess.Popen(command)
    print("Starting live stream...")

    # Wait for the process to complete or exit
    process.communicate()

# Run the stream function
if __name__ == "__main__":
    while True:
        try:
            start_stream()
        except Exception as e:
            print("Error occurred:", e)
            time.sleep(10)  # Wait a few seconds before retrying if an error occurs
