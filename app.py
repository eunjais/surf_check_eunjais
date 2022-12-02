## from python lib yo
import sys, os, re
## from Flask
from flask import (
    Flask, 
    jsonify, 
    request, 
)
from flask_cors import CORS
## from dotenv for env var
from dotenv import load_dotenv
from api_call import get_weather_data

load_dotenv()


## create flask app
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['DEBUG'] = True or os.environ.get('ENV','development') == 'development'
    return app

app = create_app()

## error handling for status code 400
@app.errorhandler(400)
def bad_request(e):
    return '<h1> Bad Request </h1>'

## error handling for status code 404
@app.errorhandler(404)
def page_not_found(e):
    return '<h1> Ooops Not Found </h1>'


## /api/beaches/search?query=<search_string>
@app.route('/api/beaches/search', methods=['GET'])
def api_beaches_search():
    # making sure request is GET
    if request.method == 'GET':
        # check if request args/query is supplied
        if not request.args:
            return jsonify({
                'success': False,
                'message': 'missing query string',
            }), 400
        # check if query params is supplied or set default to empty
        search_query = request.args.get('query', '')

        beach_results = get_weather_data(search_query)

        return jsonify({
            'success': True,
            'data': beach_results,
        })


if __name__ == '__main__':
    PORT = os.environ.get('PORT','8083')
    app.run(host='0.0.0.0', port=int(PORT))
    
