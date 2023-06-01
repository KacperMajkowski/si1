import random


class Player:
    x = 100
    y = 250
    xspd = 0
    yspd = 0
    size = 30

    grounded = False

    grav = 10

    color = (255, 0, 0)

    instructions = [0 for i in range(60)]
    currInstruction = 0

    def applyGrav(self):
        self.yspd += self.grav

    def updatePos(self, dt):
        self.x += self.xspd * dt / 1000
        self.y += self.yspd * dt / 1000

