"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(6)
    margin = 22
    line(x + margin, y + margin, x + 133 - margin, y + 133 - margin)
    line(x + margin, y + 133 - margin, x + 133 - margin, y + margin)


def drawo(x, y):
    """Draw O player."""
    color('red')
    width(6)
    up()
    goto(x + 67, y + 22)
    down()
    circle(45)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0, 'board': {}, 'game_over': False}
players = [drawx, drawo]


def winner(board, player):
    """Return True when player has completed a row, column, or diagonal."""
    lines = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    return any(all(board.get(cell) == player for cell in line) for line in lines)


def finish(message):
    """Finish the game and display its result."""
    state['game_over'] = True
    title('Tic Tac Toe - ' + message)
    print(message)


def tap(x, y):
    """Draw X or O in tapped square."""
    if state['game_over'] or not (-200 <= x < 200 and -200 <= y < 200):
        return

    column = int((x + 200) // 133)
    row = int((y + 200) // 133)
    cell = (column, row)

    if cell in state['board']:
        title('Tic Tac Toe - That square is already occupied')
        return

    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    state['board'][cell] = player
    update()

    symbol = 'X' if player == 0 else 'O'
    if winner(state['board'], player):
        finish(symbol + ' wins!')
    elif len(state['board']) == 9:
        finish('It is a tie!')
    else:
        state['player'] = not player
        next_symbol = 'X' if state['player'] == 0 else 'O'
        title('Tic Tac Toe - Turn: ' + next_symbol)


setup(420, 420, 370, 0)
title('Tic Tac Toe - Turn: X')
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
