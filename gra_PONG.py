# 1. clasa z graczami
# 2. ruch i pilka
# 3. pole gry
# 4. okno - poczatek i koniec gry

import pygame
pygame.init()

# screen
width = 800
hight = 600
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("PONG")

# configuration
framerate = 500.0           # klatki na sekunde

player_width = 10
player_hight = 100

# game
# player1_direction = 0
# player2_direction = 0
# player1_pos = 270
# player2_pos = 270
# player_speed = 5
# ball_speed_x = 1
# ball_speed_y = 1
# ball_pos_x = 290
# ball_pos_y = 290
ball_radius = 10
score_font = pygame.font.SysFont("comicsans", 50)
winning_score = 10

class Player:
    player_speed = 2

    def __init__(self, x, y, width, hight):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.hight = hight

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.hight))

    def move(self, up=True):
        if up:
            self.y -= self.player_speed
        else:
            self.y += self.player_speed
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    max_vel = 1
    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.max_vel
        self.y_vel = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (25, 25, 255), (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1

def draw(screen, players, ball, player1_score, player2_score):
    screen.fill((0, 0, 0))

    player1_score_text = score_font.render(f'{player1_score}', True, (255, 255, 255))
    player2_score_text = score_font.render(f'{player2_score}', True, (255, 255, 255))
    screen.blit(player1_score_text, (width // 4 - player1_score_text.get_width() // 2, 20))
    screen.blit(player2_score_text, (width * (3/4) - player2_score_text.get_width() // 2, 20))

    for player in players:
        player.draw(screen)

    for i in range(10, hight, hight//40):
        if i % 2 == 1:
            continue
        pygame.draw.rect(screen, (255, 255, 255), (width//2 - 1, i, 1, hight//40))

    ball.draw(screen)
    pygame.display.flip()

def collision(ball, player1, player2):
    if ball.y + ball_radius >= hight:
        ball.y_vel *= -1
    elif ball.y - ball_radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= player1.y and ball.y <= player1.y + player_hight:
            if ball.x - ball_radius <= player1.x + player_width:
                ball.x_vel *= -1

                middle_y = player1.y + player1.hight / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (player1.hight / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else:
        if ball.y >= player2.y and ball.y <= player2.y + player_hight:
            if ball.x + ball_radius >= player2.x:
                ball.x_vel *= -1

                middle_y = player2.y + player2.hight / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (player2.hight / 2) / ball.max_vel
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel

def player_movement(keys, player1, player2):
    if keys[pygame.K_w] and player1.y - player1.player_speed >= 0:
        player1.move(up=True)
    if keys[pygame.K_s] and player1.y + player1.player_speed + player1.hight <= hight:
        player1.move(up=False)

    if keys[pygame.K_UP] and player2.y - player2.player_speed >= 0:
        player2.move(up=True)
    if keys[pygame.K_DOWN] and player2.y + player2.player_speed + player2.hight <= hight:
        player2.move(up=False)

def main():
    run = True
    timer = pygame.time.Clock()  # obiekt sledzacy czas (tick), ile milisekund uplynelo od poprzedniego wywolania
    player1 = Player(10, hight // 2 - player_hight // 2, player_width, player_hight)
    player2 = Player(width - 10 - player_width, hight // 2 - player_hight // 2, player_width, player_hight)
    ball = Ball(width // 2, hight // 2, ball_radius)

    player1_score = 0
    player2_score = 0

    while run:
        timer.tick(framerate)
        draw(screen, [player1, player2], ball, player1_score, player2_score)
        # handle events - obsluga wyjatkow
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # x - krzyzyk w gornym rogu okna oznacza quit
                run = False
                break
        keys = pygame.key.get_pressed()
        player_movement(keys, player1, player2)

        ball.move()
        collision(ball, player1, player2)

        if ball.x < 0:
            player2_score += 1
            ball.reset()
        elif ball.x > width:
            player1_score += 1
            ball.reset()

        won = False
        if player1_score >= winning_score:
            won = True
            win_text = "Player1 wygrales!"
        elif player2_score >= winning_score:
            won = True
            win_text = "Player2 wygrales!"

        if won:
            text = score_font.render(win_text, True, (255,255,255))
            screen.blit(text, (width//2 - text.get_width()//2, hight//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            player1.reset()
            player2.reset()
            player1 = 0
            player2 = 0

    pygame.quit()

if __name__ == "__main__":
    main()


        # ksztalty na ekranie - 2 prostokaty i kolo

        # player1 = pygame.draw.rect(screen, (255, 255, 255), [10, player1_pos, 10, 60])
        # player2 = pygame.draw.rect(screen, (255, 255, 255), [580, player2_pos, 10, 60])
        # ball = pygame.draw.circle(screen, (25, 25, 255), [ball_pos_x, ball_pos_y], 10)
        #
        # ball_pos_x += ball_speed_x
        # ball_pos_y += ball_speed_y
        #
        # if ball_pos_x <= 0 or ball_pos_x >= 600:
        #     ball_speed_x *= -1
        # if ball_pos_y <= 0 or ball_pos_y >= 600:
        #     ball_speed_y *= -1


        #
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player1_pos -= 1
        # if keys[pygame.K_s]:
        #     player1_pos += 1
        # if keys[pygame.K_UP]:
        #     player2_pos -= 1
        # if keys[pygame.K_DOWN]:
        #     player2_pos += 1

        # player1_pos += 1 * player1_direction
        # player2_pos += 1 * player2_direction
