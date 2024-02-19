class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        print("Library opened.")

    def __del__(self):
        self.file.close()
        print("Library closed.")

    def list_all_books(self):
        all_info = []
        with open("books.txt", "r") as file1:
            all_lines = file1.readlines()
            if len(all_lines) == 0:
                print("Library is empty!!!")
                return
            for i in range(len(all_lines)):
                all_info.append(all_lines[i].strip().split(","))
                if len(all_info) >1:
                    print("Title : ",all_info[i][0])
                    print("Author Name : ",all_info[i][1])

    def add_book(self):
        book_title = input("Enter the book title : ")
        book_author = input("Enter the name of author : ")
        release_year = input("Enter release year of book : ")
        number_of_pages = input("Enter number of pages of book : ")
        new_string = f"{book_title},{book_author},{release_year},{number_of_pages}\n"
        with open("books.txt", "a+") as file1:
            file1.write(new_string)

    def remove_book(self):
        all_info = []
        my_string=""
        counter = 0
        title = input("Enter title book which you want to remove : ")
        with open("books.txt", "r") as file1:
            all_lines = file1.readlines()
            if len(all_lines) ==1:
                print("Library is empty!!!")
                return
            for i in range(len(all_lines)):
                all_lines[i] = all_lines[i].strip()
                all_info.append(all_lines[i].split(","))
        for i in all_info:
            if i[0] == title:
                break
            counter+=1
            if len(all_info) == counter:
                print("Invalid book title")
                return
        all_info.pop(counter)
        with open("books.txt", "w") as file1:
            for i in all_info:
                my_string = f"{i[0]},{i[1]},{i[2]},{i[3]}\n"
                file1.write(my_string)


lib = Library()
print("***MENU***\n1) List Books\n2) Add Book\n3) Remove Book")
choose = input("Choose your item from menu : ")
if choose == "1":
    lib.list_all_books()
elif choose == "2":
    lib.add_book()
elif choose == "3":
    lib.remove_book()
else:
    print("Invalid character !!!")
