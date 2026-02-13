import pygame           
import sys              
import time           
import projectile
import math
from functions import projectile_collision

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_CAPTION = 'Missile Command - Walcome'
SCREEN_BACKGROUND = (0,0,0)

pygame.init()           #Intialize the game

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))            # Create screen 
pygame.display.set_caption(SCREEN_CAPTION)      # Set title screen
screen.fill(SCREEN_BACKGROUND)                            # Fill screen with grey color
clock = pygame.time.Clock()     # Create clock to set and track FPS

# You can create a surface with text on it. For this take a look at this short example:
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Times new roman', 30)

boom_pos = None
boom_radius = 0

offense_rockets = []        # List with rockets from the attacking force

max_nr_of_rockets = 1
for idx in range(max_nr_of_rockets):
    rocket = projectile.Projectile(screen.get_width(), "offense")
    offense_rockets.append(rocket)

FONT = pygame.font.SysFont("Sans", 20)  # Fint for text to display something on screen
hit_or_not = False
start_time = pygame.time.get_ticks()

running = True                  
while running == True:          
    for event in pygame.event.get():            # Get events and loop through these events
        if event.type == pygame.QUIT:           # Exit Event? For instance the exit button from window
            running=False                       # The game shoudl stop running
        elif event.type == pygame.MOUSEBUTTONUP :                       # If mouse clicked then defensive player launched explosion, so this should be drawn
            rocket_player = projectile.Projectile(screen.get_width(), "defense")
            # print("Muisknop geklikt op: ",pygame.mouse.get_pos())
            boom_pos = pygame.mouse.get_pos()
            boom_radius = 0

    screen.fill((0,0,0))                  # Continue the game and fill screen, or repaint screen
    # pygame.draw.rect(screen, (255,0,0), (x,y,200,50))   # Draw something on the screen

    if pygame.time.get_ticks() - start_time >= 2000: #When more than 2 seconds have passed create a new rocket
        start_time = pygame.time.get_ticks()
        offense_rockets.append(projectile.Projectile(screen.get_width(), "offense"))
    
    message = 'Milliseconds since enter: ' + str(pygame.time.get_ticks() - start_time)
    screen.blit(FONT.render(message, True, (255,255,255)), (20, 20))

    for rocket in offense_rockets:
        rocket.update()
        pygame.draw.line(screen, (0,255,0),(rocket.start_position.x, rocket.start_position.y),(rocket.pos.x, rocket.pos.y))
        pygame.draw.ellipse(screen,(255,0,0),(rocket.pos.x, rocket.pos.y, 10,10))

        if boom_pos != None:
            hit_or_not = projectile_collision(rocket.pos, 5, boom_pos, boom_radius)

        if rocket.pos.y >= screen.get_height() or rocket.pos.x < 0 or rocket.pos.x > screen.get_width() or hit_or_not:
            offense_rockets.remove(rocket)

        if len(offense_rockets) < max_nr_of_rockets:
            for nr_of_rockets in range(max_nr_of_rockets - len(offense_rockets)):
                rocket = projectile.Projectile(screen.get_width(), "offense")
                offense_rockets.append(rocket)

    #Draw the explosion for the defensive player
    #This shoudl be part of the rocket loop. If is was a hit then the rocket shoulld
    #be removed from the list and the user should get points or some other reward
    if boom_pos != None:
        pygame.draw.circle(screen,(0,0,255),(boom_pos[0], boom_pos[1]),boom_radius,2)
        boom_radius += 1
        if boom_radius > 100:
            boom_pos = None

    pygame.display.flip()                       # Update screen
        
    clock.tick(60)          # Set FPS to 60

# Game Exit? Then go through these statements
screen.fill((255,255,255))
pygame.display.flip()

pygame.quit()
sys.exit()

# key events of interest:
# pygame.K_[.....] Keystroke 
# pygame.MOUSE[....] Something with the mouse