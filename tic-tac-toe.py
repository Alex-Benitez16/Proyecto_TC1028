# ========== FUNCIONES ===========

# Función para dibujar el tablero vacío
def print_board():
    print("       |       |       ")
    print("       |       |       ")
    print("       |       |       ")
    print("-------|-------|-------")
    print("       |       |       ")
    print("       |       |       ")
    print("       |       |       ")
    print("-------|-------|-------")
    print("       |       |       ")
    print("       |       |       ")
    print("       |       |       ")

# Función para imprimir número de juego
def print_game(number):
    print('\n---------- GAME', number, '---------- \n \n')

# Imprimir quién ganó y aumentar su puntaje
# Esta función va tomar como parámetro winner, que va a ser un valor booleano
def winner(winner):
    global player_1
    global player_2
    global player_1_score
    global player_2_score
    if winner:
        print(player_1, 'wins this game!')
        player_1_score += 1

    else:
        print(player_2, 'wins this game!')
        player_2_score += 1

# ============= PUNTAJE ==============

player_1_score = 0
player_2_score = 0

# ============== JUEGO ===============

# Elección de nombre
player_1 = input('Choose player 1 name: ')
player_2 = input('Choose player 2 name: ')

# Aquí va a ir algo para limpiar/clear la terminal

# Imprimir el número del juego
print_game(1)

# Suponemos que el jugador 1 ganó
winner(True)
print(player_1_score)