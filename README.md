# Proyecto_TC1028

## Batalla Épica: Tic-Tac-Toe de los Titanes

---
### Historia

El objetivo del proyecto es programar un juego de gato que se pueda jugar con dos personas en la misma computadora. 

Este no es el típico juego de tres en raya. ¡Es mucho más que eso! Bienvenidos a una batalla épica entre las fuerzas primordiales de **Orden y Caos**. En un universo antiguo, estos titanes libraron batallas que sacudieron los cimientos de la existencia, y lo hicieron a través de un juego sagrado. Un simple tablero de nueve casillas... pero sus jugadas tenían el poder de moldear galaxias.

Con el tiempo, los titanes desaparecieron, dejando su juego como legado, un enigma escondido bajo la apariencia de un simple pasatiempo. Ahora, ustedes han sido elegidos para retomar esta batalla y reclamar el poder de los antiguos titanes.

### ¿Cómo jugar?

Tic-Tac-Toe es un juego simple en su superficie:

- Dos jugadores se turnan para colocar sus símbolos (X u O) en un tablero de 3x3.
- El objetivo es formar una línea de tres símbolos horizontales, verticales o diagonales.
- Las casillas se seleccionan especificando la columna y la fila
- ¡Pero cuidado! Cada movimiento tiene repercusiones cósmicas.

### Instrucciones

1. Clona el repositorio y extraelo
2. Ejecuta el juego usando `python tic-tac-toe.py` dentro del directorio donde lo guardaste
3. Juega con estrategia, cada casilla cuenta!

---
## Librerías utilizadas

### Os

Ver [documentación](https://www.w3schools.com/python/module_os.asp).

Esta librería fue utilizada para borrar la terminal y crear une espacio en blanco. 

```python
os.system('clear')
```

Con este método se logra escribir un comando a la terminal.

### Platform

Ver [documentación](https://docs.python.org/es/3/library/platform.html).

Esta librería fue utilizada para reconocer en qué sistema operar se está ejecutando el código y decidir si se utilizará el comando `clear` o `cls`.

```python
platform.system()
```

Fue el método utilizado.

### Time

Ver [documentación](https://docs.python.org/3/library/time.html).

Esta librería fue utilizada para esperar cierto tiempo entre impresión de carácteres y generar el efecto de videojuego.

```python
time.sleep(0.1)
```

Fue el método utilizado.

### Random

Ver [documentación](https://www.w3schools.com/python/module_random.asp).

Esta librería fue utlizada para randomizar un mensaje después de cada ronda.

```python
random.random()
```

Fue el método utilizado para lograr esto. 
