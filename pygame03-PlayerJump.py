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
    player = pygame.Rect(200,200,playerWidth,playerHeight)#pygame.Rect(left,right,width,height)
    
    #How fast the player moves
    velocity = 5
    
    #Jump properties
    isJumping = False
    mass = 1

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

        if isJumping == False: #JUMP
            if keys[pygame.K_SPACE]: 
                isJumping = True

        if keys[pygame.K_ESCAPE]: # CLOSE GAME
            done_Running = True

        if isJumping: #if isJump is True
            #F = 1/2 * m * v^2 
            # Where F is the force up/down, m is the mass of the object and v is the velocity
            # The velocity goes down over time because when the object jumps the velocity will not increase more in this simulation.
            # When object reaches the ground, the jump ends
            force = (1/2)*mass*(velocity**2)
            player.y = player.y - force
            velocity = velocity-1

            if velocity < 0: # if player reached the max height
                mass = -2
            
            if velocity <= -6: # if player reached original state before the jump
                isJumping = False
                velocity = 5
                mass = 1

        #BOUNDARIES
        if player.x < 0: player.x = 0 #left boundary wall 
        if player.x > screenWidth - playerWidth: player.x = screenWidth - playerWidth #right boundary wall 
        if player.y < 0: player.y = 0 #top boundary wall
        if player.y > screenHeight - playerHeight: player.y = screenHeight - playerHeight #bottom boundary wall

        #the box
        screen.fill((40,40,40))
        
        #draw player
        pygame.draw.rect(screen, (150, 200, 20), player)
        pygame.display.update()
        pygame.time.delay(10)
        clock.tick(60)
        


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()