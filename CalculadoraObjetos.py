class Calculadora:
    def __init__(self, primerNumero, segundoNumero):
        self.num1 = int(primerNumero)
        self.num2 = int(segundoNumero)

    def sumar(self):
        suma = self.num1 + self.num2
        print("el resultado de la suma es: ", suma)

    def restar(self):
        resta = self.num1 - self.num2
        print("el resultado de la resta es: ", resta)

    def multiplicar(self):
        multiplicacion = self.num1 * self.num2
        print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self):
        divicion = self.num1 / self.num2
        print("el resultado de la divición es: ", divicion)
