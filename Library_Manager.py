import json
import os

library_file ='library.txt'

# Load library from file
def load_library():
  if os.path.exists(library_file):
    with open(library_file,'r') as file:
      return json.load(file)
    
  return []

# Save library to file
def save_library(library):
  with open(library_file,'w') as file:
    json.dump(library, file)

# Add a new book
def add_book(library):
  title = input("Enter the title of the book: ")
  author = input("Enter the author of the book: ")
  year = input("Enter the year of the book: ")
  genre = input("Enter the genre of the book: ")
  read = input("Have you read this book? (yes/No): ").lower() == 'yes'


  new_book = {
  'title' : title,
  'author' : author,
  'year' : year,
  'genre' : genre,
  'read' : read
}

  library.append(new_book)
  save_library(library)
  print(f'✅ Book {title} added successfully!')

# Remove a book

def remove_book(library):
  title = input("Enter the title of book to remove from library")
  initial_length = len(library)
  library = [book for book in library if book['title'].lower()!= title]
  if len(library) < initial_length:
    save_library(library)
    print(f" 🗑 Book {title} removed succesfully.")

  else:
    print(f"❌ Book {title} not found in library.")


# Search for books
def search_library(library):
    search_by = input("Search by 'title' or 'author': ").strip().lower()

    if search_by not in ['title', 'author']:
        print("Invalid search field. Please choose 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").strip().lower()

    results = []
    for book in library:
        if search_by in book:
            if search_term in book[search_by].lower():
                results.append(book)

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")


  # display all books
def display_all_books(library):
  if library:
    for book in library:
        status = "Read" if book['read'] else "unread"
        print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
         
  else:
      print("The library is empty")


# Display statics
def display_statistics(library):
  total_books = len(library)
  read_books = len([book for book in library if book['read']])
  read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

  print (f"Total books : {total_books}")
  print(f"Read percentage : {read_percentage:.2f}")


# main function
def main():
  library = load_library()
  
  
  while True:
    print("Welcome to Library Manager")
    print("***********Menu***********")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search the library")
    print("4. Display all books")
    print("5. Display Read statistics")
    print("6. Exit")

    choice = input("enter your choice : ")
    if choice =='1':
      add_book(library)
    
    elif choice == '2':
      remove_book(library)

    elif choice == '3':
      search_library(library)

    elif choice == '4':
      display_all_books(library)

    elif choice ==  '5':
      display_statistics(library)
    
    elif choice == '6':
      print("Library closed !")
    
    else:
      print("Invalid choice. Select from menu")

if __name__ == '__main__':
  main()
