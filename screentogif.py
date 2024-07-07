import pyautogui
import numpy as np
from PIL import Image, ImageSequence
import time
import winsound
import os

# TODO: HELLO
# ADJUST: delay before recording in seconds
initial_delay = 3

# ADJUST: duration of recording in seconds
duration = 20

screen_width, screen_height = pyautogui.size()

frames = []

# ADJUST: determine the filename for saving
base_filename = "screen_capture.gif"
filename_counter = 1

while os.path.exists(f"{base_filename[:-4]}_{filename_counter}.gif"):
    filename_counter += 1

output_gif = f"{base_filename[:-4]}_{filename_counter}.gif"

# display countdown before recording
for i in range(initial_delay, 0, -1):
    print(f"Starting recording in {i}...", end='\r')
    time.sleep(1)

print("\nRecording started...")
winsound.Beep(1000, 500) # beep

try:
    for _ in range(duration * 10): 
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frames.append(Image.fromarray(frame))
        print(f"Captured {len(frames)} frames", end='\r')

except KeyboardInterrupt:
    pass

print("\nRecording finished...")
winsound.Beep(1500, 500)  # beep

if frames:
    frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"Recording saved as {output_gif}")
else:
    print("No frames captured.")
