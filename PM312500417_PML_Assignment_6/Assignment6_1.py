# #1.Write a program which contains one class named as BookStore.
# BookStore class contains two instance variables as Name ,Author.
# That class contains one class variable as NoOfBooks which is initialise to 0.
# There is one instance methods of class as Display which displays name , Author and number of books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
# Obj1.Display() # Linux System Programming by Robert Love. No of books : 1
# Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
# Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2

class BookStore:

    NoOfBooks = 0 #class variable

    def __init__(self,value1,value2): #constructor
        self.Name = value1  #instance variable
        self.Author = value2  #instance variable
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def display(self):
        print("Name of book is",'"',self.Name,'"')    
        print("Author of book",'"',self.Name,'"',"is",'"',self.Author,'"')
        print("Current no. of available copies of books in store is:",BookStore.NoOfBooks)

     


def main():

    name = None
    author = None

    print("Please enter name of book:")
    name = input()

    print("Please enter name of author of book:")
    author = input()

    bobj1 = BookStore(value2=author,value1=name)

    bobj1.display()



if __name__ == "__main__":
    main()    
