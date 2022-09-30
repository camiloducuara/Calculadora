class Animal:

    def __init__(self, color, alimento, medio):
        self.color = color
        self.alimento = alimento
        self.medio = medio

    def dormir(self):
        return "Estoy durmiendo"

    def comer(self):
        print("Estoy comiendo")

    def sonido(self):
        print("No determinado")
