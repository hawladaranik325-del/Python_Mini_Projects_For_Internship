import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🧱 Brick Breaker Game by SK Sahil")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW= (255, 255, 0)

# Clock
clock = pygame.time.Clock()

# Paddle setup
paddle_width = 100
paddle_height = 10
paddle = pygame.Rect(WIDTH//2 - paddle_width//2, HEIGHT - 30, paddle_width, paddle_height)
paddle_speed = 7

# Ball setup
ball = pygame.Rect(WIDTH//2 - 8, HEIGHT//2, 16, 16)
ball_speed = [4, -4]

# Brick setup
brick_rows = 5
brick_cols = 8
brick_width = 70
brick_height = 20
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + 5) + 35
        brick_y = row * (brick_height + 5) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Score
score = 0
font = pygame.font.SysFont("Arial", 25)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.bottom >= HEIGHT:
        running = False  # Game Over

    # Paddle collision
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Brick collision
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed[1] *= -1
            score += 10
            break

    # Draw everything
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, YELLOW, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Score display
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Win condition
    if not bricks:
        win_text = font.render("🎉 You Win!", True, GREEN)
        screen.blit(win_text, (WIDTH//2 - 60, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    pygame.display.flip()
    clock.tick(60)

# Game Over screen
screen.fill(BLACK)
msg = font.render(f"Game Over! Final Score: {score}", True, WHITE)
screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
