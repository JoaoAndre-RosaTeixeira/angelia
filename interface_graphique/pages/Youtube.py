from tkinter import *

from interface_graphique.pages.header import header

class Youtube:
    primary_bg = "#d4d4d4"

    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)

    def start(self):
        header(self, self.frame_canvas)