import psycopg2
  
def add_name(name, score, level,tablename):
    config = psycopg2.connect(
            host='localhost', 
            database='postgres',
            port = '5433',
            user='postgres',
            password='321qaz'
            )
  
    config.autocommit = True
    cursor = config.cursor()
  
    sql = f"""INSERT INTO {tablename} (username, user_score, user_level) VALUES ('{name}', '{score}', '{level}');"""
  
    cursor.execute(sql)
  
    config.commit()
    config.close()
def update_score(name, score, level,tablename):
    config = psycopg2.connect(
            host='localhost', 
            database='postgres',
            port = '5433',
            user='postgres',
            password='321qaz'
            )
  
    config.autocommit = True
    cursor = config.cursor()
  
    sql_update_query = f"""Update {tablename} set user_score = '{score}' where username = '{name}'"""
    sql_update_query1 = f"""Update {tablename} set user_level = '{level}'  where username = '{name}'"""
    cursor.execute(sql_update_query)
    cursor.execute(sql_update_query1)
  
    config.commit()
    config.close()
def update_record(name,tablename,new_score):
    config = psycopg2.connect(
        host='localhost', 
        database='postgres',
        port = '5433',
        user='postgres',
        password='321qaz'
        )
    config.autocommit = True
    cursor = config.cursor()
    
    sql = f"""Update {tablename} set рекорд = '{new_score}' where username = '{name}'"""
    cursor.execute(sql)
    
#     for i in cursor.fetchall():
#         score = i
#     old_score = score[0]    
# #     print(type(int(old_score)))
#     old_score = int(old_score)
#     print(old_score)
#     if new_score > old_score:
#             cursor.execute(f"""Update {tablename} set рекорд = '{new_score}' where username = '{name}'""")

    config.commit()
    config.close()

def check_data(name,tablename):
    config = psycopg2.connect(
            host='localhost', 
            database='postgres',
            port = '5433',
            user='postgres',
            password='321qaz'
            )
  
    config.autocommit = True
    cursor = config.cursor()
  
    sql_update_query = f"""Select * from {tablename} where username != '' """
    
    cursor.execute(sql_update_query)
    names = []
    for i in cursor.fetchall():
        names.append(i[1])
    if name in names:
            return False
    else:
            return True    
    config.commit()
    config.close()
def record(tablename,name):
    config = psycopg2.connect(
        host='localhost', 
        database='postgres',
        port = '5433',
        user='postgres',
        password='321qaz'
        )
    config.autocommit = True
    cursor = config.cursor()
    
    sql = f"""Select user_score from {tablename} where username = '{name}'"""
    cursor.execute(sql)
    for i in cursor.fetchall():
        return int(i[0])
    config.commit()
    config.close()
    
    
# check_data('SSS','snake')
# update_record('Samat','snake',213)
print(record('snake','Ernat'))
# sql2 = f'''DELETE FROM phonebook
# WHERE username='{name}' ;'''