
class store:

    def __init__(self, name, author, isbn, price) -> None:
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price

    def print(self):
        print(self.name)

class book:

    books = []

    def __init__(self, bookname, author, isbn, price):
        # Empty Constructor
        s = store(bookname,author,isbn,price)
        self.books.append(s) 

    def getById(self,id):
        return self.books[id-1]
    
    def sort(self):
        return self.books.sort()
    
    def deleteAll(self):
        return self.books.clear()

    def total(self):
        return sum(map(lambda b : b.price, self.books))
    
    def printAll(self):
        for book in self.books:
            print("======================")
            print("Book name", book.name)
            print("Book isbn", book.isbn)
            print("Book author", book.author)
            print("Book price", book.price)
    
    print("---------Printed all books-------------")


if "__MAIN__":
    print("========== MAIN METHOD =============")

    bookshop = book("JAVA", "MADHU", "ABC12345", 299)

    bookshop = book("JAVA", "MADHU", "ABC12345", 299)

    bookshop.printAll()

    print(bookshop.getById(1))
    print(bookshop.total())

