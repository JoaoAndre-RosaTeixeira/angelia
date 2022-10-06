from tkinter import *

from interface_graphique.pages.Spotify import Spotify
from interface_graphique.pages.Template import Template
from interface_graphique.pages.Top_ten import Top_ten
from interface_graphique.pages.Youtube import Youtube


class Home(Template):
    primary_bg = "#d4d4d4"

    def __init__(self, window, width, height):
        super().__init__()
        self.top_ten = Top_ten(window, width, height)
        self.youtube = Youtube(window, width, height)
        self.spotify = Spotify(window, width, height)
        self.window = window
        self.width = width
        self.height = height
        self.image = PhotoImage(file="background.png")
        self.image.zoom(4, 4)
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)
        self.frame_canvas.create_image(self.image.width() / 2, self.image.height() / 2, image=self.image)

        # self.image = PhotoImage(file="background.png")
        #
        # self.frame_image = Canvas(self.window, width=self.width, height=self.height, bg=self.primary_bg, bd=1,
        #                       relief=SOLID)
        # self.frame_image.create_image(self.width / 2, self.height / 3.5, image=self.image)


        self.row = 0
        self.column = 0


    def start(self):
        self.row = 0
        self.column = 0

        # self.frame_image.pack()
        self.frame_canvas.pack(expand=YES)
        self.header()

        div = self.new_row()
        button_Top_ten = Button(div, text="Potentiel top 50", font=("Arial", 20), bg='white', fg='black', command=self.Button_topten)
        button_Top_ten.pack(expand=YES, side=LEFT, padx=15)

        button_spotifiy = Button(div, text="Spotify stats", padx=15, font=("Arial", 20), bg='white', fg='black', command=self.Button_spotify)
        button_spotifiy.pack(expand=YES, side=LEFT, padx=15)

        # for song in self.database.songs.songs:
        #     div = header.new_row()
        #     label_title = Label(div, text=song.popularity, font=("Courrier", 36), bg=self.primary_bg, padx=30)
        #     label_title.pack(expand=YES)
        self.window.mainloop()


