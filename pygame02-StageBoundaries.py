import sys
import pygame

def main():

    #Game window title 
    pygame.display.set_caption("Moving Box")

    #Set game screen 
    screenWidth = 640
    screenHeight = 480
    screen = pygame.display.set_mode((screenWidth,screenHeight))

    #Set game framerate
    clock = pygame.time.Clock()

    #Player Attributes
    playerWidth = 60
    playerHeight = 60
    player = pygame.Rect(300,220,playerWidth,playerHeight)#pygame.Rect(left,right,width,height)
    
    #How fast the player moves
    velocity = 20

    done_Running = False
    while not done_Running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done_Running = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #move LEFT
            player.x -= velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #move RIGHT 
            player.x += velocity
        if keys[pygame.K_UP] or keys[pygame.K_w]: #move UP
            player.y -= velocity
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: #move DOWN
            player.y += velocity
        if keys[pygame.K_ESCAPE]: # CLOSE GAME
            done_Running = True

        #BOUNDARIES
        #if player.x < 0: player.x = 0 #left boundary wall 
        #if player.x > screenWidth - playerWidth: player.x = screenWidth - playerWidth #right boundary wall 
        #if player.y < 0: player.y = 0 #top boundary wall
        #if player.y > screenHeight - playerHeight: player.y = screenHeight - playerHeight #bottom boundary wall

        #LOOPING BOUNDARIES
        if player.x < 0: #left boundary wall
            player.x = screenWidth - playerWidth  

        if player.x > screenWidth - playerWidth: #right boundary wall 
            player.x = 0 

        if player.y < 0: #top boundary wall
            player.y = screenHeight - playerHeight 

        if player.y > screenHeight - playerHeight: #bottom boundary wall
            player.y = 0 

        #the box
        screen.fill((40,40,40))
        
        #draw player
        pygame.draw.rect(screen, (150, 200, 20), player)
        pygame.display.update()
        clock.tick(30)
        


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()