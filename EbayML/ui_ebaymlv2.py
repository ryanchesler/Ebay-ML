# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Magic\OneDrive\Documents\EbayResources\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import tensorflow as tf
from PyQt4 import QtCore, QtGui
import urllib.request
import pickle
from xml.dom.minidom import parse
import sys
import webbrowser
import numpy
import gensim
datastore = {}
try:
    _fromUtf8 = QtCore.QString.fromUtf8
    
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(361, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout.addLayout(self.horizontalLayout)
        name = "a search"
        self.name = name
        self.searchdb ="searchterm.pk1"
        self.searchesstore = open(self.searchdb, 'rb')
        self.searches = pickle.load(self.searchesstore)
        self.searchesstore.close()
        self.listWidget = QtGui.QListWidget()
        self.listWidget.addItems(self.searches)
        self.listWidget.setCurrentRow(0)
        self.y = self.listWidget.currentRow()
        buttonLayout = QtGui.QVBoxLayout()
        for text, slot in (("&Add...", self.add),
                           ("&Edit...", self.edit),
                           ("&Remove...", self.remove),
                           ("&Sort", self.listWidget.sortItems)):
            button = QtGui.QPushButton(text)
            buttonLayout.addWidget(button)
            QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), slot)
        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.listWidget)
        self.layout.addLayout(buttonLayout)
        self.verticalLayout.addLayout(self.layout)
        self.verticalLayout.addLayout
        self.iterate = QtGui.QPushButton(self.centralwidget)
        self.iterate.setObjectName(_fromUtf8("iterate"))
        self.verticalLayout.addWidget(self.iterate)
        self.trainword = QtGui.QPushButton(self.centralwidget)
        self.trainword.setObjectName(_fromUtf8("Train Words"))
        self.verticalLayout.addWidget(self.trainword)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.acceptableprice = QtGui.QLineEdit(self.centralwidget)
        self.acceptableprice.setObjectName(_fromUtf8("acceptableprice"))
        self.horizontalLayout_3.addWidget(self.acceptableprice)
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout_3.addWidget(self.search)
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setObjectName(_fromUtf8("back"))
        self.horizontalLayout_3.addWidget(self.back)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.interested = QtGui.QPushButton(self.centralwidget)
        self.interested.setObjectName(_fromUtf8("interested"))
        self.horizontalLayout_3.addWidget(self.interested)
        self.notinterested = QtGui.QPushButton(self.centralwidget)
        self.notinterested.setObjectName(_fromUtf8("notinterested"))
        self.horizontalLayout_3.addWidget(self.notinterested)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        
        QtCore.QObject.connect(self.back, QtCore.SIGNAL("clicked()"), self.backfunc)
        QtCore.QObject.connect(self.search, QtCore.SIGNAL("clicked()"), self.makesearch)
        QtCore.QObject.connect(self.interested, QtCore.SIGNAL("clicked()"), self.classintfunc)
        QtCore.QObject.connect(self.notinterested, QtCore.SIGNAL("clicked()"), self.classnotintfunc)
        QtCore.QObject.connect(self.iterate, QtCore.SIGNAL("clicked()"), self.iteratefunc)
        QtCore.QObject.connect(self.trainword, QtCore.SIGNAL("clicked()"), self.word2vec)
        self.retranslateUi(MainWindow)
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.search.setText(_translate("MainWindow", "Search", None))
        self.iterate.setText(_translate("MainWindow", "Iterate", None))
        self.trainword.setText(_translate("MainWindow", "Word2Vec", None))
        self.interested.setText(_translate("MainWindow", "Interested", None))
        self.notinterested.setText(_translate("MainWindow", "Not Interested", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.back.setText(_translate("MainWindow", "Back", None))
    def add(self):
        row = self.listWidget.currentRow()
        title = "Add {}".format(self.name)
        string, ok = QtGui.QInputDialog.getText(MainWindow,title, title)
        if ok and string:
            self.listWidget.insertItem(row, string)
        self.searchesstore = open(self.searchdb, 'rb')
        self.searches = pickle.load(self.searchesstore)
        self.searchesstore.close()
        if string not in self.searches:
            self.searches.append(string)
            self.searchesstore = open(self.searchdb, 'wb')
            pickle.dump(self.searches, self.searchesstore)
            self.searchesstore.close()


    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        self.searchesstore = open(self.searchdb, 'rb')
        self.searches = pickle.load(self.searchesstore)
        self.searchesstore.close()
        self.searches.remove(item.text())
        if item is not None:
            title = "Edit {}".format(self.name)
            string, ok = QtGui.QInputDialog.getText(MainWindow, title, title,
                    QtGui.QLineEdit.Normal, item.text())
            if ok and string:
                item.setText(string)    
            self.searches.insert(row, item.text())
            self.searchesstore = open(self.searchdb, 'wb')
            pickle.dump(self.searches, self.searchesstore)
            self.searchesstore.close()
            

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        self.searchesstore = open(self.searchdb, 'rb')
        self.searches = pickle.load(self.searchesstore)
        self.searchesstore.close()
        self.searches.remove(item.text())
        if item is None:
            return
        reply = QtGui.QMessageBox.question(MainWindow, "Remove {}".format(
                self.name), "Remove {} `{}'?".format(
                self.name, item.text()),
                QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item
        self.searchesstore = open(self.searchdb, 'wb')
        pickle.dump(self.searches, self.searchesstore)
        self.searchesstore.close()
    def accept(self):
        self.stringlist = []
        for row in range(self.listWidget.count()):
            self.stringlist.append(self.listWidget.item(row).text())
        self.emit(SIGNAL("acceptedList(QStringList)"), self.stringlist)
        QDialog.accept(self)
        
    def makesearch(self):
        global x
        dbfile ="ebaydata.pk1"
        dbstore = open(dbfile, 'rb')
        global itemData
        itemData = pickle.load(dbstore)
        dbstore.close()
        x = 0
        global search
        search = self.listWidget.currentItem().text()
        self.buttonClicked(search, x)
    def backfunc(self):
        global x
        x-=1
        global search
        self.buttonClicked(search, x)
    def classintfunc(self):
        global x
        x+=1
        search = self.listWidget.currentItem().text()
        self.classint(search, x)
    def classnotintfunc(self):
        global x
        x+=1
        search = self.listWidget.currentItem().text()
        self.classnotint(search, x)
    def buttonClicked(self,search, x):
        print(x)
        ThreadClass.datascrape(ThreadClass, search, x)
        self.openBrowser(itemURL)
    def classint(self,search, x):
        accprice = self.acceptableprice.text()
        ThreadClass.datastore(ThreadClass, itemData, [1,0], accprice)
        self.findNewListing()
        ThreadClass.datascrape(ThreadClass, search, x)
        self.openBrowser(itemURL)        
    def classnotint(self, search, x):
        ThreadClass.datastore(ThreadClass, itemData, [0,1], 0)
        self.findNewListing()
        ThreadClass.datascrape(ThreadClass, search, x)
        self.openBrowser(itemURL)
    def openBrowser(self, itemURL):
        webbrowser.open(itemURL, new=0, autoraise=True)
    def findNewListing(self):
        global x
        print(x)
        try:
            itemId = items[x].getElementsByTagName("itemId")[0].firstChild.data
            while itemId in itemData:
                x+=1
                itemId = items[x].getElementsByTagName("itemId")[0].firstChild.data
        except:
            print("No more items")
    def iteratefunc(self):
        self.y = self.listWidget.currentRow() 
        self.y+=1
        self.listWidget.setCurrentRow(self.y)
        self.makesearch()
    def word2vecfunc(self):
        self.word2vec()
        
    def word2vec(self):
        dbfile ="ebaydata.pk1"
        dbstore = open(dbfile, 'rb')
        datadump = pickle.load(dbstore)
        dbstore.close()
        words = []
        for k, v in datadump.items():
            split = v[0].split()
            words.append(split)
        firstsent = words[0]
        bigram = gensim.models.phrases.Phrases(words)
        print(bigram[firstsent])
        model = gensim.models.Word2Vec(bigram[words], min_count = 5, size = 20, alpha = .025, iter = 5, hs=1, negative = 0)
        print(model)
        print(model.score(["i7 4770".split()]))
        print(model[search])
        print(model.most_similar(search))
        

class ThreadClass(QtCore.QThread):
    def __init__(self):
        super(ThreadClass, self).__init__()
    def datascrape(ThreadClass, searchterm, x):
        if (x < 1):
                url = 'http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&sortOrder=PricePlusShippingLowest&buyerPostalCode=92128&SERVICE-VERSION=1.13.0&SECURITY-APPNAME=RyanChes-EbaySear-PRD-d13d69895-95fa1322&RESPONSE-DATA-FORMAT=XML&REST-PAYLOAD&keywords=' + searchterm
                url = url.replace(" ", "%20")
                apiResult = urllib.request.urlopen(url)
                document = apiResult
                parseddoc = parse(document)
                global items
                items = parseddoc.getElementsByTagName("item")
                global listingTitle
                global currentPrice
                global shippingPrice
                global cond
                global itemId
                global previewImage
                global listingType
        else:
            pass
        global itemURL
        global itemId
        try:
            itemId = items[x].getElementsByTagName("itemId")[0].firstChild.data
            listingTitle = items[x].getElementsByTagName("title")[0].firstChild.data
            region = items[x].getElementsByTagName("globalId")[0].firstChild.data
            timeLeft = items[x].getElementsByTagName("timeLeft")[0].firstChild.data
            listingCategory = items[x].getElementsByTagName("categoryId")[0].firstChild.data
            location = items[x].getElementsByTagName("location")[0].firstChild.data
            country = items[x].getElementsByTagName("country")[0].firstChild.data
            shippingCost = items[x].getElementsByTagName("shippingServiceCost")[0].firstChild.data
            shipToLocations = items[x].getElementsByTagName("shipToLocations")[0].firstChild.data
            currentPrice = items[x].getElementsByTagName("currentPrice")[0].firstChild.data
            bestOffer = items[x].getElementsByTagName("bestOfferEnabled")[0].firstChild.data
            itemURL = items[x].getElementsByTagName("viewItemURL")[0].firstChild.data
            listingType = items[x].getElementsByTagName("listingType")[0].firstChild.data
        except:
            print("some item could not be parsed")
        try:
                cond = items[x].getElementsByTagName("conditionDisplayName")[0].firstChild.data
                condId = items[x].getElementsByTagName("conditionId")[0].firstChild.data
        except:
                pass
        global itemData
        try:
            itemData[itemId] = [listingTitle, region, timeLeft, listingCategory, location, country, shippingCost, shipToLocations, currentPrice, bestOffer, itemURL, listingType]
        except:
            print("items could not be put in dict")
        try:
            itemData[itemId].append(condId)
        except:
            pass
    def datastore(ThreadClass, itemData, datalabel, accprice):
        global itemId
        itemData[itemId][8] = accprice
        dbfile ="ebaydata.pk1"
        dbstore = open(dbfile, 'wb')
        try:
            print(datalabel)
            print (itemData[itemId])
            itemData[itemId].append(datalabel)            
            pickle.dump(itemData, dbstore)
        except:
            print("Item Data was not valid")
        dbstore.close()
        
            
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

