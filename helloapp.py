from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Define an Resource, HelloAPI, below with get method and map it to URLs '/' and '/index/'
# The get method should return a dictionary {'message': 'Hello World!!!'}


if __name__ == '__main__':
    app.run()