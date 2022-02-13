import database

def insert_review(review, rating, listing_id, user_id):
    database.sql_write("INSERT INTO reviews (review, rating, listing_id, user_id) VALUES (%s, %s, %s, %s);", [
        review,
        rating,
        listing_id,
        user_id,
    ])

def get_reviews(listing_id):
    return database.sql_select("SELECT * FROM reviews WHERE listing_id = %s", [listing_id])

def get_all_reviews():
    return database.sql_select("SELECT * FROM reviews", [])
