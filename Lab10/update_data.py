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
number = input()
  
sql_update_query = f"""Update phonebook set number = '{number}' where username = '{name}'"""
cursor.execute(sql_update_query)

config.commit()
config.close()