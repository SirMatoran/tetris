import pygame

from piece import Piece
from colors import GREY_BORDER, GREY_BORDER_BACKGROUND, GREY_TEXT, PINK_PIECE, RED_PIECE

DEFAULT_FONT = 'Arial'

def draw_points(screen: pygame.Surface, score: int):
    font20 = pygame.font.SysFont(DEFAULT_FONT, 20)
    txtsurfGameOver = font20.render("Score: " + str(score), True, GREY_TEXT)
    screen.blit(
        txtsurfGameOver,
        (
            screen.get_width() - txtsurfGameOver.get_width() - (screen.get_width() // 20),
            screen.get_height() // 30,
        ),
    )


def draw_piece(screen: pygame.Surface, piece: Piece, SQUARE_SIZE: int):
    positionY = 0
    for line in piece.shape:
        positionX = 0
        for square in line:
            squarePositionY = (piece.positionY + positionY) * SQUARE_SIZE
            if square == 1:
                squarePositionX = (piece.positionX + positionX) * SQUARE_SIZE
                pygame.draw.rect(
                    screen,
                    RED_PIECE,
                    [squarePositionX, squarePositionY, SQUARE_SIZE, SQUARE_SIZE],
                )
                pygame.draw.rect(
                    screen,
                    GREY_BORDER,
                    [squarePositionX, squarePositionY, SQUARE_SIZE, SQUARE_SIZE],
                    1,
                )
            positionX = positionX + 1
        positionY = positionY + 1


def draw_grid(screen: pygame.Surface, grid: [], SQUARE_SIZE: int):
    positionY = 0
    for line in grid:
        squarePositionY = positionY * SQUARE_SIZE
        positionX = 0
        for sqare in line:
            squarePositionX = positionX * SQUARE_SIZE
            color = PINK_PIECE if sqare == 1 else GREY_BORDER_BACKGROUND
            pygame.draw.rect(
                screen,
                color,
                [squarePositionX, squarePositionY, SQUARE_SIZE, SQUARE_SIZE],
                0 if sqare == 1 else 1,  # complete square if there is a piece
            )
            positionX = positionX + 1
        positionY = positionY + 1

def show_game_over_screen(screen: pygame.Surface, SQUARE_SIZE: int):
    font36 = pygame.font.SysFont(DEFAULT_FONT, 36)
    font16 = pygame.font.SysFont(DEFAULT_FONT, 16)
    txtsurfGameOver = font36.render("Game Over", True, RED_PIECE)
    txtsurfPressSpace = font16.render(
        "Press SPACE for restart the game", True, GREY_TEXT
    )
    screen.blit(
        txtsurfGameOver,
        (
            screen.get_width() // 2 - txtsurfGameOver.get_width() // 2,
            screen.get_height() // 3 - txtsurfGameOver.get_height() // 2,
        ),
    )
    screen.blit(
        txtsurfPressSpace,
        (
            screen.get_width() // 2 - txtsurfPressSpace.get_width() // 2,
            (screen.get_height() + SQUARE_SIZE * 3) // 3 - txtsurfPressSpace.get_height() // 2,
        ),
    )