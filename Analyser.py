import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('Reviews.csv')
df.head()

stopwords = set(stopwords.words('english'))
stopwords.update(["br", "href"])

textt = " ".join(review for review in df.Text)

df = df[df['Score'] != 3]
df['sentiment'] = df['Score'].apply(lambda rating: +1 if rating > 3 else -1)

positive = df[df['sentiment'] == 1]
negative = df[df['sentiment'] == -1]

stopwords.update(["br", "href", "good", "great"])


pos = " ".join(str(review) for review in positive.Summary if pd.notnull(review))
neg = " ".join(str(review) for review in negative.Summary if pd.notnull(review))


def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"'))
    return final


df['Text'] = df['Text'].apply(remove_punctuation)
df = df.dropna(subset=['Summary'])
df['Summary'] = df['Summary'].apply(remove_punctuation)

dfNew = df[['Summary', 'sentiment']]
dfNew.head()

index = df.index
df['random_number'] = np.random.randn(len(index))
train = df[df['random_number'] <= 0.8]
test = df[df['random_number'] > 0.8]

vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_matrix = vectorizer.fit_transform(train['Summary'])
test_matrix = vectorizer.transform(test['Summary'])

model = LogisticRegression(max_iter=1000)

X_train = train_matrix
X_test = test_matrix
y_train = train['sentiment']
y_test = test['sentiment']

model.fit(X_train, y_train)
predictions = model.predict(X_test)

def predict_sentiment(input_text):
    processed_text = remove_punctuation(input_text)
    text_matrix = vectorizer.transform([processed_text])

    prediction = model.predict(text_matrix)[0]

    if prediction == 1:
        return "Positive"
    else:
        return "Negative"

print("Loading...")
file1 = open("speech.txt","r")
a = file1.read()
b = predict_sentiment(a)
print("Loading......\n")

with open('speech.txt', 'a') as f:
    f.write('\n'+ b)
f.close()

print("Analysis Done!")
