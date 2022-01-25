from pynput import mouse
from playsound import playsound
from threading import Thread
from argparse import ArgumentParser
from sys import path
from os import chdir

class Boom:
    def __init__(self):
        self.args = ArgumentParser()
        self.args.add_argument('-r', '--rock', help='We Stay Hungry', action='store_true', default=False)
        self.args = self.args.parse_args()

        if self.args.rock:
            self.clips = ['Face-Off/ItsAboutDrive.mp3', 'Face-Off/ItsAboutPower.mp3', 'Face-Off/WeStayHungry.mp3', 'Face-Off/WeDevour.mp3', 'Face-Off/PutInTheWork.mp3', 'Face-Off/PutInTheHours.mp3', 'Face-Off/ToTakeWhatsOurs.mp3']
        else:
            self.clips = ['boom.mp3']
        
        chdir(path[0])

        self.increment = 0

    def clip(self):
        file = self.clips[self.increment]
        self.increment = (self.increment + 1) % len(self.clips)
        return file

    def run(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self,x, y, button, pressed):
        if pressed:
            Thread(target=playsound, args=(self.clip(),), daemon=True).start()

Boom().run()

