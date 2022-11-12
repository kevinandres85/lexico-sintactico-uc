def primero(producciones, no_terminales, terminales):                                    # Función para calcular el conjunto primero
    prim = {}                                                                            # Se crea un diccionario vacío
    for terminal in terminales:                                                          # Se recorre el conjunto de terminales
        prim[terminal] = {terminal}                                                      # Se añade el terminal al diccionario
    prim['e'] = {'e'}                                                                    # Se añade el símbolo lambda al diccionario
    for no_terminal in no_terminales:                                                    # Se recorre el conjunto de no terminales
        prim[no_terminal] = set()                                                        # Se añade el no terminal al diccionario como llave y un conjunto vacío como valor
    while True:                                                                          # Se crea un ciclo infinito para calcular el conjunto primero
        cambio = False                                                                   # Se crea una variable para saber si hubo un cambio en el conjunto primero de algún no terminal
        for produccion in producciones:                                                  # Se recorre el conjunto de producciones de la gramática
            izq, der = produccion.split(' -> ')                                          # Se separa la producción en la parte izquierda y derecha de la flecha de la producción (izq -> der)
            if der in terminales:                                                        # Si la parte derecha de la producción es un terminal
                if der not in prim[izq]:                                                 # Si el terminal no está en el conjunto primero del no terminal de la izquierda
                    prim[izq].add(der)                                                   # Se añade el terminal al conjunto primero del no terminal de la izquierda de la producción 
                    cambio = True                                                        # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto primero de algún no terminal 
            else:                                                                        # Si la parte derecha de la producción es un no terminal o una combinación de no terminales y terminales
                for simbolo in der:                                                      # Se recorre la parte derecha de la producción 
                    if simbolo in terminales:                                            # Si el símbolo es un terminal 
                        if simbolo not in prim[izq]:                                     # Si el terminal no está en el conjunto primero del no terminal de la izquierda de la producción 
                            prim[izq].add(simbolo)                                       # Se añade el terminal al conjunto primero del no terminal de la izquierda de la producción 
                            cambio = True                                                # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto primero de algún no terminal 
                        break                                                            # Se rompe el ciclo for para pasar a la siguiente producción 
                    else:                                                                # Si el símbolo es un no terminal 
                        for simbolo_prim in prim[simbolo]:                               # Se recorre el conjunto primero del no terminal 
                            if simbolo_prim not in prim[izq]:                            # Si el símbolo del conjunto primero del no terminal no está en el conjunto primero del no terminal de la izquierda de la producción 
                                prim[izq].add(simbolo_prim)                              # Se añade el símbolo del conjunto primero del no terminal al conjunto primero del no terminal de la izquierda de la producción 
                                cambio = True                                            # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto primero de algún no terminal 
                        if 'e' not in prim[simbolo]:                                     # Si el símbolo lambda no está en el conjunto primero del no terminal 
                            break                                                        # Se rompe el ciclo for para pasar a la siguiente producción 
                else:                                                                    # Si el ciclo for termina sin romperse
                    if 'e' not in prim[izq]:                                             # Si el símbolo lambda no está en el conjunto primero del no terminal de la izquierda de la producción
                        prim[izq].add('e')                                               # Se añade el símbolo lambda al conjunto primero del no terminal de la izquierda de la producción
                        cambio = True                                                    # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto primero de algún no terminal
        if not cambio:                                                                   # Si no hubo ningún cambio en el conjunto primero de algún no terminal 
            break                                                                        # Se rompe el ciclo while para terminar el cálculo del conjunto primero 
    return prim                                                                          # Se regresa el diccionario con el conjunto primero de cada no terminal de la gramática 



def siguiente(producciones, no_terminales, terminales, prim, inicio):                     # Función para calcular el conjunto siguiente de cada no terminal de la gramática 
    sig = {}                                                                              # Se crea un diccionario vacío para guardar el conjunto siguiente de cada no terminal de la gramática 
    for no_terminal in no_terminales:                                                     # Se recorre el conjunto de no terminales de la gramática
        sig[no_terminal] = set()                                                          # Se crea un conjunto vacío para guardar el conjunto siguiente del no terminal
    sig[inicio].add('$')                                                                  # Se añade el símbolo de fin de cadena al conjunto siguiente del símbolo inicial de la gramática 
    while True:                                                                           # Ciclo while infinito para calcular el conjunto siguiente de cada no terminal de la gramática
        cambio = False                                                                    # Variable para indicar si hubo un cambio en el conjunto siguiente de algún no terminal
        for produccion in producciones:                                                   # Se recorren las producciones de la gramática
            izq, der = produccion.split(' -> ')                                           # Se separa la parte izquierda de la parte derecha de la producción
            for i in range(len(der)):                                                     # Se recorre la parte derecha de la producción
                if der[i] in no_terminales:                                               # Si el símbolo es un no terminal
                    if i + 1 < len(der):                                                  # Si el índice es menor al tamaño de la parte derecha de la producción
                        for simbolo in prim[der[i + 1]]:                                  # Se recorre el conjunto primero del símbolo siguiente al no terminal
                            if simbolo != 'e' and simbolo not in sig[der[i]]:             # Si el símbolo no es el símbolo lambda y no está en el conjunto siguiente del no terminal
                                sig[der[i]].add(simbolo)                                  # Se añade el símbolo al conjunto siguiente del no terminal
                                cambio = True                                             # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto siguiente de algún no terminal
                        if 'e' in prim[der[i + 1]]:                                       # Si el símbolo lambda está en el conjunto primero del símbolo siguiente al no terminal
                            for simbolo in sig[izq]:                                      # Se recorre el conjunto siguiente del no terminal de la izquierda de la producción
                                if simbolo not in sig[der[i]]:                            # Si el símbolo no está en el conjunto siguiente del no terminal
                                    sig[der[i]].add(simbolo)                              # Se añade el símbolo al conjunto siguiente del no terminal
                                    cambio = True                                         # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto siguiente de algún no terminal
                    else:                                                                 # Si el índice es igual al tamaño de la parte derecha de la producción
                        for simbolo in sig[izq]:                                          # Se recorre el conjunto siguiente del no terminal de la izquierda de la producción
                            if simbolo not in sig[der[i]]:                                # Si el símbolo no está en el conjunto siguiente del no terminal
                                sig[der[i]].add(simbolo)                                  # Se añade el símbolo al conjunto siguiente del no terminal
                                cambio = True                                             # Se cambia el valor de la variable cambio a True para indicar que hubo un cambio en el conjunto siguiente de algún no terminal
        if not cambio:                                                                    # Si no hubo ningún cambio en el conjunto siguiente de algún no terminal
            break                                                                         # Se rompe el ciclo while para terminar el cálculo del conjunto siguiente
    return sig                                                                            # Se regresa el diccionario con el conjunto siguiente de cada no terminal de la gramática



# Funcion Inicial del programa
if __name__ == "__main__": 
        
        # ingresar el numero de producciones
        n = int(input("Ingrese el número de producciones: "))                             #Solicitar el numero de producciones
        print('\n')
        
        # Ingresa las producciones
        producciones = []                                                                 #Lista de producciones
        print("Ingrese las producciones de la gramatica:")                                #Solicitar las producciones
        for i in range(n):                                                                #Para cada produccion ingresada
            producciones.append(input()) 

        # Gramatica ingresada
        print('\n')
        print(' ' * 10 + 'Gramatica ingresada:')                                                     #Imprimir la gramatica ingresada
        gramatica = list(zip(producciones))
        for i in range(len(gramatica)):
           print(gramatica[i][0])


      # Mostrar los conjuntos de primeros y siguientes para la gramatica ingresada
        no_terminales = set()                                                             #Conjunto de no terminales
        terminales = set()                                                                #Conjunto de terminales
        for produccion in producciones:                                                   #Para cada produccion de la gramatica ingresada 
            izq, der = produccion.split(' -> ')                                           #Separar la parte izquierda de la parte derecha de la produccion 
            no_terminales.add(izq)                                                        #Agregar el no terminal de la izquierda a la lista de no terminales 
            for simbolo in der:                                                           #Para cada simbolo de la parte derecha de la produccion 
                if simbolo not in no_terminales:                                          #Si el simbolo no es un no terminal 
                    terminales.add(simbolo)                                               #Agregar el simbolo a la lista de terminales 
        
        prim = primero(producciones, no_terminales, terminales)                           #Conjunto de primeros
        print('\n')
        print(' ' * 10 + 'Conjunto de Primeros')                                          #Mostrar los conjuntos de primeros 
        for no_terminal in no_terminales:                                                 #Para cada no terminal de la gramatica ingresada 
            print(no_terminal + ' ' * (10 - len(no_terminal)) + str(prim[no_terminal]))   #Mostrar el no terminal y su conjunto de primeros 
       
        sig = siguiente(producciones, no_terminales, terminales, prim, producciones[0][0]) #Conjunto de siguientes 
        print('\n')
        print(' ' * 10 + 'Conjunto de Siguientes')                                         #Mostrar los conjuntos de siguientes 
        for no_terminal in no_terminales:                                                  #Para cada no terminal de la gramatica ingresada 
            print(no_terminal + ' ' * (10 - len(no_terminal)) + str(sig[no_terminal]))     #Mostrar el no terminal y su conjunto de siguientes 
       
             
            