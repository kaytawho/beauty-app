import database

def insert_listing(name, state, suburb, image_url, website, description, user_id):
    database.sql_write("INSERT INTO listings(name, state, suburb, image_url, website, description, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s);", [
        name,
        state,
        suburb,
        image_url,
        website,
        description,
        user_id
    ])

def get_listing(id):
    results = database.sql_select("SELECT * FROM listings WHERE id = %s", [id])
    result = results[0]
    return result

def get_all_listings():
    results = database.sql_select("SELECT * FROM listings", [])
    return results

def update_listing(name, state, suburb, image_url, website, description, id):
    database.sql_write("UPDATE listings set name = %s, state = %s, suburb = %s, image_url = %s, website = %s, description = %s WHERE id = %s", [
        name,
        state,
        suburb,
        image_url,
        website,
        description,
        id
    ])

def delete_listing(id):
    database.sql_write("DELETE FROM listings WHERE id = %s", [id])
