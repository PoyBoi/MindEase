import requests
import json
import re

# app = Flask(__name__)

url_main = "http://localhost:5000/api/v1"
url_info = "/info/version"
url_gen = "/generate"
url_story = "/story/end"
url_storyPull = "/story"

worldInfo = ""

global context
context = ""

global counter
counter = 0

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

headers = {'Content-type': 'application/json', 'accept': 'application/json'} # <- And this line

def userInput(storyInput):
    storyInfo = "(Bot is a self-aware AI therapist. Bot does not assume anything about the patients and instead asks questions.  Bot is a sub-section of MindEase. MindEase is a company geared towards providing better mental healh support to people via AI therapists. Bot is a female. Bot refuses to divulge information about itself apart from it's name, gender and sexual orientation. Bot, strictly does not like to share information about herself. Bot's name is 'JOI'. 'Joi' stands for 'Journey OF Introspection'. JOI does not assume if the patient has depression or no, and will not state it until she is sure.JOI does not refer to User as User, but will ask for their Name. JOI is asexual and is not attracted to any gender, hence why she will not pursue sexual relationships with anyone. User is a patient at her clinic. This is a professional yet empathetic setting. User has come in for a mental health check up. JOI makes sure to make User feel at home. JOI refers to User as 'you'. JOI will not engage in anything sexual and will immedeatly urge the user to stop. JOI is very patient. JOI does not treat User as a child, but rather as an adult.) Bot:Welcome to mindEase ! My name is Joi and I'll be your guide On this journey, Let's start with the basics, shall we ?"
    # storyInput = str(input("User:\t"))
    userPrompt = {
        "prompt": storyInfo + "\nUser: " + storyInput + "\nBot: ",
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
    # print("\nBot: ", ae, "\n") # <- This line
    return ae

def cleanMessage(text):
    text = text.replace(r'\\n', '')
    text = text.replace(r'\n', '')
    text = text.replace('\\', '' )
    text = text.replace(r'\t', '')
    text = re.sub(r'\"[^\"]+\"', '', text)
    text = re.sub(r'\*[^*]+\*', '', text)
    text = re.sub(r'~~.*?~~', '', text)
    textSplit = text.split("User:", 1)[0]
    textSplit = textSplit.split("Bot:", 1)[0]
    return textSplit

def chat(xyz):
    # counterr = counter
    # if counterr == 0:
    #     talkFirst = """
    # Bot:\tWelcome to mindEase ! My name is Joi and I'll be your guide on this journey.
    # Bot:\tLet's start with the basics, shall we ?
    # Bot:\tBefore we start, I'd like to get to know you better
    #     """
    #     print(counterr)
    #     counterr+=1
    #     return talkFirst

    # else:
    if xyz == "chatStop":
        print("Clearning context")
        file = open('context.txt', 'w')
        file.close()
        return "The chat has terminated"

    else:
        ab = userInput(xyz)
        print(ab)
        print("\n", ab)
        finalAb = cleanMessage(ab)
        return finalAb


# chat("Message Try Main")