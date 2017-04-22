import pickle
import urllib.request
from xml.dom.minidom import parse
import sys
import random
searchdb ="searchterm.pk1"
searchesstore = open(searchdb, 'rb')
searches = pickle.load(searchesstore)
searchesstore.close()
wordsfile = "words.pk1"
wordstore = open(wordsfile, 'rb')
words = pickle.load(wordstore)
wordstore.close()
searchindex = 1
while searchindex != -1:
    searchindex = random.randrange(0,len(searches))
    search = searches[searchindex]
    print(search)
    url = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&sortOrder=StartTimeNewest&buyerPostalCode=92128&SERVICE-VERSION=1.13.0&SECURITY-APPNAME=RyanChes-EbaySear-PRD-d13d69895-95fa1322&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&keywords=' + search
    url = url.replace(" ", "%20")
    apiResult = urllib.request.urlopen(url)
    document = apiResult
    parseddoc = parse(document)
    items = parseddoc.getElementsByTagName("item")
    x = 0
    for item in items:
        if item in items:
            try:
                
                listingTitle = items[x].getElementsByTagName("title")[0].firstChild.data
                x+=1
                
                if listingTitle not in words:
                    words.append(listingTitle)
                    wordstore = open(wordsfile, 'wb')
                    pickle.dump(words, wordstore)
                    wordstore.close()
            except:
                wordstore.close()
                print("something went wrong")
        else:
            pass

