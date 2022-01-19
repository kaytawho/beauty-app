from flask import Blueprint, request, session, redirect, render_template
from models.listing import delete_listing, get_all_listings, get_listing, insert_listing, update_listing

listing_controller = Blueprint("listing_controller", __name__, template_folder="../templates/listings")

@listing_controller.route('/listings')
def listings():
    listing_items = get_all_listings()

    return render_template('listings.html', listing_items=listing_items)

@listing_controller.route('/listings/create')
def create():
    if not session.get('user_id'):
        return redirect('/login')
    return render_template('create.html')
        
@listing_controller.route('/listings', methods=["POST"])
def insert():
    if not session.get('user_id'):
        return redirect('/login')
    # INSERT INTO DB
    insert_listing(
        request.form.get('name'),
        request.form.get('state'),
        request.form.get('suburb'),
        request.form.get('image_url'),
        request.form.get('website'),
        request.form.get('description'),
        session.get('user_id'),
    )

    return redirect('/')

@listing_controller.route('/listings/<id>')
def show(id):
    listing = get_listing(id)
    return render_template('show.html', listing=listing)

@listing_controller.route('/listings/<id>/edit')
def edit(id):
    if not session.get('user_id'):
        return redirect('/login')
    listing = get_listing(id)
    return render_template('edit.html', listing=listing)

@listing_controller.route('/listings/<id>', methods=["POST"])
def update(id):
    if not session.get('user_id'):
        return redirect('/login')
    name = request.form.get("name")
    state = request.form.get("state")
    suburb = request.form.get("suburb")
    image_url = request.form.get("image_url")
    website = request.form.get("website")
    description = request.form.get("description")
    # UPDATE
    update_listing(name, state, suburb, image_url, website, description, id)
    return redirect('/')

@listing_controller.route('/listings/<id>/delete', methods=["POST"])
def delete(id):
    if not session.get('user_id'):
        return redirect('/login')
    delete_listing(id)
    return redirect('/')