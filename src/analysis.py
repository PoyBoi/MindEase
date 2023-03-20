import lib.dependancies as dependancies
import input as inp

dataset = dependancies.pd.DataFrame(inp.textClassified)
dependancies.pd.set_option('display.max_colwidth', None)

classifier = dependancies.pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)
classifierDep = dependancies.pipeline("sentiment-analysis", model= "cardiffnlp/twitter-xlm-roberta-base-sentiment", tokenizer= "cardiffnlp/twitter-xlm-roberta-base-sentiment", return_all_scores=True)

# Sentimental Analysis

textClassified = []

# for i in inp.text:
#     try:
#         temp = classifier(i)
#         textClassified.append({"Quote: ": i, "analysis: ":temp})
#     except:
#         pass

temp = classifier(inp.inputData)
textClassified.append({"Quote: ": "inputData", "analysis: ":temp})

for i in textClassified: 
    print(i, "\n")

# WordCloud Analysis

