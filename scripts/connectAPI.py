import requests
import json
from flask import Flask, request, jsonify

# app = Flask(__name__)

url_main = "http://localhost:5000/api/v1"
url_info = "/info/version"
url_gen = "/generate"
url_story = "/story/end"
url_storyPull = "/story"

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


worldInfo = ""

# Have to set worldinfo and add to end of story, and then apply it with the "use_story" or whatever, use below for reference
# https://cdn.discordapp.com/attachments/1007049562415960144/1080009425860952065/image.png
# https://www.reddit.com/r/KoboldAI/comments/10penqx/i_am_trying_to_learn_how_to_use_the_koboldai/
# https://www.reddit.com/r/KoboldAI/comments/123hkua/how_to_make_chatbot_using_api/

# response = requests.get(url_main+url_info)

# 1) Little Interest or pleasure in doing things
# 2) Feeling, down, depressed or hopeless
# 3) Trouble falling or staying asleep, or sleeping too much
# 4) Feeling tired or having little energy
# 5) Poor appetite or overeating
# 6) Feeling bad about yourself, or that you are failure or you have let yourself or your family down
# 7) Trouble concentrating on things, such as reading the newspaper or watching television
# 8) Moving or speaking so slowly that other people could have noticed. Or the opposite-being so fidgety or restless that you have been moving around a lot more that usual
# 9) Thoughts that you would be better off dead, or of hurting yourself
# 10) IF you have checked off any problems, how difficult have these problems made it for you to do your work, take case of things at home, or get along with other people?

headers = {'Content-type': 'application/json', 'accept': 'application/json'} # <- And this line

print("""
Bot:\tWelcome to mindEase ! My name is Joi and I'll be your guide On this journey.
Bot:\tLet's start with the basics, shall we ?
""")

def userInput():
    storyInfo = "Bot is a therapist. User is a patient at his clinic. This is a formal yet mepathetic setting. User has come in for a depression check up. \nBot:\tWelcome to mindEase ! My name is Joi and I'll be your guide On this journey, Let's start with the basics, shall we ?"
    storyInput = str(input("User:\t"))
    userPrompt = {
        "prompt": storyInfo+ "\nUser: " + storyInput + "\nBot: ",
        "use_story" : False,
        "use_world_info" : False,
        "temperature": 0.5,
        "top_p": 0.9
    }
    storyInfo = storyInfo + storyInput
    # print(storyInfo)
    # setting the prompt to send up for generation
    response = requests.post(url_main+url_gen, data=json.dumps(userPrompt), headers=headers) # <-this line
    ae = response.text[23:-5]
    print("\nBot: ", ae, "\n") # <- This line

def storySet():
    # Doesn't work
    storyInfo = {
        'prompt': storyInfo
    }

    # setting the story context
    response = requests.post(url_main+url_story, headers=headers, json=storyInfo)
    response = requests.get(url_main+url_storyPull, headers=headers)
    print(response)

while(True):
    userInput()
    # chat()