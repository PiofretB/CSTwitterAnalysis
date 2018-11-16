from textblob import TextBlob
import nltk

zen = TextBlob('''Beautiful is better than ugly.
               Explicit is better than implicit.
               Simple is better than complex.''')
print(zen.words)
print(zen.sentences)
for sentence in zen.sentences:
    print(sentence.tags)
    print(sentence.sentiment)

print(zen.translate(to='ja'))

b = TextBlob("I havv goood speling!")
print(b.correct())
