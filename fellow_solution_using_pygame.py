# Initialize pygame
import pygame

pygame.init()

# Constants

WIDTH, HEIGHT = 800, 600

BALL_SPEED = [4, -4]

PADDLE_SPEED = 7

BRICK_ROWS, BRICK_COLS = 5, 10

BRICK_WIDTH, BRICK_HEIGHT = 75, 30

# Colors

WHITE = (255, 255, 255)

RED = (200, 50, 50)

BLUE = (50, 50, 200)

# Screen setup

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Breakout Game")

# Ball setup

ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)

ball_speed = BALL_SPEED[:]

# Paddle setup

paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 30, 120, 10)

# Bricks setup

bricks = [pygame.Rect(c * (BRICK_WIDTH + 5) + 35, r * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)

          for r in range(BRICK_ROWS) for c in range(BRICK_COLS)]

# Game loop

running = True

while running:

    screen.fill(WHITE)

    # Event handling

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Paddle movement

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-PADDLE_SPEED, 0)

    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(PADDLE_SPEED, 0)

    # Ball movement

    ball.move_ip(ball_speed[0], ball_speed[1])

    # Ball collision with walls

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddle

    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Ball collision with bricks

    for brick in bricks[:]:

        if ball.colliderect(brick):
            bricks.remove(brick)

            ball_speed[1] = -ball_speed[1]

            break

    # Ball out of bounds

    if ball.bottom >= HEIGHT:
        running = False

    # Drawing elements

    pygame.draw.rect(screen, BLUE, paddle)

    pygame.draw.ellipse(screen, RED, ball)

    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    pygame.display.flip()

    pygame.time.delay(15)

pygame.quit()