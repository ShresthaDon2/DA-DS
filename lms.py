# LMS => Library management system
# 1. Add books, update ,remove, delete
# 2. Types of book => Physical, online

# books = []

# class Book:
#     type = "Physical Book"
    
#     def __init__(self,name,author,pages):
#         self.name = name
#         self.author = author
#         self.pages = pages
#         books.append(self.name)
# spiderman = Book("Spiderman","ABC",114)
# harry_potter = Book("Harry Potter","J.K Rowling",411)

# print(spiderman.name)

# print(books)


import os

class Book:
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.name} is being called"

class Ebook(Book):
    def __init__(self,name,author,pages,file_size):
        super().__init__(name,author,pages)
        self.file_size = file_size


class Library:
    def __init__(self,filename = "library.txt"):
        self.filename = filename
        self.books = self.load_books()
        
    def load_books(self):
        books=[]
        if os.path.exists(self.filename):
          with open(self.filename,"r") as file:
              for i in file:
                  books.append(i.strip())
        return books  
    
    def save_books(self):
        with open(self.filename,"w") as file:
            for book in self.books:
                file.write(book + "\n")
                
        
    def add_book(self,book):
        try:
            self.books.append(book.name)
            self.save_books()
            print(f"{book.name} added to library")
        except Exception as e:
            print("Error",e)
            
    def remove_book(self, book_name):
        try:
            if book_name in self.books:
                self.books.remove(book_name)
                self.save_books()
                print(f"{book_name} has been removed.")
            else:
                print("Book not found.")
        except Exception as e:
            print(" Error removing book:", e)

    def search_book(self, book_name):
        try:
            if book_name in self.books:
                print(f"{book_name} found in library.")
            else:
                print(" Book not found.")
        except Exception as e:
            print("Error searching book:", e)

    def display_books(self):
        if not self.books:
            print(" No books available in the library.")
        else:
            print("\n Books in Library:")
            for book in self.books:
                print(f" - {book}")
            
    

def main():
    l1 = Library()


    book1 = Book("Harry Potter", "J.K Rowling", 415)
    ebook1 = Ebook("Game of Thrones", "G.R.R. Martin", 850, "5MB")
    l1.add_book(book1)
    l1.add_book(ebook1)
  
    while True:
        print("\n======= LIBRARY MENU =======")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            try:
                name = input("Enter book name: ")
                author = input("Enter author name: ")
                pages = int(input("Enter number of pages: "))
                book_type = input("Is it an Ebook? (y/n): ").lower()
                if book_type == "y":
                    size = input("Enter file size: ")
                    new_book = Ebook(name, author, pages, size)
                else:
                    new_book = Book(name, author, pages)
                l1.add_book(new_book)
            except Exception as e:
                print("Error adding book:", e)

        elif choice == 2:
            book_name = input("Enter the book name to remove: ")
            l1.remove_book(book_name)

        elif choice == 3:
            book_name = input("Enter the book name to search: ")
            l1.search_book(book_name)

        elif choice == 4:
            l1.display_books()

        elif choice == 5:
            print(" Exiting Library System. Goodbye!")
            break

        else:
            print(" Invalid choice. Please try again.")



if __name__ == "__main__":
    main()