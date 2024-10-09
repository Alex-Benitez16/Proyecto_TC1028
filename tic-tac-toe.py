'''
Dueño: Alejandro .....
Descripción general: ....
'''
import time
import os
import platform

# ========== FUNCIONES =========== #

'''
    Nombre función: 
    Que hce la función? 
    Parametro 
    Que regresa 
'''
# platform.system() me regresa ya sea 'Windows' o 'Linux'
# os.system ejecuta un comando para la terminal
def clear_terminal():
    if(platform.system() == "Windows"):
        os.system('cls')
    else: 
        os.system('clear')

# time.sleep hace que el programa espere cierto tiempo antes de seguir 
# con la siguiente instrucción
# flush= True es porque un print solo hace flush (soltar lo que tiene en la terminal)
# cuando encuentra un \n, asi que tengo que especificar que en cada print haga un flush
# end_line es por si quiero terminar la línea ahí (\n) o si quiero continuar en la misma
def print_cool(string, end_line=True):
    array = list(string)
    speed_of_printing = 0.03

    for i in array:
        print(i, end='', flush=True)
        time.sleep(speed_of_printing)
    if(end_line):
        print('\n')

def print_cool_fast(string, end_line=True):
    array = list(string)
    speed_of_printing = 0.001

    for i in array:
        print(i, end='', flush=True)
        time.sleep(speed_of_printing)
    if(end_line):
        print('\n')

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
def update_board(array, player, row, column):
    array[row - 1][column - 1] = player

# Selección de lugar donde poner la ficha
def select_square(array):
    # Preguntar al jugador donde
    print_cool("\nChoose column: 1 for left, 2 for middle, 3 for right: ", False)
    a = int(input()) # a pide un valor de 1 o 2 o 3
    print_cool("\nChoose row: 1 for top, 2 for middle, 3 for bottom: ", False)
    b = int(input()) # b pide un valor de 1 o 2 o 3
    
    # Si a o b no estan dentro de los valores deseados, repetir input hasta que lo esten
    while((a != 1 and a != 2 and a !=3 ) or (b != 1 and b != 2 and b != 3)):
        print_cool("\nInvalid entry. Please try again.\n")
        print_cool("\nChoose column: 1 for left, 2 for middle, 3 for right: ", False)
        a = int(input())
        print_cool("\nChoose row: 1 for top, 2 for middle, 3 for bottom: ", False)
        b = int(input())

    # Si la casilla seleccionada ya esta ocupada, volver a pedir los valores hasta que se elija una casilla desocupada 
    while(array[b - 1][a - 1] == 'X' or array[b - 1][a - 1] == 'O'):
        print_cool("\nSquare already occupied. Please choose a different square.\n")
        print_cool("\nChoose column: 1 for left, 2 for middle, 3 for right: ", False)
        a = int(input())
        print_cool("\nChoose row: 1 for top, 2 for middle, 3 for bottom: ", False)
        b = int(input())

        # Volver a verificar que los valores sean los deseados. TODO CAMBIAR ESTOS DOS WHILES A OTRA FUNCION?
        while((a != 1 and a != 2 and a !=3 ) or (b != 1 and b != 2 and b != 3)):
            print_cool("\nInvalid entry. Please try again.\n")
            print_cool("\nChoose column: 1 for left, 2 for middle, 3 for right: ", False)
            a = int(input())
            print_cool("\nChoose row: 1 for top, 2 for middle, 3 for bottom: ", False)
            b = int(input())

    return a, b

# TODO encontrar una forma de que al meter valores que no sean int el programa no crashee

# Esta función checa todas las posibles formas de ganar y si alguna a ocurrido
def check_win_condition(array, player):
    if(array[0][0] == array[0][1] == array[0][2] == player):
        return True
    elif(array[1][0] == array[1][1] == array[1][2] == player):
        return True
    elif(array[2][0] == array[2][1] == array[2][2] == player):
        return True
    elif(array[0][0] == array[1][0] == array[2][0] == player):
        return True
    elif(array[0][1] == array[1][1] == array[2][1] == player):
        return True
    elif(array[0][2] == array[1][2] == array[2][2] == player):
        return True
    elif(array[0][0] == array[1][1] == array[2][2] == player):
        return True
    elif(array[0][2] == array[1][1] == array[2][0] == player):
        return True
    else:
        return False

def ask_for_players_names():
   print_cool("Choose player 1 name: ", False)
   name1 = input()
   print_cool("Choose player 2 name: ", False)
   name2 = input()
   return name1, name2

def press_enter_to_continue():
    print_cool("Press enter to continue... ")
    enter = input()

def print_instructions(player1, player2):
    print_cool(f"Alright, alright. {player1}, {player2}, \
               I need to make something very, very clear.")
    print_cool(f"This ain't no regular tic-tac-toe. No, no, no.")
    print_cool(f"Have it known that thi IS WAR.")
    print_cool(f"Make no mistake. Your honor is on the line. \
               Your next 50 years WILL be detirmined by this one game.")
    print_cool(f"Do you understand now?    Good.")
    
    press_enter_to_continue()
    clear_terminal()

    print_cool(f"So, I bet you are wondering why is that.\
                Allow me to explain. ")

    print_cool_fast(f"Let me take you back... back to a time long \
                    before we ever thought to use mere symbols on a \
                    grid for entertainment.", False)
    print_cool_fast(f"Centuries ago, in a realm not bound by time or \
                    space, there existed two opposing forces: Order \
                    and Chaos.", False)
    print_cool_fast(f"They were not just cosmic ideas, no, they were \
                    living, breathing titans. Their battles raged \
                    for eons.", False)
    print_cool_fast(f"And at the heart of it all, their eternal \
                    struggle, was a sacred game. A game so powerful, \
                    so dangerous, it could shape entire universes.")

    print_cool_fast(f"The game? A simple grid. Nine spaces. \
                    But it was far more than that. To mere mortals, \
                    it may look like child's play.", False)
    print_cool_fast(f"But to the Titans? It was the ultimate \
                    test of strategy, cunning, and resilience.", False)
    print_cool_fast(f"Each mark placed on the grid did not just \
                    fill a space. It sent shockwaves across galaxies. \
                    A move was more than a move.", False)
    print_cool_fast(f"It was an assertion of will, an imposition of destiny.")

    print_cool_fast(f"For every round of this game, the balance \
                    of existence teetered. A single victory could mean \
                    prosperity for an entire universe.", False)
    print_cool_fast(f"A single defeat could mean ruin, as worlds would crumble \
                    into dust, swallowed by the void.", False)
    print_cool_fast(f"Order and Chaos were locked in this conflict, \
                    neither side able to claim ultimate victory. \
                    Not until the fateful day... when they disappeared.", False)
    print_cool_fast(f"No one knows how or why. \
                    Some say they destroyed each other. \
                    Others say they ascended beyond our understanding.", False)
    print_cool_fast(f"But they left behind their game. \
                    And with it, the rules. And with those rules, their power.")

    print_cool_fast(f"The game found its way through the cosmos, \
                    passing through the hands of gods, emperors, warriors, \
                    and scholars.", False)
    print_cool_fast(f"Each time it was played, reality itself trembled. \
                    Yet, the true nature of the game remained hidden, \
                    passed off as mere amusement for the naive.", False)
    print_cool_fast(f"But you... {player1}, {player2}... you are different.", False)
    print_cool_fast(f"You have been chosen. Whether by fate, destiny, \
                    or some ancient force, you now hold the power of the Titans \
                    in your hands.", False)
    print_cool_fast(f"You may think this is a game of tic-tac-toe, \
                    but know this: every move, every decision, \
                    ripples through the fabric of reality.")
    
    print_cool_fast(f"Win... and you will shape your world in your image. \
                    The stars will align for you, and your name will echo \
                    in the halls of eternity.", False)
    print_cool_fast(f"Lose... and Chaos will consume everything you hold dear. \
                    The very ground beneath you will tremble, \
                    the skies will darken, and your legacy?", False)
    print_cool_fast(f"It will be dust, scattered across the win-")

    time.sleep(2)
    clear_terminal()

    print_cool(f"But we don't care about lore, do we?")
    print_cool(f"What we want to see is BLOODSHED.")
    print_cool(f"So, without further ado...")
    print_cool(f"LADIES AND GENTLEMEN, I WELCOME YOU TO THIS BATTLE OF ATTRITION.")
    print_cool(f"{player1.upper()} VS {player2.upper()}. \
               LET US SEE WHO SHALL GAIN THE GLORY. ")
    
    press_enter_to_continue()
    print_cool(f"Btw I'm rooting for {player2}.")


    

#  ========== VARIABLES ========== #

# Matriz de tokens?/fichas? Inicializado con espacios en blanco
tokens = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

player1_token = 'O'
player2_token = 'X'

player1_has_won = False
player2_has_won = False

score = {"player1": 0, "player2": 0}

round_number = 1

# ========= JUEGO ========== #

# Rogar al jugador que no crashee el programa. Ver linea 47 para referencia
clear_terminal()
player1, player2 = ask_for_players_names()
print_instructions(player1, player2)

while(round_number < 10 and not player1_has_won and not player2_has_won):

    clear_terminal()
    print_board(tokens)

    if(round_number % 2 != 0):
        column, row = select_square(tokens)
        update_board(tokens, player1_token, row, column)
    else:
        column, row = select_square(tokens)
        update_board(tokens, player2_token, row, column)

    clear_terminal()
    print_board(tokens)

    player1_has_won = check_win_condition(tokens, player1_token)
    player2_has_won = check_win_condition(tokens, player2_token)

    round_number += 1
