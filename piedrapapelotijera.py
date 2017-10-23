import random
miEleccion = int(input("1.- Piedra, 2.- Papel, 3.- Tijera: "))
suEleccion = random.randint(1,3)

opciones = ['Piedra','Papel','Tijera']
print("Yo elegi: ",opciones[miEleccion-1])
print("Compu eligio: ",opciones[suEleccion-1])

if miEleccion == 1 and suEleccion == 2:
	print("Gana compu")

elif miEleccion == 1 and suEleccion == 3:
	print("Gano yo")

elif miEleccion == 2 and suEleccion == 1:
	print("Gano yo")

elif miEleccion == 2 and suEleccion == 3:
	print("Gana compu")

elif miEleccion == 3 and suEleccion == 1:
	print("Gana compu")

elif miEleccion == 3 and suEleccion == 2:
	print("Gano yo")

elif miEleccion == suEleccion:
	print("Empate")