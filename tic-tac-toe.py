# ========== FUNCIONES =========== #


# Función para dibujar el tablero vacío
def print_board():
    print("         |         |         ")
    print("         |         |         ")
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("         |         |         ")
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("         |         |         ")
    print("         |         |         ")

# Función para imprimir número de juego 
def print_game(number):
    print('\n---------- GAME', number, '---------- \n \n')

# Imprimir quién ganó y aumentar su puntaje
# Esta función va tomar como parámetro winner, que va a ser un valor booleano
def winner(player_1_won):
    global player_1
    global player_2
    global player_1_score
    global player_2_score
    if player_1_won:
        print(player_1, 'wins this game!')
        player_1_score += 1

    else:
        print(player_2, 'wins this game!')
        player_2_score += 1


# ============= RONDAS =============== #


# Declarar la primera ronda como 1
round = 1


def is_player_1_turn():
    global round
    # Si el número de ronda no es par es turno del jugador 1
    if round % 2 != 0:
        round += 1
        return True
    # Si el número de ronda es par es turno del jugador 2
    else:
        round += 1
        return False



# ============= PUNTAJE ============== #


player_1_score = 0
player_2_score = 0


# ============== JUEGO =============== #


# Elección de nombre
player_1 = input('Choose player 1 name: ')
player_2 = input('Choose player 2 name: ')

# Aquí va a ir algo para limpiar/clear la terminal

# Imprimir el número del juego
print_game(1)

print_board()

# Suponemos que el jugador 1 ganó
winner(True)
print(player_1_score)