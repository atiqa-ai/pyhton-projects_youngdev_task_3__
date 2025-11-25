# 📚 Library Management System (LMS)


import datetime
import os


class LMS:
    """This class manages library operations like adding, viewing, issuing, and returning books."""

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dic = {}
        self.initialize_books()

    def initialize_books(self):
        """Reads the list of books from a text file and loads them into a dictionary."""
        try:
            with open(self.list_of_books, "r") as f:
                content = f.readlines()
            id = 101
            for line in content:
                book_title = line.strip()
                self.books_dic.update({
                    str(id): {
                        "book title": book_title,
                        "lender name": "",
                        "issue date": "",
                        "status": "Available"
                    }
                })
                id += 1
        except FileNotFoundError:
            print(f"⚠️ Error: The file '{self.list_of_books}' was not found.")
            exit()

    def display_books(self):
        """Displays all books along with their availability."""
        print(f"\n📚 Books available in {self.library_name}:\n")
        print("ID\t\tTitle\t\t\tStatus")
        print("==============================================")
        for book_id, info in self.books_dic.items():
            print(f"{book_id}\t\t{info['book title']}\t\t[{info['status']}]")

    def issue_book(self):
        """Issues a book to a user if available."""
        book_id = input("\nEnter Book ID to issue: ").strip()
        name = input("Enter your name: ").strip()

        if book_id in self.books_dic.keys():
            if self.books_dic[book_id]["status"] == "Available":
                self.books_dic[book_id]["lender name"] = name
                self.books_dic[book_id]["issue date"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.books_dic[book_id]["status"] = "Issued"
                print(f"\n✅ Book '{self.books_dic[book_id]['book title']}' issued to {name}.")
            else:
                print(f"❌ Sorry, this book is already issued to {self.books_dic[book_id]['lender name']}.")
        else:
            print("⚠️ Invalid Book ID!")

    def add_book(self):
        """Adds a new book to the library and updates the file."""
        new_book = input("\nEnter the title of the new book: ").strip()
        new_id = str(max(map(int, self.books_dic.keys())) + 1)
        self.books_dic[new_id] = {
            "book title": new_book,
            "lender name": "",
            "issue date": "",
            "status": "Available"
        }

        with open(self.list_of_books, "a") as f:
            f.write(f"\n{new_book}")

        print(f"✅ Book '{new_book}' added successfully with ID {new_id}.")

    def return_book(self):
        """Marks a book as returned."""
        book_id = input("\nEnter Book ID to return: ").strip()

        if book_id in self.books_dic.keys():
            if self.books_dic[book_id]["status"] == "Issued":
                self.books_dic[book_id]["lender name"] = ""
                self.books_dic[book_id]["issue date"] = ""
                self.books_dic[book_id]["status"] = "Available"
                print(f"✅ Book '{self.books_dic[book_id]['book title']}' returned successfully.")
            else:
                print("⚠️ This book is not issued to anyone.")
        else:
            print("⚠️ Invalid Book ID!")


# ---------------- MAIN PROGRAM ----------------
def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "list_of_books.txt")

    library = LMS(file_path, "📖 My Python Library")

    while True:
        # show available books before menu
        library.display_books()

        print("\n========= Library Menu =========")
        print("1. Issue Book")
        print("2. Add New Book")
        print("3. Return Book")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            library.issue_book()
        elif choice == "2":
            library.add_book()
        elif choice == "3":
            library.return_book()
        elif choice == "4":
            print("📚 Thank you for using the Library Management System!")
            break
        else:
            print("⚠️ Invalid choice! Please select from 1–4.")


if __name__ == "__main__":
    main()
