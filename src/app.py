from random import choice
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html', url=get_url()) 
    
    return app


def get_url():
    return choice(open('src/images').read().splitlines())
