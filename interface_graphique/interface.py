from tkinter import *
from database.main_sql import create_connection
from database.sql_class.Database import Database
import pandas as pd



def start():
    primary_bg = "#d4d4d4"
    window = Tk()

    window.title("Angelia")
    window.geometry("1080x720")
    window.minsize(480,360)
    window.iconbitmap("ressource\image\logo.ico")
    window.config(background= primary_bg)

    
    

    

    print("test")
    new_data = create_connection(r"ressource\Sources_data.db")
        
    data_sql = Database(new_data)

    frame_container = Frame(window, bg=primary_bg)  

    frame_tittle = Frame(frame_container, bg=primary_bg)    

    label_title = Label(frame_tittle, text="bienvenue sur Angelia", font=("Arial", 36), bg=primary_bg)
    label_title.pack()

    label_subtitle = Label(frame_tittle, text="IA de prediction de popularité des musiques", font=("Arial", 22), bg=primary_bg)
    label_subtitle.pack()

    frame_data = Frame(frame_container, bg=primary_bg)
    
    for data in data_sql.data:
        data_extract = Label(frame_data, text=data, font=("Arial", 10), bg=primary_bg )
        data_extract.pack()
        
    frame_tittle.pack(expand=YES)
    frame_data.pack(expand=YES)

    frame_dashboard_container = Frame(frame_container, bg=primary_bg)
    frame_dashboard = Label(frame_data, text=data, font=("Arial", 10), bg=primary_bg )
    df = pd.DataFrame(data_sql.data)


    
    frame_container.pack(expand=YES)

    window.mainloop()