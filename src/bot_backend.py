import lib.dependancies as dependencies
import src.analysis as analysis
import os
#have to work for the dependencies part wiith the above

model_name = 'facebook/blenderbot-400M-distill'

tokenizer = dependencies.BlenderbotTokenizer.from_pretrained(model_name)
model = dependencies.TFBlenderbotForConditionalGeneration.from_pretrained(model_name)

def segregrate(text, mode):
    if mode == "start":
        temp = "<s> " + text
        return temp
    elif mode == "end":
        temp = text + " </s> <s>"
        return temp

def endCheck(text):
    temp = text
    temp.rstrip("</s")
    temp.lstrip("<s>")
    return text
    
def conversation():
    inputText, conversation, count = "", "", 0
    clearScrn = 0

    while inputText != "exit":

        if inputText == "":
            pass
        else:
            inputs = tokenizer([conversation], return_tensors='tf')
            outputs = model.generate(**inputs)
            outputText = endCheck(tokenizer.decode(outputs[0]).rstrip("<pad>"))

            # Should be redundant code with usage of the defintion i call
            # outputText = outputText.lstrip("<s>")
            # outputText = outputText.rstrip("</s")

            print("Counsellor: \t", outputText)
            conversation += segregrate(outputText, "end")

            # Below is trying to access the user's name if they have given it to us via conversation
            # conversation_context = outputs.encoder_last_hidden_state[0][inputs["input_ids"].shape[1]-1]["conversation"]
            # if "user" in conversation_context and "name" in conversation_context["user"]:
            #     user_name = conversation_context["user"]["name"]
            # response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            # print(response_text, user_name)
        if clearScrn == 0:
            os.system('cls')
            clearScrn = 1
        inputText = str(input("Human: \t"))

        # Running the sentimental analysis on the input text
        # to be even more efficient, we can use SA on the output to make sure that it is a good response, and if not, ask the 
        #   conversational model to be more strict about the mood and context, and look out for key words
        if inputText != "log" or inputText != "exit":
            # Have to make changes as to what gets returned via this function call and how to make it useful
            analysis.inputAnalysis(inputText)
        # If the user gives a sad response, make a primer for example as to how they are feeling, and as per how they respond to that, we can
        # make the AI ask the user how they are feeling, and through that answer can change the scope of the conversation

        conversation += segregrate(inputText, "end")

        # Using this as a way to selectively view logs
        if inputText.startswith("log"):
            print(conversation)
            inputText.rstrip("log")

        # Need to add max_length and/or max_new_tokens so that i can work wioth longer conversations

#__main__
# conversation()