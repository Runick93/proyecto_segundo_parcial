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



def cargar_naves(tablero:list) -> list:
    contador = 0

    while contador < 10:
        rnd_fila = random.randint(0, len(tablero) - 1)
        rnd_col =  random.randint(0, len(tablero) - 1)
        
        # Submarinos
        if contador < 4:  
            if tablero[rnd_fila][rnd_col] == 1:
                continue          
            
            tablero[rnd_fila][rnd_col] = 1
            print(f"Submarino: [{[rnd_fila]}] [{[rnd_col]}]")
        
        # Destructores
        elif contador > 3 and contador < 7:
            if rnd_col > 8:
                continue

            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1:
                continue 
            
            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            print(f"Destructor: [{[rnd_fila]}] [{[rnd_col]}]")
            print(f"Destructor: [{[rnd_fila]}] [{[rnd_col + 1]}]")
        
        # Cruceros
        elif contador > 6 and contador < 9:
            if rnd_col > 7:
                continue
            
            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1 or tablero[rnd_fila][rnd_col + 2] == 1:
                continue

            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            tablero[rnd_fila][rnd_col + 2] = 1
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col]}]")
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col + 1]}]")
            print(f"Crucero: [{[rnd_fila]}] [{[rnd_col + 2]}]")
        
        # Acorazados
        elif contador > 8:
            if rnd_col > 6:
                continue
            
            if tablero[rnd_fila][rnd_col] == 1 or tablero[rnd_fila][rnd_col + 1] == 1 or tablero[rnd_fila][rnd_col + 2] == 1 or tablero[rnd_fila][rnd_col + 3] == 1:
                continue

            tablero[rnd_fila][rnd_col] = 1
            tablero[rnd_fila][rnd_col + 1] = 1
            tablero[rnd_fila][rnd_col + 2] = 1
            tablero[rnd_fila][rnd_col + 3] = 1  
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col]}]")     
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 1]}]")       
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 2]}]")       
            print(f"Acorazado: [{[rnd_fila]}] [{[rnd_col + 3]}]")               
        
        contador += 1


    return tablero


# Validaciones:
# Validar que no se superpongan las naves.
# Validar que no queren la mitad de una nave fuera de la matriz.


# detectar donde si ya hay una nave en esa posicion.
# generar naves
#    - Submarinos   : [fila] [col] = 1
#    - Destructores : [fila] [col] [col] = 1
#    - Crucero      : [fila] [col] [col] [col] = 1
#    - Acorazado    : [fila] [col] [col] [col] [col] = 1



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