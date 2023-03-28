# Basic to-do List
## - For the Prediction Model
1) ~Add word doc to repo~
2) ~Find out the basic data points for the dataset~
3) Make a questionare for the data input (training)
4) Start surveying people
5) Get atleast 50 column entries
6) Make a model that predicts the illness based off data points, and for this i think random forest might be the best bet going forward, it basically is decision tree but better, and we need a model that would use mutliple and not so well connected data points to work well together, and RF does it best for us

## - For the NLP
1) Find out whether to use new or old model for the talking part
2) Find dataset to train off of
3) Use chatGPT's API to make the chatbot, it says that we can modify the APi call to fit our needs, paraphrasing:
>For example, you can control the length and type of responses, the amount of context I use to generate responses, and the level of 
>creativity or randomness in my responses. You can also fine-tune my language generation by providing specific prompts or examples that 
>I can learn from. Additionally, you can use programming languages such as Python or JavaScript to create custom scripts or wrappers 
>around the OpenAI API to further modify and tailor the responses you receive. Overall, the OpenAI API provides a lot of flexibility 
>and customization options, so you can integrate me in a way that best meets the needs of your project. If you have specific 
>requirements or questions about how to modify my behavior, feel free to ask and I'll do my best to assist you.
4) We'll have access to GPT's contextualization skill, but i think we need to have a history-keeping mechanism of our own that logs chats

## - For the input understanding 
1) Train the model to understand certain keywords
2) Teach it to relate keywords to moods (Sentiment Analysis, Mood Analysis)


## Project To-do's:
1) ~https://huggingface.co/blog/sentiment-analysis-python;~
2) Start with tokenisation ideation and how to work with it
3) Make a model that predicts depression and other stuff based on rating on the emotion scale
4) Start on the NLP front for making believeable conversations, implent ideas from todolist app // Use chatGPT's API
5) ~Need to download tf.model.h5, it's 1 gig~
6) ~Need to make a listed dictionary of emotions based on their importance per inputText, and then sort them, and be able to show the topmost emotion as the prevalant emotion~
7) ~Figure out the iteration scenario with the input model and sort out the situation with the scoresList (We can instead just call the function on an interation)~
8) ~Figure out how to associate words with emotions and then make a wordcloud of the most common words associated with the emotion~
9) ~Make a wordcloud of the main words associated with positive and negative emotions in that specific text~
10) Start to learn how to teach the AI to contextualize in a conversation, use a detailed tree structure to make it understand the context of the conversation // use detailed tree structure to make it understand the context of the conversation
11) Understand how the wordcloud works and based on start with tokenization

## In Project:
### In /SRC:
#### analysis ~
1) ~Need to clean up the code, make it more readable and understandable, remove the unnecessary comments~
2) Figure out how to get neccessary items from the list that is returned
3) Try to make the code more optimised, it's too cluttered and slow as of now
4) ~Understand how to go forward with the dataFrame workflow of the list that is returned, and how to visualise it with wordcloud~
5) ~Configure wordcloud~
#### test ~
1) Use it for dump commands and testing
#### input ~
1) Try to add more text for the analysis to see how the output works out
### In /plugins:
1) Try making a new plugin for each redudant piece of code that is there in the form of comments to make sure it works
2) Don't forget to import this plugin folder into the main src folder
### For the chatBot:
1) Try to use chatGPT's API to have the insertion for the chatbot

## Databases // Reading Sources
1) https://www.kaggle.com/datasets/arashnic/the-depression-dataset
2) https://data.world/datasets/depression (each link has a source file inside)
3) https://datasets.simula.no/depresjon/
4) https://paperswithcode.com/task/depression-detection (Imp to look at, uses speech data to pred)
5) https://www.nature.com/articles/s41597-022-01211-x (Uses brainwaves and speech analysis)
6) https://www.hindawi.com/journals/cin/2022/5731532/ (Isn't this what we are doing ?)
7) https://github.com/kharrigian/mental-health-datasets (Dataset Megadoc)
8) https://link.springer.com/article/10.1007/s00521-021-06426-4 (Paper on Deep Learning and RNN to detect depression on text based)
9) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8675644/ (Child depression detection using ML, uses the YMM dataset)

## Project Pre-Requisites:
1) Text Preprocessing: This involves cleaning, tokenizing, and normalizing the text to remove any noise, stop words, punctuation, and convert the text to a standardized format.
2) Feature Extraction: In this step, you will need to convert the preprocessed text into numerical representations (features) that can be used by the machine learning algorithms. Common methods for feature extraction in NLP include Bag of Words, TF-IDF, Word2Vec, and GloVe.
3) Machine Learning Algorithms: You will need to be familiar with different ML algorithms such as Decision Trees, Naive Bayes, Logistic Regression, and Neural Networks. You will also need to know how to train, validate, and test these models.
4) Evaluation Metrics: You will need to be able to evaluate the performance of your machine learning models using metrics such as accuracy, precision, recall, F1-score, and confusion matrix.
5) Dataset Creation: You will need to have a dataset of conversations between people with and without depression to train your model. You will also need to ensure that your dataset is balanced, representative, and annotated correctly.

## Courses:

To get started with these topics, you can take online courses such as "Natural Language Processing with Python" by NLTK, "Applied Machine Learning" by Coursera, "Machine Learning A-Z" by Udemy, or "Deep Learning Specialization" by Coursera.
1) https://in.coursera.org/learn/machine-learning
2) https://in.coursera.org/specializations/deep-learning#courses
3) https://in.coursera.org/specializations/data-science-python#courses

## - Database Metrics:

1) Demographic Info:
> Age, Gender, Ethinicity, education, employment status, financial status, (relationship status <- doubtful)
2) Family History:
> If any conditions run in the family
3) Medical History:
> Past and current medical conditions, medications, treatments
4) Symptoms:
> Detailed information on a person's current and past symptoms, including severity, duration, and frequency
5) Life events:
> Traumatic events, major life changes, and other significant experiences
6) Substance usage:
> Information about alcohol, tobacco, and drug use can help to diagnose substance abuse or addiction
7) Support system:
> Relationships with family, friends, and colleagues
8) Stress levels:
> Self explanatory, can be broken down into thresholds and sources
9) Personal beliefs: (doubtful)
> Personal beliefs and attitudes towards mental health, including stigma, can affect a person's willingness to seek help and comply with treatment
