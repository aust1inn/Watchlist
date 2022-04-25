from flask import render_template
from app import app


@app.route('/')
def index():
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title)

@app.route('/movie/<int:movie_id>')
def movies(movie_id):
    return render_template('movie.html', id = movie_id)
