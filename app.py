import pprint
import requests
import pandas as pd
from pandas.io.json import json_normalize
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from stop_word import extract_stop_in_sentence , remove_punctuation
#nltk.download()  Pour installer les packages

dictionary = requests.get('https://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey=853e02b0ec344bd182ea180e7fb93bf9').json()

stop_words = set(stopwords.words('french')) 
data = dictionary['articles']
#pprint.pprint(dictionary['articles']) #Afficher en console tout en gardant la structure de données JSON
json_normalize(data)
#print(data[)



df = pd.DataFrame(data)
#df["content"].astype(str)
#print(type(df['content'][0]))
#words = df.title.str.split(expand=True).stack()
#words = words[words.isin(selected_words)]

#print(words.value_counts())
list_word = []
for item in df.title:
    data = nltk.word_tokenize(str(item))
    if data[0] != 'None':
        #print(' ')
        #print('Title :')
        #print( data[-1] )
        data = " ".join(str(d) for d in data)
        data = remove_punctuation(data)
        print(data)
        list_word = list_word + extract_stop_in_sentence(data)

#word_tokens = list_word

list_word_df = pd.DataFrame({'title':list_word})

print(list_word_df)

count_word_df = list_word_df['title'].value_counts().to_frame()

for w in count_word_df:
    print(" ")


#print(nltk.word_tokenize(df['content'][0]))

