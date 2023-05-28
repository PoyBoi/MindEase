# Calling all the imports
import lib.dependancies as dependancies
import src.input as inp
# Had to import this module as it wasn't working in dependancies.py
from matplotlib import pyplot as plt

# Choosing the classfier model

classifier = dependancies.pipeline(
    "text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True
    # "sentiment-analysis", model= "cardiffnlp/twitter-xlm-roberta-base-sentiment", tokenizer= "cardiffnlp/twitter-xlm-roberta-base-sentiment", return_all_scores=True
    )

# Initializing the variables meant for storing
textClassified, scores, scoreList,  maxEmotion, scoresList = {}, [], [], [], []


# -> Sentimental Analysis
# This block of code is used to sort the list of dictionaries based on the score value 
# There has to be a better way to make this more optimized, but this works for now
def classifyingText(inputData, mode):

    global scores, scoreList, textClassified # Settoing the global variables so they can be called outside the function

    if (mode == "single"): # This block of code is used to classify a single message
        # classifier = modelSelection
        temp = classifier(inputData)
        for i in temp:
            for j in i:
                tempDict = {}
                scores.append(j["score"])
        scores.sort(reverse=True)
        for k in scores:
            for l in i:
                if (l["score"] == k):
                    tempDict = {"label" : l["label"], "score": k}
                    scoreList.append(tempDict)
        textClassified[inputData] = scoreList
        # # -> This block of code is used to print the main emotion conveyed by the message
        # print("The main emotion conveyed by this message was", scoresList[0]["label"], "with a score of", scoresList[0]["score"])
        scores, scoreList = [], [] # Resetting the variables

    elif (mode == "multiple"): # This block of code is used to classify multiple messages
        for p in inputData:
            temp = classifier(p)
            for i in temp:
                for j in i:
                    tempDict = {}
                    scores.append(j["score"])
            scores.sort(reverse=True)
            for k in scores:
                for l in i:
                    if (l["score"] == k):
                        tempDict = {"label" : l["label"], "score": k}
                        scoreList.append(tempDict)
            textClassified[p] = scoreList
            # # -> This block of code is used to print the main emotion conveyed by the message
            # print("The main emotion conveyed by this message was", scoresList[0]["label"], "with a score of", scoresList[0]["score"])
            scores, scoreList = [], []

# How to reach a specific value of emotion in a specific quote :
# --> textClassified[quote][emotionID(0 = top, -1 = last)]

def inputAnalysis(inputDataText):

    # Calling the model selection function
    #modelSelection()

    # This block is used to set the the input
    inputData = (
        # inp.text
        # inp.inputData
        inputDataText
        # "Hey, hi, how are you doing?, I am fine, I love you"
    )

    classifyingText(inputData, # Calling the function
                    # "multiple" # You can change the modes here
                    "single"
                    )

    listText = [i for i in textClassified] # Turning it into a Panda's DataFrame
    # print(listText)

    listValues = [i for i in textClassified.values()] # Listing values [{"label":..., "score":...}]
    emotionList = ["sadness", "anger", "fear", "love", "joy", "surprise"] # List of emotions

    for k in emotionList: # Writes the scoresList that deals with the emotions in rows, sorting for usage in dataframe
        temp = []
        for i in listValues:
            for j in i:
                if j["label"] == k:
                    temp.append(j["score"])
        scoresList.append(temp)

    for i in textClassified.values(): # Setting the primary emotion for each quote
        maxEmotion.append(i[0]["label"])

    dataset = dependancies.pd.DataFrame( # Creating the dataframe
        {
            "Text": listText,
            emotionList[0] : scoresList[0],
            emotionList[1] : scoresList[1],
            emotionList[2] : scoresList[2],
            emotionList[3] : scoresList[3],
            emotionList[4] : scoresList[4],
            emotionList[5] : scoresList[5],
            "Emotion" : maxEmotion
        }
    )

    dependancies.pd.set_option('display.max_colwidth', None)
    print(dataset)

# -> WordCloud Analysis
def wordCloudAnalysis(emotionList, dataset):
    for i in emotionList: # Itesrating through the emotions to make a wordcloud for each emotion, will skip if no words are present
        try:
            positive_quotes = dataset['Text'][dataset["Emotion"] == i]
            stop_words = [
                "Name", ":", "Text" , "dtype", "object", "Series", "t", "1", "2", "3", "4", "l"
                ] + list(dependancies.STOPWORDS)
            positive_wordcloud = dependancies.WordCloud(max_font_size=50, max_words=100, background_color="white"
                                                        , stopwords = stop_words
                                                        ).generate(str(positive_quotes))
            plt.figure()
            plt.title(i+"- Wordcloud")
            plt.imshow(positive_wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.show()
        # Error Handling in case of missing words
        except:
            pass

#__main__
inputAnalysis("I like penguins !")