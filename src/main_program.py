import pygame           
import sys              
import time           
import projectile
import math

pygame.init()           #Intialize the game

def projectile_collision(offence, offence_radius, defence, defence_radius):
    distance = math.sqrt((offence.x + defence[0])**2 +(offence.y + defence[1])**2)
    return distance < offence_radius + defence_radius

screen = pygame.display.set_mode((800, 600))            # Create screen 
pygame.display.set_caption("Missile Command")      # Set title screen
screen.fill((0, 0, 0))                            # Fill screen with grey color
clock = pygame.time.Clock()     # Create clock to set and track FPS
x,y=0,0                         # Set x,y initial coordinates
boom_pos = None
boom_radius = 0

rocket = projectile.Projectile()

running = True                  
while running == True:          
    for event in pygame.event.get():            # Get events and loop through these events
        if event.type == pygame.QUIT:           # Exit Event? For instance the exit button from window
            running=False                       # The game shoudl stop running
        elif event.type == pygame.MOUSEBUTTONUP :                       # If mouse clicked then defensive player launched explosion, so this should be drawn
            print("Muisknop geklikt op: ",pygame.mouse.get_pos())
            boom_pos = pygame.mouse.get_pos()
            boom_radius = 0
    
    screen.fill((0,0,0))                  # Continue the game and fill screen, or repaint screen
    # pygame.draw.rect(screen, (255,0,0), (x,y,200,50))   # Draw something on the screen

    rocket.update()

    for idx in range(len(rocket.previouspos)):        
        pygame.draw.ellipse(screen,(0,255,0),(rocket.previouspos[idx].x, rocket.previouspos[idx].y, 10,10))    
    pygame.draw.ellipse(screen,(255,0,0),(rocket.pos.x, rocket.pos.y, 10,10))

    #Draw the explosion for the defensive player
    if boom_pos != None:
        pygame.draw.circle(screen,(0,0,255),(boom_pos[0], boom_pos[1]),boom_radius)
        boom_radius += 1
        if boom_radius > 100:
            boom_pos = None

    if boom_pos != None:
        hit_or_not = projectile_collision(rocket.pos, 10, boom_pos, boom_radius)
        print(hit_or_not)


    pygame.display.flip()                       # Update screen
        
    x+=2                    # Update x, y coordinates
    y+=3
    clock.tick(60)          # Set FPS to 60

# Game Exit? Then go through these statements
screen.fill((255,255,255))
pygame.display.flip()

pygame.quit()
sys.exit()

# key events of interest:
# pygame.K_[.....] Keystroke 
# pygame.MOUSE[....] Something with the mouse