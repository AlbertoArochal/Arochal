
import time
import random
import pandas as pd
<<<<<<< HEAD

'''Library system management'''

class library:                  # Class library that generate a random key in order to acces staff functions, and another one to be able to delete books of the catalogue
    secret_key = random.randint(1000, 9999)                   
    delkey = random.randint(100, 999)                         

    def __init__(self, libraryName, allBooks, listOfBooks): 
=======
import numpy as np

class library:
    secret_key = random.randint(1000, 9999)                   
    delkey = random.randint(100, 999)                         

    def __init__(self, libraryName, allBooks, listOfBooks):
>>>>>>> feature.readme
        self.lendbooklis = {}
        self.allBooks = allBooks
        self.list_of_books = listOfBooks
        self.libraryName = libraryName

<<<<<<< HEAD
    def displayAllBooks(self):              # Display books of the catalogue. You must choose the amount of books you want to import from a 500+ books stored in a csv, when you start the program.
=======
    def displayAllBooks(self):
>>>>>>> feature.readme
        print(self.allBooks)

    def displayBooks(self):                           
        return print(self.list_of_books)
 
<<<<<<< HEAD
    def lendBook(self):                            #lend book functions, available to users, but not to staff.  
=======
    def lendBook(self):                                
>>>>>>> feature.readme
        lenderName = input("Enter your name : ")
        lendBook = input("Enter book you want to lend : ")
        if lendBook in self.list_of_books:
            print("You can take the book and donn't forgot to return on time.")
            self.lendbooklis[lenderName] = lendBook
            self.list_of_books.remove(lendBook)
        else:
            print(f"Book '{lendBook}' is currently not available")

    def displaylendedbook(self):                               
        return print(self.lendbooklis)

<<<<<<< HEAD
    def addBook(self):                                          #Add book function, available to staff, not to regular users of the library.
=======
    def addBook(self):                                          
>>>>>>> feature.readme
        addbok = input("Enter the book you want to add : ")
        self.list_of_books.append(addbok)
        self.allBooks.append(addbok)

<<<<<<< HEAD
    def returnBook(self):                                      # Returns a lend book to the available catalogue, available to regular users.
=======
    def returnBook(self):                                      
>>>>>>> feature.readme
        retname = input("Enter your name : ")
        retbok = input("Enter book you want to return : ")
        self.list_of_books.append(retbok)
        self.lendbooklis.pop(retname)

<<<<<<< HEAD
    def removeBook(self):                                     # Erase completely a book from the catalogue, available only to staff users with deletion random key.
=======
    def removeBook(self):                                     
>>>>>>> feature.readme
        count = 2
        while (count > 0):
            rmvkey = input("Enter 'Deletion-key' = ")
            if rmvkey == self.delkey:
                delbook = input("enter book you want to remove from your library : ")
                if delbook in self.list_of_books:
                    self.list_of_books.remove(delbook)
                    self.allBooks.remove(delbook)
                    break
<<<<<<< HEAD
                else: print("The book is not present on our catalogue")
=======
                else: print("No such book in library to remove")
>>>>>>> feature.readme
            else:
                    print("Invalid key!")
            count -= 1

<<<<<<< HEAD
    def changeKey(self):                                    # Change staff key function. 
=======
    def changeKey(self):
>>>>>>> feature.readme
        key = int(input("Enter secret key : "))
        count = 2
        while count>0:
            if key == self.secret_key:
                while True:
<<<<<<< HEAD
                    keyChange = input("1 --> Change Secret Key\n\t2 --> Change deletion key")
                    if keyChange == "1":
                        while True:
                            new_secretKey1 = int(input("Enter new Secret key : "))
                            new_secretKey2 = int(input("Re enter new Secret key : "))
=======
                    keyChange = input("\t1 --> Change Secret Key\n\t2 --> Change deletion key")
                    if keyChange == "1":
                        while True:
                            new_secretKey1 = int(input("Enter new Secret key : "))
                            new_secretKey2 = int(input("Re-enter new Secret key : "))
>>>>>>> feature.readme
                            if new_secretKey1 == new_secretKey2:
                                self.secret_key = new_secretKey1
                                break
                            else:
                                print("key didn't match..!")
                                continue
                    elif keyChange == "2":
                        while True:
                            new_delKey1 = int(input("Enter new Deletion key : "))
                            new_delKey2 = int(input("Re-enter new Deletion key : "))
                            if new_delKey1 == new_delKey2:
                                self.delkey = new_delKey1
                                break
                            else:
                                print("key didn't match..!")
                                continue
                    elif keyChange == "0":
                        print("exit...")
                        time.sleep(3)
                        break
                    else:
                        print('The option you have choose is not available..! Try again')
                        continue
            else:
                print('THE INTRODUCED KEY IS NOT VALID..!')
                count -= 1
                continue

<<<<<<< HEAD

# Menu for staff members of the library available only if you introduce the correct key when you start the program.

def admin():
    print("\t Display all books --> 1\t Lend book --> 2\n Display lended books --> 3 Add new book --> 4"
          "\n Return a book --> 5 Remove book --> 6\nDisplay All books --> 7"
          "Change Key/Password --> 8\n Exit --> 0")
=======
def admin():
    print("\tDisplay all available books --> 1\tLend book --> 2\n\tDisplay lended books --> 3\t\t\tAdd new book --> 4"
          "\n\tReturn a book --> 5\t\t\t\t\tRemove book --> 6\n\tDisplay All books --> 7"
          "\t\t\t\tChange Keys --> 8\n\tExit --> 0")
>>>>>>> feature.readme
    choice = int(input("Enter your choice : "))
    Exit = False
    try:
        while Exit is not True:
            if choice == 0:
                localtime = time.asctime(time.localtime(time.time()))
                Exit = True
<<<<<<< HEAD
                return f"Thank You, hope you like our service!{localtime}"
=======
                return f"Thank You, hope you like our service!\t\t\t\t{localtime}"
>>>>>>> feature.readme
            elif choice == 1:
                xlib.displayBooks()
            elif choice == 2:
                xlib.lendBook()
            elif choice == 3:
                xlib.displaylendedbook()
            elif choice == 4:
                xlib.addBook()
            elif choice == 5:
                xlib.returnBook()
            elif choice == 6:
                xlib.removeBook()
            elif choice == 7:
                xlib.displayAllBooks()
            elif choice == 8:
                xlib.changeKey()
            else:
                print("Invalid choice")
<<<<<<< HEAD
            choice = int(input("Enter action : "))
    except Exception as e:
        print(e)

#Regular user menu, available if you dont have staff key or choose to not introduce it.

def userfun():
    print("  Display catalogue --> 1Lend book --> 2 Display all books --> 4\t"
          "\tReturn a book --> 3 Exit --> 0")
=======
            choice = int(input("Enter your choice : "))
    except Exception as e:
        print(e)


def userfun():
    print("  Display entire catalogue --> 1\t\t\tLend book --> 2\n\t\t    Display all books --> 4\t"
          "\tReturn a book --> 3\nExit --> 0")
>>>>>>> feature.readme
    choice = int(input("Enter your choice : "))
    Exit = False
    while Exit is not True:
        if choice == 0:
            localtime = time.asctime(time.localtime(time.time()))
            Exit = True
<<<<<<< HEAD
            return f"Thank You, please visit us again soon!!"
=======
            return f"Thank You, please visit us again soon!!\t\t\t\t"
>>>>>>> feature.readme
        elif choice == 1:
            xlib.displayBooks()
        elif choice == 2:
            xlib.lendBook()
        elif choice == 3:
            xlib.returnBook()
        elif choice == 4:
            xlib.displayAllBooks()
        else:
            print("Invalid choice")
        choice = int(input("Enter your choice : "))

<<<<<<< HEAD

# Menu where you must choose the amount of books in the catalogue you want to get from csv file.
exit = False
while exit is not True:
    libname = input("Enter your library name : ")
    initial_stock = int(input("Enter the amount of books you're putting in library : "))
=======
exit = False
while exit is not True:
    libname = input("Enter your library name : ")
    initial_stock = int(input("Enter amount of books you're putting in library : "))
>>>>>>> feature.readme
    initial_book_list = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = ['title'], nrows = initial_stock)
    print("enter books")
    for item in range(initial_stock):
        bookstock = {'title': input()}
        initial_book_list.append(bookstock, ignore_index=True)
    ALLBOOKS = initial_book_list[:]
    xlib = library(libname, ALLBOOKS, initial_book_list)

<<<<<<< HEAD
    print(f"\tYour secret key = {library.secret_key} Your deletion key = {library.delkey}")

    all_set = input("We're all set, press any key to star press 0 to make changes or setup again"
                    "")
=======
    print(f"\tYour secret key = {library.secret_key}\n\t Your deletion key = {library.delkey}\n")

    all_set = input("We're all set, press any key to start\t\t\tpress 0 to make changes or setup again\n"
                    "\t\t\t\t\t\t\t\t\t\t ")
>>>>>>> feature.readme
    if all_set == "0":
        continue
    else:
        break

<<<<<<< HEAD
# Initial menu of the program, where tyou need to choose to enter as a member of the staff or not.

=======
>>>>>>> feature.readme
lib2 = library.secret_key                 

if __name__ == '__main__':                
    localtime = time.asctime(time.localtime(time.time()))
<<<<<<< HEAD
    print(f"{localtime}Exit --> 0")
=======
    print(f"{localtime}\t\t\t\t\t\t\tExit --> 0")
>>>>>>> feature.readme
    Exit = False
    while Exit is not True:
        user = input("Are you a member of the staff (y/n) : ")
        kc=2
        if user == "y":
            while(kc > 0):
                adkey = int(input("Enter Staff key : "))
                if adkey == lib2:
<<<<<<< HEAD
                    print("WELCOME DEAR CUSTOMER")
=======
                    print("////////////WELCOME DEAR CUSTOMER/////////////")
>>>>>>> feature.readme
                    print(admin())
                    break
                else:
                    print("Invalid key!")
                kc -= 1
        elif user == "n":
<<<<<<< HEAD
            print(f"Welcome to {xlib.libraryName}")
=======
            print(f"/////////////////////Welcome to {xlib.libraryName}//////////////////////// ")
>>>>>>> feature.readme
            print(userfun())
        elif user == "0":
            Exit = True
            continue
        else:
            print("Please answer in y for 'yes' or n for 'no' ")







    
