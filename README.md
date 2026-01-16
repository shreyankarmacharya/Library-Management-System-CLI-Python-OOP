Library Management System (Python CLI, OOP):

Description:
This is a simple Library Management System implemented in Python using Object-Oriented Programming (OOP) principles.
The program allows users to register, add books, borrow and return books, and view available books. It simulates a basic CLI library system and tracks user borrowings, book availability, and simple fines for late returns.


Features:
User Management: Register new users with unique IDs and names.
Book Management: Add new books with ID, title, author, and availability status.
Borrowing Books: Users can borrow books if available and if they have not exceeded the maximum of 5 borrowed books.
Returning Books: Users can return books, with a fine calculation for late returns (after 5 hours).
View Books: Display all books or only available books.
User Count: Display the total number of registered users.
Data Integrity: Prevents borrowing unavailable books and tracks borrowed books per user.
CLI Menu: Interactive command-line interface for easy use.


Design Highlights:
Classes:
Book: Represents a book with ID, title, author, and availability.
User: Represents a library user with ID, name, and a list of borrowed books.
Library: Manages all users and books, handles borrowing and returning logic.

Encapsulation: Private attributes for sensitive data (Book.__isAvailable, User.__UserID) with getter/setter methods.
Robust Return Codes: Methods return codes (1, -1, -10) for success, empty list, or not found scenarios.
OOP Practices: Clear separation of responsibilities between classes and clean methods for each action.



Assumptions:
All user inputs are of the correct type (int for IDs and hours, str for names).
Book and user IDs are assumed to be unique but not enforced.
Optional features like due dates beyond simple hour-based fines are not implemented.
Duplicate borrowing of the same book by the same user is prevented via availability checks.


How to Use:
Run the Python script.
Choose from the CLI menu: register users, add books, borrow/return books, or view information.
Borrowed books are tracked per user, and availability is updated automatically.
Returning books calculates fines if the book is returned after 5 hours.



Future Enhancements:
Enforce unique BookIDs and UserIDs.
Add a more detailed due date and fine system.
Implement persistent storage (save/load users and books to a file).
Add an AI or automated assistant for recommendations.
Create a GUI interface for improved usability.
