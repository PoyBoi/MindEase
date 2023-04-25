import connectAPI as connect
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/myPythonFile.py', methods=['POST'])
def my_python_function():
  data = request.get_json()
  input_value = data['input']
  # do something with input_value
  print(input_value)
  return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run()



# @app.route('/http://localhost:5000/api/v1', methods=['GET', 'PUT', 'POST', 'DELETE'])
# def chat():
#     # Get user input from frontend
#     user_input = request.json.get('input')

#     # AI model prompt
#     prompt = f"Bot: Hi, how can I assist you today?\nUser: {user_input}\nBot:"

#     # AI model parameters
#     data = {
#         "prompt": prompt,
#         "max_tokens": 50,
#         "temperature": 0.7,
#     }

#     # Send request to OpenAI API to generate a response
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer " + "YOUR_API_KEY"
#     }
#     response = requests.post(url_main+url_gen, data=json.dumps(data), headers=headers)
#     response_json = response.json()
#     chat_response = response_json["choices"][0]["text"].strip()

#     # Return response to frontend
#     return jsonify({'response': chat_response})