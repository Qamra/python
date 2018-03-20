import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories = genre))
genre_word = [(genre,word)
              for genre in ['news','romance']
              for word in brown.words(categories = genre)]
print(len(genre_word))
print(genre_word[:4])