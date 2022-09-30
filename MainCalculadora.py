from CalculadoraObjetos import Calculadora

num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

calculadora = Calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir()