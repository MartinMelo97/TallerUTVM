alumno = {}

nombre = input("Nombre: ")

alumno['name'] = nombre

edad = int(input("Edad: "))
alumno['edad'] = edad

sexo = input("Sexo: ")
alumno['sexo'] = sexo

regular = input("Ingresa S si eres regular, si no ingresa N")

if regular == 'S':
	alumno['regular'] = True
else:
	alumno['regular'] = False

print(alumno)