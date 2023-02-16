# 1. clasa z graczami
# 2. ruch i pilka
# 3. pole gry
# 4. okno - poczatek i koniec gry

import pygame, sys
from ja import Ja

class Game(object):

    def __init__(self):
        #config
        self.tps_max = 500.0  # ticks per second - szybkość poruszania sie obiektu

        #initialization
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Ping-Pong')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player1 = Ja(self)
        self.player2 = Ja(self)

        while True:
            # handle events - obsluga wyjatkow
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # ticking - rownanie szybkosci obiektu, klatki na sekunde (fps)
            self.tps_delta += self.tps_clock.tick() / 1000.0  # dlugosc pracy programu - konwersja na sekundy
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drawing
            self.screen.fill((0, 0, 0))  # koloruje ekran na czarno, bez tego przesuwajacy sie obiekt pozostawia slad
            self.draw()
            pygame.display.flip()

    def tick(self):
        # checking input - ruch obiektu, x - os prawo-lewo, y - os gora-dol
        self.player1.tick()
        keys1 = pygame.key.get_pressed()
        self.player2.tick()
        keys2 = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     self.player1.y -= 1
        # if keys[pygame.K_s]:
        #     self.player1.y += 1

    def draw(self):
        self.player1.draw()
        self.player2.draw()
        # drawing
        # self.player1 = pygame.Rect(10, 300, 20, 100)
        # pygame.draw.rect(self.screen, (225, 225, 225), pygame.Rect(10, 300, 20, 100))

if __name__ == "__main__":
    Game()



# w pygame jest podwojne buforowanie czyli sa jakby dwie kartki
# 1. niewidoczna dla uzytkowanika na ktorej sie rysuje cos co chcemy
# 2. widoczna dla uzytkownika
# 3. musimy wpisac komende zeby kartki zamienily sie miejscami czyli po narysowaniu obiektu
# ma ukazac sie kartka 1 z obiektem , a pusta kartka 2 zostaje schowana
# komenda zeby zupdatowac obraz to pygame.display.flip()


# class User:
#     def player1(self, color, lenght, width, move):
#         self.color = color
#         self.lenght = lenght
#         self.width = width
#
#
# player1 = User()
# player2 = User()


