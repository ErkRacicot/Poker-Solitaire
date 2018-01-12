import random
import operator
import pygame, sys, os
from pygame.locals import *

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
        for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']: #where 1 is Clubs, 2 is Diamonds, 3 is Hearts, 4 is Spades
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
def front_card_in_row(mylist = [], *arguments):
    print(len(mylist))

myDeck = Deck()
myDeck.shuffle_deck()
display = pygame.display.set_mode((1180, 700))
row = []
row_suits = []
hand = []
row_xpos = -190
row_ypos = 20
card_width = 160
card_height = 232
active_card = 0
loop_count = 0
temp_loop = 0
row_check = 0
which_row = 0
selected = bool
background = pygame.image.load('MiscPhotos/green_felt.jpg')
background = pygame.transform.scale(background, (1180, 700))
display.blit(background, (0, 0))
visual_deck = pygame.image.load('MiscPhotos/start-screen-card2.png')
visual_deck = pygame.transform.scale(visual_deck, (card_width, card_height))
display.blit(visual_deck, (1010, 20))
for i in range(5):
    row_xpos += 200
    row.append([])
    row_suits.append([])
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
        
                                    
                    
        
                   
               
        
    










