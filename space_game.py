import pygame, random, sys

# Initialize
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✈️ Space Shooter by Anik Hawladar")

# Colors
WHITE = (255,255,255)
RED   = (255,0,0)
BLUE  = (0,150,255)
YELLOW= (255,255,0)
BLACK = (0,0,0)

# Clock
clock = pygame.time.Clock()

# Player
player = pygame.Rect(WIDTH//2 - 25, HEIGHT-80, 50, 40)
player_speed = 6

# Bullets
bullets = []
bullet_speed = 7

# Enemies
enemies = []
enemy_speed = 3
enemy_spawn_delay = 30
frame_count = 0

# Score
score = 0
font = pygame.font.SysFont("Arial", 28)

# Game Loop
running = True
while running:
    screen.fill((10,10,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and player.left > 0: player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH: player.x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) == 0 or bullets[-1].y < HEIGHT-200:
            bullets.append(pygame.Rect(player.centerx-2, player.y, 5, 10))

    # Bullets
    for b in bullets[:]:
        b.y -= bullet_speed
        if b.y < 0: bullets.remove(b)

    # Enemies
    frame_count += 1
    if frame_count % enemy_spawn_delay == 0:
        x = random.randint(0, WIDTH-40)
        enemies.append(pygame.Rect(x, -40, 40, 40))

    for e in enemies[:]:
        e.y += enemy_speed
        if e.y > HEIGHT: enemies.remove(e)

    # Collisions
    for e in enemies[:]:
        for b in bullets[:]:
            if e.colliderect(b):
                enemies.remove(e)
                bullets.remove(b)
                score += 10
                break
        if e.colliderect(player):
            running = False

    # Draw
    pygame.draw.rect(screen, BLUE, player)
    for b in bullets: pygame.draw.rect(screen, YELLOW, b)
    for e in enemies: pygame.draw.rect(screen, RED, e)

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Game Over
screen.fill(BLACK)
msg = font.render(f"Game Over! Final Score: {score}", True, WHITE)
screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()  
