import re

def remove_text_between_asterisks(text):
    text = re.sub(r'\".*?\"', '', text)
    text = re.sub(r'\*.*?"\*', '', text)
    textNew = text.split("User:", 1)[0]
    textNew = text.split("Bot:", 1)[0]
    print(textNew)
    return text

str = '''Alright then, first question - what do you consider your biggest issue? \"What do you consider your biggest issue?\" User: was written on the screen of the computer. It was a simple task, and one that could have been easily answered by most people. However, not everyone would answer this way, so there was a chance that some questions might need more than one response.'''
result = remove_text_between_asterisks(str)
# print(result) # "This is a  with  text to remove"