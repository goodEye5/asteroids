from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position ,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        old_radius = self.radius
        a = Asteroid(self.position.x,self.position.y,old_radius - ASTEROID_MIN_RADIUS)
        b = Asteroid(self.position.x,self.position.y,old_radius - ASTEROID_MIN_RADIUS)
        a.velocity = 1.2*self.velocity.rotate(random_angle)
        b.velocity = 1.2*self.velocity.rotate(-random_angle)
