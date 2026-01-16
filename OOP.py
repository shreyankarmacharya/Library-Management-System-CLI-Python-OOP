class Book:
    def __init__(self, book_idP, titleP, authorP, is_availableP):
        self.BookID = book_idP
        self.Title = titleP
        self.Author = authorP
        self.__isAvailable = is_availableP

    def SetStatus(self, status):
        if status.lower() == 'borrowed':
            self.__isAvailable = False
        elif status.lower() == 'returned':
            self.__isAvailable = True
        else:
            return -1

    def GetStatus(self):
        return self.__isAvailable

    def DisplayAllInfo(self):
        return self.BookID, self.Title, self.Author



class User:
    def __init__(self, user_idP, nameP):
        self.__UserID = user_idP
        self.__Name = nameP
        self.BorrowedList = []
        self.BorrowNumber = 0

    def RemoveBook(self, BookID):
        if self.BorrowNumber == 0:
            return -1
        else:
            for x in range(self.BorrowNumber):
                if self.BorrowedList[x] == BookID:
                    self.BorrowedList.pop(x)
                    self.BorrowNumber -= 1
                    return 1
            return -10 #these -10 returned will later be clear why, as sometimes -1 is when thing doesnt exist, -10 when not found

    def AddBook(self, BookID):
        self.BorrowedList.append(BookID)
        self.BorrowNumber += 1
        return 1

    def GetID(self):
        return self.__UserID

class Library:
    def __init__(self):
        self.__UserList = []
        self.__BookList = []

    def UserExists(self, ID):
        if len(self.__UserList) == 0:
            return -1
        for x in range(len(self.__UserList)):
            if self.__UserList[x].GetID() == ID:
                return self.__UserList[x]
        else:
            return -10

    def BookExists(self, ID):
        if len(self.__BookList) == 0:
            return -1
        for x in range(len(self.__BookList)):
            if self.__BookList[x].BookID == ID:
                return self.__BookList[x]

        return -10


    def AddToBookList(self, book):
        self.__BookList.append(book)

    def RegisterUser(self, user):
        self.__UserList.append(user)
        return 1

    def BorrowBook(self, user, book):
        if book.GetStatus() == True and user.BorrowNumber < 5:
            user.AddBook(book.BookID)
            book.SetStatus('borrowed')
            return 1
        elif book.GetStatus() == False:
            return -1
        else:
            return -10

    def ReturnBook(self, user, book, numhours):
        if book.GetStatus() == False and user.BorrowNumber > 0:
            for x in range(user.BorrowNumber):
                if user.BorrowedList[x] == book.BookID:
                    user.RemoveBook(book.BookID)
                    book.SetStatus('returned')
                    if numhours>5:
                        print("You owe us Rs", (numhours-5) * 10)
                    return 1
            return -1
        elif book.GetStatus() == True:
            return -10
        else:
            return -100

    def DisplayAllBooks(self):
        if len(self.__BookList) == 0:
            print('No books present')
        else:
            for x in range(len(self.__BookList)):
                print(self.__BookList[x].DisplayAllInfo())

    def DisplayAvailableBooks(self):
        if len(self.__BookList) == 0:
            print('No books present')
        else:
            for x in range(len(self.__BookList)):
                if self.__BookList[x].GetStatus() == True:
                    print(self.__BookList[x].DisplayAllInfo())

    def NumberOfUsers(self):
        return len(self.__UserList)


library = Library()

while True:

    userinput = input("""
1. Register user
2. Add book
3. Borrow book
4. Return book
5. Show available books
6. Show all books
7. Show user count
8. Exit
""")
    match int(userinput):
        case 1:
            userid = int(input('Enter user id: '))
            name = input('Enter name: ')
            user1 = User(userid, name)
            if library.RegisterUser(user1) == 1:
                print('Success!')
        case 2:
            bookid = int(input('Enter the book id: '))
            bookname = input('Enter the book name: ')
            bookauthor = input('Enter the book author: ')
            library.AddToBookList(Book(bookid, bookname, bookauthor, True)) # did 'True" cuz it should be available because it is JUST registered
        case 3:
            borrowerID = int(input('Enter the user ID of the borrower: '))
            BorrowingBookID = int(input('Enter the Book ID you want to borrow: ')) #assumes book exists, can code it to check it but i aint doing all that

            if library.UserExists(borrowerID) == -1:
                print('No Users are registered')
            elif library.UserExists(borrowerID) == -10:
                print('Specific user id not found, please register')
            else:
                if library.BookExists(BorrowingBookID) == -1:
                    print('Book list empty')
                elif library.BookExists(BorrowingBookID) == -10:
                    print('Book not found')
                else:
                    if library.BorrowBook(library.UserExists(borrowerID), library.BookExists(BorrowingBookID)) == 1:
                        print("Success!")
                    elif library.BorrowBook(library.UserExists(borrowerID), library.BookExists(BorrowingBookID)) == -1:
                        print('Book is currently being borrowed')
                    else:
                        print('User has borrowed the maximum number of books, please return some to borrow again')



        case 4:
            returnerID = int(input('Enter the user ID of the returner: '))
            returningBookID = int(input('Enter the Book ID you want to return: ')) #assumes book exists, can code it to check it but i aint doing all that
            hourstaken = int(input("How many hours did you take it"))

            if library.UserExists(returnerID) == -1:
                print('No Users are registered')
            elif library.UserExists(returnerID) == -10:
                print('Specific user id not found, please register')
            else:
                if library.BookExists(returningBookID) == -1:
                    print('BookList is empty')
                elif library.BookExists(returningBookID) == -10:
                    print('Book not found')
                else:
                    if library.ReturnBook(library.UserExists(returnerID), library.BookExists(returningBookID), hourstaken) == 1:
                        print("Success!")
                    elif library.ReturnBook(library.UserExists(returnerID), library.BookExists(returningBookID), hourstaken) == -1:
                        print("Book not found in the user's borrow list")
                    elif library.ReturnBook(library.UserExists(returnerID), library.BookExists(returningBookID), hourstaken) == -10:
                        print('Book has not been pre-borrowed, make sure the details are right')
                    else:
                        print('User has not borrowed a book till now. Make sure the details are right')


        case 5:
            library.DisplayAvailableBooks()
        case 6:
            library.DisplayAllBooks()
        case 7:
            print(library.NumberOfUsers())
        case 8:
            break
        case _:
            print('Invalid input')