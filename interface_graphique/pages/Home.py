from tkinter import *

from database.sql_class.Database import Database
from interface_graphique.interface import Main
from interface_graphique.pages.Deezer import Deezer
from interface_graphique.pages.Spotify import Spotify
from interface_graphique.pages.Top_ten import Top_ten
from interface_graphique.pages.Youtube import Youtube


class Home(Main):
    top_ten = Top_ten()
    youtube = Youtube()
    deezer = Deezer()
    spotify = Spotify()

    def __init__(self):
        super().__init__()
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)

    def start(self):
        self.header()

        div = self.new_row()
        button_Top_ten = Button(div, text="Top 10 des potentiel top 50", font=("Arial", 20), bg='white', fg='black', command=self.new_window)
        button_Top_ten.pack(expand=YES)

        div = self.new_row()
        button_youtube = Button(div, text="Youtube stats", padx=15, font=("Arial", 20), bg='white', fg='black')
        button_youtube.pack(expand=YES, side=LEFT, padx=15)

        button_deezer = Button(div, text="Deezer stats", padx=15, font=("Arial", 20), bg='white', fg='black')
        button_deezer.pack(expand=YES, side=LEFT, padx=15)

        button_spotifiy = Button(div, text="Spotifiy stats", padx=15, font=("Arial", 20), bg='white', fg='black')
        button_spotifiy.pack(expand=YES, side=LEFT, padx=15)

        # for song in self.database.songs.songs:
        #     div = self.new_row()
        #     label_title = Label(div, text=song.popularity, font=("Courrier", 36), bg=self.primary_bg, padx=30)
        #     label_title.pack(expand=YES)


        self.start_window()

