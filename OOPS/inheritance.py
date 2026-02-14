import datetime

class libraryItem:
    def __init__(self, pT, pA, pI):
        self.__title = pT
        self.__authorArtist = pA
        self.__itemID = pI
        self.__onLoan = False
        self.__dueDate = None

    def getTitle(self):
        return self.__title
    def getAuthorArtist(self):
        return self.__authorArtist
    def getItemID(self):
        return self.__itemID
    def getOnLoan(self):
        return self.__onLoan
    def getDueDate(self):
        return self.__dueDate

    def borrowing(self):
        self.__onLoan = True
        self.__dueDate = datetime.date.today() + datetime.timedelta(weeks=1)

    def returning(self):
        self.__onLoan = False
        self.__dueDate = None

    def printDetails(self):
        print("Title:", self.__title)
        print("Author/Artist:", self.__authorArtist)
        print("Item ID:", self.__itemID)
        print("On Loan:", self.__onLoan)
        print("Due date:", self.__dueDate)

class book(libraryItem):
    def __init__(self, pT, pA, pI):
        libraryItem.__init__(self, pT, pA, pI)
        self.__isRequested = False
        self.__numberOfRequests = 0

    def getIsRequested(self):
        return self.__isRequested
    def getNumberOfRequests(self):
        return self.__numberOfRequests
    def requested(self):
        self.__isRequested = True
        self.__numberOfRequests += 1



    # POLYMORPHISM: a method behaving differently in a subclass. It is redefined in the subclass to do something additionally or something else entirely 
    def printDetails(self):
        libraryItem.printDetails(self)
        print(self.__isRequested)
        print(self.__numberOfRequests)



class CD(libraryItem):
    def __init__(self, pT, pA, pI, pG):
        libraryItem.__init__(self, pT, pA, pI)
        self.__genre = pG
    
    def getGenre(self):
        return self.__genre
    
    def printDetails(self):
        libraryItem.printDetails(self)
        print(self.__genre)
    
'''myBook = book("Harry Potter", "Jk ", 1)
myBook.printDetails()
myBook.borrowing()
myBook.requested()
myBook.printDetails()'''

myCD = CD("Tere pyaar min", "Atif bhai", "3", "romance")
myCD.printDetails()