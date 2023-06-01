import random
import time

import pygame as pg
import pygame.display
import playerClass, backgroundClass, genetic

pg.init()

bots = []
for i in range(10):
    bot = playerClass.Player()
    bot.instructions = [0 for j in range(100)]
    bots.append(bot)

for bot in bots:
    genetic.mutate(bot.instructions)
    print(bot.instructions)

background = backgroundClass.Background()
surface = pg.display.set_mode((512, 384))
width, height = surface.get_size()

walls = [(70, 300), (100, 300), (130, 300), (160, 300), (190, 300), (190, 270), (220, 300), (250, 300)]

events = pg.event.get()


def game():
    running = True
    clock = pg.time.Clock()
    while running:
        dt = clock.tick(60)
        global events
        events = pg.event.get()
        gameStep(dt)
        for event in events:
            if event.type == pg.QUIT:
                running = False


def drawBackground():
    surface.fill(background.color)


def erasePlayer(player):
    pg.draw.rect(surface, background.color, pygame.Rect(player.x, player.y, player.size, player.size))


def drawPlayer(player):
    pg.draw.rect(surface, player.color, pygame.Rect(player.x, player.y, player.size, player.size))


def playerMovement(player):
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                player.yspd = -250

    keys = pg.key.get_pressed()
    if keys[pygame.K_a]:
        player.xspd = -200
    elif keys[pygame.K_d]:
        player.xspd = 200
    else:
        player.xspd = 0


def playerMovementFromInstructions(player):
    inst = player.instructions[player.currInstruction]
    if inst == 1:
        player.xspd = -200
    elif inst == 2:
        player.xspd = 200
    elif inst == 3 and player.grounded:
        player.yspd = -250
        player.grounded = False

    if player.currInstruction < len(player.instructions) - 1:
        player.currInstruction += 1
    else:
        player.currInstruction = 0


def playerHorizontalCollisions(dt, player):
    for wall in walls:
        px = player.x
        wx = wall[0]
        py = player.y
        wy = wall[1]
        wallSize = 30
        if py + player.size > wy and py < wy + wallSize:
            if px + player.size <= wx <= px + player.size + player.xspd * dt / 1000:
                player.x = wx - player.size
                player.xspd = 0

            if px + player.xspd * dt / 1000 <= wx + wallSize <= px:
                player.x = wx + wallSize
                player.xspd = 0


def playerVerticalCollisions(dt, player):
    for wall in walls:
        px = player.x
        wx = wall[0]
        py = player.y
        wy = wall[1]
        wallSize = 30
        if wx <= px + player.size and px <= wx + wallSize:
            if wy <= py + player.size <= wy + wallSize and player.yspd > 0:
                player.y = wy - player.size
                player.yspd = 0
                player.grounded = True


def drawWalls():
    wallColor = (40, 40, 40)
    wallSize = 30
    for wall in walls:
        pg.draw.rect(surface, wallColor, pygame.Rect(wall[0], wall[1], wallSize, wallSize))


def gameStep(dt,):
    drawBackground()
    # playerMovement()
    for player in bots:
        playerMovementFromInstructions(player)
        playerHorizontalCollisions(dt, player)
        playerVerticalCollisions(dt, player)
        player.updatePos(dt)
        player.applyGrav()
        drawPlayer(player)
    drawWalls()

    pygame.display.flip()


game()







