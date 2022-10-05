from tkinter import *

from interface_graphique.pages.Spotify import Spotify
from interface_graphique.pages.Top_ten import Top_ten
from interface_graphique.pages.Youtube import Youtube
from interface_graphique.pages.header import header


class Home():
    primary_bg = "#d4d4d4"

    def __init__(self, window, width, height):
        self.top_ten = Top_ten(window, width, height)
        self.youtube = Youtube(window, width, height)
        self.spotify = Spotify(window, width, height)
        self.window = window
        self.width = width
        self.height = height
        self.home_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)
        self.row = 0
        self.column = 0


    def start(self):
        self.row = 0
        self.column = 0

        self.home_canvas.pack()

        header(self, self.home_canvas)

        div = self.new_row(self.home_canvas)
        button_Top_ten = Button(div, text="Top 10 des potentiel top 50", font=("Arial", 20), bg='white', fg='black')
        button_Top_ten.pack(expand=YES)

        div = self.new_row(self.home_canvas)
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
        self.window.mainloop()


    def new_row(self, canva):
        self.column = 0
        grid = Frame(canva, bg=self.primary_bg, pady=15)
        grid.grid(row=self.row, column=self.column)
        self.row += 1
        return grid

    def new_column(self, canva):
        self.column += 1
        grid = Frame(canva, bg=self.primary_bg)
        grid.grid(row=self.row, column=self.column)
        return grid
