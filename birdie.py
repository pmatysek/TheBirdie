import pygame
import game

ANIMATION_SPEED = 5
JUMP_SPEED = 12

score = 0

pygame.init()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('THE BIRDIE')

black = (0, 0, 0)
white = (255, 255, 255)

bird = game.Bird()
background = game.Background()
obstacles = game.init_obstacles()

background.init()
clock = pygame.time.Clock()
crashed = False

x = (display_width * 0.45)
y = (display_height * 0.8)

bird.x = 300
bird.y = 0

index = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.vertical_speed = JUMP_SPEED

    gameDisplay.fill(white)
    background.display(gameDisplay)
    if index == ANIMATION_SPEED:
        bird.update()
        index = 0

    bird.display(gameDisplay)
    for obstacle in obstacles:
        if bird.x == obstacle.x:
            score += 1
        obstacle.display(gameDisplay)

    text_surface = my_font.render(str(score), False, (0, 0, 0))
    gameDisplay.blit(text_surface, (750, 0))

    crashed = bird.check_if_crashed(obstacles)

    pygame.display.update()
    clock.tick(60)
    index += 1

text_surface = my_font.render("GAME OVER", False, (0, 0, 0))
gameDisplay.blit(text_surface, (300, 300))
pygame.display.update()

new_game = False
while not new_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            new_game = True
        if event.type == pygame.KEYDOWN:
            new_game = True

pygame.quit()
quit()
