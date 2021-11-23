from werkzeug.wrappers import request, Response
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Hello(Resource):
  def get(self):
    return jsonify({'message': 'hello python'})
  def post(self):
    data = request.get__json()
    return jsonify({'data': data}), 201
class Square(Resource):
  def get(self, num):
    return jsonify({'square': num**2})
    
class Cube(Resource):
  def get(self, num):
    return jsonify({'cube': num**3})

class Simpleintrest(Resource):
  def get(self, p,r,t):
    return jsonify({'simpleintrest': (p*r*t)/100})

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Cube, '/cube/<int:num>')
api.add_resource(Simpleintrest, '/si/p/<int:p>/r/<int:r>/t/<int:t>')

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 9001, app)
  