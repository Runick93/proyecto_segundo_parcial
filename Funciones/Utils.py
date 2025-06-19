import random

def inicializar_matriz(cantidad_filas: int, cantidad_columnas:int, valor_inicial: any = 0) -> list:
    """
    Funcion que permite inicializar una matriz con las respectivas filas y columnas indicadas por parametro

    Args:
        cantidad_filas (int): La cantidad de filas que tendra la matriz
        cantidad_columnas (int): La cantidad de columnas que tendra la matriz
        valor_inicial (any, optional): description. Defaults to 0. El valos con el cual se inicializara la matriz

    Returns:
        list: Una matriz con las columnas, filas y inicializada con los valores recibidos por parametro
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
    return matriz



def inicializar_naves(tablero:list) -> dict:
    contador = 0
    contador_nave = 0

    diccionario = {
        "tablero": tablero,
        "submarinos": [],
        "destructores": [],
        "cruceros": [],
        "acorazados": []
    }

    while contador < 10:
        rnd_fila = random.randint(0, len(tablero) - 1)
        rnd_col =  random.randint(0, len(tablero) - 1)
        
        # Submarinos
        if contador < 4:  
            if tablero[rnd_fila][rnd_col] == 1:
                continue          
            
            tablero[rnd_fila][rnd_col] = 1
            submarino = []
            submarino.append(rnd_fila)
            submarino.append(rnd_col)
            diccionario["submarinos"].append(submarino)
            print(f"Submarino: [{[rnd_fila]}] [{[rnd_col]}]")
        
        # Destructores
        elif contador > 3 and contador < 7:
            if rnd_col > 8:
                continue

            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1:
                continue 

            contador_nave+= 1
            
            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            destructor = []
            destructor.append(rnd_fila)
            for i in range(2):
                destructor.append(rnd_fila)
                destructor.append(rnd_col+i)
            diccionario["destructores"].append(destructor)
            print(f"Destructor: [{[rnd_fila]}] [{[rnd_col]}]")
            print(f"Destructor: [{[rnd_fila]}] [{[rnd_col + 1]}]")
        
        # Cruceros
        elif contador > 6 and contador < 9:
            contador_nave = 0
            if rnd_col > 7:
                continue
            
            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1 or tablero[rnd_fila][rnd_col + 2] == 1:
                continue

            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            tablero[rnd_fila][rnd_col + 2] = 1
            crucero = []
            crucero.append(rnd_fila)
            for i in range(3):
                destructor.append(rnd_fila)
                crucero.append(rnd_col+i)

            diccionario["cruceros"].append(crucero)
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col]}]")
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col + 1]}]")
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col + 2]}]")
        
        # Acorazados
        elif contador > 8:
            contador_nave = 0
            if rnd_col > 6:
                continue
            
            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1 or tablero[rnd_fila][rnd_col + 2] == 1 or tablero[rnd_fila][rnd_col + 3] == 1:
                continue

            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            tablero[rnd_fila][rnd_col + 2] = 1
            tablero[rnd_fila][rnd_col + 3] = 1
            acorazado = []
            acorazado.append(rnd_fila)
            for i in range(4):
                destructor.append(rnd_fila)
                acorazado.append(rnd_col+i)
            diccionario["acorazados"].append(acorazado)
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col]}]")     
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 1]}]")       
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 2]}]")       
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 3]}]")               
        
        contador += 1

    return diccionario

#imprimir matriz
def imprimir_tablero(matriz_notas:list):
    """
    Imprime tablero
    
    Args:
        matriz_notas: Son las notas de las materias de los alumnos.
    Returns:
        None.
    """
    for i in range(len(matriz_notas)):        
        for j in range(len(matriz_notas[i])):
            print(matriz_notas[i][j], end=" | ")
        print("")