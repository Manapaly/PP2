
create or replace procedure add_name(
    username varchar,

)
as $$
declare
    return_username VARCHAR;
begin
    insert into phonebook_lab11(username)
    values(username)
    returning username into return_username;
    insert into phonebook_lab11(username)
    values(return_username);
end;
$$
language plpgsql;
"""
create or replace procedure add_number(
    userid integer,
    user_name varchar,
    user_soname varchar,
    e_mail varchar,
    user_number varchar
)
as $$

begin
    insert into phonebook_lab11(user_id,username,usersoname,email,usernumber) values (userid,user_name,user_soname,e_mail,user_number);
end;
$$
language plpgsql;
"""
"""
create or replace procedure update_number(
    user_name varchar,
    user_number varchar
)
as $$

begin
    Update phonebook_lab11 set usernumber = user_number where username = user_name;
end;
$$
language plpgsql;
"""
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