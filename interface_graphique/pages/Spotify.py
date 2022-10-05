from tkinter import *

from interface_graphique.interface import Main


class Spotify(Main):

    def __init__(self):
        super().__init__()
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)

    def start(self):
        self.header()