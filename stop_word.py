from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import string

def extract_stop_in_sentence(sentence):



    if " - " in sentence :
        sentence = sentence[:sentence.index(" - ")] # Exclure le nom de l'article ( " - Le Monde " , "- LCI")

    stop_words = set(stopwords.words('french')) #Langue du dictionnaire

    word_tokens = word_tokenize(sentence) #Découpage de la phrase

    tagged_sent = pos_tag(word_tokens) # Avoir les POS TAGGER de chaque mot phrase

    #print(tagged_sent)
    word_tokens = [word for word,pos in tagged_sent if pos == 'NNP']

    filtered_sentence = [] 

    for w in word_tokens: #  Pour chaque mot de la liste
        if w not in stop_words: # Si le mot indexé n'est pas dans le dictionnaire des noms communs
            filtered_sentence.append(w) # On l'ajoute dans notre liste finale

    return filtered_sentence # Afin d'avoir qu'une liste sans noms communs


def strip_punctuation(sentence):
    #table = str.maketrans({key: None for key in string.punctuation})
    for i in sentence: 
         if i in string.punctuation:   
            print("Punctuation: " + i) 
   
    for c in string.punctuation:
        sentence= sentence.replace(c,"")
    
    #return sentence.translate(table)
    return sentence


def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result



#sentence = "Red Dead Redemption 2 arrivera sur PC le 5 novembre, ainsi que sur Google Stadia - Les Numériques" #La phrase concernée

#print(extract_stop_in_sentence(sentence))
