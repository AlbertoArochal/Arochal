import pandas as pd
columns = ['bookID', 'title', 'authors']
registry = pd.read_csv('/home/arochal/repos/Arochal/library/data/data/books.csv', usecols = columns)
registry['Available'] = True
print(registry.loc[registry['bookID'] == '123'])
registry.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books_registry.csv',index = False, header = True)


def borrow_book(b_bookID = input('introduce bookID: ')):
    if b_bookID in registry['bookID'] == True:
        print('correcto')
        ##registry[registry['bookID'] == b_bookID].Available = False
        ##print('You borrowed the book successfully, please return it in 15 days')
        ##registry.to_csv(r'/home/arochal/repos/Arochal/library/data/data/books_registry.csv',index = False, header = True)
    else:
        'The book you typed is not available at the time, plese try again in some days'
    

borrow_book()