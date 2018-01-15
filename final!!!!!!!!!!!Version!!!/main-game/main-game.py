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


myfontx = pygame.font.SysFont("edyra demo", 80)
myfont2 = pygame.font.SysFont("edyra demo", 56)
myfont3 = pygame.font.SysFont("knight brush demo", 80)
tpoker = myfontx.render("Poker", 1, (0,0,0), 0)
tsolitaire = myfont2.render("Solitare", 1, (0,0,0), 0)
tstart = myfont3.render("Start", 1 ,(0,0,0), 0)
thowtoplay = myfont3.render("How To Play", 1,(0,0,0), 0 )
#toptions = myfont3.render("Options", 1,(0,0,0),0)
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
                      
                      screenv =1
                      pygame.display.flip() 

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 200 and mousey < 260):
                    
                    tstart = myfont3.render("Start",1 ,(0,0,127), 0)
                else:
                    tstart = myfont3.render("Start",1 ,(0,0,0), 0)
    #how to play button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 50 and mousex < 350 and mousey > 260 and mousey < 320):
                    
                    screenv=2
                    pygame.display.flip()

            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 50 and mousex < 350 and mousey > 260 and mousey < 320):
                    
                    thowtoplay = myfont3.render("How To Play", 1,(0,0,127), 0 )
                else:
                    thowtoplay = myfont3.render("How To Play", 1,(0,0,0), 0 )  
    #options
           # if event.type == pygame.MOUSEBUTTONDOWN:
           #     mousex, mousey = event.pos
           #     if (mousex > 120 and mousex < 290 and mousey > 320 and mousey < 380):
           #         print('options!!')


            #if event.type == pygame.MOUSEMOTION:
            #     mousex, mousey = event.pos
            #     if (mousex > 120 and mousex < 290 and mousey > 320 and mousey < 380):
            #        print('whats up')
            #        toptions = myfont3.render("Options", 1,(0,0,127),0)
            #     else:
            #       toptions = myfont3.render("Options", 1,(0,0,0),0)
    #exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 400 and mousey < 460):
                    
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                if (mousex > 130 and mousex < 280 and mousey > 400 and mousey < 460):
                    
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
            #Screen.blit(toptions, (120,320))
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
            #roptions = pygame.Surface((170,60))
            #roptions.set_alpha(0)
            #roptions.fill(transparent)
            #Screen.blit(roptions,(120,320))
#rexit
            rexit = pygame.Surface((150,60))
            rexit.set_alpha(0)
            rexit.fill(transparent)
            Screen.blit(rexit,(130,400))

    #game screen
        if screenv == 1:
            class Card():

                def __init__(self, value, suit, xpos, ypos, face, suit_val):
                    self.value = value
                    self.suit = suit
                    self.xpos = xpos
                    self.ypos = ypos
                    self.face = face
                    self.suit_val = suit_val
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

                def show_card(self):
        #Queue the image to the next update
                    display.blit(self.face, (self.xpos, self.ypos))

     
            class Deck():

                card_list = []

                def __init__(self):
                    self.construct_deck()
                    self._playing_pile = []
                    self._discard_pile = []

                def construct_deck(self):
                    for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
                        if s == 'Clubs':
                            self.suit_val = 1
                        elif s == 'Diamonds':
                            self.suit_val = 2
                        elif s == 'Hearts':
                            self.suit_val = 3
                        elif s == 'Spades':
                            self.suit_val = 4
                        for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                            self.flipped = False
                            self.xpos = -190
                            self.ypos = 20
                            self.face = pygame.image.load(os.path.join('CardsForPython', str(v)+s+'.png'))
                            self.face = pygame.transform.scale(self.face, (160, 232))
                            self.card_list.append(Card(v, s ,self.xpos, self.ypos, self.face, self.suit_val))
                
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
            def check_for_flush(suitlist = [], *suits):
                suit_count = 0
                for i in range(5):
                    if suitlist[0] == suitlist[i]:
                        suit_count += 1
                if suit_count == 5:
                    return True
                else:
                    return False
            def check_for_straight(straightcards = [], *cards):
                if straightcards[4].value - straightcards[0].value == 4:
                    return True
                else:
                    return False
            def check_for_wheel_straight(straightcards = [], *cards):
                if straightcards[4].value == 14 and straightcards[0].value == 2 and straightcards[1].value == 3 and straightcards[2].value == 4 and straightcards[3].value == 5:
                    return True
                else:
                    return False
            def check_for_broadway_straight(straightcards = [], *cards):
                if straightcards[0].value == 10 and straightcards[1].value == 11 and straightcards[2].value == 12 and straightcards[3].value == 13 and straightcards[4].value == 14:
                    return True
                else:
                    return False
            pygame.init()
            myDeck = Deck()
            myDeck.shuffle_deck()
            display = pygame.display.set_mode((1180, 700))
            row = []
            row_suits = []
            row_flush = [bool, bool, bool, bool, bool]
            row_broadway_straight = [bool, bool, bool, bool, bool]
            row_straight = [bool, bool, bool, bool, bool]
            row_wheel_straight = [bool, bool, bool, bool, bool]
            hand = []
            row_xpos = -190
            row_ypos = 20
            card_width = 160
            card_height = 232
            active_card = 0
            loop_count = 0
            temp_loop = 0
            temp_score = 0
            score = 0
            selected = bool
            background = pygame.image.load(os.path.join('img','green_felt.jpg'))
            background = pygame.transform.scale(background, (1180, 700))
            display.blit(background, (0, 0))
            visual_deck = pygame.image.load(os.path.join('img','start-screen-card2.png'))
            visual_deck = pygame.transform.scale(visual_deck, (card_width, card_height))
            display.blit(visual_deck, (1010, 20))
            yellow = (255, 204, 0)
            white = (255, 255, 255)
            myfont = pygame.font.SysFont("MS UI Gothic", 30)
            clickcheck = 0
            for i in range(5):
                row_xpos += 200
                row.append([])
                row_suits.append([])
                hand.append([])
                beginning_card = myDeck.draw_card_from_deck()
                row[i].append(beginning_card)
                row_suits[i].append(beginning_card.suit_val)
                row[i][0].xpos = row_xpos 
                row[i][0].ypos = row_ypos
                row[i][0].show_card()
            cardcount = 5

            active_card = myDeck.draw_card_from_deck()
            active_card.xpos = 1010
            active_card.ypos = 280
            active_card.show_card()
            cardcount += 1

#Main Game Loop
#game ends when 25 cards have been drawn
            while cardcount <= 25:

                row_selected = -1 #a row hasn't been selected yet
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos

            #determine which row is clicked
            #allow any card in row j to be clicked
                        for i in range(5):
                            for j in row[i]:
                                if j.face.get_rect().collidepoint(x-j.xpos, y-j.ypos) and row_selected < 0:
                                    row_selected = i
                        #print('row selected' + str(row_selected))
                        
            #move active card to selected row                     
                        if row_selected >= 0:
                            if len(row[row_selected]) < 5: #only allow a row to have five cards
                    #print('length of row' + str(len(row[row_selected])))
                    
                                row[row_selected].append(active_card)
                                row[row_selected].sort(key=operator.attrgetter('value'))
                                row_suits[row_selected].append(active_card.suit_val)
                    #re-arrange x and y coordinates of cards in changed row
                                for j in range(len(row[row_selected])):
                                    row[row_selected][j].xpos = 10 + row_selected * 200
                                    row[row_selected][j].ypos = 20 + j * 50

                    #draw new active card
                        
                                active_card = myDeck.draw_card_from_deck()
                                active_card.xpos = 1010
                                active_card.ypos = 280
                                cardcount += 1

    #Update Game Screen

    #display background
                display.blit(background, (0, 0))
    #display deck
                display.blit(visual_deck, (1010, 20))
    #display active card
                active_card.show_card()
    
    #Show all cards and queue updates
                for i in range(5):
                    for j in row[i]:
                        j.show_card()
                pygame.display.update()
#add code here to calculate the scoring    
            display.blit(background, (0, 0))
            display.blit(visual_deck, (1010, 20))
            for i in range(5):
                for j in row[i]:
                    j.show_card()
            pygame.display.flip()

            for checkflush in range(5): # check for a flush
                row_flush[checkflush] = check_for_flush(row_suits[checkflush])
   
            for wheelstraight in range(5):
                row_wheel_straight[wheelstraight] = check_for_wheel_straight(row[wheelstraight])
    
            for broadwaystraight in range(5):
                row_broadway_straight[broadwaystraight] = check_for_broadway_straight(row[broadwaystraight])
   
            for checkstraight in range(5):
                row_straight[checkstraight] = check_for_straight(row[checkstraight])
   
            for makehand in range(5):
                for i in range(13):
                    what_card = sum(c.value == i +2 for c in row[makehand])
                    if what_card > 0:
                        hand[makehand].append(what_card)
                    hand[makehand].sort()
                    hand[makehand].reverse()
    
            for whathand in range(5):
                if hand[whathand][0] == 4:#this is 4 of a kind
                    temp_score += 50
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("Four of a kind", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('four of a kind', 'row', whathand+1)
                    score += 50
                    temp_score = 0
                elif hand[whathand][0] == 3 and hand[whathand][1] == 2:
                    temp_score += 30
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("Full house", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('full house', 'row', whathand+1)
                    score += 30
                    temp_score = 0
                elif hand[whathand][0] == 3:
                    temp_score += 10
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("three of a kind", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('three of a kind', 'row', whathand+1)
                    score += 10
                    temp_score = 0
                elif hand[whathand][0] == 2 and hand[whathand][1] == 2:
                    temp_score += 5
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("Two pair", 1,white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('two pair', 'row', whathand+1)
                    score += 5
                    temp_score = 0
                elif hand[whathand][0] == 2:
                    temp_score += 2
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("pair", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('pair', 'row', whathand+1)
                    score += 2
                    temp_score = 0
                elif row_straight[whathand] == True and row_broadway_straight[whathand] == True and row_flush[whathand] == True:
                    temp_score += 100
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("Royal flush", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('royal flush', 'row', whathand+1)
                    score += 100
                    temp_score = 0
                elif (row_straight[whathand] == True or row_wheel_straight[whathand] == True) and row_broadway_straight[whathand] == False and row_flush[whathand] == True:
                    temp_score += 75
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("straight flush", 1,white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('straight flush')
                    score += 75
                    temp_score = 0
                elif row_flush[whathand] == True:
                    temp_score += 20
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("Flush", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('flush', 'row', whathand+1)
                    score += 20
                    temp_score = 0
                elif row_straight[whathand] == True or row_wheel_straight[whathand] == True:
                    temp_score += 15
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("straight", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('straight', 'row', whathand+1)
                    score += 15
                    temp_score = 0
                else:
                    temp_score = 0
                    handscore = myfont.render(str(temp_score), 1, white, 0)
                    display.blit(handscore, ((75+whathand*200), 550))
                    text = myfont.render("no points", 1, white, 0)
                    display.blit(text, ((10+whathand*200), 500))
                    print('no points')
                    temp_score = 0


            text = myfont.render("Score: ", 1,white, 0)
            display.blit(text, (1010, 500))
            myscore = myfont.render(str(score), 1, yellow, 0)
            display.blit(myscore , (1080, 500))
            playagain = myfont3.render('Play Again', 1 ,(0,0,0), 0)
            display.blit(playagain,(10,620))
            exitp = myfont3.render('Menu',1,(0,0,0),0)
            display.blit(exitp , (1025,620))
            pygame.display.flip()
            clickcheck = 1
            while clickcheck == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mousex, mousey = event.pos
                        if (mousex > 10 and mousex < 200 and mousey > 640 and mousey < 700):
                            

                             playagain = myfont3.render('Play Again', 1 ,(0,0,127), 0)
                        else:
                            playagain = myfont3.render('Play Again', 1 ,(0,0,0), 0)
                    if event.type == pygame.MOUSEBUTTONDOWN: #play again button is clicked


                        mousex,mousey = event.pos
                        if (mousex > 10 and mousex < 200 and mousey > 620 and mousey < 700):
                            
                            screenv = 1
                        
                            clickcheck = 0
                            pygame.display.flip()
                    if event.type == pygame.MOUSEBUTTONDOWN: #play again button is clicked
                         mousex,mousey = event.pos
                         if (mousex > 1030 and mousex < 1230 and mousey > 620 and mousey < 700):
                            
                            screenv = 0
                            Screen = pygame.display.set_mode((x1,y1))
                            clickcheck = 0
                            pygame.display.flip() #exit button is clicked
                #screenv = 0
            
            


        if screenv == 2:
            howscreen = pygame.display.set_mode((1200,700))
            howbg = pygame.image.load(os.path.join('img','poker-hand-rankings3.jpg'))
            howscreen.blit(howbg,(0,0))    
            myfont4 = pygame.font.SysFont("Gisha", 20)
            line1 = myfont4.render("Poker Solitaire is a combination of the timeless leisure", 1, (0,0,0), 0)
            line2 = myfont4.render("classic, Solitaire, and Poker. The game begins with cards", 1, (0,0,0), 0)
            line3 = myfont4.render("dealt out side by side, creating five rows. The goal is to", 1, (0,0,0), 0)
            line4 = myfont4.render("create five of the best poker hand you can (see hand ", 1, (0,0,0), 0)
            line5 = myfont4.render("ranking chart for more details). At the end of the game ", 1, (0,0,0), 0)
            line6 = myfont4.render("based on the different hands you create, a score is ", 1, (0,0,0), 0)
            line7 = myfont4.render("calculated. Good Luck! ", 1, (0,0,0), 0)
            hback = myfont3.render("Back",1,(0,0,0),0)
            for event in pygame.event.get():
                #if event.type == pygame.MOUSEBUTTONDOWN:
                #    mousex, mousey = event.pos
                #    if (mousex > 430 and mousex < 550 and mousey > 550 and mousey < 610):
                #        print('start!!!')
                #       screenv = 0
                #        Screen = pygame.display.set_mode((x1,y1))
                #        pygame.display.update() 

                if event.type == pygame.MOUSEMOTION:
                    mousex, mousey = event.pos
                    if (mousex > 430 and mousex < 550 and mousey > 550 and mousey < 610):
                        
                        hback = myfont3.render("Back",1,(0,0,127),0)
                        screenv = 0
                        Screen = pygame.display.set_mode((x1,y1))
                        pygame.display.update() 
                    else:
                        hback = myfont3.render("Back",1,(0,0,0),0)


            rback = pygame.Surface((120,60))
            rback.set_alpha(0)
            rback.fill(transparent)
            howscreen.blit(rback,(430,550))
            howscreen.blit(thowtoplay,(410,20))
            howscreen.blit(line1,(355,110))
            howscreen.blit(line2,(355,135))
            howscreen.blit(line3,(355,160))
            howscreen.blit(line4,(355,185))
            howscreen.blit(line5,(355,210))
            howscreen.blit(line6,(355,235))
            howscreen.blit(line7,(355,260))
            howscreen.blit(hback,(430,550))
            pygame.display.flip()
    pygame.display.flip()




    
    


