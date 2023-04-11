
# ----> Miscellaneous <----
test = [
    {
        "1" : {"Quote": "AA", "Fact":"True"},
        "2" : {"Quote": "BB", "Fact":"False"},
        "3" : {"Quote": "CC", "Fact":"True"}
    }
]

x = "1"

print(test[0]["1"]["Fact"])

# ----> From input.py <----

# sentiment_pipeline = pipeline("sentiment-analysis")
# specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
# data = ["I love you", "I hate you"]
# print(sentiment_pipeline(data))
# print(specific_model(data))