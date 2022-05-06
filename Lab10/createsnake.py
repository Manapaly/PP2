#create
import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5433',
    user='postgres',
    password='321qaz'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE SNAKE(
        username  VARCHAR(12),
        user_score  VARCHAR(12),
        user_level VARCHAR(12)
    )
    '''
)
config.commit()
current.close()
config.close()