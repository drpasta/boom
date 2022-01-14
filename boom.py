from pynput import mouse
from playsound import playsound
import threading


def on_click(x, y, button, pressed):
    if pressed:
        threading.Thread(target=playsound, args=(
            'boom.mp3',), daemon=True).start()


with mouse.Listener(on_click=on_click) as listener:
    listener.join()
