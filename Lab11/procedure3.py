
from tkinter import EXCEPTION
import psycopg2
from config import config

def delete_user(name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call delete_user(%s)',(name,))
        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
      
    finally:
        if conn is not None:
            conn.close()

delete_user("Samat")
   
