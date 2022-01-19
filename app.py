from flask import Flask, redirect, render_template
import os
import psycopg2

SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from controllers.listing_controller import listing_controller
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.review_controller import review_controller


@app.route('/')
def index():
    return redirect('/listings')


## Controllers
app.register_blueprint(listing_controller)
app.register_blueprint(session_controller)
app.register_blueprint(user_controller)
app.register_blueprint(review_controller)



if __name__ == "__main__":
    app.run(debug=True)