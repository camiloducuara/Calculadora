class calculadora:
    def __init__(self, primernumero, segundonumero):
        self.num1 = int(num1)
        self.num2 = int(num2)

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


num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()