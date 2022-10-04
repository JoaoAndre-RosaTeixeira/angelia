from tkinter import *

from database.sql_class.Database import Database
from interface_graphique.interface import Main


class Home(Main):

    def __init__(self):
        super().__init__()

    def start(self):
        new_label = self.new_column()
        label_title = Label(new_label, text="Bienvenue sur Angelia", font=("Arial", 36), bg=self.primary_bg)
        label_title.pack(expand=YES)
        new_label = self.new_column()
        label_subtitle = Label(new_label, text="IA de prediction de popularité des musiques", font=("Arial", 22),
                               bg=self.primary_bg)
        label_subtitle.pack(expand=YES)
        self.start_window()

