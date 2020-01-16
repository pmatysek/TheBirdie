import pygame
from random import randint

BIRD_WIDTH = 53
BIRD_HEIGHT = 46
OBSTACLE_WIDTH = 100


class Bird:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.vertical_speed = 0
        self.falling_parameter = 0.7

        self.images = []
        self.images.append(load_sprite('images/bird1.png', BIRD_WIDTH, BIRD_HEIGHT))
        self.images.append(load_sprite('images/bird2.png', BIRD_WIDTH, BIRD_HEIGHT))
        self.images.append(load_sprite('images/bird3.png', BIRD_WIDTH, BIRD_HEIGHT))
        self.images.append(load_sprite('images/bird4.png', BIRD_WIDTH, BIRD_HEIGHT))

        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def display(self, game_display):
        self.y -= self.vertical_speed
        self.vertical_speed -= self.falling_parameter
        game_display.blit(self.image, (self.x, self.y))

    def check_if_crashed(self, obstacles):
        if self.y > 500:
            return True
        for obstacle in obstacles:
            if obstacle.x < self.x < obstacle.x + OBSTACLE_WIDTH:
                return (self.y < obstacle.y[obstacle.index] - 150) or (self.y > obstacle.y[obstacle.index] - BIRD_HEIGHT)


class Background:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.moving_x = 0
        self.moving_speed = 5
        self.bg1 = None
        self.bg2 = None

    def init(self):
        self.bg1 = load_sprite('images/background1.png', 800, 600)
        self.bg2 = load_sprite('images/background2.png', 800, 600)

    def display(self, game_display):
        game_display.blit(self.bg1, (self.x, self.y))
        game_display.blit(self.bg2, (self.moving_x, self.y))
        game_display.blit(self.bg2, (self.moving_x + 800, self.y))

        self.moving_x -= self.moving_speed
        if self.moving_x == -800:
            self.moving_x = 0


class Obstacle:
    def __init__(self):
        self.x = 800
        self.y = [335, 278, 392]
        self.y2 = 0

        self.moving_speed = 5
        self.image1 = []
        self.image2 = []
        self.index = randint(0, 2)

    def get_height(self):
        return 128 + self.index * 57

    def init(self):
        self.image1.append(load_sprite('images/obstacle3.png', OBSTACLE_WIDTH, 185))
        self.image2.append(pygame.transform.rotate(load_sprite('images/obstacle3.png', OBSTACLE_WIDTH, 185), 180))
        self.image1.append(load_sprite('images/obstacle4.png', OBSTACLE_WIDTH, 242))
        self.image2.append(pygame.transform.rotate(load_sprite('images/obstacle2.png', OBSTACLE_WIDTH, 128), 180))
        self.image1.append(load_sprite('images/obstacle2.png', OBSTACLE_WIDTH, 128))
        self.image2.append(pygame.transform.rotate(load_sprite('images/obstacle4.png', OBSTACLE_WIDTH, 242), 180))

    def display(self, game_display):
        game_display.blit(self.image1[self.index], (self.x, self.y[self.index]))
        game_display.blit(self.image2[self.index], (self.x, self.y2))

        self.x -= self.moving_speed
        if self.x < -OBSTACLE_WIDTH:
            self.x = 800
            self.index = randint(0, 2)


def load_sprite(image, width, heigh):
    picture = pygame.image.load(image)
    return pygame.transform.scale(picture, (width, heigh))


def init_obstacles():
    obstacles = []
    for i in range(0, 2):
        ob = Obstacle()
        ob.x += i * 400
        ob.init()
        obstacles.append(ob)
    return obstacles
