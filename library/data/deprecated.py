import pandas as pd

'''def edit_book_menu(ISBN = input('Introduce ISBN code: ')):
    book_cols = ['title', 'authors', 'isbn', '  num_pages']
    book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = book_cols)
    if book_catalogue[book_catalogue.str.contains(ISBN).any(1)]:
        select_options_menu = input('What field would you want to edit: 1- All | 2- Title | 3- Author(s) | 4- ISBN Code | 5- Number of Pages | 6- Age Rating | 7- Quit')
        try:
            if float(select_options_menu) == 1:
                print('pasando')
            elif select_options_menu == 2:
                print(str(edit_title(ISBN)))
            elif float(select_options_menu) == 3:
                print(str(edit_author(ISBN)))
            elif float(select_options_menu) == 4:
                priont(str(edit_isbn(ISBN)))
            elif float(select_options_menu) == 5:
                print(str(edit_n_pages(ISBN)))
            elif float(select_options_menu) == 6:
                print(str(edit_age_rating(ISBN)))
            else:
                print('pasando')
                pass
        except:
            return print('The option is not valid. Edition process will be terminated')
    else:
        return print('That isbn is not in our database, bitch')
        
edit_book_menu()'''

book_cols = ['bookID', 'title', 'authors', 'average_rating', '  num_pages']
book_catalogue = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', sep = ',', nrows = 500, usecols = book_cols )
book_catalogue.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books.csv', index = False)
