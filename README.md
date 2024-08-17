# Proyecto_TC1028

## The Library Quest 

El propósito de este proyecto es desarrollar un juego sencillo usando los conceptos de programación aprendidos durante el curso. La idea es que el juego se juegue completamente **dentro de la terminal**, y que sea completamente a **base de texto**. 

### Temática

La temática es un estudiante del Instituto Tecnológico y de Estudios Superiores Monterrey buscando *el libro* para finalmente entregar su proyecto final de química. A lo largo de esta gran travesía se enfrentará a cuatro enemigos formidables: la bibliotecaria habladora, el fantasma del silencio, el ratón de biblioteca, y manuscrito misterioso. 

### Estructura

1. Instrucciones breves del navegamiento del juego
2. Introducción y selección de nombre
3. Encuentro 1
4. Encuentro 2
5. Encuentro 3
6. Encuentro 4
7. Final
8. Agradecimientos

Planeo que el juego sea breve y sencillo. Primero contará con un pequeño texto que explique como será el navegamiento del mismo. Después habrá una pequeña introducción del personaje donde el jugador también podrá elejir su nombre de jugador. El juego constará de cuatro encuentros contra algunos personajes. Finalmente habrá una conclusión y agradecimientos.

### Algortimos

// Ask for player's name

EO(playerName)
    // Check if it's a string or force it to be a string
    // Save the player's name in a varible

    playerName = player_name // This function won't be local

    return print('The librarian takes the credential and reads it.')
    // Press enter to continue
    print('"Hmmm, so you are..."')
    // Press enter to continue
    print('She hesitates.")
    // Press enter to continue
    Print(playerName + '...?')
    // Press enter to continue
EF (return)

// Visit a door. The door that progresses the story will always be the third.

EF(door_chosen)
    if(door_chosen == true) // Check if door has already been visited
        return print('You have already been here')
    else if(first_door == false)
        first_door = true
        return 