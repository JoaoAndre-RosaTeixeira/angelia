from tkinter import *

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from interface_graphique.pages.header import header


class Top_ten:
    primary_bg = "#d4d4d4"
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)


    def start(self):
        header(self, self.frame_canvas)

        # div = self.new_row()
        # self.top_window = Frame(div, width=self.width, height=self.height/1.5, bg='white')
        # self.top_window.pack(expand=YES)
        # button_deezer = Button(self.top_window, text="Home", padx=15, font=("Arial", 20), bg='white', fg='black',
        #                        command=self.end)
        # button_deezer.pack(expand=YES, side=TOP, pady=15)
        #
        # div = self.new_column()
        #
        #
        # #is work
        # # plt.xlabel("duration")
        # # plt.ylabel("popularity")
        # # plt.scatter(self.database.songs.get_duration(), self.database.songs.get_popularity(), color="blue")
        # # plt.savefig('plot1.png')
        # # image = PhotoImage(file="plot1.png").zoom(31).subsample(50)
        #
        # df_chansons = pd.read_csv("ressource\chansons.csv")
        #
        # heatmap = sns.heatmap(df_chansons.corr())
        # heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 12}, pad=12, x=50)
        # heatmap.figure.savefig('heatmap_figure.png', dpi=600)
        #
        # image = PhotoImage(file="heatmap_figure.png").subsample(6)
        #
        #
        # frame_canvas = Canvas(self.top_window, width=self.width, height=self.height/1.5, bg=self.primary_bg, bd=1, relief=SOLID)
        # frame_canvas.create_image(self.width / 2, self.height / 3, image=image)
        # frame_canvas.pack(expand=YES)
        #
        # plt.close()

        self.window.mainloop()

    def end(self):
        self.frame_canvas.destroy()
        self.start()

