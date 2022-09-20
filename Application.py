if __name__ == '__main__':
    import random
    import pygame


    pygame.init()


    Window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    Title = pygame.display.set_caption('PingPong')

    Clock = pygame.time.Clock()
    FPS = 60

    Background = pygame.transform.scale(pygame.image.load('Application.jpg'), (1920, 1080))

    ball_image = pygame.transform.scale(pygame.image.load('ball.png'), (100, 100))

    player1_image = pygame.Surface((30, 250))
    player1_image.fill((255, 0, 0))

    player2_image = pygame.Surface((30, 250))
    player2_image.fill((0, 0, 255))

    start = False
    player1_score = 0
    player2_score = 0
    scores = pygame.font.SysFont('Arial', 48)


    class Player(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int, image: object) -> None:
            self.image = image

            self.rect = image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.speed = 10

        def update(self) -> None:
            Window.blit(self.image, (self.rect.x, self.rect.y))

    
    class Ball(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int, image: object) -> None:
            self.image = image

            self.rect = image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.dx = 0
            self.dy = 0

            self.speed = 10

        def update(self) -> None:
            Window.blit(self.image, (self.rect.x, self.rect.y))
    
    ball = Ball(900, 500, ball_image)
    player1 = Player(100, 400, player1_image)
    player2 = Player(1800, 400, player2_image)


    while True:
        pygame.display.update()
        Window.blit(Background, (0, 0))
        Window.blit(scores.render(f'{player1_score} : {player2_score}', True, (255, 255, 255)), (Window.get_height() / 2 + 375, 10))
        player1.update()
        player2.update()

        if start:
            ball.update()

            if pygame.sprite.collide_rect(player1, ball):
                ball.dx = ball.speed

                if random.randint(0, 1):
                    ball.dy = ball.speed
                else:
                    ball.dy = -ball.speed

                ball.speed += 1
            if pygame.sprite.collide_rect(player2, ball):
                ball.dx = -ball.speed

                if random.randint(0, 1):
                    ball.dy = ball.speed
                else:
                    ball.dy = -ball.speed

                ball.speed += 1

            if ball.rect.y >= 980:
                ball.dy = -ball.speed
            if ball.rect.y <= 100:
                ball.dy = ball.speed
            if ball.rect.x >= 1920:
                ball = Ball(900, 500, ball_image)
                start = False
                player2_score += 1
            if ball.rect.x <= 0:
                ball = Ball(900, 500, ball_image)
                start = False
                player1_score += 1

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                player1.rect.y -= player1.speed
            if keys[pygame.K_s]:
                player1.rect.y += player1.speed
            if keys[pygame.K_UP]:
                player2.rect.y -= player2.speed
            if keys[pygame.K_DOWN]:
                player2.rect.y += player2.speed

            ball.rect.x += ball.dx
            ball.rect.y += ball.dy
        
            Clock.tick(FPS)
        else:
            Window.blit(scores.render('Press Enter to start game.', True, (255, 255, 255)), (Window.get_height() / 2 + 200, Window.get_height() - 100))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                if random.randint(0, 1):
                    ball.dx += 10
                    start = True
                else:
                    ball.dx -= 10
                    start = True


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()