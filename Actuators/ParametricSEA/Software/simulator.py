from math import pi
import random
import pygame
import PyParticles4

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles4.Environment((width, height))
universe.colour = (255,255,255)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.1)
universe.mass_of_air = 0.02


universe.addParticles(x= 100, y=50, mass=10, size=16, speed=0.1, elasticity=1, colour=(20,40,200), fixed=1)
universe.addParticles(x= 100, y=150, mass=10, size=16, speed=0.1, elasticity=1, colour=(20,40,200))
universe.addParticles(x= 100, y=250, mass=10, size=16, speed=0.1, elasticity=1, colour=(20,40,200), fixed=1)

universe.addSpring(0,1, length=90, strength=0.5)
universe.addSpring(1,2, length=90, strength=0.5)
#universe.addSpring(0,2, length=210, strength=10)

selected_particle = None
paused = False
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = universe.findParticle(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)

    force1 = universe.springs[0].getForce()
    if abs(force1*2) < 128:
      force1 *= 2
    force2 = universe.springs[1].getForce()*2
    if abs(force2*2) < 128:
      force2 *= 2
    print force1, force2

    pygame.draw.rect(screen, (128,0,128),pygame.Rect(75,25,50,250),0)
    pygame.draw.rect(screen, (128+force1,128+force1*-1,0),pygame.Rect(80,30,40,100),0)
    pygame.draw.rect(screen, (128+force2,128+force2*-1,0),pygame.Rect(80,170,40,100),0)

    for s in universe.springs:
        #pygame.draw.rect(screen, (0,0,0), pygame.Rect(int(s.p1.x-4), int(s.p1.y),int(s.p2.x)-int(s.p1.x)+8, int(s.p2.y)-int(s.p1.y)),0)
        pygame.draw.aaline(screen, (0,0,0), (int(s.p1.x), int(s.p1.y)),(int(s.p2.x), int(s.p2.y)))
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
  

    pygame.display.flip()