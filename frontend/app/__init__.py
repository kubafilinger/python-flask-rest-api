from flask import Flask, render_template
import requests

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def music():
        api_key = 'tajnyklucz'
        url = 'http://127.0.0.1:5000/music'
        params = {'API_KEY': api_key}

        response = requests.get(url, params=params)
        music = response.json()

        return render_template('base.html', music=music)
    return app