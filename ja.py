import pygame
from pygame.math import Vector2

class Ja(object):

    def __init__(self, game):
        self.game = game
        self.speed = 1.0
        # self.gravity = 0.1              # wspolczynnik "grawitacji" - opadania

        size = self.game.screen.get_size()      #rozmiar ekranu

        self.pos = Vector2(size[0]/21,size[1]/21)         #vector2 - wektor dwuelementowy, pojawia sie na srodku ekranu /2
        self.vel = Vector2(1,0)
        self.acc = Vector2(0,0)

    def add_force(self, force):
        self.acc += force

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))
        if pressed[pygame.K_UP]:
            self.add_force(Vector2(0, -self.speed))
        if pressed[pygame.K_DOWN]:
            self.add_force(Vector2(0, self.speed))
        if pressed[pygame.K_LEFT]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_RIGHT]:
            self.add_force(Vector2(self.speed, 0))


        # Physics
        self.vel *= 0.01                    # "opór powietrza"
        # self.vel -= Vector2(0,-self.gravity)      # grawitacja, czyli obiekt opada
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     self.player1.y -= 1
        # if keys[pygame.K_s]:
        #     self.player1.y += 1

    def draw(self):

        #base triangle
        # points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]   # wspolrzedne pkt, laczac je powstaje trojkat
        #rotate points
        # angle = self.vel.angle_to(Vector2(0,1))
        # points = [p.rotate(angle) for p in points]
        #fix y axis
        # points = [Vector2(p.x, p.y*-1) for p in points]
        # #add curent position
        # points = [Vector2(self.pos+p*2) for p in points]
        #draw triangle
        # rysowanie poligonów, czyli laczenie pkt, trojkat, *2 zwiekszanie obiektu
        # pygame.draw.polygon(self.game.screen, (255, 0, 255), points)

        rect1 = pygame.Rect(self.pos.x, self.pos.y, 50, 100)
        pygame.draw.rect(self.game.screen, (225, 2, 225), rect1)

        rect2 = pygame.Rect(self.pos.x, self.pos.y, 20, 100)
        pygame.draw.rect(self.game.screen, (255, 255, 255), rect2)

# player1 = Player()
# player2 = Player()