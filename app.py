import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db,db_drop_and_create_all, Movie, Actor
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  #db_drop_and_create_all()

  @app.after_request
  def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

  # ROUTES

  @app.route('/', methods=['GET'])
  def greeting():

    return jsonify({
        'success': True,
        'message':'Hello world!, This is capstone project'
    }), 200
  
  @app.route('/actors', methods=['GET'])
  @requires_auth('get:actors')
  def get_actors(jwt):
    
    # Get all actors from DB
    actors = Actor.query.all()
    formatted_actors = [actor.format() for actor in actors]

    if len(actors) == 0:
            abort(404)

    return jsonify({
        'success': True,
        'actors': formatted_actors
    }), 200

  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(jwt):
    
    # Get all movies from DB
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]

    if len(movies) == 0:
            abort(404)

    return jsonify({
        'success': True,
        'movies': formatted_movies
    }), 200

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(jwt,actor_id):

    # Get the actor by the given id
    actor = Actor.query.filter(
        Actor.id == actor_id).one_or_none()

    if actor is None:
        abort(404)
    try:
        actor.delete()

        return jsonify({
            'success': True,
            'deleted_id': actor_id
        }), 200

    except:
        abort(422)

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(jwt, movie_id):

    # Get the movie by the given id
    movie = Movie.query.filter(
        Movie.id == movie_id).one_or_none()

    if movie is None:
        abort(404)
    try:
        movie.delete()

        return jsonify({
            'success': True,
            'deleted_id': movie_id
        }), 200

    except:
        abort(422)

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def add_new_actor(jwt):

    try:
        body = request.get_json()
        actor_name = body['name']
        actor_age = body['age']
        actor_gender = body['gender']

        new_actor = Actor(name=actor_name,
                          age=actor_age, gender=actor_gender
                          )

        new_actor.create()

        return jsonify({
            'success': True,
            'new_actor': new_actor.format()
        }), 200

    except:
        abort(422)
  
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def add_new_movie(jwt):

    try:
        body = request.get_json()
        movie_title = body['title']
        movie_release_date = body['release_date']

        new_movie = Movie(title=movie_title,
                          release_date=movie_release_date
                          )

        new_movie.create()

        return jsonify({
            'success': True,
            'new_movie': new_movie.format()
        }), 200

    except:
        abort(422)

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(jwt, actor_id):

    # Get the actor by the given id
    actor = Actor.query.filter(
        Actor.id == actor_id).one_or_none()

    if actor is None:
        abort(404)

    try:

        body = request.get_json()

        if 'name' in body:
            actor.name = body['name']

        if 'age' in body:
            actor.age = body['age']
 
        if 'gender' in body:
            actor.gender = body['gender']

        actor.update()

        return jsonify({
            'success': True,
            'updated_actor': actor.format()
        }), 200

    except:
        abort(422)
  
  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(jwt, movie_id):

    # Get the movie by the given id
    movie = Movie.query.filter(
        Movie.id == movie_id).one_or_none()

    if movie is None:
        abort(404)

    try:

        body = request.get_json()

        if 'title' in body:
            movie.title = body['title']

        if 'release_date' in body:
            movie.release_date = body['release_date']
 
        movie.update()

        return jsonify({
            'success': True,
            'updated_movie': movie.format()
        }), 200

    except:
        abort(422)

  # Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404
  
  @app.errorhandler(401)
  def method_not_allowed(error):
      return jsonify({
          'success': False,
          'error': 401,
          'message': 'method not allowed'
      }), 401

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          'success': False,
          'error': 400,
          'message': 'bad request'
      }), 400

  @app.errorhandler(AuthError)
  def handle_auth_error(error):
    response = jsonify(error.error)
    response.status_code = error.status_code
    return response
  return app
  
app = create_app()

if __name__ == '__main__':
    app.run()