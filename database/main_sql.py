import sqlite3



def create_connection(db_file):
    print("hello")
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        print("Base de données crée et correctement connectée à SQLite")
        sql = "SELECT name, popularity from chansons ORDER BY popularity DESC LIMIT 10;"
        cur.execute(sql)
        res = cur.fetchall()
        print("Données class created")        
        #for p in res:
        #    print(f"{p}\n")
        cur.close()
        conn.close()
        print("La connexion SQLite est fermée")
        return res
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)
    finally:
        if conn:
            conn.close()




