from pydantic import ValidationError
from dto.author import Author
from dto.bookItem import  BookItem
from dto.bookStore import BookStore

def creating_items():
    print()
#correct start
    try: 
        my_author1= Author(
            author_name="J.R.R. Tolkien",
            author_id="SIAK-1144"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : Author 1:  {my_author1}')

    try: 
        my_author2= Author(
            author_name="Dan Brown",
            author_id="DBUS-7028"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : Author 2:  {my_author2}')

    try:
        my_book1= BookItem(
            book_name= "The Lord of The Rings",
            book_author=    my_author1,
            year_published="1954"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : book 1:  {my_book1}')

    try:
        my_book2= BookItem(
            book_name= "DaVinci Code",
            book_author=    my_author2,
            year_published="2003"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : book 2:  {my_book2}')

    try:
        my_book_store1=BookStore(
            name_of_bookstore="Puro Verso",
            book_shelve=[my_book1, my_book2]
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')        
    else:
        print(f'POSITIVE : BookStore 1 :  {my_book_store1}'), print()#giving spacing
# end of correct entries

#incorrect values as variable for print referencing 
    wrong_author_name1="J.R.R. 4olkien"
    wrong_author_name2="j.j.r. tolkien"
    wrong_author_id="SI3K-1?44"
    wrong_publishing_year ="2025"
    wrong_book_shelve=[my_book1, my_author1]
#end of incorrect values as variable for print referencing

#start of TRYing wrong entries
    try: #wrong name
        my_wrong_author1= Author(
            author_name=wrong_author_name1,
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor name ({wrong_author_name1})')

    try: #wrong name
        my_wrong_author2= Author(
            author_name=wrong_author_name2,
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor name ({wrong_author_name2})')    

    try: #wrong id
        my_wrong_author2= Author(
            author_name="J.R.R. Tolkien",
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor id ({wrong_author_id})')

    try: #wrong publishing year
        my_wrong_book1= BookItem(
            book_name= "The Lord of The Rings",
            book_author= my_author1,
            year_published=wrong_publishing_year
        )
    except ValidationError as ve:
        print(f'Inserting WRONG publishing year ({wrong_publishing_year})')

    try: #wrong item added instead of BOOK class item
        my_wrong_book_store1=BookStore(
            name_of_bookstore="Puro Verso",
            book_shelve=wrong_book_shelve
        )
    except ValidationError as ve:
        print(f'Inserting WRONG bookshelve ({wrong_book_shelve})')

def main():
    creating_items()

if __name__=="__main__":
    main()