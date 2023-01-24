from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

app.config['SECRET_KEY'] = 'INITIATING ONLINE TESTS'

@app.route('/')
def home():
    return 'initiated successfully!'
    
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
    
  