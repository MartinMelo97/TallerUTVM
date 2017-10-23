num = int(input("Dame el numero limite"))
arregloImpares = []
for i in range(0,num):

	if i % 2 == 0:
		print(i**2)

	else:
		arregloImpares.append(i**3)

print(arregloImpares)
