# Example file showing a circle moving on screen
import random

import pygame
from pygame import Surface

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


class Enemy:

    def __init__(self, screen: Surface):
        radius = random.choice([30, 40, 50])
        self.screen = screen
        self.position = pygame.Vector2(
            random.randrange(0 + radius, self.screen.get_width() - radius),
            random.randrange(0 + radius, self.screen.get_height() - radius)
        )
        self.size = radius
        self.color = random.choice(['blue', 'yellow', 'purple'])

        self.speed = 100

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)

    def decrease_position(self, delta_time):
        self.position.y += self.speed * delta_time


class Player:

    def __init__(
            self,
            screen,
            position,
            size,
            color
    ):
        self.screen = screen
        self.position = position
        self.size = size
        self.color = color
        self.player_speed = 600
        self.is_angry = False
        self.angry_timer = 0

    def check_out_of_bounds(self):
        # Limiting our players posision
        if self.position.x < 0:
            self.position.x = self.screen.get_width() + self.size
        if self.position.y < self.size:
            self.position.y = self.size
        if self.position.y > self.screen.get_height() - self.size:
            self.position.y = self.screen.get_height() - self.size
        if self.position.x > self.screen.get_width() + self.size:
            self.position.x = 0

    def draw(self):
        self.check_out_of_bounds()
        if self.is_angry:
            if self.angry_timer < clock.get_rawtime():
                self.become_normal()
        pygame.draw.circle(self.screen, self.color, self.position, self.size)
        self.draw_fake_enemies()

    def move_up(self, delta_time):
        self.position.y -= self.player_speed * delta_time

    def move_down(self, delta_time):
        self.position.y += self.player_speed * delta_time

    def move_right(self, delta_time):
        self.position.x += self.player_speed * delta_time

    def move_left(self, delta_time):
        self.position.x -= self.player_speed * delta_time

    def become_angry(self):
        if self.is_angry:
            return
        self.player_speed = 1200
        self.color = 'red'
        self.size += 20
        self.is_angry = True
        self.angry_timer = clock.get_rawtime() + 5  # From the moment we became angry + 10 seconds

    def become_normal(self):
        if not self.is_angry:
            return
        self.player_speed = 600
        self.color = 'blue'
        self.size -= 20
        self.is_angry = False

    def draw_fake_enemies(self):
        first_fake_circle_pos = self.position.copy()
        second_fake_circle_pos = self.position.copy()
        first_fake_circle_pos.x -= self.screen.get_width() + self.size
        second_fake_circle_pos.x += self.screen.get_width() + self.size
        pygame.draw.circle(self.screen, self.color, first_fake_circle_pos, self.size)
        pygame.draw.circle(self.screen, self.color, second_fake_circle_pos, self.size)


player_entity = Player(screen, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 30, 'green')

enemies_list = []

for time in range(5):
    enemies_list.append(
        Enemy(screen)
    )


def make_sure_theres_n_enemies(list_of_enemies, n):
    current_lenth_of_enemis = len(list_of_enemies)
    if n == current_lenth_of_enemis:
        return
    for a in range(n - current_lenth_of_enemis):
        list_of_enemies.append(Enemy(screen))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_entity.move_up(dt)
    if keys[pygame.K_s]:
        player_entity.move_down(dt)
    if keys[pygame.K_a]:
        player_entity.move_left(dt)
    if keys[pygame.K_d]:
        player_entity.move_right(dt)

    if keys[pygame.K_r]:
        player_entity.become_angry()

    # flip() the display to put your work on screen
    for enemy in enemies_list:
        enemy.decrease_position(dt)
        enemy.draw()

    player_entity.draw()
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
