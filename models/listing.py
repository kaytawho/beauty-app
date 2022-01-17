import database


# INSERT INTO DB
def insert_listing(name, state, suburb, image_url, website, description):
    database.sql_write("INSERT INTO listings(name, state, suburb, image_url, website, description) VALUES (%s, %s, %s, %s, %s, %s);", [
        name,
        state,
        suburb,
        image_url,
        website,
        description,
    ])

# SELECT LISTING FROM DB
def get_listing(id):
    results = database.sql_select("SELECT id, name, state, suburb, image_url, website, description FROM listings WHERE id = %s", [id])
    result = results[0]
    return result

# SELECT ALL LISTINGS FROM DB
def get_all_listings():
    results = database.sql_select("SELECT id, name, state, suburb, image_url, website, description FROM listings", [])
    return results

# UPDATE LISTINGS IN DB
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

# DELETE LISTING FROM DB
def delete_listing(id):
    database.sql_write("DELETE FROM listings WHERE id = %s", [id])
