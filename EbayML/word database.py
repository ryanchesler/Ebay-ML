import pickle
import sys
words = []
wordsfile = "processeddata.pk1"
wordstore = open(wordsfile, 'wb')
pickle.dump(words, wordstore)
wordstore.close()
        
