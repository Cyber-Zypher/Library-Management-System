# Coded by my beloved friends at M E D U S A  Infosystems India
 
import pymysql

# Database connection
db = pymysql.connect(
    host='localhost',
    user='UNAME',
    password='PASSWORD',
    database='DB_NAME'
)

# Cursor to interact with the database
cursor = db.cursor()

def add_book(title, author, publication_year):
    sql = "INSERT INTO books (title, author, publication_year) VALUES (%s, %s, %s)"
    values = (title, author, publication_year)
    cursor.execute(sql, values)
    db.commit()

def display_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")

def delete_book(book_id):
    sql = "DELETE FROM books WHERE id = %s"
    cursor.execute(sql, (book_id,))
    db.commit()

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Delete Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            publication_year = int(input("Enter publication year: "))
            add_book(title, author, publication_year)
            print("Book added successfully!")

        elif choice == '2':
            print("\nList of Books:")
            display_books()

        elif choice == '3':
            book_id = int(input("Enter the ID of the book you want to delete: "))
            delete_book(book_id)
            print("Book deleted successfully!")
            if book_id == '':
                print("No Records Found")

        elif choice == '4':
            break
        elif choice == '':
            print("Please choose an option.")
        else:
            print("Invalid choice. Please select again.")

    db.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
