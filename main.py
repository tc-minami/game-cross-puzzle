import pygame
from pygame.locals import *
import sys
from logging import getLogger

logger = getLogger(__name__)
isWindowActive = True

cellStartPos = (50, 50)
cellSize = 50
cellColorOn = (150, 50, 50)
cellColorOff = (50, 50, 50)
maxRow = 10
maxColumn = 10

cellStatus = [[False for row in range(maxRow)] for col in range(maxColumn)]

# Main loop
def main():
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode( \
        (cellSize * maxRow + cellStartPos[0] * 2, cellSize * maxColumn  + cellStartPos[1] * 2))
    pygame.display.set_caption("タイトルだよ")

    isWindowActive = True
    while(isWindowActive):
        # screen.fill((255, 63, 10))
        pygame.display.update()

        # for row in range(maxRow):
        #     for col in range(maxColumn):
        #         drawBox((row + col) % 2 == 0, screen, row, col)
        #         # drawBox(cellStatus[row][col], screen, row, col)

        drawAllCells(screen)
        drawAllBorders(screen)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN: updateClickEvents(event)
            if event.type == QUIT:
                pygame.quit()
                isWindowActive = False
                # sys.exit()

        # for event in pygame.event.get():
        #     if event.type == MOUSEBUTTONDOWN:
        #         x = event.pos[0]
        #         # logger.debug("Pressed At ${x}")
        #         print("Pos = " + str(event.pos[0]) + "/" + str(event.pos[1]))
        #         # onClick(event.pos.x, event.pos.y)
        #
        #     if event.type == QUIT:
        #         pygame.quit()
        #         sys.exit()

def drawBox(isOn, screen, rowIndex, colIndex):
    pygame.draw.rect(screen,\
        cellColorOn if isOn else cellColorOff,\
        Rect(cellStartPos[0] + rowIndex * cellSize,\
            cellStartPos[1] + colIndex * cellSize,\
            cellSize,\
            cellSize))

def drawAllCells(screen):
    for row in range(maxRow):
        for col in range(maxColumn):
            drawBox(cellStatus[row][col], screen, row, col)
            # drawBox((row + col) % 2 == 0, screen, row, col)


def drawAllBorders(screen):
    lineColor = (30, 30, 30)
    start = (0, 0)
    end = (0, 0)
    lineSize = 3

    for row in range(maxRow + 1):
        start = (cellStartPos[0] + (cellSize * row), cellStartPos[1])
        end = (start[0], start[1] + (cellSize * maxColumn))
        pygame.draw.line(screen, lineColor, start, end, lineSize)

    for col in range(maxColumn + 1):
        start = (cellStartPos[0], cellStartPos[1] + (cellSize * col))
        end = (start[0]+ (cellSize * maxRow), start[1])
        pygame.draw.line(screen, lineColor, start, end, lineSize)

def updateClickEvents(event):
    if event.type == MOUSEBUTTONDOWN:
        if(event.button == 1): onClickLeft(event.pos[0], event.pos[1])
        if(event.button == 3): onClickRight(event.pos[0], event.pos[1])

def onClickLeft(x, y):
    print("Click Left : Pos = " + str(x) + "/" + str(y))

    cellPos = getClickCell(x, y)
    if cellPos != None:
        __revertCellStatus(cellPos[0], cellPos[1])
        __revertCellStatus(cellPos[0] - 1, cellPos[1])
        __revertCellStatus(cellPos[0] + 1, cellPos[1])
        __revertCellStatus(cellPos[0], cellPos[1] - 1)
        __revertCellStatus(cellPos[0], cellPos[1] + 1)

    print("Click Left : Cell = " + str(cellPos))

def onClickRight(x, y):
    print("Click Right : Pos = " + str(x) + "/" + str(y))

def getClickCell(x, y):
    if x < cellStartPos[0] and y < cellStartPos[1]: return None

    cellPos = \
        ((int)((x - cellStartPos[0]) / cellSize), \
        (int)((y - cellStartPos[1]) / cellSize))

    if cellPos[0] < 0 \
        or cellPos[0] >= maxRow \
        or cellPos[1] < 0 \
        or cellPos[1] >= maxColumn:
            return None

    return cellPos

def __revertCellStatus(x, y):
    if x < 0 or x >= maxRow: return
    if y < 0 or y >= maxColumn: return

    print("Revert Cell : x = " + str(x) + " y = " + str(y))

    cellStatus[x][y] = not(cellStatus[x][y])

if __name__ == "__main__":
    main()
