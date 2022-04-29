import psycopg2

try:
    # connect to exist database
    config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5433',
    user='postgres',
    password='321qaz'
    )
    config.autocommit = True
    
    # the cursor for perfoming database operations
    # cursor = connection.cursor()
    

    name = str(input())
    number = str(input())
        
    # insert data into a table
    with config.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO phonebook (username, number) VALUES
            ('{name}', '{number}');"""
        )
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)