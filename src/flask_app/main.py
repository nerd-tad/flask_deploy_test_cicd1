from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return 'initiated successfully!'
    
@app.route('/check-secrets')
def check_secrets():
    #if length of secret keys compared are equal voila.
    if len(os.environ.get('SECRET_KEY')) == 19:
        return 'OK'
    else:
        return 'NOT_OK'
    
@app.route('/dummy-data')
def dummy_data():
    return jsonify(
        {
            'title':'struggle',
            'body': 'you can never dared imagine how it will hit you.'
        }
    )
    
if __name__ == '__main__':
    app.run(debug=True, port=10001)
    
  
