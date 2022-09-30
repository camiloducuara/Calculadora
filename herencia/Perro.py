from herencia.Animal import Animal


class Perro(Animal):

    def __init__(self, color, alimento, medio, raza):
        super().__init__(color, alimento, medio)
        self.raza = raza

    def sonido(self):
        print("Ladra*")


