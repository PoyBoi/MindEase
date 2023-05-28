import re

def remove_text_between_asterisks(text):
    print(text)
    text = re.sub(r'\"[^\"]+\"', '', text)
    text = re.sub(r'\*[^*]+\*', '', text)
    text = text.replace('\\', '' )
    textNew = text.split("User:", 2)[0]
    textNew = textNew.split("Bot:", 2)[0]
    return textNew

str = 'Alright then, \ first question - what do *you consider* your biggest issue? \"What do you consider your biggest issue?\" User: was written on the screen of the computer. It was a simple task, and one that could have been easily answered by most people. However, not everyone would answer this way, so there was a chance that some questions might need more than one response.'
result = remove_text_between_asterisks(str)
print("\n")
print(result) # "This is a  with  text to remove"