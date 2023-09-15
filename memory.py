"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

# Se importan las librerías necesarias para el funcionamiento del programa.

import random as rd
import turtle as tt
import freegames as fg

# Se definen las variables necesarias para el funcionamiento del programa.

car = fg.path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0

# Dibuja un cuadrado en la posición (x, y).


def square(x, y):
    tt.up()
    tt.goto(x, y)
    tt.down()
    tt.color('black', 'white')
    tt.begin_fill()
    for count in range(4):
        tt.forward(50)
        tt.left(90)
    tt.end_fill()


# Convierte las coordenadas (x, y) en un índice de mosaico.

def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Convierte el índice de mosaico en coordenadas (x, y).


def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Actualiza el marcador y los mosaicos ocultos basados en el toque.


def tap(x, y):
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Contador de taps

    global taps
    taps += 1  # Se incrementa el número de taps
    print("Taps: ", taps)  # Se imprime el número de taps

    # Checar si todos los mosaicos están descubiertos

    if True not in hide:
        print("Todos los mosaicos han sido descubiertos")


# Dibuja el tablero.

def draw():
    tt.clear()
    tt.goto(0, 0)
    tt.shape(car)
    tt.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        tt.up()
        tt.goto(x + 2, y)
        tt.color('black')
        tt.write(tiles[mark], font=('Arial', 30, 'normal'))

    tt.update()
    tt.ontimer(draw, 100)

# Inicializa los mosaicos ocultos.


rd.shuffle(tiles)

# Se define el tamaño de la ventana

tt.setup(420, 420, 370, 0)

# Se define la imagen del fondo de pantalla

tt.addshape(car)

# Se oculta la tortuga

tt.hideturtle()

# Desactiva la animación de la tortuga

tt.tracer(False)

# Se define la función que se ejecuta al hacer click en la ventana

tt.onscreenclick(tap)

# Se ejecuta la función draw para que se dibuje el tablero

draw()

# Se ejecuta el juego

tt.done()
