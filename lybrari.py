class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
        self.barow=False


    def __str__(self):
        status="borweed" if self.barow else "Available"
        return f"{self.title} | {self.author} | {self.year} | {status}"
        
class Library:
    def __init__(self):
        self.book=[]
        
    def add_book(self):
        book=input("enter your book name you want to add: ")
        author=input("ente name of author")
        year=input("Enter year of books")
        
        new_book=Book(book,author,year)
        self.book.append(new_book)

        print("Your book is add sussucfully!!!")


    def show_book(self):
        if len(self.book)==0:
            print("NO books are found..")
        else:
            print("\nAll books are:")
            for book in self.book:
                print(book)    


    def seacrh_book(self):
        search=input("Enter title of the book:")
        found = False
        for book in self.book:
            if book.title.lower() == search.lower():
                print("book found")
                print(book)
                found=True
                break
        if not found:
                print("Book not found!")

    def borrow_book(self):
        title=input("enter tile of the book")
        found=False
        for book in self.book:
            if book.title.lower()==title.lower():
                found=True
                if book.borrow==False:
                    book.borrow=True
                    print(f"{book.title} is borrowed successfully..")
                else:
                    print("Book is already borrwed!!")    
                break

        if not found:
                print("Boook is not found")   

    def retrun(self):
        title=input("enter tile of the book")
        found=False
        for book in self.book:
            if book.title.lower()==title.lower():
                found=True
                if book.borrow==True:
                    book.borrow=False
                    print(f"{book.title}Book is retrun sussesfully..")

                else:
                    print(f"{book.title} is not borrowed , Please try again!!")    
        if not found:
            print("Book is not available")

lib1= Library()

while True:
    print("\n📚 Library Menu")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice=input("Enter your choice>>")


    if choice == "1":
        lib1.show_book()
    elif choice == "2":
        lib1.show_book()
    elif choice == "3":
        lib1.seacrh_book()
    elif choice == "4":
        lib1.borrow_book()
    elif choice == "5":
        lib1.retrun()
    elif choice == "6":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")

