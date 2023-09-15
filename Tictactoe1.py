"""Tic Tac Toe

Ejercicios

1. Modificar el tamaño, el color de los símbolos "X" y "O" y centrarlos.
2. Validar si una casilla ya se encuentra ocupada.
"""

from turtle import *
from freegames import line


# Define una matriz para representar el estado del tablero.
board = [[' ' for _ in range(3)] for _ in range(3)]


# Define una función para dibujar el tablero de Tictactoe.
def grid():
    """Dibuja el tablero de Tictactoe."""
    line(-67, 200, -67, -200)  # Línea vertical izquierda.
    line(67, 200, 67, -200)    # Línea vertical derecha.
    line(-200, -67, 200, -67)  # Línea horizontal inferior.
    line(-200, 67, 200, 67)    # Línea horizontal superior.


# Define una función para dibujar la "X".
def drawx(x, y):
    """Dibuja la "X" para el jugador."""
    color("purple")  # Modifica el color de la línea.
    width(3)         # Modifica el ancho de la línea.
    """Ajusta las coordenadas para centrar la "X" en el cuadro."""
    x += 16
    y += 16
    line(x, y, x + 100, y + 100)  # Dibuja una línea diagonal (parte superior izquierda a inferior derecha).
    line(x, y + 100, x + 100, y)  # Dibuja una línea diagonal (parte superior derecha a inferior izquierda).
   

# Define una función para dibujar la "O".
def drawo(x, y):
    """Dibuja la "O" para el jugador."""
    color("pink")  # Modifica el color de la línea.
    width(3)       # Modifica el ancho de la línea.
    """Ajusta las coordenadas para centrar la "O" en el cuadro."""
    x += 67          
    y += 67          
    up()             
    goto(x, y - 55)  # Mueve el cursor a la posición central del círculo.
    down()           
    circle(55)  # Dibuja un círculo de radio 55.


# Define una función para redondear un valor a la cuadrícula con un tamaño de 133.
def floor(value):
    """Redondea el valor hacia abajo a la cuadrícula con un tamaño de 133."""
    return ((value + 200) // 133) * 133 - 200


# Inicializa el estado del juego con el jugador 0 (X).
state = {'player': 0}


# Crea una lista de funciones de dibujo para los jugadores (X y O).
players = [drawx, drawo]


def is_valid_move(row, col):
    """Verifica si una casilla es válida y no está ocupada."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


# Define una función para manejar el evento de hacer clic en la pantalla.
def tap(x, y):
    """Dibuja una X o una O en el cuadro donde se hizo clic."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    """Calcula la fila y columna correspondientes a la casilla clicada."""
    row = int((y + 200) // 133)
    col = int((x + 200) // 133)
    if is_valid_move(row, col):
        draw = players[player]
        draw(x, y)
        update()
        board[row][col] = 'X' if player == 0 else 'O'
        state['player'] = 1 - player  # Alterna al siguiente jugador



# Configura la ventana Turtle y dibuja el tablero inicial.
setup(420, 420, 370, 0)  # Configura el tamaño de la ventana y su posición.
hideturtle()             # Oculta el cursor de Turtle.
tracer(False)            # Desactiva la animación.
grid()                   # Dibuja el tablero.
update()                 # Actualiza la pantalla.


# Asocia la función 'tap' al evento de clic en la pantalla.
onscreenclick(tap)


# Finaliza el programa cuando se cierra la ventana.
done()