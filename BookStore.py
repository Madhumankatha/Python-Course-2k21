class Book:

    def __init__(self, name, author, isbn, price = 0 ):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price

class BookStore:

    books = []
    selectedBook = []

    def __init__(self, name, author, isbn, price ):
        b = Book(name,author,isbn = isbn, price = price)
        self.books.append(b)
    
    def show(self):
        print("============== AVAILBALE BOOKS ==========")
        
        pos=0

        for book in self.books:
            print("============ ", pos, " ==========") 
            pos += 1   
            self.display(book)
            
    
    def select(self):
        print("========== SELECT A BOOK =======")
        print("====== HOW MANY BOOK YOU WANT? ======")
        neededBooks = int(input())

        for i in range(0, neededBooks ):
            print("====== INPUT THE BOOK NO ======")
            selectedBook = int(input())
            print("========== SELECTED A BOOK =======")
            b = self.getBookById(selectedBook - 1)
            self.selectedBook.append(b)
            print(self.display(b))

    def getBookById(self, position):
        return self.books[position]

    def display(self, book):
        print("Book name : ", book.name)
        print("Book ISBN : ", book.isbn)
        print("Book Price : ", book.price)
        print("Book Author : ",book.author)

    def selectedBooks(self):
        return self.selectedBook


class BillCounter:

    books = []
    def __init__(self, myBooks):
        self.books = myBooks
    
    def display(self):
        pos = 0
        for book in self.books:
            print("============ BILL COUNTER BOOKS ========")
            pos += 1
            print("============ BOOK NO", pos,"========")
            print("Book name : ", book.name)
            print("Book ISBN : ", book.isbn)
            print("Book Price : ", book.price)
            print("Book Author : ",book.author)

    def getTotal(self):
        total = sum(map(lambda b : b.price, self.books))
        print("=========== TOTAL PRICE =======")
        print(total)
    
    def getMax(self):
        total = max(map(lambda b : b.price, self.books))
        print("=========== MAX PRICE =======")
        print(total)

    def getMin(self):
        total = min(map(lambda b : b.price, self.books))
        print("=========== MIN PRICE =======")
        print(total)

    def getAuthors(self):
        print("================== AUTHORS =============")
        authors = map(lambda a : a.author, self.books)
        for author in authors:
            print(author)
    

    def delete(self):
        print("=========== DO YOU WANT DELETE? 1 = YES, 0 = NO")
        choice = int(input())
        if (choice == 1):
            print("=========== ENTER BOOK NUMBER =======")
            position = int(input())
            self.books.remove(self.getBookById(position))
        else:
            print("=========== NO BOOKS =========")

    def getBookById(self, position):
        return self.books[position - 1]

    
if "__MAIN__":

    print("========== WELCOME TO BOOK STORE ==========")

    bs = BookStore("JAVA", "ABC", "ABC123", 299)
    bs = BookStore("C++", "XYZ", "XYZ123", 499)
    bs = BookStore("C#", "ABC", "ABC567", 399)
    bs = BookStore("PYTHON", "XYZ", "XYZ567", 699)
    
    bs.show()

    bs.select()

    selectedBooks = bs.selectedBooks()
    
    print(selectedBooks)

    bc = BillCounter(selectedBooks)

    bc.display()

    bc.delete()

    bc.getTotal()

    bc.getMax()

    bc.getMin()

    bc.getAuthors()
