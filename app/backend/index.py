from flask import Flask
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return 'Hello World!'

@app.route('/items/<int:count>', methods=['GET'])
@cross_origin()
def items(count):
    return f'{count}'

if __name__ == '__main__':
    app.run()
