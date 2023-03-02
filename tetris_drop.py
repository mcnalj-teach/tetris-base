import random, sys, time, pygame
from pygame.locals import *

FPS = 40
WINDOWWIDTH = 600
WINDOWHEIGHT = 800
BOARDWIDTH = 350
BOARDHEIGHT = 700
PIECESIZE = 35

WHITE = (255, 255,255)
BRIGHTGREEN = (0, 255, 255)
DARKGRAY = (169, 169, 169)
BLACK = (0, 0, 0)
RED = (155, 0, 0)
YELLOW = (155, 155, 0)
LIGHTBLUE = (173, 216, 230)
BLUE = (3, 37, 126)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
PURPLE = (221, 160, 221)
bgColor = DARKGRAY

pygame.init()

FPSCLOCK = pygame.time.Clock()

SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Blocky')

BASICFONT = pygame.font.SysFont('tahoma', 24)

def setCenterThreeDown(pieceX, pieceHeight):
    pieceList = [
        pygame.Rect(pieceX-PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX + PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE)
    ]
    return pieceList

def setCenterThreeLeft(pieceX, pieceHeight):
    pieceList = [
        pygame.Rect(pieceX+PIECESIZE, pieceHeight - PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX, pieceHeight, PIECESIZE, PIECESIZE)
    ]
    return pieceList

def setCenterThreeUp(pieceX, pieceHeight):
    pieceList = [
        pygame.Rect(pieceX+(2*PIECESIZE), pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE)
    ]
    return pieceList

def setCenterThreeRight(pieceX, pieceHeight):
    pieceList = [
        pygame.Rect(pieceX+PIECESIZE, pieceHeight - PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+PIECESIZE, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX+(2*PIECESIZE), pieceHeight, PIECESIZE, PIECESIZE)
    ]
    return pieceList

def setBlock(pieceX, pieceHeight):
    pieceList = [
        pygame.Rect(pieceX, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX + PIECESIZE, pieceHeight, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE),
        pygame.Rect(pieceX + PIECESIZE, pieceHeight + PIECESIZE, PIECESIZE, PIECESIZE)
    ]
    return pieceList

def setPieceList(orientation, pieceX, pieceHeight):
    functionDictionary = {
        "down": {
            "block": setBlock,
            "centerThree": setCenterThreeDown,
        },
        "left": {
            "block": setBlock,
            "centerThree": setCenterThreeLeft,
        },
        "up": {
            "block": setBlock,
            "centerThree": setCenterThreeUp,
        },
        "right": {
            "block": setBlock,
            "centerThree": setCenterThreeRight,
        }
    }
    return functionDictionary[orientation][pieceType](pieceX, pieceHeight)

def rotateClockwise(orientation):
    if orientation == "down":
        return "left"
    elif orientation == "left":
        return "up"
    elif orientation == "up":
        return "right"
    elif orientation == "right":
        return "down"

def drawShape(blockList, color):
    for block in blockList:
        pygame.draw.rect(SCREEN, color, block)

running = True
orientation = "up"
pieceTypes = ["stick", "backwardsEl", "el", "block", "backwardsZ", "centerThree", "z"]
pieceColors = [LIGHTBLUE, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED ]
pieceType = pieceTypes[5]
color = pieceColors[5]
currentRow = 0
pieceHeight = 65 + (currentRow * 35)
pieceX = 230
global blockList
blockList = setPieceList(orientation, pieceX, pieceHeight)
speed = 250

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                orientation = rotateClockwise(orientation)
                blockList  = setPieceList(orientation, pieceX, pieceHeight)
                drawShape(blockList, color)
                pygame.display.update()

    pieceHeight = 50 + (currentRow * 35)
    SCREEN.fill(bgColor)
    pygame.draw.rect(SCREEN, BLACK, (125, 50, BOARDWIDTH, BOARDHEIGHT))
    blockList  = setPieceList(orientation, pieceX, pieceHeight)
    drawShape(blockList, color)
    pygame.display.update()
    pygame.time.wait(speed)
    currentRow = currentRow + 1
    FPSCLOCK.tick(FPS)
