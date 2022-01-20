from flask import Blueprint, request, session, redirect, render_template
from controllers.listing_controller import listings
from models.review import delete_review, get_all_reviews, get_reviews, insert_review, update_review
from models.listing import get_listing

review_controller = Blueprint("review_controller", __name__, template_folder="../templates/reviews")

@review_controller.route('/listings/<listingId>/reviews')
def reviews(listingId):
    review_items = get_reviews(listingId)
    listing = get_listing(listingId)
    return render_template('reviews.html', review_items=review_items, listing=listing)

@review_controller.route('/listings/<listingId>/reviews/create')
def create(listingId):
    if not session.get('user_id'):
        return redirect('/login')
    listing = get_listing(listingId)
    return render_template('create-review.html', listing=listing)
        
@review_controller.route('/listings/<listingId>/reviews', methods=["POST"])
def insert(listingId):
    if not session.get('user_id'):
        return redirect('/login')
    listing = get_listing(listingId)
    # INSERT INTO DB
    insert_review(
        request.form.get('review'),
        request.form.get('rating', type=int),
        listingId,
        session.get('user_id')
    )

    return redirect(f'/listings/{listingId}/reviews', listing=listing)


##CODE BELOW NEEDS ATTENTION

# @review_controller.route('/listings/<listingId>/reviews')
# def show(listingId):
#     reviews = get_reviews(listingId)
#     return render_template('show-review.html', reviews=reviews)

# @review_controller.route('/listings/<listingId>/reviews/<reviewId>')
# def edit(listingId, reviewId):
#     if not session.get('user_id'):
#         return redirect('/login')
#     review = get_reviews(listingId)
#     return render_template('edit-review.html', review=review)

# @review_controller.route('/listings/<listingId>/reviews/<reviewId>', methods=["POST"])
# def update(listingId, reviewId):
#     if not session.get('user_id'):
#         return redirect('/login')
#     review = request.form.get('review'),
#     rating = request.form.get('rating'),
#     session.get('user_id'),
#     # UPDATE
#     update_review(review, rating, id)
#     return redirect('/')

# @review_controller.route('/listings/<listingId>/reviews/<reviewId>/delete', methods=["POST"])
# def delete(reviewId):
#     if not session.get('user_id'):
#         return redirect('/login')
#     delete_review(reviewId)
#     return redirect('/')