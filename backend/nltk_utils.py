


import numpy as np
import nltk

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

nltk.download('averaged_perceptron_tagger')



def tokenize(sentence):

    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number

    """

    return nltk.word_tokenize(sentence)


def lemmatize(word):

    """
    Lemmatizing = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [lemmatize(w) for w in words]
    -> ["organ", "organ", "organ"]


    """

    return wnl.lemmatize(word)




def bag_of_words(tokenized_sentence, words):


    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag  = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """


    # Lemmatize each word
    sentence_words = [lemmatize(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
    