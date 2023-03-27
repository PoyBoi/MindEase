import lib.dependancies as dependancies
import input as inp

classifier = dependancies.pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
# classifierDep = dependancies.pipeline("sentiment-analysis", model= "cardiffnlp/twitter-xlm-roberta-base-sentiment", tokenizer= "cardiffnlp/twitter-xlm-roberta-base-sentiment", return_all_scores=True)

# -> Sentimental Analysis

inputData = inp.text
# inputData = inp.inputData
# inputData = "Hey, hi, how are you doing?, I am fine, I love you"

# -> This block of code is used to sort the list of dictionaries based on the score value 
def classifyingText(inputData, mode):

    global scores, scoresList, textClassified

    if (mode == "single"):
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
                    scoresList.append(tempDict)
        textClassified[inputData] = scoresList
        # print("The main emotion conveyed by this message was", scoresList[0]["label"], "with a score of", scoresList[0]["score"])
        scores, scoresList = [], []

    elif (mode == "multiple"):
        for p in inputData:
            temp = classifier(p)
            for i in temp:
                # print(i)
                for j in i:
                    tempDict = {}
                    scores.append(j["score"])
            scores.sort(reverse=True)
            for k in scores:
                for l in i:
                    if (l["score"] == k):
                        # print(l["label"])
                        tempDict = {"label" : l["label"], "score": k}
                        scoresList.append(tempDict)
            # print(scoresList)
            textClassified[p] = scoresList

            # # -> This block of code is used to print the main emotion conveyed by the message
            # print("The main emotion conveyed by this message was", scoresList[0]["label"], "with a score of", scoresList[0]["score"])

            # print(textClassified[0][p])
            scores, scoresList = [], []

# How to reach a specific value of emotion in a specific quote :
# --> textClassified[quote][emotionID(0 = top, -1 = last)]

textClassified, scores, scoresList = {}, [], []

# classifyingText(inputData, "single")
classifyingText(inputData, "multiple")

# # -> Turning it into a Panda's DataFrame
print(textClassified.items())
# dataset = dependancies.pd.DataFrame(textClassified.items(), columns=['tweet', 'sentiment'])
# dependancies.pd.set_option('display.max_colwidth', None)
# print(dataset.head())

# -> WordCloud Analysis

# -> Positive words
# positive_tweets = dependancies.df['tweet'][dependancies.df["sentiment"] == 'POS']
# # stop_words = ["https", "co", "RT"] + list(STOPWORDS)
# positive_wordcloud = dependancies.WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords = stop_words).generate(str(positive_tweets))
# dependancies.plt.figure()
# dependancies.plt.title("Positive Tweets - Wordcloud")
# dependancies.plt.imshow(positive_wordcloud, interpolation="bilinear")
# dependancies.plt.axis("off")
# dependancies.plt.show()