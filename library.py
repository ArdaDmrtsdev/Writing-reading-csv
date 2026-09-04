class InvalidISBNError(Exception):
    pass
class BookNotFoundError(Exception):
    pass

class BookAlreadyBorrowedError(Exception):
    pass

class Book:

    def __init__(self,title,author,isbn):

         self.title=title
         self.author=author
         self.isbn=isbn
         self.is_barrowed=False

    @property
    def isbn(self):
           return self._isbn

    @isbn.setter
    def isbn(self,isbn):
             cleanIsbn=isbn.replace("-","")
             if len(cleanIsbn)!=13:
                raise  InvalidISBNError("İnvalid isbn number")
             self._isbn=isbn

    def __str__(self):
       return f"{self.title} {self.author}  {self.isbn}"


class Library:

     total_books=0

     def __init__(self,name):
       self.name=name
       self.books=[]

     def addBook(self,book):

        self.books.append(book)
        Library.total_books+=1
        print(f"{book.title}- Kütüphaneye eklendi")

     def barrow_book(self,isbn):

                 cleanedIsbn=isbn.replace("-","")
                 foundIsbn=None
                 for book in self.books:
                      if book.isbn==cleanedIsbn:
                           foundIsbn=book
                           break

                 if not foundIsbn:
                      raise  BookNotFoundError("Aranilan kitap bulunamadi")
                 if foundIsbn.is_barrowed:
                      raise BookAlreadyBorrowedError("Kitap ödünç verilmiştir zaten")
                 foundIsbn.is_barrowed=True
                 return foundIsbn
     
     def __str__(self):
          return f"{self.name} Kütüphanesi Kitap sayisi : {len(self.books)}"


def main():

          library=Library("Kocaeli Kütüphane")
          book1=Book("Suç ve Ceza","Fyodor Dostoyevski","9789750719387")
          book2=Book("1984","George Orwell","9789750718533")
          book3=Book("Simyaci","Paulo Coelho","9789750726434")
          library.addBook(book1)
          library.addBook(book2)
          library.addBook(book3)
          print(f"Sistemdeki Toplam Kitap sayisi : {Library.total_books}")

          getBarrow=input("Ödünç almak istediğiniz kitabin ISBN nedir : ")

          try:
                  book_barrow=library.barrow_book(isbn=getBarrow)
                  print(f"{book_barrow.title} :Kitabi başariyla alindi")
          except BookNotFoundError as e:
               print(f"Hata :{e} ")
          except InvalidISBNError as e:
               print(f"Hata :{e} ")
          except BookAlreadyBorrowedError as e:
               print(f"Hata :{e} ")

if __name__ == "__main__":
  main()
