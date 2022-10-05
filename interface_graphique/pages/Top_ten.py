from tkinter import *

from interface_graphique.interface import Main

class Top_ten(Main):


    def __init__(self):
        super().__init__()
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)

    def start(self):
        self.start_window()
        self.new_window()
        self.header()


