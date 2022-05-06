
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
  
  
sql = '''COPY phonebook_lab11(user_id,username,usersoname,email,usernumber)
FROM 'D:\pp\pp2\LAB11A\data.csv'
DELIMITER ' '
CSV HEADER;'''
  
cursor.execute(sql)
  
sql3 = '''select * from phonebook_lab11;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
config.commit()
config.close()