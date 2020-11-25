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
    velocity = 10
    
    #Jump properties
    isJumping = False
    jumpCount = 10

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

        if not(isJumping): #if isJumping is false Player can go up, down and jump
            if keys[pygame.K_UP] or keys[pygame.K_w]: #move UP
                player.y -= velocity
            if keys[pygame.K_DOWN] or keys[pygame.K_s]: #move DOWN
                player.y += velocity
            if keys[pygame.K_SPACE]: 
                isJumping = True

        else:
            if jumpCount >= -10:
                print(player.y)
                player.y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 2
            else: # Will execute if jump is finished
                jumpCount = 10
                isJumping = False
                # Resetting our Variables

        if keys[pygame.K_ESCAPE]: # CLOSE GAME
            done_Running = True

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