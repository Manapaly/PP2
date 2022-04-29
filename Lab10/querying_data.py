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
  
  
sql = '''SELECT * FROM phonebook'''
sql1 = '''SELECT USERNAME FROM phonebook'''
sql2 = '''SELECT number from phonebook'''
  
cursor.execute(sql2)

for i in cursor.fetchall():
    print(*i)
  
config.commit()
config.close()