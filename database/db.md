The two main datasets that we have considered for this project are :
1) Adult Depression (LGHC Indicator) [https://data.world/chhs/5a281abf-1730-43b0-b17b-ac6a35db5760]
2) 


We considered merging these databases into one however, we noticed that the integrity of the data and the accuracy of the training model would be more difficult to maintain. Keeping the the databases separate allows us to select and tune the features of the model more effectively and reduces the risk of an erroneous model due to lack of data integrity.

The code will also reference another paper written by Heinrich Dinkel on "Text-based depression detection on sparse data" (https://paperswithcode.com/paper/text-based-depression-detection-what-triggers). We beleive this study will be beneficial in creating an effective model and assist with model predictions and assistance by analyzing the subtle cues users will drop in chat. We intend to reference the study's approach to real-world approach to context-aware detection of depression by using pretrained contextual sentence embeddings with the usage of certain keywords.
