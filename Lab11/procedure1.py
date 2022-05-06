
import psycopg2
from config import config
from django.db import connection 

def add_number(id,name,soname,email,nomer):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call add_number(%s,%s,%s,%s,%s)', (id,name,soname,email,nomer))
        conn.commit()
        cur.close()
        
    except:
        update_number(name,nomer)
        print('Этот пользователь уже существует, из за этого поменялся только номер телефона')
        # update_number('Samat','87779870000')
        # conn.commit()
        # cur.close()
    finally:
        if conn is not None:
            conn.close()
        
def update_number(name,nomer):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call update_number(%s,%s)',(name,nomer))
        conn.commit()
        cur.close()
        
    except:
        print('error')
      
    finally:
        if conn is not None:
            conn.close()

add_number(11,"Samat", 'Manapaly','sss_super','87777777777')
   
