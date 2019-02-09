"""
This program was made Fall of 2017 after I
had learned about isometric ellipses in
architectural drawings. I applied what I
learned to draw on paper and apply it to this
program. The program takes a size, creates an
ellipse off the size, centers it, and allows size
manipulation with the "w" and "s" keys.

I, Austin Lowery, am the designer of this code and
claim ownership of it.

Copyright 2017, Austin Lowery, All rights reserved.
"""

import pygame

### Creates an adjustable isometric ellipse ###
def isometricEllipse(size, diagLineLength):
    loopExit = wDown = sDown = False
    ### Start Change Circle Loop ###
    while not loopExit:
        for event in pygame.event.get():
            # if window exit clicked, exit window
            if event.type == pygame.QUIT:
                loopExit = True

            # determines if w or s is held down so that ellipse size increases
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                     wDown = True
                elif event.key == pygame.K_s:
                    sDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    wDown = False
                elif event.key == pygame.K_s:
                    sDown = False

        # if w is held down
        if wDown == True:
            # increase ellipse size
            size += 5
            # diagonal line length is sqrt(3x^2 / 4)
            diagLineLength = ( (3 * size**2) / 4)**(1/2)
        # if s is held down and the size is greater than 5
        elif sDown == True and size > 5:
            size -= 5
            diagLineLength = ( (3 * size**2) / 4)**(1/2)

        # fill screen with a purplish color
        gameDisplay.fill((188,174,193))

        # the size times sqrt(3)
        intersect = size*3**(1/2)

        # allows only a specific area to be drawn to then creates a large circle
        # that cuts off the unneeded excess
        # Portion: Left Large Circle
        clip = pygame.Rect((300+round(intersect/6), 0, 300-round(intersect/6), 600))
        gameDisplay.set_clip(clip)
        gameDisplay.fill((188,174,193))
        pygame.draw.circle(gameDisplay,(0,0,0),(-round(size/2)+300,300),round(intersect/2))

        # Portion: Right Large Circle
        clip = pygame.Rect((0, 0, 300-round(intersect/6), 600))
        gameDisplay.set_clip(clip)
        gameDisplay.fill((188,174,193))
        pygame.draw.circle(gameDisplay,(0,0,0),(round(size/2)+300,300),round(intersect/2))

        # Portion: 
        clip = pygame.Rect((300-round(intersect/6), 0, round(intersect/3), 600))
        gameDisplay.set_clip(clip)
        pygame.draw.circle(gameDisplay,(0,0,0),(300,round(intersect/6)+300),round(intersect/6))

        # Portion: Small Top Circle
        pygame.draw.rect(gameDisplay,(0,0,0),(300-round(intersect/6),300-round(size/2)+round(diagLineLength),round(intersect/3),(round(size/2)-round(diagLineLength))*2))
        # Portion: Small Bottom Circle
        pygame.draw.circle(gameDisplay,(0,0,0),(300,-round(intersect/6)+300),round(intersect/6))
        

        # square between the empty space created by the circles
        pygame.draw.rect(gameDisplay,(0,0,0),(300-round(intersect/6),300-round(size/2)+round(diagLineLength),round(intersect/3),(round(size/2)-round(diagLineLength))*2))
        
        # updates screen and ticks for 7 frames
        pygame.display.update()
        clock.tick(7)
                           
    ### End Change Circle Loop ###

    pygame.quit()



### Begin User Input and Response ###
contLoop = True
while contLoop:
    print(contLoop)
    inputText = True
    # loop to make sure user enters valid value ie a number greater than 0 or a letter
    while inputText:
        text = input("Elipse Size (type a letter to exit) = ")
        try:
            size = int(text)
            if size <= 0:
                print("No numbers less than or equal to zero.")
            else:
                inputText = False
        except:
            print("Exiting program...")
            contLoop = inputText = False

    # if user entered letter, exit program
    if not contLoop: break

    diagLineLength=(3*size**2/4)**(1/2)
    print("Length of Diagonal: ",round(diagLineLength))

    intersect = size*3**(1/2)
    
    # draw line from (0, +/- 50) & (+/- 50,0) to ( +/- round(diagLineLength), +/- round(diagLineLength)/3**2)
    print("( 0 ,",round(size/2),") -> (",-round(diagLineLength),",",-round(diagLineLength/3**(1/2)),")")
    print("(",-round(diagLineLength),", 0 ) -> (",round(diagLineLength),",",-round(diagLineLength/3**(1/2)),")")
    print("( 0 ,",-round(size/2),") -> (",round(diagLineLength),",",round(diagLineLength/3**(1/2)),")")
    print("(",round(diagLineLength),", 0 ) -> (",-round(diagLineLength),",",round(diagLineLength/3**(1/2)),")")
    print("Small Circle on ( 0 ,",round(intersect/6),") and ( 0 ,",-round(intersect/6),") with a diameter of",round(intersect/3))
    print("Large Circle on ( 0 ,",-round(size/2),") and ( 0 ,",round(size/2),") with a diameter of",round(intersect))

    pygame.init()
    gameDisplay = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()
    isometricEllipse(size,diagLineLength)
    
### End User Input and Response ###

quit()


