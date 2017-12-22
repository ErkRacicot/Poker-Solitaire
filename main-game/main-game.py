
import pygame, sys, os
from pygame.locals import *

pygame.init()
game = 1
x1=400
y1=580
Screen = pygame.display.set_mode((x1,y1))
   

bg = pygame.image.load(os.path.join('img','start-screen-card2.png'))

file = (os.path.join('music', 'poker-solitare-track-1.mp3'))

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)


myfont = pygame.font.SysFont("edyra demo", 80)
myfont2 = pygame.font.SysFont("edyra demo", 56)
myfont3 = pygame.font.SysFont("knight brush demo", 80)
tpoker = myfont.render("Poker", 1, (0,0,0), 0)
tsolitaire = myfont2.render("Solitare", 1, (0,0,0), 0)
tstart = myfont3.render("Start", 1 ,(0,0,0), 0)
thowtoplay = myfont3.render("How To Play", 1,(0,0,0), 0 )
toptions = myfont3.render("Options", 1,(0,0,0),0)
texit = myfont3.render("Exit", 1,(0,0,0),0)
   




transparent=(21,32,49)
screenv = 0 

running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
                       
    #start button
        if screenv == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                  mousex, mousey = event.pos
                  if (mousex > 130 and mousex < 280 and mousey > 200 and mousey < 260):
                      print('start!!!')
                      screenv =1


            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 200 and mousey < 260):
                    print('hi')
                    tstart = myfont3.render("Start",1 ,(0,0,127), 0)
                else:
                    tstart = myfont3.render("Start",1 ,(0,0,0), 0)
    #how to play button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 50 and mousex < 350 and mousey > 260 and mousey < 320):
                    print('how to play!!!')
               

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 50 and mousex < 350 and mousey > 260 and mousey < 320):
                    print('hello')
                    thowtoplay = myfont3.render("How To Play", 1,(0,0,127), 0 )
                else:
                    thowtoplay = myfont3.render("How To Play", 1,(0,0,0), 0 )  
    #options
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 120 and mousex < 290 and mousey > 320 and mousey < 380):
                    print('options!!')


            if event.type == pygame.MOUSEMOTION:
                 mousex, mousey = event.pos
                 if (mousex > 120 and mousex < 290 and mousey > 320 and mousey < 380):
                    print('whats up')
                    toptions = myfont3.render("Options", 1,(0,0,127),0)
                 else:
                   toptions = myfont3.render("Options", 1,(0,0,0),0)
    #exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 400 and mousey < 460):
                    print('exit!!')
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 400 and mousey < 460):
                    print('wus good')
                    texit = myfont3.render("Exit", 1,(0,0,127),0)
                else:
                    texit = myfont3.render("Exit", 1,(0,0,0),0)
    #game screen
        if screenv == 1:
            Screen = pygame.display.set_mode((1200,700))

                
    pygame.event.get()
    bg = pygame.transform.scale(bg,(x1,y1))
    Screen.blit(bg, (0, 0))

    Screen.blit(tpoker,(0,50))
    Screen.blit(tsolitaire,(0,125))
    Screen.blit(tstart, (130, 200))
    Screen.blit(thowtoplay,(50,260))
    Screen.blit(toptions, (120,320))
    Screen.blit(texit, (140, 390))
#start
    rstart = pygame.Surface((150,60))
    rstart.set_alpha(0)
    rstart.fill(transparent)
    Screen.blit(rstart,(130,200))
   
#rhowtoplay
    rhowtoplay = pygame.Surface((300,60))
    rhowtoplay.set_alpha(0)
    rhowtoplay.fill(transparent)
    Screen.blit(rhowtoplay,(50,260))

#roptions
    roptions = pygame.Surface((170,60))
    roptions.set_alpha(0)
    roptions.fill(transparent)
    Screen.blit(roptions,(120,320))
#rexit
    rexit = pygame.Surface((150,60))
    rexit.set_alpha(0)
    rexit.fill(transparent)
    Screen.blit(rexit,(130,400))



    
    pygame.display.flip()




    
    


