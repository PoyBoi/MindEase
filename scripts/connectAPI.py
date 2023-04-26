import requests
import json

# app = Flask(__name__)

url_main = "http://localhost:5000/api/v1"
url_info = "/info/version"
url_gen = "/generate"
url_story = "/story/end"
url_storyPull = "/story"

worldInfo = ""

# Have to set worldinfo and add to end of story, and then apply it with the "use_story" or whatever, use below for reference
# https://cdn.discordapp.com/attachments/1007049562415960144/1080009425860952065/image.png
# https://www.reddit.com/r/KoboldAI/comments/10penqx/i_am_trying_to_learn_how_to_use_the_koboldai/
# https://www.reddit.com/r/KoboldAI/comments/123hkua/how_to_make_chatbot_using_api/

# response = requests.get(url_main+url_info)

# Q) IF you have checked off any problems, how difficult have these problems made it for you to do your work, take case of things at home, or get along with other people?

qList = [
    "Have you noticed a lack of interest or pleasure in doing things in your day to day life ?", 
    "Have you been feeling, down or hopeless recently ?",
    "Do you have trouble falling or staying asleep, or do you sleep too much ?",
    "Have you noticed feeling fatigued or having little energy throughout the day ?",
    "Have you observed any changes in your eating habits, like eating too little or eating too much ?",
    "Do you recurrently see yourself in a negative light, or feel like you're letting people around you down ?",
    "Do you struggle with maintaining focus during passive activities, like reading or watching the TV",
    "Have people pointed out that you move sluggishly, or on the contrary, are very fidgety or restless ?",
    "Have you ever had thought about self harm ?"
    ]

qListRange = len(qList)

headers = {'Content-type': 'application/json', 'accept': 'application/json'} # <- And this line

def userInput():
    storyInfo = "Bot is a therapist. Bot is a female. Bot's name is 'Joi'. 'Joi' is short for Joanna. User is a patient at her clinic. This is a professional yet empathetic setting. User has come in for a mental health check up. Bot makes sure to make User feel at home. Bot refers to User as 'you'. Bot and user do not take physical actions or reactions. Bot is very patient. Bot does not treat User as a child, but rather as an adult. \nBot:\tWelcome to mindEase ! My name is Joi and I'll be your guide On this journey, Let's start with the basics, shall we ?"
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
    ae = response.text[21:-5]
    print("\nBot: ", ae, "\n") # <- This line

def test():
    print("Working")

def storySet():
    # Doesn't work
    storyInfo = {
        'prompt': storyInfo
    }

    # setting the story context
    response = requests.post(url_main+url_story, headers=headers, json=storyInfo)
    response = requests.get(url_main+url_storyPull, headers=headers)
    print(response)

def chat():
    print("""
Bot:\tWelcome to mindEase ! My name is Joi and I'll be your guide on this journey.
Bot:\tLet's start with the basics, shall we ?
Bot:\tBefore we start, I'd like to get to know you better
    """)
    while True:
        userInput()

chat()