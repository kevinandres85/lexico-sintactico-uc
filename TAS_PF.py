
from distutils.log import error


gramatica = {
	"E":[["T","E'"]],
    "E'":[["+", "T", "E'"], ["e"]],
    "T":[["F", "T'"]],
    "T'":[["*", "F", "T'"], ["e"]],
	"F":["(E)","i"]
}

primeros = {
    "E":["(", "i"],
    "T":["(", "i"],
    "F":["(", "i"],
    "E'":["+", "e"],
    "T'":["*", "e"]
}

siguientes = {
    "E":[")", "$"],
    "E'":[")", "$"],
    "T":["+", ")", "$"],
    "T'":["+", ")", "$"],
    "F" :["+", "*", "$"]
}

producciones = {
    "E":["TE'"],
    "E'":["+TE'", "e"],
    "T":["FT'"],
    "T'":["*FT'", "e"],
    "F":["(E)", "i"]
    
}

#crear lista de tokens 
tokens= []
for i in gramatica:
	for j in gramatica[i]:
		for k in j:
			if k not in gramatica:
				tokens.append(k)

tokens = list(map(lambda x: x.replace('e', '$'), set(tokens)))

# crear TAS
tas = {}
for i in gramatica:
    for j in tokens:
        if j not in primeros[i]:
            tas[i,j] = ""
        else: 
            tas[i,j] = producciones[i][0]
    if "e" in primeros[i]:
        for j in tokens:
            if j in siguientes[i]:
                tas[i,j] = "e"

tas["F","i"] = "i"
print("---------------------------------------------")  
#Imprimir tabla 
printTas = "     |"
for i in tokens:
    printTas+= f"   {i: <9}|"
print(printTas)

for i in gramatica:
    printTas = f" {i: <2}  "
    for j in tokens:
        if(tas[i,j] == ""):
           printTas+=f"|{tas[i,j]: <12}"
        else:
            printTas+=f"| {i}->{tas[i,j]: <7}"
    print(f'{"-":-<80}') 
    print(printTas)



#PRUEBA ESCR
print("------------------------------------------------")
print("PRUEBA ESCRITORIO")
cadena = input("Ingrese cadena:")
cadena+="$"

pila = []
x = "$"
a = ""
cadena = list(cadena)
pila.append(x)
salida = {}
cima = ""

def inv_cadena(cadena):
    lcadena = list(cadena)
    if("'" in lcadena):
      pos = lcadena[lcadena.index("'") - 1]
      lcadena[lcadena.index("'") - 1]+="'"
      lcadena.remove("'")
    return lcadena[::-1]

for x in gramatica:
    pila.append(x)
    break

def iterar(pila,a):
    cima = pila[-1]
    if (cima in tokens or cima =="$"):
            if(cima == a):
                pila.pop()
                print("Pila: ", pila)
                print("Salida:")
                print("-----------------------------------")
                return
            else:
                error
    else:
            pila.pop()
            prod = tas[cima,a]
            pila+=inv_cadena(prod)
            if(prod == "e"):
                pila.pop()
    print("Pila: ", pila)
    print("Salida: ",cima,"->",prod)
    print("---------------------------")
    iterar(pila, a)
            
while a != "$":
  for a in cadena:
        iterar(pila, a)
        
           


