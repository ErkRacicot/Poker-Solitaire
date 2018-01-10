import random
import operator
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
                      pygame.display.flip() 

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
                    screenv=2
                    pygame.display.flip()

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

    #game screen
        if screenv == 1:
            class Card():

                def __init__(self, value, suit, xpos, ypos, face):
                    self.value = value
                    self.suit = suit
                    self.xpos = xpos
                    self.ypos = ypos
                    self.face = face

                def show_card(self):
                    if self.value == 11:
                        face_value = 'Jack'
                    elif self.value == 12:
                        face_value = 'Queen'
                    elif self.value == 13:
                        face_value = 'King'
                    elif self.value == 14:
                        face_value = 'Ace'
                    else:
                        face_value = self.value

                    display.blit(self.face, (self.xpos, self.ypos))
                    pygame.display.update()

     
            class Deck():

                card_list = []

                def __init__(self):
                    self.construct_deck()
                    self._playing_pile = []
                    self._discard_pile = []

                def construct_deck(self):
                    for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
                        for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                            self.flipped = False
                            self.xpos = -190
                            self.ypos = 20
                            self.face = pygame.image.load(os.path.join('CardsForPython', str(v)+s+'.png'))
                            self.face = pygame.transform.scale(self.face, (160, 232))
                            self.card_list.append(Card(v, s,self.xpos, self.ypos, self.face))
                
                def show_deck(self):
                    for card in self.card_list:
                        card.show_card()

                def show_playing_pile(self):
                    for card in self._playing_pile:
                        card.show_card()

                def show_discard_pile(self):
                    for card in self._discard_pile:
                        card.show_card()

                def shuffle_deck(self):
                    self.shuffled_cards = random.shuffle(self.card_list)

                def draw_card_from_deck(self):
                    self._draw_from_deck = self.card_list.pop()
                    return self._draw_from_deck

                def return_card_to_deck(self):
                    self._return_to_deck = self.card_list.append(self._draw_from_deck)
                    return self._return_to_deck

                def put_card_in_playing_pile(self):
                    self._put_in_playing_pile = self._playing_pile.append(self._draw_from_deck)
                    return self._put_in_playing_pile

                def put_card_in_discard_pile(self):
                    self._put_in_discard_pile = self._discard_pile.append(self._draw_from_deck)
                    return self._put_in_discard_pile
            def front_card_in_row(mylist = [], *arguments):
                print(len(mylist))
            myDeck = Deck()
            myDeck.shuffle_deck()
            display = pygame.display.set_mode((1180, 700))
            row = []
            row_xpos = -190
            row_ypos = 20
            card_width = 160
            card_height = 232
            active_card = 0
            loop_count = 0
            temp_loop = 0
            row_check = 0
            selected = bool
            background = pygame.image.load(os.path.join('img','green_felt.jpg'))
            background = pygame.transform.scale(background, (1180, 700))
            display.blit(background, (0, 0))
            visual_deck = pygame.image.load(os.path.join('img','start-screen-card2.png'))
            visual_deck = pygame.transform.scale(visual_deck, (card_width, card_height))
            display.blit(visual_deck, (1010, 20))
            for i in range(5):
                row_xpos += 200
                row.append([])
                beginning_card = myDeck.draw_card_from_deck()
                row[i].append(beginning_card)
                row[i][0].xpos = row_xpos 
                row[i][0].ypos = row_ypos
                row[i][0].show_card()
            cardcount = 5
            while cardcount < 25:
                active_card = myDeck.draw_card_from_deck()
                cardcount += 1
                active_card.xpos = 1010
                active_card.ypos = 280
                active_card.show_card()
                temp_loop = 1
                while temp_loop == 1: #loop to check for picked row
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = event.pos
                            for i in range(5):
                                for j in row[i]:
                                    if j.face.get_rect().collidepoint(x-j.xpos, y-j.ypos):
                                        print('row has been picked') 


        if screenv == 2:
            howscreen = pygame.display.set_mode((1200,700))
            howbg = pygame.image.load(os.path.join('img','poker-hand-rankings.png'))
            howscreen.blit(howbg,(0,0))    
   


    
    pygame.display.flip()




    
    


