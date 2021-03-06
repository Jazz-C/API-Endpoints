from flask import Flask, jsonify
from models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    setup_db(app)
    cors = CORS(app)

    # CORS Headers 
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    @app.route('/plants')
    def get_plants():
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
            'success': True,
            'plants': formatted_plants
        })


    return app