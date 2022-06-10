import os
from flask import Flask, jsonify, abort, request
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movies, Castings
from auth import AuthError, requires_auth
import json
import sys


def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  

  # @app.route('/')
  # def index():
  #   return "Welcome to the last project "

  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies_list(payload):
    
    list_movies = Movies.query.order_by('id').all()
    movies_details = [i.format() for i in list_movies]
    
    if len(list_movies) == 0:
      abort(404)

    return jsonify({
      'movies': movies_details,
      'permissions': payload['permissions']
    })

  @app.route('/castings', methods=['GET'])
  @requires_auth('get:castings')
  def get_castings_list(payload):

    list_castings = Castings.query.order_by('id').all()
    castings_details = [i.format() for i in list_castings]
    
    if len(list_castings) == 0:
      abort(404)

    return jsonify({
      'movies': castings_details,
      'permissions': payload['permissions']
    })

  @app.route('/movies/create', methods=['POST'])
  @requires_auth('post:movie')
  def post_movie(payload):
    
    body = request.get_json()
    # try:
    movie_title = body.get('title', None)
    movie_release = body.get('release_date', None)
    if not movie_title or not movie_release:
      abort(400)
    else:
      new_movies_list = Movies(title=movie_title, release_date=movie_release)
      new_movies_list.insert()

      return jsonify({
      "success": True,
      'permissions': payload['permissions']})
   


  @app.route('/castings/create', methods=['POST'])
  @requires_auth('post:casting')
  def post_casting(payload):
    body = request.get_json()
    casting_name = body.get('name', None)
    casting_age = body.get('age', None)
    casting_gender = body.get('gender', None)
    
    if not casting_name or not casting_age or not casting_gender:
      abort(400)
    else:
      new_casting_list = Castings(name=casting_name, age=casting_age, gender=casting_gender)
    
      new_casting_list.insert()
    
    return jsonify({
    "success": True,
    'permissions': payload['permissions']})
    

  @app.route('/movies/<int:movie_id>/edit', methods=['PATCH'])
  @requires_auth('patch:movie')
  def update_movie(payload, movie_id):
    movie = Movies.query.filter(Movies.id==movie_id).one_or_none()
  
    body = request.get_json()
    movie_title = body.get('title', None)
    movie_release = body.get('release_date', None)
    if not movie_title:
      abort(400)
    else:
      movie.title = movie_title
      movie.release_date = movie_release
      movie.update()

      return jsonify({
      "success": True,
      'permissions': payload['permissions']})
    

  @app.route('/castings/<int:casting_id>/edit', methods=['PATCH'])
  @requires_auth('patch:casting')
  def update_castings(payload, casting_id):
    casting = Castings.query.filter(Castings.id==casting_id).one_or_none()
    body = request.get_json()
    
    casting_name = body.get('name', None)
      
    casting_age = body.get('age', None)
    casting_gender = body.get('gender', None)
    if not casting_name:
      abort(400)
    else:
      casting.name = casting_name
      casting.age = casting_age
      casting.gender = casting_gender
      casting.update()

      return jsonify({
      "success": True,
      'permissions': payload['permissions']})
    

  @app.route('/castings/<int:casting_id>', methods=['DELETE'])
  @requires_auth('patch:casting')
  def delete_casting(payload, casting_id):
    try:
      casting = Castings.query.filter(Castings.id==casting_id).one_or_none()
      casting.delete()
      return jsonify({
      "success": True,
      'permissions': payload['permissions']})

    except:
      abort(400)


  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload, movie_id):
    try:
      movie = Movies.query.filter(Movies.id==movie_id).one_or_none()
      movie.delete()
      return jsonify({
      "success": True,
      'permissions': payload['permissions']})

    except:
      abort(400)


  @app.errorhandler(404)
  def not_found(error):
          return (
              jsonify({"success": False, "error": 404,
                      "message": "resource not found"}),
              404,
          )

  @app.errorhandler(422)
  def unprocessable(error):
          return (
              jsonify({"success": False, "error": 422,
                      "message": "unprocessable"}),
              422,
          )

  @app.errorhandler(400)
  def bad_request(error):
          return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
          return (
              jsonify({"success": False, "error": 405,
                      "message": "method not allowed"}),
              405,
          )

  @app.errorhandler(500)
  def server_error(error):

          return (
              jsonify({"success": False, "error": 500,
                      "message": "Internal Server Error"}),
              500,
          )
  
  return app

APP = create_app()
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)

# if __name__ == '__main__':
#     APP.run(host='0.0.0.0', port=8080, debug=True)

#curl -d '{"title": "John Wick: Chapter 2", "release_date": "2017-06-13"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8080/movies/create 