"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from .models import Movie
from .forms import MovieForm
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'uploads'

    from . import db
    db.init_app(app)

    @app.route('/')
    def index():
        return jsonify(message="This is the beginning of our API")

    @app.route('/api/v1/movies', methods=['POST'])
    def add_movie():
        form = MovieForm()
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            poster_img = form.poster.data
            filename = secure_filename(poster_img.filename)
            poster_img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            movie = Movie(title, description, filename)
            db.session.add(movie)
            db.session.commit()
            result = jsonify({
                "message": "Movie Successfully added",
                "title": title,
                "poster": filename,
                "description": description
            })
            return result
        else:
            errors = form_errors(form)
            error_list = {"errors": errors}
            return jsonify(error_list)

    @app.route('/api/v1/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        data = []
        for movie in movies:
            data.append({
                "id": movie.id,
                "title": movie.title,
                "description": movie.description,
                "poster": url_for('get_poster', filename=movie.poster)
            })
        return jsonify(mov=data)

    @app.route('/api/v1/posters/<filename>')
    def get_poster(filename):
        return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

    @app.route('/api/v1/csrf-token', methods=['GET'])
    def get_csrf_token():
        return jsonify({'csrf_token': generate_csrf()})

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app


def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (getattr(form, field).label.text, error)
            error_messages.append(message)
    return error_messages
