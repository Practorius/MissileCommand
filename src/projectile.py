import random
import pygame

class Projectile:
    
    def __init__(self, screen_width, projectile_type):
        
        if projectile_type == 'defense':
            self.max_magnitude = 2
            self.pos = pygame.math.Vector2(random.random()*screen_width/2, 0)
        elif projectile_type == 'offense':
            self.max_magnitude = 1
            self.pos = pygame.math.Vector2(random.random()*screen_width, 0)
        elif projectile_type == 'airplane':
            self.max_magnitude = 0.5
        else:
            self.max_magnitude = 0

        self.velocity = pygame.math.Vector2(random.random(),random.random())
        pygame.math.Vector2.scale_to_length(self.velocity, self.max_magnitude)
        self.start_position = self.pos.copy()
        

    def update(self):
        self.pos += self.velocity
