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
"""
create or replace procedure delete_user(
    user_name varchar
)
as $$
begin
    delete from phonebook_lab11 where username = user_name;
end;
$$
language plpgsql;
"""
)
config.commit()
current.close()
config.close()