
def suma(numero1=0, numero2=0):
	return numero1 + numero2

def resta(numero1=0,numero2=0):
	return numero1 - numero2

def multiplicacion(numero1=0,numero2=0):
	return numero1 * numero2

def division(numero1=0,numero2=0):
	return numero1 / numero2

def division_exacta(numero1=0,numero2=0):
	return numero1 // numero2

def modulo(numero1=0,numero2=0):
	return numero1 % numero2

def suma_cuadrados(numero1=0,numero2=0):
	return numero1**2 + numero2**2

num1 = int(input("Dame el numero 1: "))
num2 = int(input("Dame el numero 2: "))

print("La suma es:",suma(num1,num2))
print("La resta es:",resta(num1,num2))
print("La multiplicacion es:",multiplicacion(num1,num2))
print("La division es:",division(num1,num2))
print("La division exacta es:",division_exacta(num1,num2))
print("El módulo es:",modulo(num1,num2))
print("La suma de cuadrados es:",suma_cuadrados(num1,num2))
