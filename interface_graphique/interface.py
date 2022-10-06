from tkinter import *

from database.sql_class.Database import Database
import matplotlib.pyplot as plt

from interface_graphique.pages.Home import Home

class Main:
    primary_bg = "#d4d4d4"
    window = Tk()
    window.title("Angelia")
    window.geometry("1400x800")
    window.minsize(480, 360)
    window.iconbitmap("ressource\image\logo.ico")
    window.config(background=primary_bg)
    ressource_data = "ressource\Sources_data.db"
    width = window.winfo_width()
    height = window.winfo_height()

    home = Home(window, width, height)

    def start(self):
        self.home.start()



    # def new_label(self, label):
    #    label.pack(expand=YES)

    #
    # def new_window(self):
    #     self.frame_container.destroy()
    #     self.frame_container.config(bg=self.primary_bg, width=self.width, height=self.height)
    #     self.frame_container.pack(expand=True)
    #     print(self.frame_container)


    # plt.xlabel("duration")
    # plt.ylabel("popularity")
    # plt.scatter(Database.songs.get_duration(), Database.songs.get_popularity(), color="blue")
    # plt.savefig('plot1.png')
    #
    # width = 400
    # height = 300
    #
    # image = PhotoImage(file="plot1.png").zoom(31).subsample(50)
    #
    # frame_canvas = Canvas(frame_data, width=width, height=height, bg=primary_bg, bd=1, relief=SOLID)
    # frame_canvas.create_image(width / 2, height / 2, image=image)
    # frame_canvas.pack(expand=YES)
    #
    # plt.close()

    # colones_for_table_interface = ["name", "popularity", "artists"]
    # l = 0 # futur usation for grid or canvas for table
    # c = 0 # futur usation for grid or canvas for table
    # for colone in colones_for_table_interface:
    #     data_colone = Frame(frame_data, bg=primary_bg, bd=1, relief=SOLID)
    #     colone_value = Label(data_colone, text=colone, font=("Arial", 10), bg=primary_bg)
    #     colone_value.pack(side=TOP, expand=YES)
    #     for song in database.songs:
    #         data_line = Frame(data_colone, bg=primary_bg, bd=1, relief=SOLID)
    #         if colone == "artists":
    #             for artist in song.artists:
    #                 colone_value = Label(data_line, text=f"({artist.name})", font=("Arial", 10), bg=primary_bg)
    #                 colone_value.pack(side=LEFT, expand=YES)
    #         else:
    #             colone_value = Label(data_line, text=getattr(song, colone), font=("Arial", 10), bg=primary_bg)
    #             colone_value.pack(side=LEFT, expand=YES)
    #         data_line.pack(expand=YES)
    #     data_colone.pack(side=LEFT, expand=YES)
