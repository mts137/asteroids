import pygame
import random
from logger import log_event
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(angle)
        asteroid2_velocity = self.velocity.rotate(-angle)
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid1.velocity = asteroid1_velocity
        asteroid2.velocity = asteroid2_velocity
