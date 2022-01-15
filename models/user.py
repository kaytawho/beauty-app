import database
import bcrypt

def insert_user(name, email, password):
    # Decode the generated hash to convert it to a string to insert into DB
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT INTO users (name, email, password)"
        + " VALUES(%s, %s, %s)", [name, email, password])

def get_user(id):
    pass

def get_user_by_email(email):
    results = database.sql_select("SELECT * FROM users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None

def get_all_users():
    pass

def update_user(id, name, email):
    pass

def delete_user(id):
    pass