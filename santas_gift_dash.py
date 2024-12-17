import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Initialize the Mixer for Sound
pygame.mixer.init()

# Game Window Settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Santa's Gift Dash")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

# Load Images
santa_img = pygame.image.load("assets/images/santa.png").convert_alpha()
player_img = pygame.image.load("assets/images/player.png").convert_alpha()
gift_img = pygame.image.load("assets/images/gift.png").convert_alpha()
grinch_img = pygame.image.load("assets/images/grinch.png").convert_alpha()
background_img = pygame.image.load("assets/images/background.png").convert()
obstacles_img = pygame.image.load("assets/images/obstacles.png").convert_alpha()

# Resize Images
santa_img = pygame.transform.scale(santa_img, (80, 80))
player_img = pygame.transform.scale(player_img, (60, 100))
gift_img = pygame.transform.scale(gift_img, (40, 40))
grinch_img = pygame.transform.scale(grinch_img, (60, 60))
obstacles_img = pygame.transform.scale(obstacles_img, (60, 60))

# Load Background Music
pygame.mixer.music.load("assets/sounds/festive_theme.mp3")
pygame.mixer.music.set_volume(0.5)  # Adjust background music volume
pygame.mixer.music.play(-1)  # Loop music indefinitely

# Clock and Game Variables
clock = pygame.time.Clock()
lives = 10
score = 0
game_time = 600  # 10 minutes
start_time = time.time()
pause = False

# Player Variables
player_x = 100
player_y = SCREEN_HEIGHT - 150
player_speed = 7
player_jump = False
gravity = 1
y_velocity = 0

# Santa Variables
santa_x = SCREEN_WIDTH - 100
santa_y = SCREEN_HEIGHT - 400
gift_drop_timer = 0
gifts = []

# Obstacles Variables
obstacle_spawn_timer = 0
obstacles = []

# Functions
def display_text(text, x, y, color=BLACK, size="small"):
    """Render and display text on the screen."""
    if size == "small":
        txt_surface = font.render(text, True, color)
    else:
        txt_surface = big_font.render(text, True, color)
    screen.blit(txt_surface, (x, y))

def spawn_gift():
    """Spawn a new gift below Santa."""
    return {"x": santa_x + 20, "y": santa_y}

def spawn_obstacle():
    """Spawn a new obstacle at the right edge."""
    return {"x": SCREEN_WIDTH, "y": SCREEN_HEIGHT - 150}

def end_screen(message):
    """Display the end screen."""
    screen.fill(WHITE)
    display_text(message, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, RED, "big")
    display_text("Press R to Play Again", SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50, BLACK)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                reset_game()
                return

def reset_game():
    """Reset game variables to start over."""
    global score, lives, santa_x, gifts, obstacles, start_time
    score = 0
    lives = 10
    santa_x = SCREEN_WIDTH - 100
    gifts.clear()
    obstacles.clear()
    start_time = time.time()

# Main Game Loop
running = True
reset_game()

while running:
    current_time = int(game_time - (time.time() - start_time))
    if current_time <= 0:
        end_screen("YOU WON!")
    screen.blit(background_img, (0, 0))  # Draw Background

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pause = not pause

    # Pause Menu
    if pause:
        display_text("PAUSED", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, RED, "big")
        pygame.display.flip()
        continue

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 60:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not player_jump:
        player_jump = True
        y_velocity = -12

    # Gravity
    if player_jump:
        player_y += y_velocity
        y_velocity += gravity
        if player_y >= SCREEN_HEIGHT - 150:
            player_y = SCREEN_HEIGHT - 150
            player_jump = False

    # Santa and Gift Logic
    santa_x -= 5
    if santa_x < -80:
        santa_x = SCREEN_WIDTH - 100
    gift_drop_timer += 1
    if gift_drop_timer > 120:
        gifts.append(spawn_gift())
        gift_drop_timer = 0
    for gift in gifts[:]:
        gift["y"] += 3
        if player_x < gift["x"] < player_x + 60 and player_y < gift["y"] < player_y + 100:
            score += 10
            gifts.remove(gift)
        elif gift["y"] > SCREEN_HEIGHT:
            gifts.remove(gift)
            lives -= 1

    # Obstacles Logic
    obstacle_spawn_timer += 1
    if obstacle_spawn_timer > 150:
        obstacles.append(spawn_obstacle())
        obstacle_spawn_timer = 0
    for obstacle in obstacles[:]:
        obstacle["x"] -= 8
        if player_x < obstacle["x"] < player_x + 60 and player_y == SCREEN_HEIGHT - 150:
            lives -= 1
            obstacles.remove(obstacle)
        if obstacle["x"] < -60:
            obstacles.remove(obstacle)

    # Draw Game Elements
    screen.blit(santa_img, (santa_x, santa_y))
    screen.blit(player_img, (player_x, player_y))
    for gift in gifts:
        screen.blit(gift_img, (gift["x"], gift["y"]))
    for obstacle in obstacles:
        screen.blit(obstacles_img, (obstacle["x"], obstacle["y"]))

    # HUD Display
    display_text(f"Score: {score}", 10, 10, BLACK)
    display_text(f"Lives: {lives}", SCREEN_WIDTH - 150, 10, BLACK)
    display_text(f"Time: {current_time}", SCREEN_WIDTH // 2 - 50, 10, BLACK)

    # Game Over Condition
    if lives <= 0:
        end_screen("YOU LOST!")

    # Update Display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
