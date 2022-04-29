
import psycopg2
  
config = psycopg2.connect(
        host='localhost', 
        database='postgres',
        port = '5433',
        user='postgres',
        password='321qaz'
        )
  
config.autocommit = True
cursor = config.cursor()
  
name = input()

  
sql2 = f'''DELETE FROM phonebook
WHERE username='{name}' ;'''
  
cursor.execute(sql2)

config.commit()
config.close()