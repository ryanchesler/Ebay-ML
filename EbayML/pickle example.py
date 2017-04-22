import pickle
wordfile ="words.pk1"
wordstore = open(wordfile, 'rb')
wordtrain = pickle.load(wordstore)
wordstore.close()

filteredfile ="processeddata2.pk1"
filteredstore = open(filteredfile, 'wb')
pickle.dump(featurelist, filteredstore)
filteredstore.close()
