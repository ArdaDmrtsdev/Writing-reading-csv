import csv
from abc import ABC, abstractmethod

class InvalidRatingNumber(Exception):
   pass

class InvalidWatched(Exception):
    pass

class InvalidMovieObject(Exception):
    pass

class MovieNotFound(Exception):
    pass

class DuplicateMovieError(Exception):
    pass

class Media(ABC):

    def __init__(self, title, genre, year, rating, watched):

           self.title = title
           self.genre = genre
           self.year = year
           self.rating = rating
           self.watched = watched

    @abstractmethod
    def get_info(self):
        pass

class Movie(Media):


    def __init__(self,title,genre,year,rating=0,watched=False):

          super().__init__(title=title,genre=genre,year=year,rating=rating,watched=watched)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):

      if 0<= rating <=10:
          self._rating=rating
      else:
          raise InvalidRatingNumber("Geçersiz rating sayısı")


    @property
    def watched(self):
        return self._watched
    @watched.setter
    def watched(self,watched):

          if not isinstance(watched,bool):
                 raise InvalidWatched("Watched typı booleandır.")
          self._watched=watched

    def __str__(self):

        if self.watched==True:
          return f"{self.title}({self.year}) -{self.genre}- {self.rating}/10 watched "
        return   f"{self.title}({self.year}) -{self.genre}- {self.rating}/10 not watched "

    def __eq__(self, value):

        if isinstance(value,Movie):  #control value is a Movie object ?
            return self.title==value.title and self.year==value.year
        return False

    def __hash__(self):
        return hash((self.title,self.year))

    def get_info(self):
      
      if self.watched:
           status = "Watched"
      else:
           status = "Not Watched"

      return f"{self.title} ({self.year}) - {self.genre} - {self.rating}/10 - {status}"

class MovieManager:

      def __init__(self):

          self.movies=[]

      def add_movie(self,movie):

           if isinstance(movie,Movie):
               for new in self.movies:
                   if new==movie:
                       raise DuplicateMovieError("Movie already there")
               self.movies.append(movie)
               return f"Succesfull add movie -{movie.title}"
           else:
            raise InvalidMovieObject("Invalid Object Type")
           
      def remove_movie(self,title):

         for index, movie in enumerate(self.movies): #Forda gezerken o anki movie  objesını ve onun indexini alırız.
 
           if title == movie.title:
              self.movies.pop(index)
              return f"Succesfull remove the movie -{title}"

         raise MovieNotFound("Movie not Found")

      def search_movie(self,title):

          for new in self.movies:
              if title==new.title:
                  return new
          raise MovieNotFound("Movie not found")

      def list_movies(self):

          if not self.movies:
              print("Library is empty Havent any book")
          for new in self.movies:
              print(new)

      def save_to_csv(self):

          with open("movies.csv","a",newline="") as file :
               writer=csv.DictWriter(file,fieldnames=["title","genre","year","rating","watched"])

               for movie in self.movies:

                  writer.writerow({"title":movie.title,"genre":movie.genre,"year":movie.year,"rating":movie.rating,"watched":movie.watched})
                  print(f"Eklendi : {movie}")
      def read_to_csv(self):
          
          try:
           with open("movies.csv") as file:
                reader = csv.DictReader(file)

                for row in reader :
                     title=row["title"]
                     genre=row["genre"]
                     year=int(row["year"])
                     rating=float(row["rating"])
                     watched= row["watched"]=="True"
                     newMovie=Movie(title=title,genre=genre,year=year,rating=rating,watched=watched)
                     self.movies.append(newMovie)

                for movie in sorted(self.movies,key=lambda movie:movie.year):
                     print(f"{movie.title} {movie.genre} {movie.year} {movie.rating} {movie.watched}")

          except FileNotFoundError:
              pass

def main():

      manager=MovieManager()
      manager.read_to_csv()

    #   movie1 = Movie(title="Inception", genre="Sci-Fi", year=2010, rating=9, watched=True)
    #   movie2 = Movie(title="Interstellar", genre="Sci-Fi", year=2014, rating=8.5, watched=False)
    #   movie3 = Movie(title="The Godfather", genre="Crime", year=1972, rating=9.5, watched=True)
 
    #   print(manager.add_movie(movie1))
    #   print(manager.add_movie(movie2))
    #   print(manager.add_movie(movie3))
 
    #   manager.list_movies()
 
    #   manager.save_to_csv()



if __name__=="__main__":
    main()