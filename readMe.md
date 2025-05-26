# mindEase 

#### An AI-powered personal mental health coach that can analyze your mental state, suggest coping strategies, and help you manage stress and anxiety

# The idea basically

The main idea of this project is to be able to diagnose basic mental health conditions such as depression via the use of a binary search/AVL or whatever tree. 
Natural Language processing is a very important part of this project, we will ask the user indirect questions and from that we will take the data we need and work towards diagnosing the patient. So the workflow will be: there exist questions that ascertain specific things, indirectly, for example, asking the user how they have been feeling emotionally, or how excited they are on a day to day basis, the core of this is to disguise the question in such a manner that the final data that we take is not easily understood by the user so that they do not change the answer to meet a certain answer archetype. This is where NLP comes into play, we use NLP to decode or understand what the person has said into data readable form and then turn this information into data points and from these data points, we can run a search tree and narrow down to the best (ouch) mental illness, and nothing at all. Now that I think about it, a tree is a bad idea and a best fit line would be a better idea to implement because we will have an error margin and a bias margin so to use a tree would be a big error, and by using a line we can have a more open range of final destinations instead of pre-defined points. About the part that humans are different and that no two people are the same is a very valid point to bring forth, but all tendencies have some underlying symptoms, loneliness is often passed off by people as “nah I don’t enjoy their company”, sometimes, very rarely, that’s the case but in majority of the cases it’s some underlying issue that the user has not found about, and often on deeper introspection, they turn over the root cause, and sometimes even after finding the root cause, they choose to ignore it, as a wrong diagnosis, this is known as the personal bias, I don’t know a name for this but I think this fits pretty well. It's funny if you guys are cloning this project thinking it's a one-stop shop for your project and/or submission, it's not, app.py won't work unless you have oobabooga installed. Go figure. Honestly it's better if you use an openAI API at this point, save yourself the pain, and get back to this when you actually have something worth to show from a skill perspective, cloning this repository will do you absolutely zero good, lmao. This is where the need for a counsellor comes in, but in india, as we know, mental health is a mental “illness” and many people often don’t come out and ask for help, even when there are people willing to do it, often having their livelihoods depend on it (we’re taking that away lol), so to make it more anonymous so that a person can log on, have a small chat and understand what they’re feeling is not unique to them and that they have a way out of that tunnel of darkness, and maybe this can push them to actually consult an IRL counsellor, another idea for counsellors is to have them give us training data that we can work upon, further improving the model, but keeping in mind to not over train it. The idea is very simple but the execution is going to be tough. It can either be an app or a website, either works, depends what you all vote for. The input is going to be in forms of paragraphs that will be broken down using NLP, we’ll be borrowing that tech so yeah, we can train our own model based on what we mean to extract and understand what the user subliminally means. So yeah, that about does it.

# Star History

[![Star History Chart](https://api.star-history.com/svg?repos=PoyBoi/MindEase&type=Date)](https://star-history.com/#PoyBoi/MindEase&Date)

# Steps on what to do:

1) Research: Conduct thorough research on the topic of mental illness and the current state of AI in this field. This will help you understand the problem better, identify the challenges and limitations, and get inspiration for your project.
2) Data Collection: Gather large and diverse data sets of patients with different mental illnesses. This could include data on symptoms, diagnosis, and treatment, as well as demographic information and medical history. Make sure the data is properly annotated and labeled. 
3) Preprocessing: Clean, preprocess, and organize the data to ensure that it is in the right format for input into the model. You may need to remove any irrelevant or missing data and normalize the data to make it easier for the model to process. 
4) Model Selection: Choose an appropriate machine learning model for your problem, such as a decision tree, random forest, support vector machine, or deep neural network. You may want to consider the size of the data set, the complexity of the problem, and the available computational resources when making your selection. 
5) Model Training: Train the selected model on the preprocessed data. You may want to split the data into training and validation sets to assess the performance of the model. 
6) Model Evaluation: Evaluate the performance of the trained model by testing it on a separate data set. This will give you an idea of how well the model generalizes to new data. You may want to use metrics such as accuracy, precision, recall, and F1 score to assess the performance of the model. 
7) Fine-Tuning: Based on the evaluation results, fine-tune the model by adjusting its hyperparameters or using different algorithms. Repeat the training and evaluation steps until you achieve a satisfactory level of performance.
8) Deployment: Once you are satisfied with the performance of the model, deploy it in a real-world setting. You may want to consider the ethical and privacy implications of your project and ensure that you have obtained the necessary approvals and permissions.

# Which models to use:

For an AI project that deals with identifying mental illnesses, a deep learning model such as a convolutional neural network (CNN) or recurrent neural network (RNN) could be a good choice.

Deep learning models have shown great success in handling complex problems that involve image and text data, and they can learn to automatically extract features from the data. In this case, the symptoms of mental illnesses can be treated as either text or numerical data, and a deep learning model can learn to classify them based on the available data.

However, it's important to note that deep learning models can be computationally intensive and may require a lot of data to train effectively. In such a case, you may consider using a transfer learning approach, where you can fine-tune a pre-trained model on a similar task with a smaller data set.

In conclusion, while deep learning models can be a good choice for this problem, it's essential to evaluate the performance of different models and fine-tune the model until you achieve the desired level of accuracy.
 
# GPT’s thoughts on this project:

### Mental illness is a complex and challenging area of healthcare, and AI has the potential to play a significant role in improving our understanding and treatment of these conditions. Here are some of the current challenges and limitations in using AI for mental illness:
1) Data Quality and Availability: One of the biggest challenges in using AI for mental illness is obtaining high-quality data. Mental health data is often collected through self-reported measures, which can be unreliable, and there is a lack of standardization in data collection methods. This makes it difficult to build robust AI models that can accurately diagnose and treat mental illness.
2) Bias: Another major challenge in using AI for mental illness is the potential for bias in the algorithms. This can occur due to biases in the training data, or due to algorithmic biases that are built into the models. For example, AI models that have been trained on predominantly male data may not perform well in diagnosing and treating women, who often experience mental health issues differently.
3) Ethical Concerns: The use of AI in mental health also raises ethical concerns, such as patient privacy and confidentiality, the potential for AI-based diagnoses to be used in discriminatory ways, and the possibility of AI systems making decisions that have significant impacts on individuals' lives without adequate human oversight.
4) Lack of Clinical Validation: Despite some promising results in using AI for mental illness, there is still a lack of clinical validation for many AI-based approaches. This means that while AI models may show promising results in research settings, they may not perform as well when applied in real-world clinical settings.
5) Integration with Clinical Practice: Another challenge in using AI for mental illness is integrating AI technologies into existing clinical practice. This includes ensuring that AI systems are user-friendly and accessible for healthcare professionals, and that they can be easily integrated into existing workflows.
#### Despite these challenges and limitations, the use of AI in mental health is a promising field, and researchers and healthcare professionals are working to overcome these barriers and develop effective AI-based solutions for mental illness.
 
# GPT on how to deal with understanding NLP:

1.	Preprocessing: Clean the text by removing punctuations, stop words, and converting all the words to lowercase.
2.	Sentiment Analysis: Use sentiment analysis algorithms to classify the overall sentiment of the text into positive, negative, or neutral.
3.	Emotion Detection: Use Natural Language Processing (NLP) techniques to extract emotions from the text. There are several pre-trained models available that can detect emotions such as anger, joy, sadness, fear, and disgust.
4.	Keyword Extraction: Use NLP techniques such as TF-IDF, text summarization, and topic modeling to extract the most important words and phrases in the text.
5.	Mental Health Information Extraction: Use NLP techniques to identify words and phrases related to mental health and analyze the frequency and co-occurrence of these words.
6.	Evaluation: Evaluate the performance of the algorithms by comparing the results with human annotations.
 
# My thoughts:

We need to find the target illnesses first, then we need to work our way to up by finding the causes, triggers, and the shared causes. Then we need to find a suitable dataset that puts them all together, we can use onehotencoder or a similar <something> that will turn of all into binary. Then using a model we can plot the line <or whatever> and obviously we’ll need to have a split of test and training data. This will predict the illness but this is not even the biggest challenge, the biggest challenge is going to be that of the NLP forefront, we’ll need to be able to read the answer<prompt> and then extract what we need. After that is done, we can couple them both and then use test cases from physiatrists and see how well our model performs, we’ll also need to see if we either overfit or underfit our model, this could be the turning point, for the better or for the worse. After this comes the front end, we’ll need to design it in a very minimalistic way, either a website or an app, whatever we do, it must be very simple to use, and should have the ability to be built upon, take inspiration from chatGPT. For collecting the data from the user we’ll need questions that will target the chinks in their armor, and from those answers we’ll compile our own answer, the final part of this is to suggest what the person can do, depending on the answers that the person gives, we can give them basic primer examples of what they can do and in the end we will have to specify for them to seek professional mental health help, and that our model is accurate but not precise <or the other way around whatever idk>.   In my usage cases with chatGPT, it has been very uptight so instead of training the model on very strict English vernacular, we can maybe loosen it up a little bit so that the conversation feels more grounded and more realistic. We can try to read behavior via messages, people use computer vision to test for anxiety like nail biting, knuckle cracking etc, but our challenge lies in understanding that from the messages that the person sends, the time between the message, and other such behavioral characteristics can be helped to determine such factors for us. We can also train the bot to act like a human in places like he got seenzoned, for him to wait for a few hours and say something like, “really busy are we not”, or “it’s getting colder without you here” and other cliché things, we aim to make this bot very human like and approachable, we also need ice-breaking questions from the bot like “Do you speak Spanish ?”, questions like this will break the ice and will also help us collect prior data on the user.

# How to use GPT for the chatbot:
1. Use the OpenAI API: You can use the OpenAI API to integrate me as a chat bot in your project. OpenAI provides a simple API that allows you to interact with me using a few lines of code. You will need to sign up for an API key and follow the documentation provided by OpenAI to get started.

2. Use a pre-built integration: There are several pre-built integrations available for different programming languages and frameworks. For example, there are integrations available for Python, Node.js, and Ruby on Rails. You can find these integrations by searching for "OpenAI GPT-3 integration" online.

3. Build your own integration: If you have more technical expertise, you can build your own integration using the OpenAI API. This will require more coding knowledge and familiarity with APIs and web services.

4. Keep in mind that we have only 100,000 API calls per month in the free tier. If you need more API calls, you can upgrade to a paid plan.
  
5. In general, the attribution should include the OpenAI logo and a statement that your project is "Powered by OpenAI." You may also be required to include additional attribution depending on the type and frequency of your usage.
  
6. Yes, I can remember the context of conversations during API calls, allowing me to maintain a consistent and coherent dialogue with users over multiple turns. To achieve this, you can pass in previous conversations or chat history as context to each API call. This context can be in the form of text or structured data, depending on your project's needs. By providing context, I can use the information from previous interactions to generate more personalized and relevant responses. This can be especially useful in a chatbot scenario where the conversation may span multiple turns and topics.
 
# Research Area:

### Today, we are facing a severe mental health crisis. A fifth of adults in the US, or over 50 million people, experienced a mental illness in 2019-20, according to Mental Health America’s 2023 report.
AI for mental health is gaining a foothold across clinical practice, already now. In particular, the following technologies have the most potential for an impact:
1) Machine learning (ML) and deep learning (DL) that provide greater accuracy in diagnosing mental health conditions and predicting patient outcomes
2)	Computer vision for imaging data analysis and understanding non-verbal cues, such as facial expression, gestures, eye gaze, or human pose
3)	Natural language processing (NLP) for speech recognition and text analysis that is used for simulating human conversations via chatbot computer programs, as well as for creating and understanding clinical documentation
4) People tend to believe that robots don’t judge, are unbiased, and can provide instant answers to health-related questions.
5) The most popular AI-powered virtual therapists include Woebot, Replika, Wysa, Ellie, Elomia, and Tess.
6) This conversational agent was launched via Facebook Messenger, but there were some criticisms with this, as Facebook, and not Woebot or the individual, owned the conversation data
7) AI is helping doctors to spot mental illness earlier and to make more accurate choices in treatment plans.



 
# Reading Area:

1) Using Psychological Artificial Intelligence (Tess) to Relieve Symptoms of Depression and Anxiety: Randomized Controlled Trial - PMC (nih.gov)
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6315222/

2) Paper on using AI for mental health (an overview)
qt9gx593b0_noSplash_d814b6b41c76cb874050695d2bf30ced.pdf (escholarship.org)
https://escholarship.org/content/qt9gx593b0/qt9gx593b0_noSplash_d814b6b41c76cb874050695d2bf30ced.pdf?t=qd3z26


  
3) Can Chatbots Help Support a Person's Mental Health? Perceptions and Views from Mental Healthcare Professionals and Experts (acm.org)
https://dl.acm.org/doi/fullHtml/10.1145/3453175

4) What Role Could Artificial Intelligence Play in Mental Healthcare? (healthitanalytics.com)
https://healthitanalytics.com/features/what-role-could-artificial-intelligence-play-in-mental-healthcare

5) 4 ways AI is improving mental health therapy | World Economic Forum (weforum.org)
https://www.weforum.org/agenda/2021/12/ai-mental-health-cbt-therapy/

6) Artificial intelligence in prediction of mental health disorders induced by the COVID-19 pandemic among health care workers - PMC (nih.gov)
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7358693/

 
# Ideas for improvement in the future:

1)	This is for use in public scenarios where the patient will have a camera that will see how they react to certain info, this can be used with or without the AI chatbot and can be used for example in a live session with a professional, but the one thing that we have to see is the privacy of the end user, and the consent to give it, because if someone knows they are being watched they will behave in a much different manner and will not let their true side be expressed.

2)	Implement this technology into a social media bot, like a bot on Instagram that can talk to people and stuff.

3)	
 
# MISC:

1) Our project is basically an AI counselor, it will have generative interactive capabilities that will allow for it to have a conversation with the end user. Our AI will be able to diagnose the end user with basic mental health conditions using text input provided by the user in specifically targeted questions, and our AI will extract the data needed from the text input and will learn about the user’s condition, if any for if not placebo or incorrect information preceding the auto-diagnosis. We know that each person is different there can be no static response order for certain diagnosis, and this is where real counselors will outshine the AI, our AI’s basic goal is to break the taboo of seeking mental health help in India, to provide a platform where people can be free and talk to an AI that feels almost like a real counselor
2) Our project aims to remove the stringent taboo of mental health and it’s stigma that is imbued in the Indian society, by offering a platform that enables anonymous counseling around the clock without any bias and will give people an incentive to open up about almost anything. This project is not aimed to be a companion or an interactive helper, but we would like for it to be something that can dig through the mud and find what really it is that is plaguing someone, if anything at all, and to hopefully make them feel that maybe it is worth going out and seeking help at a professional, that maybe it wasn’t normal to feel reclusively under the weather all the time.

# How to run:

1) Find the play.bat in the root of the folder and run it, load the model and make sure its 4b mode on
2) run the app.py file
3) run the HTML files in the python workspace folder and the bot should work
