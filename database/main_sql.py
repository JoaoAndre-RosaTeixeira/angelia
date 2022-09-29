import sqlite3


def create_connection(db_file):
    print("hello")
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        print("Base de données crée et correctement connectée à SQLite")
        sql = "SELECT *;"
        cur.execute(sql)
        res = cur.fetchall()
        print("La version de SQLite est: ", res)
        cur.close()
        conn.close()
        print("La connexion SQLite est fermée")
    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)
    finally:
        if conn:
            conn.close()




