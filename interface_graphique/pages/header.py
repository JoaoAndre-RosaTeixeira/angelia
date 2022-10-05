from tkinter import *

def header(self, canvas):
    div = self.new_row(canvas)
    label_title = Label(div, text="Bienvenue sur Angelia", font=("Courrier", 36), bg=self.primary_bg, padx=30)
    label_title.pack(expand=YES)
    div = self.new_row(canvas)
    label_subtitle = Label(div, text="IA de prediction de popularité des musiques", font=("Courrier", 22),
                           bg=self.primary_bg, padx=30)
    label_subtitle.pack(expand=YES)