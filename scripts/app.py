from flask import Flask, request, jsonify
import requests
from flask_cors import cross_origin, CORS
import connectAPI as CAP

app = Flask(__name__)
app.config['CORS_HEADERS'] = "Content-Type"
CORS(app)

# cors = CORS(app, resources={r"/receive_message": {"origins": "http://localhost:5500"}})

@app.route('/receive_message', methods=['POST', 'GET', 'OPTIONS'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def receive_message():
    word = " "
    if request.method == "GET":
        return "Get Success" 
    return "Success"

@app.route('/post_test', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def post_message():
    if request.method == "POST":
        fileAppend = open('context.txt', 'a')
        fileRead = open('context.txt', 'r')
        fileData = str(fileRead.readline())

        message = request.get_json()
        userInput = message["message"]
        if userInput == "chatStop":
            response = CAP.chat("chatStop")
        else:
            response = CAP.chat(fileData + "User:" + userInput)

            fileAppend.write("User:" + userInput + "Bot:" +response)

        fileAppend.close()
        fileRead.close()

        return response

if __name__ == '__main__':
    app.run(host = "localhost", port=8000, debug = True)