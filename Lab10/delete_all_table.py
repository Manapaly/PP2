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

sql_update_query = f"""DELETE FROM phonebook"""
cursor.execute(sql_update_query)

config.commit()
config.close()