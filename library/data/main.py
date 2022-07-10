import books as b
from datetime import date
import pandas as pd


listOfBooks = pd.red_csv('/home/arochal/repos/Arochal/library/data/data/books.csv')

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def add_book(self):
        b.add_book()

    def edit_book(self):
        b.edit_book_info()

    def delete_book(self):
        b.del_book()
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day!")

class Student: 
    def requestBook(self):

        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centralLibrary = Library([listOfBooks.title.head()])
    student = Student()
    
    while(True):
        welcomeMsg = '''\n Welcome to Norco Public Library!
        Please choose an option:
        1. Request a book
        2. Return a book
        3. Exit the Library'''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()  
            centralLibrary.borrowBook(student.requestBook())
        elif a == 2:
            centralLibrary.returnBook(student.returnBook())
        elif a == 3:
            print("Thanks for choosing our Library.")
            break
        else:
            print("Invalid Choice!")






    
