# Basic-Speech-Recognizer-and-Sentiment-Analyser
Python program which records audio, converts it into text and perform simple sentiment analysis on it


I have taken much help from this article for the sentiment analyser and it would be a crime to not mention it OwO:
https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6

First of all, you have to download https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews?select=Reviews.csv dataset and move the Reviews.csv file into the main directory.

Then, you have to run Speech-to-text.py. This will create two files in the directory- recording.wav and speech.txt.

Finally, run the Analyser.py which will add the sentiment in another line just below the transcribed text.

Keep in mind this is a shallow model using just countvectorizer and Logistic Regression. Some of the further improvements and interesting things that can be done are:
1. Use a more complex model, maybe a sequential neural network?
2. Use a better feature extractor such as tf-idf vectorizer.
3. Plot the embededded word vectors and see how close the similar words lie.

Thats all from me. 
See you next time. 

Laters!
![image](https://github.com/wannasleepforlong/Basic-Speech-Recognizer-and-Sentiment-Analyser/assets/109717763/66a27e3f-57be-4c5b-bb73-481509a2af3c)
