import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Ping Pong Game')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)


font = pygame.font.Font(None, 50)


ball = pygame.Rect(320, 240, 20, 20)
ball_speed = [3, 3]

player_paddle = pygame.Rect(20, 200, 10, 80)
ai_paddle = pygame.Rect(610, 200, 10, 80)

paddle_speed = 5

player_score = 0
ai_score = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_paddle.bottom < 480:
        player_paddle.y += paddle_speed

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= 480:
        ball_speed[1] = -ball_speed[1]
    
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed[0] = -ball_speed[0]

    if ai_paddle.centery < ball.centery and ai_paddle.bottom < 480:
        ai_paddle.y += paddle_speed
    if ai_paddle.centery > ball.centery and ai_paddle.top > 0:
        ai_paddle.y -= paddle_speed

    if ball.left <= 0:
        ai_score += 1  # AI scores
        ball.x, ball.y = 320, 240
        ball_speed[0] = -ball_speed[0]
    if ball.right >= 640:
        player_score += 1  # Player scores
        ball.x, ball.y = 320, 240
        ball_speed[0] = -ball_speed[0]

    
    screen.fill(BLACK)

    # Draw paddles, ball, and the center line
    pygame.draw.rect(screen, BLUE, player_paddle)
    pygame.draw.rect(screen, RED, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (320, 0), (320, 480))

    
    player_text = font.render(f'{player_score}', True, BLUE)
    screen.blit(player_text, (30, 10))

    ai_text = font.render(f'{ai_score}', True, RED)
    screen.blit(ai_text, (580, 10))

    
    pygame.display.flip()

    
    clock.tick(60)

pygame.quit()