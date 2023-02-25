from ..lib.dependancies import *

# sentiment_pipeline = pipeline("sentiment-analysis")
# specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
# data = ["I love you", "I hate you"]
# print(sentiment_pipeline(data))
# print(specific_model(data))

classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)

inputData = """
I'm not really sure what's going on with me lately. I just feel so...off. Like something isn't quite right, but I can't put my finger on it.

Sometimes I feel really sad and down, and other times I feel like I'm just going through the motions of life without really feeling anything. It's like I'm numb to everything around me, and I can't seem to shake it.

I've tried talking to my friends and family about how I'm feeling, but I just can't seem to find the right words. It's like there's something blocking me from really expressing myself, and I'm not even sure what that is.

I've tried doing things that usually make me happy, like playing video games or hanging out with friends, but it's like nothing really brings me joy anymore. I just feel kind of...empty.

I don't know if what I'm feeling is depression or if it's something else entirely. Maybe I'm just going through a rough patch and things will get better soon. Or maybe I need to talk to a professional about what's going on.

It's all just really confusing and overwhelming right now. I wish I could figure out what's going on in my head and heart, but for now, I'll just keep trying to take things one day at a time.
"""
prediction = classifier(inputData)
print(prediction)