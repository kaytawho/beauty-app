import database


# INSERT REVIEW INTO DB
def insert_review(review, rating, listing_id, user_id):
    database.sql_write("INSERT INTO reviews (review, rating, listing_id, user_id) VALUES (%s, %s, %s, %s);", [
        review,
        rating,
        listing_id,
        user_id,
    ])

# SELECT REVIEW FROM DB
def get_reviews(listing_id):
    results = database.sql_select("SELECT * FROM reviews WHERE listing_id = %s", [listing_id])
    return results

# SELECT ALL REVIEW FROM DB
def get_all_reviews():
    results = database.sql_select("SELECT * FROM reviews", [])
    return results
