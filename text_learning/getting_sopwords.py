### if this is the first time than your use nltk it's necessary make
#import nltk
#nltk.download() #and download all corpora

## using stopwords
#from nltk.corpus import stopwords

#sw = stopwords.words('english')

#print len(sw)


###using NLTK for stemming

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')

print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")


french_stemmer = SnowballStemmer('french')
print french_stemmer.stem('marche')


### which one should you do first?
### bag of words representation or stemming
## the good answers is Stemming before constructing your bag-of-words.



##              TFIDF
## TF = Term Frequency
## IDF = Inverse Document Frequency