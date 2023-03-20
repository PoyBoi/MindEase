import lib.dependancies as dependancies
import input as inp

textClassified, scores, scoresList = [], [], []

classifier = dependancies.pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
# classifierDep = dependancies.pipeline("sentiment-analysis", model= "cardiffnlp/twitter-xlm-roberta-base-sentiment", tokenizer= "cardiffnlp/twitter-xlm-roberta-base-sentiment", return_all_scores=True)

# -> Sentimental Analysis

# -> Code for iterating through the list of quotes if multiple quotes are present
# for i in inp.text:
#     try:
#         temp = classifier(i)
#         textClassified.append({"Quote: ": i, "analysis: ":temp})
#     except:
#         pass

# -> Change the input location here
# inputData = inp.text[2]
inputData = inp.inputData

temp = classifier(inputData)
# temp = [[{'label': 'sadness', 'score': 0.9989571571350098}, {'label': 'joy', 'score': 0.0002897530503105372}, {'label': 'love', 'score': 0.000231609505135566}, {'label': 'anger', 'score': 0.0002326384565094486}, {'label': 'fear', 'score': 0.0001424543297616765}, {'label': 'surprise', 'score': 0.00014639980508945882}]]

# -> This block of code is used to sort the list of dictionaries based on the score value 
for i in temp:
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

# -> This block of code is used to print the main emotion conveyed by the message
print("The main emotion conveyed by this message was", scoresList[0]["label"], "with a score of", scoresList[0]["score"])

# -> Turning it into a Panda's DataFrame
dataset = dependancies.pd.DataFrame(scoresList)
dependancies.pd.set_option('display.max_colwidth', None)
print(dataset.head())

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