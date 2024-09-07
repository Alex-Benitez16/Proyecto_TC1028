# ========== FUNCIONES =========== #

# Imprime el gato con los tokens?/fichas? (no se como se llaman) en el tablero
def print_board(array):
    print("\n\n         |         |         ")
    print("   ", array[0][0], "   |   ", array[0][1], "   |   ", array[0][2])
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("   ", array[1][0], "   |   ", array[1][1], "   |   ", array[1][2])
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("   ", array[2][0], "   |   ", array[2][1], "   |   ", array[2][2])
    print("         |         |         \n")

# Actualiza el tablero con los inputs del jugador. Como los arreglos inician en 0 restar 1
def update_board(array, player):
    array[row - 1][column - 1] = player

# Selección de lugar donde poner la ficha
def select_square(array):
    # Preguntar al jugador donde
    a = int(input("\nChoose column: 1 for left, 2 for middle, 3 for right :")) # a pide un valor de 1 o 2 o 3
    b = int(input("\nChoose row: 1 for top, 2 for middle, 3 for bottom :")) # b pide un valor de 1 o 2 o 3
    
    # Si a o b no estan dentro de los valores deseados, repetir input hasta que lo esten
    while((a != 1 and a != 2 and a !=3 ) or (b != 1 and b != 2 and b != 3)):
        print("\nInvalid entry. Please try again.\n")
        a = int(input("\nChoose column: 1 for left, 2 for middle, 3 for right: "))
        b = int(input("\nChoose row: 1 for top, 2 for middle, 3 for bottom: "))

    # Si la casilla seleccionada ya esta ocupada, volver a pedir los valores hasta que se elija una casilla desocupada 
    while(array[b - 1][a - 1] == 'X' or array[b - 1][a - 1] == 'O'):
        print("\nSquare already occupied. Please choose a different square.\n")
        a = int(input("\nChoose column: 1 for left, 2 for middle, 3 for right: "))
        b = int(input("\nChoose row: 1 for top, 2 for middle, 3 for bottom: "))

        # Volver a verificar que los valores sean los deseados. TODO CAMBIAR ESTOS DOS WHILES A OTRA FUNCION?
        while((a != 1 and a != 2 and a !=3 ) or (b != 1 and b != 2 and b != 3)):
            print("\nInvalid entry. Please try again.\n")
            a = int(input("\nChoose column: 1 for left, 2 for middle, 3 for right: "))
            b = int(input("\nChoose row: 1 for top, 2 for middle, 3 for bottom: "))

    return a, b

# TODO encontrar una forma de que al meter valores que no sean int el programa no crashee

#  ========== VARIABLES ========== #

# Matriz de tokens?/fichas? Inicializado con espacios en blanco
tokens = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player1_token = 'O'
player2_token = 'X'

round_number = 1

# ========= JUEGO ========== #

# Rogar al jugador que no crashee el programa. Ver linea 47 para referencia
print("\n\nDear player, I BEG you, do not enter non-integer values.\n\n")

# While temporal en lo que descubro como hacer una win condition
while(round_number < 10):
    if(round_number % 2 != 0):
        column, row = select_square(tokens)
        update_board(tokens, player1_token)
    else:
        column, row = select_square(tokens)
        update_board(tokens, player2_token)

    print_board(tokens)

    round_number += 1
    