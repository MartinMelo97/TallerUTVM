frase = input("Dame la frase")

arreglo = frase.split(" ")
print("Hay",len(arreglo)," palabras")

print("La primer palabra es: ",arreglo[0])

print(arreglo[2:])

arreglo.append("UTVM")
print(arreglo)

arreglo.reverse()
print(arreglo)

arreglo.pop()
print(arreglo)

longitud=len(arreglo) - 1
print(len(arreglo[longitud]))