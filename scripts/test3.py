from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/receive_message', methods=['POST'])
@cross_origin()
def store_data():
    data = request.json['message']
    print(data)
    return 'Data received'

if __name__ == '__main__':
    app.run(host = "localhost", port=8000, debug = True)