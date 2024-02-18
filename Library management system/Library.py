class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        # books.txt dosyasındaki tüm kitapları listele
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        # Yeni bir kitap ekleyin
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")

        book_line = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_line)
        print("Book added successfully!")

    def remove_book(self):
        # Bir kitabı kaldırın
        title_to_remove = input("Enter the title of the book to remove: ")

        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        print("Book removed successfully!")


lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

    choice = input("Enter your choice (1-3, or 'q' to quit): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 'q'.")
