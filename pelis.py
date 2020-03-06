import random

class Movie:
    
    def __init__(self, title):
        self.rank = random.randint(0,10)
        self.title = title.lower() # con la función lower() se le asignan mayúsculas al inicio de cada palabra
        print("La película " + self.title + " fue puntuada con: " + str(self.rank) + " puntos por los críticos.")
    
    def get_rank(self):
        return(str(self.rank))

    def get_title(self):
        return(str(self.title))

    def get_like(self):
        if self.rank + 1 <= 10:
            self.rank = self.rank + 1
            print("La película " + self.title + " se le sumó un punto y ahora tiene: " + str(self.rank))
        elif self.rank == 10:
            print("la película " + self.title + " ya no se le suma porque tiene un DIEZ.")
    
    def get_dislike(self):
        if self.rank - 1 > 0:
            self.rank = self.rank - 1
            print("La película " + self.title + " se le quitó un punto y ahora tiene una calificación de: " + str(self.rank))
        else:
            self.rank == 0
            print("la película " + self.title + " ya no se le resta porque tiene un CERO de calificación.")

risa = Movie("La Risa en Vacaciones")
bole = Movie("El Bolero de Raquel")
deta = Movie("Ahí Está el Detalle")
prob = Movie("Nosotros los Pobres")
garc = Movie("Los Tres García")
zorr = Movie("La Marca del Zorrillo")
huas = Movie("Los Tres Huastecos")
cuid = Movie("Dos Tipos de cuidado")

movies = [risa, bole, deta, prob, garc, zorr, huas, cuid]

for movies in movies:
    print("+-+-+-+-+-+")
    movies.get_like()
    movies.get_dislike()