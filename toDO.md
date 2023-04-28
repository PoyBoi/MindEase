# Basic to-do List
## - For the Prediction Model
1) ~Add word doc to repo~
2) ~Find out the basic data points for the dataset~
3) ~Make a questionare for the data input (training)~
4) Start surveying people
5) Get atleast 50 column entries
6) ~Make a model that predicts the illness based off data points, and for this i think random forest might be the best bet going forward, it basically is decision tree but better, and we need a model that would use mutliple and not so well connected data points to work well together, and RF does it best for us~

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
10) ~Try to use Pygmalion AI to have the conversation, it's fine if it is jacked via google cloud~
11) ~Start to learn how to teach the AI to contextualize in a conversation, use a detailed tree structure to make it understand the context of the conversation // use detailed tree structure to make it understand the context of the conversation~
12) Understand how the wordcloud works and based on start with tokenization
13) ~Find a way to change the AI's name (json file needs to be edited it seems)~
14) ~Find a way to make the AI be more professional, and when time comes to be, i need for it to be more relaxed and chill~
15) ~Find a way to make the AI be better at keeping context~
16) ~Find a way to inject emotions into the conversation, and make it more natural~
17) Find a way to extract information like names and stuff
18) Find a way to inject the questions into the conversation naturally without messing up the flow of the conversation
19) Need to connect the sentimental analysis with the NLP model and figure out injection
20) ~Connection with the front end API, learn JSON and all that~
21) Need to make the sentimental analysis return -1, 0, 1 for negative, neutral, positive emotions portrayed in the text, so that the model can take heed for this
22) Sentimental analysis doesn't return correct emotion when taking in words that go with positive emotions but for example there is addition of "not", it doesn't work well, and often disregards the existance of the negative promptive word
23) ~bB_t.py line 61~
24) ~Fix error "ValueError: All arrays must be of the same length" in scripts.basicRun.py in like 3~
25) ~Need to run install.bat and then follow the tutorial and download PYG 4bit, and see how it works w/o WSL~
26) Need to add stop words to the NLP model so that it does not use racist words and responses
27) Make a function that goes through the bot's response to see what it's asking and if it's relevant, to then add it to the info dictionary
28) Need to add ignore for pycache's
29) Need to add attention mask, pad token ID, 
30) Can add a mood selector that deploys a different story setting based on the user preference
31) Need to make the git repo more clean, need to clean up readme and todo's

## ~For the Submission:~

1) ~Make a video~
2) ~Discuss the algortihm, and how it works~
3) ~Results : delivered scope~

## - For the NLP
1) ~Find out whether to use new or old model for the talking part~
2) Find dataset to train off of
3) ~Use chatGPT's API to make the chatbot, it says that we can modify the APi call to fit our needs, paraphrasing:~
4) ~In general, the attribution should include the OpenAI logo and a statement that your project is "Powered by OpenAI." You may also be required to include additional attribution depending on the type and frequency of your usage.~
5) https://huggingface.co/PygmalionAI/pygmalion-6b/tree/main
6) ~https://huggingface.co/facebook/blenderbot-400M-distill?text=Hey+my+name+is+Julien%21+How+are+you%3F~
7) https://getstream.io/blog/conversational-ai-flutter/

## ~For BlenderBOT 400M~

## - For the input understanding 
1) Train the model to understand certain keywords
2) Teach it to relate keywords to moods (Sentiment Analysis, Mood Analysis)
3) Make different and solo definitions out of each function, so that it helps in the expansion of the code

## ~How to change the name of the bot:~

## - How to work on privacy of data collected
When collecting data from a chat conversation to feed into an AI-based counselor, it's important to collect only the minimum amount of data necessary to provide the counselor's functionality. Here are some ways you can do this:

1. Identify key data points: Determine which data points are necessary for the counselor to provide effective advice or support. For example, if the counselor is providing mental health support, you may only need to collect information about the user's mood, stress level, and sleep patterns.

2. Use pre-defined response options: Use pre-defined response options or buttons to collect user data, rather than open-ended questions that may result in unnecessary data. For example, you can ask users to rate their mood on a scale of 1 to 10, rather than asking them to describe their mood in detail.

3. Filter out irrelevant data: Use natural language processing (NLP) techniques to filter out irrelevant data from the conversation. For example, you can use sentiment analysis to filter out messages that are not related to the user's mood or stress level.

4. Collect data in real-time: Collect data in real-time during the conversation, rather than collecting all data at the end of the conversation. This can help you to collect only the necessary data points and avoid collecting unnecessary or irrelevant data.

5. Anonymize user data: Anonymize user data as much as possible to protect user privacy. For example, you can use unique identifiers instead of usernames or personal information to track user conversations.

By following these best practices, you can help to ensure that you are collecting only the necessary data from chat conversations to feed into your AI-based counselor, while also protecting user privacy and building user trust.

## - How to work on the encryption of data collected
If you are feeding data to me for chatbot purposes, there are a few ways to implement encryption to protect the data:

1. Transport Layer Security (TLS): Use TLS to encrypt data in transit between your server and mine. This will help to prevent any interception or eavesdropping on the communication channel.

2. Encrypt data at rest: If you need to store user data, you can encrypt it at rest using a symmetric or asymmetric encryption algorithm. This will ensure that the data is protected even if the storage media is compromised.

3. Hash sensitive data: If you need to store sensitive data like passwords, you can hash the data using a one-way hashing algorithm like SHA-256 or bcrypt. This will help to protect the passwords in case of a data breach.

4. Use secure APIs: When communicating with me, use secure APIs that require authentication and authorization. This will ensure that only authorized parties can access the data.

It's important to note that encryption can add processing overhead and may impact performance, so it's important to consider the trade-offs between security and performance when implementing encryption.

## - Services to use for dB:
There are several services that you can use for secure storage of login details and user data. Here are some options:

### Login details:
1. Amazon Web Services (AWS) provides several secure database services, including Amazon RDS and Amazon DynamoDB, which can be used to securely store login details.
2. Google Cloud Platform (GCP) also provides secure database services like Google Cloud SQL and Google Cloud Firestore.
3. Microsoft Azure offers several secure database services, including Azure SQL Database and Azure Cosmos DB.

### User data:
1. AWS provides secure storage services like Amazon S3 and Amazon Glacier that can be used to store user data.
2. GCP offers several secure storage options like Google Cloud Storage and Google Cloud Bigtable.
3. Microsoft Azure provides secure storage services like Azure Blob Storage and Azure Data Lake Storage.

In addition to these cloud-based storage options, there are also other third-party storage providers like MongoDB Atlas, Firebase, and DigitalOcean that provide secure storage services.

It's important to evaluate each service based on your specific needs and requirements, including factors like data volume, performance, scalability, and cost. Additionally, you should also consider the security features and certifications offered by each service to ensure that they meet your security standards.

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

## Link Area
1) [KoboldAI Collab](https://colab.research.google.com/github/KoboldAI/KoboldAI-Client/blob/main/colab/GPU.ipynb#scrollTo=lVftocpwCoYw)
2) [Installation guide for above](https://www.youtube.com/watch?v=841tfxYYepM)
3) [Dive into chatBots and Dialgoue systems](https://web.stanford.edu/~jurafsky/slp3/old_dec20/24.pdf)
4) [Running PYG/Win no 8Bit](https://nemoia.ai/pages/pygmalion.html)
5) [PYG/WIN 8Bit Discord Tutorial](https://discord.com/channels/849937185893384223/1059637856206852237/1059899112608235571)
6) [Something else for the above, see if it helps](https://github.com/oobabooga/text-generation-webui/issues/20)
7) [System Requirements](https://www.reddit.com/r/PygmalionAI/comments/10dj8gl/i_found_out_how_to_run_it_localy_with_kobold_ai/)
8) [Another 8Bit Tut but using WSL](https://www.reddit.com/r/PygmalionAI/comments/10o0dfp/model_8bit_optimization_through_wsl/)
9) [Running PYG with 4.5G reddit tut](https://www.reddit.com/r/PygmalionAI/comments/129w4qh/how_to_run_pygmalion_on_45gb_of_vram_with_full/?q=windows&type=comment)
10) [How to use LLaMa 4bit](https://github.com/xNul/chat-llama-discord-bot#llama-setup-normal8bit4bit-for-text-generation-webui)
11) [API help for koboldAI](http://localhost:5000/api/latest/docs/)

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
