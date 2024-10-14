'''
Dueño: Alejandro Benítez Bravo 
Descripción general: Este es un juego de gato con 5 rondas
                     y gana el mejor de 3/5
'''

'''
=========== LIBRERIAS UTILIZADAS =============  
'''
import os
import time
import platform
import random

'''
===============================================
================== FUNCIONES ==================
===============================================
'''

'''
============ FUNCIONES DE LA TERMINAL ===============
'''
def clear_terminal():
    '''
    (if statements, librerias de os y platform )
    Parámetros: ninguno
    Que hace?: limpia la terminal
    Devuelve: nada
    '''
    if(platform.system() == "Windows"):
        os.system('cls')
    else: 
        os.system('clear')

def press_enter_to_continue():
    '''
    (variables e inputs)
    Parámetros: ninguno
    Que hace?: crea una pausa hasta que el 
               usuario ingresa un input
    Devuelve: nada, el input no se usa
    '''
    print_cool("Press enter to continue... ")
    enter = input()

'''
============== FUNCIONES DE IMPRESIÓN ===============
'''

def print_cool(string, end_line=True):
    '''
    (arreglos, strings, libreria de time, for loops)
    Parámetros: un string y bool
    Qué hace?: convierte el string a un arreglo
               para imprimir caracter por caracter
               el arreglo esperando cierto tiempo entre 
               impresión. si end_line=false entonces no 
               hará un salto de línea después de terminar
    Devuelve: nada
    '''
    array = list(string)
    speed_of_printing = 0.03

    for i in array:
        print(i, end='', flush=True)
        time.sleep(speed_of_printing)
    if(end_line):
        print('\n')

def print_cool_fast(string, end_line=True):
    '''
    (arreglos, strings, libreria de time, for loops)
    Parámetros: un string y un bool
    Qué hace: lo mismo que print_cool excepto que 
              espera menos tiempo entre caracter
              por lo que imprime más rápido
    Devuelve: nada
    '''
    array = list(string)
    speed_of_printing = 0.001

    for i in array:
        print(i, end='', flush=True)
        time.sleep(speed_of_printing)
    if(end_line):
        print('\n')

def ask_for_players_names():
    '''
    (strings, variables e inputs)
    Parámetros: ninguno
    Qué hace?: usa print_cool. pregunta por los 
               nombres de los jugadores
    Devuelve: los nombres de los jugadores
    '''
    print_cool("Choose player 1 name: ", False)
    name1 = input()
    print_cool("Choose player 2 name: ", False)
    name2 = input()
    return name1, name2

def print_instructions(player1, player2):
    '''
    (strings, libreria time)
    Parámetros: los nombres de los jugadores
    Que hace? Imprime las instrucciones y el lore
              del juego. El primer bloque de texto utiliza
              print_cool, el segundo print_cool_fast, y el 
              último print_cool (en un intento de causar gracia)
    Devuelve: nada
    ** no es necesario leer la función completa **
    '''
    print_cool(f"Alright, alright. {player1}, {player2}, " 
               "I need to make something very, very clear.")
    print_cool(f"This ain't no regular tic-tac-toe. No, no, no.")
    print_cool(f"Have it known that this IS WAR.")
    print_cool(f"Make no mistake. Your honor is on the line. "
               "Your next 50 years WILL be detirmined by this one game.")
    print_cool(f"Do you understand now?    Good.")
    
    press_enter_to_continue()
    clear_terminal()

    print_cool(f"So, I bet you are wondering why is that. "
                "Allow me to explain. ")

    print_cool_fast(f"Let me take you back... back to a time long "
                    "before we ever thought to use mere symbols on a "
                    "grid for entertainment.", False)
    print_cool_fast(f"Centuries ago, in a realm not bound by time or "
                    "space, there existed two opposing forces: Order "
                    "and Chaos.", False)
    print_cool_fast(f"They were not just cosmic ideas, no, they were "
                    "living, breathing titans. Their battles raged "
                    "for eons.", False)
    print_cool_fast(f"And at the heart of it all, their eternal "
                    "struggle, was a sacred game. A game so powerful, "
                    "so dangerous, it could shape entire universes.")

    print_cool_fast(f"The game? A simple grid. Nine spaces. "
                    "But it was far more than that. To mere mortals, "
                    "it may look like child's play.", False)
    print_cool_fast(f"But to the Titans? It was the ultimate "
                    "test of strategy, cunning, and resilience.", False)
    print_cool_fast(f"Each mark placed on the grid did not just "
                    "fill a space. It sent shockwaves across galaxies. "
                    "A move was more than a move.", False)
    print_cool_fast(f"It was an assertion of will, "
                    "an imposition of destiny.")

    print_cool_fast(f"For every round of this game, "
                    "the balance of existence teetered. "
                    "A single victory could mean "
                    "prosperity for an entire universe.", False)
    print_cool_fast(f"A single defeat could mean ruin, "
                    "as worlds would crumble "
                    "into dust, swallowed by the void.", False)
    print_cool_fast(f"Order and Chaos were locked in "
                    "this conflict, neither side able "
                    "to claim ultimate victory. "
                    "Not until the fateful day... "
                    "when they disappeared.", False)
    print_cool_fast(f"No one knows how or why. Some say "
                    "they destroyed each other. "
                    "Others say they ascended "
                    "beyond our understanding.", False)
    print_cool_fast(f"But they left behind their game. "
                    "And with it, the rules. "
                    "And with those rules, their power.")

    print_cool_fast(f"The game found its way through the cosmos, "
                    "passing through the hands of gods, emperors, "
                    "warriors, and scholars.", False)
    print_cool_fast(f"Each time it was played, reality itself trembled." 
                    "Yet, the true nature of the game remained hidden, "
                    "passed off as mere amusement for the naive.", False)
    print_cool_fast(f"But you... {player1}, {player2}... "
                    "you are different.", False)
    print_cool_fast(f"You have been chosen. Whether by fate, destiny, "
                    "or some ancient force, "
                    "you now hold the power "
                    "of the Titans in your hands.", False)
    print_cool_fast(f"You may think this is a game of tic-tac-toe, "
                    "but know this: every move, every decision, "
                    "ripples through the fabric of reality.")
    
    print_cool_fast(f"Win... and you will shape your world in your image. "
                    "The stars will align for you, "
                    "and your name will echo "
                    "in the halls of eternity.", False)
    print_cool_fast(f"Lose... and Chaos will "
                    "consume everything you hold dear. "
                    "The very ground beneath you will tremble, "
                    "the skies will darken, and your legacy?", False)
    print_cool_fast(f"It will be dust, scattered across the win-")

    time.sleep(2)
    clear_terminal()

    print_cool(f"But we don't care about lore, do we?")
    print_cool(f"What we want to see is BLOODSHED.")
    print_cool(f"So, without further ado...")
    print_cool(f"LADIES AND GENTLEMEN, "
               "I WELCOME YOU TO THIS BATTLE OF ATTRITION.")
    print_cool(f"{player1.upper()} VS {player2.upper()}. "
               "LET US SEE WHO SHALL GAIN THE GLORY. ")
    
    press_enter_to_continue()
    print_cool(f"Btw I'm rooting for {player2}.")

'''
=========== FUNCIONES DE MANIPULACIÓN DEL TABLERO ===========
'''

# la matriz que usan todas las funciones, tokens, se define más adelante

def print_board(array, round):
    '''
    (arreglos, strings)
    Parámetros: la matriz de fichas/tokens 
                actualmente en el tablero y
                el número de ronda
    Que hace?: imprime el número de ronda y el
               tablero con las fichas 
    Devuelve: nada
    '''
    print(f"\n-----------ROUND {round}-----------")
    print("\n\n         |         |         ")
    print("   ", array[0][0], "   |   ", \
          array[0][1], "   |   ", array[0][2])
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("   ", array[1][0], "   |   ", \
          array[1][1], "   |   ", array[1][2])
    print("         |         |         ")
    print("---------|---------|---------")
    print("         |         |         ")
    print("   ", array[2][0], "   |   ", \
          array[2][1], "   |   ", array[2][2])
    print("         |         |         \n")

def update_board(array, player, row, column):
    '''
    (arreglos)
    Parámetros: la matriz tokens, la ficha del 
                jugador en turno, su selección
                de fila y columna
    Que hace?: actualiza la matriz sustituyendo
               ' ' (espacio en blanco) por el la 
               ficha
    Devuelve: nada
    '''
    array[row - 1][column - 1] = player

def clear_board(array):
    '''
    (arreglos, while loops)
    Parámetros: la matriz tokens
    Que hace?: limpia la matriz sustituyendo
               todos los elementos por ' '
    Devuelve: nada
    '''
    i = 0
    while(i < len(array)):
        j = 0
        while(j < len(array[i])):
            array[i][j] = ' '
            j += 1
        i += 1

def get_valid_input(message):
    '''
    (strings, inputs, while loops, if statements)
    Parámetros: un mensaje/prompt de input
    Que hace?: pide un valor y valida si es un valor
               permitido (1, 2 o 3). en caso de que no
               vuelve a pedir el valor hasta que lo sea
    Devuelve: el valor permitido
    '''
    while True:
        try:
            print_cool(message, False)
            value = int(input())

            if(value in [1, 2, 3]):
                return value
            else:
                print_cool("\nInvalid entry. Please enter 1, 2 or 3.")
        except ValueError:
            print_cool("\nInvalid entry. Please enter a number.")

def check_unoccupied_square(array, row, column):
    '''
    (arreglos, inputs, strings, while loops)
    Parámetros: la matriz tokens, la selección de 
                fila y de columna
    Que hace?: verifica que la casilla seleccionada
               no este ocupada. en caso de estarla 
               vuelve a pedir valores válidos
    Devuelve: los valores validados y sin ocupar
    '''
    while(array[row - 1][column - 1] in ['X', 'O']):
        print_cool("\nSquare already occupied. "
        "Please choose a different square.")
        column = get_valid_input("\nChoose column: ")
        row = get_valid_input("\nChoose row: ")

    return column, row

def select_square(array):
    '''
    (arreglos, strings)
    Parámetros: la matriz tokens
    Que hace?: usa la función get_valid_input para
               pedir valores válidos y 
               check_unoccupied_square para asegurarse
               de que no esten ocupados
    Devuelve: los valores validados y sin ocupar
    '''
    row_choice_message = "\nChoose row: "
    "1 for top, 2 for middle, 3 for bottom: "
    column_choice_message = "\nChoose column: "
    "1 for left, 2 for middle, 3 for right: "

    column = get_valid_input(column_choice_message)
    row = get_valid_input(row_choice_message)

    column, row = check_unoccupied_square(array, row, column)

    return column, row

def check_win_condition(array, player_token):
    '''
    (arreglos)
    Parámetros: la matriz tokens, la ficha a evaluar
    Que hace?: verifica si alguna win-condition ha
               sucedido (probando para todas las 
               combinaciones) para la ficha seleccionada
    Devuelve: verdadero si la win-condition se cumple, 
              falso si aún no
    '''
    if(array[0][0] == array[0][1] == array[0][2] == player_token):
        return True
    elif(array[1][0] == array[1][1] == array[1][2] == player_token):
        return True
    elif(array[2][0] == array[2][1] == array[2][2] == player_token):
        return True
    elif(array[0][0] == array[1][0] == array[2][0] == player_token):
        return True
    elif(array[0][1] == array[1][1] == array[2][1] == player_token):
        return True
    elif(array[0][2] == array[1][2] == array[2][2] == player_token):
        return True
    elif(array[0][0] == array[1][1] == array[2][2] == player_token):
        return True
    elif(array[0][2] == array[1][1] == array[2][0] == player_token):
        return True
    else:
        return False

'''
================ FUNCIONES DE RONDA ===================
'''

# has_won es un diccionario que se define más adelante
# este guarda si algún jugador ha ganado

def full_round(tokens, player1_token, player2_token, has_won, round):
    '''
    (arreglos, diccionarios, while loops, if statements)
    Parámetros: la matriz tokens, las fichas de cada jugador, el
                diccionario has_won, el número de ronda
    Que hace?: mientras no hayan ocurrido 9 turnos (el número máximo
               de turnos para un juego de gato) y ningún jugador haya ganado
               se sigue el proceso de una ronda: limpiar terminal, imprimir
               tablero, los turnos impares son del jugador 1 y los pares del
               jugador 2, cada jugador selecciona su casilla y el tablero
               se actualiza, se vuelve a limpiar la terminal y se imprime 
               el tablero con los valores actualizados, y se verifican 
               las win-conditions para ambos jugadores
    Devuelve: ya me cansé de poner nada
    '''
    turn = 1
    
    while(turn < 10 \
          and not has_won["player1"] \
            and not has_won["player2"]):

        clear_terminal()
        print_board(tokens, round)

        if(turn % 2 != 0):
            column, row = select_square(tokens)
            update_board(tokens, player1_token, row, column)
        else:
            column, row = select_square(tokens)
            update_board(tokens, player2_token, row, column)

        clear_terminal()
        print_board(tokens, round)

        has_won["player1"] = check_win_condition(tokens, player1_token)
        has_won["player2"] = check_win_condition(tokens, player2_token)



        turn += 1


# score es un diccionario que guarda el puntaje

def check_for_winner(has_won, score):
    '''
    (diccionarios, if statements)
    Parámetros: diccionarios has_won y score
    Que hace?: una vez terminado full_round determina
               quién fue el ganador y le añade un punto
               al puntaje. cambia los valores de has_won
               de ambos jugadores a false
    Devuelve: naranjas
    '''
    if(has_won["player1"]):
        score["player1"] += 1

    elif(has_won["player2"]):
        score["player2"] += 1

    has_won["player1"] = False
    has_won["player2"] = False
    
def print_score(score, player1, player2):
    '''
    (if statements, diccionarios, libreria random)
    Parámatros: el puntaje y los nombres de los jugadores
    Que hace?: primero elije aleatoriamente un mensaje
               'motivacional'. después imprime los 
               puntajes actuales
    Devuelve: naranjas dulces
    '''
    choice = int(random.random() * 10) 
    if(choice == 0):
        print_cool(f"Wow, I wasn't expecting that, {player1}")
    elif(choice == 1):
        print_cool(f"Who would've thought...")
    elif(choice == 2):
        print_cool(f"Nice, {player2}")
    elif(choice == 3):
        print_cool(f"I am not surprised, {player1}")
    elif(choice == 4):
        print_cool(f"Now that's what I call a good game")
    elif(choice == 5):
        print_cool(f"...")
    elif(choice == 6):
        print_cool(f"Sweet...")
    elif(choice == 7):
        print_cool(f"What was that {player2}?")
    elif(choice == 8):
        print_cool(f"Turning the tables {player1}")
    elif(choice == 9):
        print_cool(f"Yeah, no motivational message here.")

    print_cool(f"Current score: "
               f'{player1}: {score["player1"]}, '
               f'{player2}: {score["player2"]}')

def print_winner(player1, player2, score):
    '''
    (diccionarios, if statements)
    Parámetros: nombres de los jugadores y puntaje
    Que hace?: después de las 5 rondas, verifica quien
               es el ganador y lo imprime. en caso de un
               empate no se imprime un ganador
    Devuelve: naranjas dulces limones agrios
    '''
    if(score["player1"] == score["player2"]):
        print_cool(f"I am so sorry to announce this, "
        "But ladies and getlemen we have no winner.")
    else:
        print_cool(f"WELL WELL WELL LADIES AND GENTLEMEN "
        f"IT SEEMS LIKE WE HAVE A WINNER")
        print_cool(f"LET'S GIVE A ROUND A APPLAUSE TO")
        if(score["player1"] > score["player2"]):
            print_cool(f"¡¡¡¡¡¡¡¡¡¡¡¡{player1}!!!!!!!!!!!!")
        else:
            print_cool(f"¡¡¡¡¡¡¡¡¡¡¡¡{player2}!!!!!!!!!!!!")
        
    print_cool(f"Either way, {player1} and {player2}, "
        f"thank you for playing. We hope you enjoyed.")
    
'''
========================================================
====================== VARIABLES =======================
========================================================
'''

# Matriz de fichas del tablero
tokens = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Fichas de cada jugador
player1_token = 'O'
player2_token = 'X'

# Diccionario para ver si alguien ha ganado
has_won = {"player1": False, "player2": False}

# Diccionario del puntaje
score = {"player1": 0, "player2": 0}

# Número de ronda
round_number = 1

'''
===========================================================
========================== JUEGO ==========================
===========================================================
'''

# Limpiar terminal, preguntar por nombres, imprimir lore
clear_terminal()
player1, player2 = ask_for_players_names()
print_instructions(player1, player2)

# Máximo de 5 rondas o hasta que un jugador supere llegue a 3 puntos
while(round_number <= 5 and score["player1"] < 3 and score["player2"] < 3):
    full_round(tokens, player1_token, player2_token, has_won, round_number)

    check_for_winner(has_won, score)

    print_score(score, player1, player2)

    press_enter_to_continue()

    clear_terminal()

    clear_board(tokens)
    round_number += 1

print_winner(player1, player2, score)