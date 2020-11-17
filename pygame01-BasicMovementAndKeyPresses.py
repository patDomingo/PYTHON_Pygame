import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Moving Box")

#box spawn point
x = 50
y = 50

#box size
width = 40
height = 60

velocity = 20

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= velocity
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += velocity
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= velocity
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += velocity
    if keys[pygame.K_ESCAPE]:
        run = False

    #the box
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()