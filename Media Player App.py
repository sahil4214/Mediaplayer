#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install python-vlc


# In[1]:


import tkinter as tk
from tkinter import filedialog
import vlc

# Global variables
title = "Media Player"
media_player = None
video_frame = None

def setup_ui(root):
    global video_frame

    video_frame = tk.Frame(root)
    video_frame.pack()

    play_button = tk.Button(root, text="Play", command=play_media)
    play_button.pack(side=tk.LEFT, padx=5)

    pause_button = tk.Button(root, text="Pause", command=pause_media)
    pause_button.pack(side=tk.LEFT, padx=5)

    stop_button = tk.Button(root, text="Stop", command=stop_media)
    stop_button.pack(side=tk.LEFT, padx=5)

    close_video_button = tk.Button(root, text="Close Video", command=close_video)
    close_video_button.pack(side=tk.LEFT, padx=5)

    close_audio_button = tk.Button(root, text="Close Audio", command=close_audio)
    close_audio_button.pack(side=tk.LEFT, padx=5)

    select_button = tk.Button(root, text="Select Media", command=select_media)
    select_button.pack(pady=10)

    fast_forward_button = tk.Button(root, text="Fast Forward", command=fast_forward)
    fast_forward_button.pack(pady=5)

    volume_scale = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Volume", command=set_volume)
    volume_scale.set(50)
    volume_scale.pack(pady=5)

    playback_speed_label = tk.Label(root, text="Playback Speed")
    playback_speed_label.pack()

    speed_scale = tk.Scale(root, from_=0.5, to=2, resolution=0.1, orient="horizontal", command=change_speed)
    speed_scale.set(1)
    speed_scale.pack()

def play_media():
    global media_player

    if media_player is None:
        return

    if media_player.get_state() == vlc.State.Ended:
        media_player.stop()

    media_player.play()
def pause_media():
    if media_player is None:
        return

    if media_player.get_state() == vlc.State.Playing:
        media_player.pause()

def stop_media():
    global media_player

    if media_player is not None:
        media_player.stop()

def set_volume(value):
    if media_player is not None:
        volume = int(value)
        media_player.audio_set_volume(volume)

def change_speed(value):
    if media_player is not None:
        speed = float(value)
        media_player.set_rate(speed)

def fast_forward():
    if media_player is not None:
        current_time = media_player.get_time()
        new_time = current_time + 10000  # Forward 10 seconds
        media_player.set_time(new_time)

def close_video():
    global media_player

    if media_player is not None:
        media_player.stop()
        media_player = None

def close_audio():
    global media_player

    if media_player is not None:
        media_player.audio_set_volume(0)  # Mute audio
        media_player = None

def select_media():
    file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp3 *.wav *.mp4 *.avi *.mkv")])

    if file_path:
        close_media()  # Close previous media if any
        initialize_media_player(file_path)

def initialize_media_player(file_path):
    global media_player
    instance = vlc.Instance("--no-xlib")
    media_player = instance.media_player_new()
    media = instance.media_new(file_path)
    media_player.set_media(media)

    media_player.set_xwindow(video_frame.winfo_id())
    media_player.play()
    
def close_media():
    global media_player

    if media_player is not None:
        media_player.stop()
        media_player = None

if __name__ == "__main__":
    root = tk.Tk()
    root.title(title)
    setup_ui(root)
    root.mainloop()


# In[ ]:




