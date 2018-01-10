import nltk

sentence = "i am trying this for first time"

tokens = nltk.word_tokenize(sentence)

print(tokens)

searched = sentence.concordence('trying')

print(searched)