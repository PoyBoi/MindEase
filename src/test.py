test = [
    {
        "1" : {"Quote": "AA", "Fact":"True"},
        "2" : {"Quote": "BB", "Fact":"False"},
        "3" : {"Quote": "CC", "Fact":"True"}
    }
]

x = "1"

print(test[0]["1"]["Fact"])