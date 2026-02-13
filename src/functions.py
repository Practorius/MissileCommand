import math

def projectile_collision(v1, v1_radius, v2, v2_radius):
    """ Function to calulate a collision between vehicles 
        based on their distance of center and radius of vehicle
    """
    distance = math.sqrt((v1.x - v2[0])**2 +(v1.y - v2[1])**2)
    return distance < v1_radius + v2_radius