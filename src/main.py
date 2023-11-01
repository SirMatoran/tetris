import pygame
import random

from piece import Piece
from shapes import PIECE_SHAPES
from screen import draw_grid, draw_piece, draw_points, show_game_over_screen

SQUARES_QUANTITY_IN_HEIGHT = 20
SQUARES_QUANTITY = 12
WIDTH = 480
SQUARE_SIZE = WIDTH / SQUARES_QUANTITY
HEIGHT = SQUARES_QUANTITY_IN_HEIGHT * SQUARE_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

MOVE_DOWN_AUTO = pygame.event.custom_type()
pygame.time.set_timer(MOVE_DOWN_AUTO, 1000)

piesa = Piece([[1, 1], [1, 1]], 0, 0, False)
grid = [[0 for _ in range(SQUARES_QUANTITY)] for _ in range(SQUARES_QUANTITY_IN_HEIGHT)]
gameOver = False
points = 0


def calc_piece_widht():
    return len(piesa.shape[0])


def calc_piece_height():
    return len(piesa.shape)


def check_colision(directionX: int, directionY: int):
    positionY = piesa.positionY
    for pieceLine in piesa.shape:
        positionX = piesa.positionX
        for squareValue in pieceLine:
            if (directionX < 0 and piesa.positionX == 0) or (
                directionX > 0
                and piesa.positionX == (SQUARES_QUANTITY - calc_piece_widht())
            ):
                return True

            if directionY == 1 and piesa.positionY == (
                SQUARES_QUANTITY_IN_HEIGHT - calc_piece_height()
            ):
                piesa.blocked = True
                return True

            if (
                squareValue == 1
                and grid[positionY + directionY][positionX + directionX] == 1
            ):
                if directionY == 1:
                    piesa.blocked = True
                return True
            positionX = positionX + 1

        positionY = positionY + 1
    return False


def check_shape_colision(shape: []):
    positionY = piesa.positionY
    for shapeLine in shape:
        positionX = piesa.positionX
        for shapeSquare in shapeLine:
            # sometimes the shape go out of matix range
            try:
                if shapeSquare == 1 and grid[positionY][positionX] == 1:
                    return True
            except:
                pass
            positionX += 1
        positionY += 1
    return False


def update_piece_position(x: int, y: int):
    if piesa.blocked == False and check_colision(x, y) == False:
        piesa.positionX = piesa.positionX + x
        piesa.positionY = piesa.positionY + y


def move_piece_to_grid():
    positionY = piesa.positionY
    for pieceLine in piesa.shape:
        positionX = piesa.positionX
        for pieceSquare in pieceLine:
            if grid[positionY][positionX] == 0:
                grid[positionY][positionX] = pieceSquare
            positionX += 1
        positionY += 1


def get_random_Shape():
    return PIECE_SHAPES[random.choice(range(len(PIECE_SHAPES)))]


def generate_new_piece():
    global piesa
    piesa = Piece(get_random_Shape(), 0, 0, False)


def turn_shape():
    global piesa
    linesQuantity = len(piesa.shape)
    columnsQuantity = len(piesa.shape[0])
    newShape = [[0 for _ in range(linesQuantity)] for _ in range(columnsQuantity)]

    for i in range(linesQuantity):
        for j in range(columnsQuantity):
            newShape[j][linesQuantity - 1 - i] = piesa.shape[i][j]

    if check_shape_colision(newShape) == False:
        piesa.shape = newShape
        while piesa.positionX + calc_piece_widht() > SQUARES_QUANTITY:
            piesa.positionX -= 1


def remove_complete_lines():
    global points
    for x in range(len(grid)):
        if sum(grid[x]) == SQUARES_QUANTITY:
            grid.pop(x)
            grid.insert(0, [0 for _ in range(SQUARES_QUANTITY)])
            points += 10


def main():
    global piesa, grid, gameOver, running
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and gameOver == False:
                if event.key == pygame.K_LEFT:
                    update_piece_position(-1, 0)
                if event.key == pygame.K_RIGHT:
                    update_piece_position(1, 0)
                if event.key == pygame.K_UP:
                    turn_shape()

            # Move automatic
            if event.type == MOVE_DOWN_AUTO:
                update_piece_position(0, 1)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("#303030")

        # Calculate next step

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            update_piece_position(0, 1)

        # RENDER YOUR GAME HERE
        draw_grid(screen, grid, SQUARE_SIZE)
        draw_piece(screen, piesa, SQUARE_SIZE)
        if piesa.blocked == True and gameOver == False:
            move_piece_to_grid()
            generate_new_piece()
            # Game Over
            if check_shape_colision(piesa.shape):
                gameOver = True

        remove_complete_lines()

        draw_points(screen, points)
        if gameOver == True:
            show_game_over_screen(screen, SQUARE_SIZE)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(30)  # limits FPS to 60
    pygame.quit()


if __name__ == "__main__":
    main()
