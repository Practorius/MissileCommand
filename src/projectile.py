import random
import pygame

class Projectile:
    
    def __init__(self):
        self.pos = pygame.math.Vector2(random.random(), 0)
        self.delta = 5
        self.velocity = pygame.math.Vector2(random.random(),random.random())
        self.previouspos = []
        

    def update(self):
        self.previouspos.insert(0, self.pos.copy())
        for idx in range(len(self.previouspos)):
            if idx>20:
                del self.previouspos[idx]
        #     del self.previousposx[len(self.previousposx)]
        #     del self.previousposx[len(self.previousposx)]
        self.pos += self.velocity
