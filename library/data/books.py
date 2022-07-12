
from importlib_metadata import NullFinder
import pandas as pd
from sqlalchemy import null, true

''' Función para añadir un título a la báse de datos, argumentos:
    title
    authors
    num_pages
    '''
    '''def add_book(title = input('Introduce title: '), 
    authors = input('Author(s): '), 
    num_pages = input('Number of Pages: '),
    age_rating = input('Average Rating: '), 
    bookID = input('enter bookID ')):
    book_cols = ['bookID', 'title', 'authors', 'average_rating', '  num_pages']
    book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = book_cols)
    book_catalogue.loc[len(book_catalogue.index)] = [bookID, title, authors, num_pages, age_rating]
    book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header=True)

def del_book(bookIDel = input('Introduce bookID to delete: ')):
    book_cols = ['bookID', 'title', 'authors', 'average_rating', '  num_pages']
    book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = book_cols)
    book_catalogue = book_catalogue.loc[book_catalogue['bookID'] == int(bookIDel)]
    book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header=True)

def edit_book_info(selection_edit = input('What field would you want to edit: 1- Exit | 2- Title | 3- Author(s) | 4- Number of Pages | 5- Rating: '), bookIDedit = input('Introduzca el bookID: ')):
    book_cols = ['bookID', 'title', 'authors', 'average_rating', '  num_pages']
    book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = book_cols)
    if selection_edit == '2':
        def edit_title(new_name = input('Enter new title: ')):
            book_catalogue.loc[book_catalogue.bookID == int(bookIDedit), 'title'] = new_name
            book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header = True)
        edit_title()
        print('Changes have been saved')
    elif selection_edit == '3':
        def edit_author(new_author = input('Introduce new author(s): ')):
            book_catalogue.loc[book_catalogue.bookID == int(bookIDedit), 'authors'] = new_author
            book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header = True)
        edit_author()
        print('Changes have been saved')
    elif selection_edit == '4':
        def edit_n_pages(new_n_pages = input('Enter new pages number: ')):
            book_catalogue.loc[book_catalogue.bookID == int(bookIDedit), '  num_pages'] = new_n_pages
            book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header = True)
        edit_n_pages()
        print('Changes have been saved')
    elif selection_edit == '5':
        def edit_rating(new_rate = input('Enter new rate: ')):
            book_catalogue.loc[book_catalogue.bookID == int(bookIDedit), 'average_rating'] = new_rate
            book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv',index = False, header = True)
        edit_rating()
        print('Changes have been saved')
    elif selection_edit == '1':
        print('exiting...')
        quit
    else:
        print('Selection not valid, please try again')

import pandas as pd
        
def consult_book(IDconsult = input('Introduce Book_ID to consult: ')):
    book_cols = ['bookID', 'title', 'authors', 'average_rating', '  num_pages']
    book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = book_cols)
    print(book_catalogue.loc[book_catalogue['bookID'] == int(IDconsult)])'''

















