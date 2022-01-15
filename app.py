from flask import Flask, redirect, render_template
import os
import psycopg2

# DB_URL = os.environ.get("DATABASE_URL", "dbname=beauty_app")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from controllers.listing_controller import listing_controller
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller


@app.route('/')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', []) # Query to check that the DB connected
    conn.close()
    return redirect('/listings')

@app.route('/about')
def about():
    return render_template('about.html')

## Controllers
app.register_blueprint(listing_controller)
app.register_blueprint(session_controller)
app.register_blueprint(user_controller)



if __name__ == "__main__":
    app.run(debug=True)