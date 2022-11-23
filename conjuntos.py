from readGrammar import(d)
""" gram = {
	"E":[['T', "E'"]],
    "E'":[["+", "T", "E'"], ["e"]],
    "T":[["F", "T'"]],
    "T'":[["*", "F", "T'"], ["e"]],
	"F":[['(', 'E', ')'], ['i']]
} """

gram = d
def primero(gramatica, no_terminal):
	conjunto = []
	for produccion in gramatica[no_terminal]:
		if produccion[0] in gramatica:
			conjunto += primero(gramatica, produccion[0])
		else: 
			conjunto.append(produccion[0])

	return conjunto

primeros = {}

for i in gram:
	primeros[i] = primero(gram,i)
	print(f'Primero({i}):',primeros[i])

print("-------------------------------")

def siguiente(gramatica, no_terminal):
	conjunto = []
	for produccion in gramatica:
		for simbolo in gramatica[produccion]:
			if no_terminal in simbolo:
				if simbolo.index(no_terminal)+1 != len(simbolo):
					if simbolo[-1] in primeros:
						conjunto+=primeros[simbolo[-1]]
					else:
						conjunto+=[simbolo[-1]]
				else:
					conjunto+=["e"]
				if produccion != no_terminal and "e" in conjunto:
					conjunto+= siguiente(gram,produccion)
	return conjunto

siguientes = {}
for i in gram:
	siguientes[i] = list(set(siguiente(gram,i)))
	if "e" in siguientes[i]:
		siguientes[i].pop(siguientes[i].index("e"))
	siguientes[i]+=["$"]
	print(f'Siguiente({i}):',siguientes[i])