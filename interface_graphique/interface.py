from tkinter import *
from database.sql_class.Database import Database


def start():
    primary_bg = "#d4d4d4"
    window = Tk()

    window.title("Angelia")
    window.geometry("1080x720")
    window.minsize(480, 360)
    window.iconbitmap("ressource\image\logo.ico")
    window.config(background=primary_bg)
    ressource_data = "ressource\Sources_data.db"

    database = Database(ressource_data)

    frame_container = Frame(window, bg=primary_bg)

    frame_tittle = Frame(frame_container, bg=primary_bg)

    label_title = Label(frame_tittle, text="bienvenue sur Angelia", font=("Arial", 36), bg=primary_bg)
    label_title.pack()

    label_subtitle = Label(frame_tittle, text="IA de prediction de popularité des musiques", font=("Arial", 22),
                           bg=primary_bg)
    label_subtitle.pack()

    frame_data = Frame(frame_container, bg=primary_bg)
    l = 0

    colones_for_table_interface = ["name", "popularity", "artists"]

    for colone in colones_for_table_interface:
        data_colone = Frame(frame_data, bg=primary_bg)
        colone_value = Label(data_colone, text=colone, font=("Arial", 10), bg=primary_bg)
        colone_value.pack(side=TOP)
        for song in database.songs:
            if colone == "artists":
                for artist in song.artists:
                    colone_value = Label(data_colone, text=artist.name, font=("Arial", 10), bg=primary_bg)
                    colone_value.pack(side=TOP)
            else:
                colone_value = Label(data_colone, text=getattr(song, colone), font=("Arial", 10), bg=primary_bg)
                colone_value.pack(side=TOP)
        data_colone.pack(side=LEFT, expand=YES)




    # for colone in colones_for_table_interface:
    #     data_line = Frame(frame_data, bg=primary_bg)
    #     new_frame = Frame(data_line, bg=primary_bg, bd=1,
    #                       relief=SOLID)
    #     new_label = Label(new_frame, text=colone, font=("Arial", 10), bg=primary_bg)
    #     new_frame.pack()
    #     new_label.pack()
    #     data_line.pack(side=LEFT)
    # for data_song in database.songs:
    #     data_line = Frame(frame_data, bg=primary_bg)
    #     new_frame = Frame(data_line, bg=primary_bg, bd=1,
    #               relief=SOLID)
    #     new_label = Label(new_frame, text=data_song.name, font=("Arial", 10), bg=primary_bg)
    #     new_label.pack(side=LEFT)
    #     new_frame.pack(side=LEFT)
    #     data_line.pack()
    #     l += 1

    frame_tittle.pack(expand=YES)
    frame_data.pack(expand=YES)

    frame_container.pack(expand=YES)

    window.mainloop()
