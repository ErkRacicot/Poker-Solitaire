#https://codereview.stackexchange.com/questions/172646/simple-deck-of-cards-python-program - is where the deck of cards class is from
#https://github.com/notpeter/Vector-Playing-Cards
#https://stackoverflow.com/questions/16455777/python-count-elements-in-a-list-of-objects-with-matching-attributes

import random
import operator
import pygame, sys, os
from pygame.locals import *

class Card():

    def __init__(self, value, suit, image):
        self.value = value
        self.suit = suit
        self.image = image

    def show_card(self):
        if self.value == 11:
            out = 'Jack'
        elif self.value == 12:
            out = 'Queen'
        elif self.value == 13:
            out = 'King'
        elif self.value == 14:
            out = 'Ace'
        else:
            out = self.value

        print(str(out) + " of " + str(self.suit))
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
                image = pygame.image.load(os.path.join('Pictures', 'Cards','cards-png', str(v)+s+'.png')) 
                self.card_list.append(Card(v, s, image))
                
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
        
#surface = pygame.display.set_mode(1200, 700)
myDeck = Deck()
myDeck.shuffle_deck()
first_row = []
second_row = []
third_row = []
fourth_row = []
fifth_row = []
active_card = 0
gamerunning = 1
cardcount = 5
hand1 = []
hand2 = []
hand3 = []
hand4 = []
hand5 = []
first_row_straight = bool
first_row_broadway = bool
first_row_flush = bool
second_row_straight = bool
second_row_broadway = bool
second_row_flush = bool
third_row_straight = bool
third_row_broadway = bool
third_row_flush = bool
fourth_row_straight = bool
fourth_row_broadway = bool
fourth_row_flush = bool
fifth_row_straight = bool
fifth_row_broadway = bool
fifth_row_flush = bool
suit = 0
first_row_suits = []
second_row_suits = []
third_row_suits = []
fourth_row_suits = []
fifth_row_suits = []
score = 0
first_row_xpos = 20
first_row_ypos = 20
second_row_xpos = 210
second_row_ypos = 20
third_row_xpos = 410
third_row_ypos = 20
fourth_row_xpos = 610
fourth_row_ypos = 20
fifth_row_xpos = 810
fifth_row_ypos = 20
deck_xpos = 1010
deck_ypos = 20
card_width = 160
card_height = 232
spacing = 50
display = pygame.display.set_mode((1200, 700))

#"D:\Python projects\POKER SOLITAIRE\Pictures\Midnight-Blue-Suited-Speed-Cloth.jpg": is the blue felt background image
#"D:/Python projects/POKER SOLITAIRE/Pictures/free-vector-red-poker-background.jpg": is the red felt background image
background = pygame.image.load("F:/Python projects/POKER SOLITAIRE/Pictures/free-vector-red-poker-background.jpg")
background = pygame.transform.scale(background, (1200, 700))
background = display.blit(background, (0, 0))
pygame.display.update()

#main_menu = pygame.display.set_mode((1200, 700))
#pygame.display.set_caption('POKER SOLITAIRE')

#The first card to each list is added at the beginning of the game
first_row.append(myDeck.draw_card_from_deck())
second_row.append(myDeck.draw_card_from_deck())
third_row.append(myDeck.draw_card_from_deck())
fourth_row.append(myDeck.draw_card_from_deck())
fifth_row.append(myDeck.draw_card_from_deck())

print(' One Pair = 2 points', '\n', 'Two Pair = 5 points', '\n', 'Three of a Kind = 10 points', '\n', 'Straight = 15 points', '\n', 'Flush = 20 points', '\n', 'Full House = 30 points', '\n', 'Four of a Kind = 50 points', '\n', 'Straight Flush = 75 points', '\n', 'Royal Flush = 100 points', '\n')
#initial display of cards
deck = pygame.image.load("F:/Python projects/POKER SOLITAIRE/Pictures/card back blue.png")
deck = pygame.transform.scale(deck, (card_width, card_height))
deck = display.blit(deck, (deck_xpos, deck_ypos))
print('Row 1')
first_row[0].show_card()
first_row[0].image = pygame.transform.scale(first_row[0].image, (card_width, card_height))
image = display.blit(first_row[0].image, (first_row_xpos, first_row_ypos))
if first_row[0].suit == 'Clubs':
    suit = 1
elif first_row[0].suit == 'Diamonds':
    suit = 2
elif first_row[0].suit == 'Hearts':
    suit = 3
elif first_row[0].suit == 'Spades':
    suit = 4
first_row_suits.append(suit)
print('Row 2')
second_row[0].show_card()
second_row[0].image = pygame.transform.scale(second_row[0].image, (card_width, card_height))
image = display.blit(second_row[0].image, (second_row_xpos, second_row_ypos))
if second_row[0].suit == 'Clubs':
    suit = 1
elif second_row[0].suit == 'Diamonds':
    suit = 2
elif second_row[0].suit == 'Hearts':
    suit = 3
elif second_row[0].suit == 'Spades':
    suit = 4
second_row_suits.append(suit)
print('Row 3')
third_row[0].show_card()
third_row[0].image = pygame.transform.scale(third_row[0].image, (card_width, card_height))
image = display.blit(third_row[0].image, (third_row_xpos, third_row_ypos))
if third_row[0].suit == 'Clubs':
    suit = 1
elif third_row[0].suit == 'Diamonds':
    suit = 2
elif third_row[0].suit == 'Hearts':
    suit = 3
elif third_row[0].suit == 'Spades':
    suit = 4
third_row_suits.append(suit)
print('Row 4')
fourth_row[0].show_card()
fourth_row[0].image = pygame.transform.scale(fourth_row[0].image, (card_width, card_height))
image = display.blit(fourth_row[0].image, (fourth_row_xpos, fourth_row_ypos))
if fourth_row[0].suit == 'Clubs':
    suit = 1
elif fourth_row[0].suit == 'Diamonds':
    suit = 2
elif fourth_row[0].suit == 'Hearts':
    suit = 3
elif fourth_row[0].suit == 'Spades':
    suit = 4
fourth_row_suits.append(suit)
print('Row 5')
fifth_row[0].show_card()
fifth_row[0].image = pygame.transform.scale(fifth_row[0].image, (card_width, card_height))
image = display.blit(fifth_row[0].image, (fifth_row_xpos, fifth_row_ypos))
if fifth_row[0].suit == 'Clubs':
    suit = 1
elif fifth_row[0].suit == 'Diamonds':
    suit = 2
elif fifth_row[0].suit == 'Hearts':
    suit = 3
elif fifth_row[0].suit == 'Spades':
    suit = 4
fifth_row_suits.append(suit)

#main loop

while gamerunning == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gamerunning = 0
    print("\n", "\n")
    if cardcount < 25:
        active_card = myDeck.draw_card_from_deck()
        active_card.show_card()
        active_card.image = pygame.transform.scale(active_card.image, (card_width, card_height))
        image = display.blit(active_card.image, (deck_xpos, deck_ypos + 300))
        pygame.display.update()
        cardcount += 1
        row_check = 1
        which_row = int(input('Choose the row you want this card: '))
        print()
    while row_check == 1: # row_check is used to make sure no rows are being over filled by constantly checking the length of each row list
        if which_row == 1:# Checks which row is picked
            if len(first_row) >= 5:# prevents row from exceeding 5
                print('This row is full')
                which_row = int(input('Choose a different row as this one is full: '))
            else: # row is not full. appends drawn card to the chosen row's list. checks the suit of the drawn card and assigns it a value before adding it to a list of row specific suits.
                first_row.append(active_card)
                row_check = 0
                first_row.sort(key=operator.attrgetter('value'))
                if active_card.suit == 'Clubs':
                    suit = 1
                elif active_card.suit == 'Diamonds':
                    suit = 2
                elif active_card.suit == 'Hearts':
                    suit = 3
                elif active_card.suit == 'Spades':
                    suit = 4
                first_row_suits.append(suit)
                pygame.display.update()
                    
        elif which_row == 2:
            if len(second_row) >= 5:
                print('This row is full')
                which_row = int(input('Choose a different row as this one is full: '))
            else:
                second_row.append(active_card)
                row_check = 0
                second_row.sort(key=operator.attrgetter('value'))
                if active_card.suit == 'Clubs':
                    suit = 1
                elif active_card.suit == 'Diamonds':
                    suit = 2
                elif active_card.suit == 'Hearts':
                    suit = 3
                elif active_card.suit == 'Spades':
                    suit = 4
                second_row_suits.append(suit)
                pygame.display.update()
        elif which_row == 3:
            if len(third_row) >= 5:
                print('This row is full')
                which_row = int(input('Choose a different row as this one is full: '))
            else:
                third_row.append(active_card)
                row_check = 0
                third_row.sort(key=operator.attrgetter('value'))
                if active_card.suit == 'Clubs':
                    suit = 1
                elif active_card.suit == 'Diamonds':
                    suit = 2
                elif active_card.suit == 'Hearts':
                    suit = 3
                elif active_card.suit == 'Spades':
                    suit = 4
                third_row_suits.append(suit)
                pygame.display.update()
        elif which_row == 4:
            if len(fourth_row) >= 5:
                print('This row is full')
                which_row = int(input('Choose a different row as this one is full: '))
            else:
                fourth_row.append(active_card)
                row_check = 0
                fourth_row.sort(key=operator.attrgetter('value'))
                if active_card.suit == 'Clubs':
                    suit = 1
                elif active_card.suit == 'Diamonds':
                    suit = 2
                elif active_card.suit == 'Hearts':
                    suit = 3
                elif active_card.suit == 'Spades':
                    suit = 4
                fourth_row_suits.append(suit)
                pygame.display.update()
        elif which_row == 5:
            if len(fifth_row) >= 5:
                print('This row is full')
                which_row = int(input('Choose a different row as this one is full: '))
            else:
                fifth_row.append(active_card)
                row_check = 0
                fifth_row.sort(key=operator.attrgetter('value'))
                if active_card.suit == 'Clubs':
                    suit = 1
                elif active_card.suit == 'Diamonds':
                    suit = 2
                elif active_card.suit == 'Hearts':
                    suit = 3
                elif active_card.suit == 'Spades':
                    suit = 4
                fifth_row_suits.append(suit)
                pygame.display.update()
    for card in range(len(first_row)):# prints each row after selection for location of the card
        if card == 0:
            print('Row 1')
        first_row[card].show_card()
        first_row[card].image = pygame.transform.scale(first_row[card].image, (card_width, card_height))
        image = display.blit(first_row[card].image, (first_row_xpos, first_row_ypos+(spacing*card)))
        pygame.display.flip()
    for card in range(len(second_row)):
        if card == 0:
            print('Row 2')
        second_row[card].show_card()
        second_row[card].image = pygame.transform.scale(second_row[card].image, (card_width, card_height))
        image = display.blit(second_row[card].image, (second_row_xpos, second_row_ypos+(spacing*card)))
        pygame.display.flip()
    for card in range(len(third_row)):
        if card == 0:
            print('Row 3')
        third_row[card].show_card()
        third_row[card].image = pygame.transform.scale(third_row[card].image, (card_width, card_height))
        image = display.blit(third_row[card].image, (third_row_xpos, first_row_ypos+(spacing*card)))
        pygame.display.flip()
    for card in range(len(fourth_row)):
        if card == 0:
            print('Row 4')
        fourth_row[card].show_card()
        fourth_row[card].image = pygame.transform.scale(fourth_row[card].image, (card_width, card_height))
        image = display.blit(fourth_row[card].image, (fourth_row_xpos, fourth_row_ypos+(spacing*card)))
        pygame.display.flip()
    for card in range(len(fifth_row)):
        if card == 0:
            print('Row 5')
        fifth_row[card].show_card()
        fifth_row[card].image = pygame.transform.scale(fifth_row[card].image, (card_width, card_height))
        image = display.blit(fifth_row[card].image, (fifth_row_xpos, first_row_ypos+(spacing*card)))
        pygame.display.flip()
    if cardcount >=25: # game is done being played as all the rows are filled
        gamerunning = 0
        print('\n', 'Game is complete','\n')

        
        for i in range(13): # identifies the amount of cards of a specific value appear
           how_many_cards = sum(c.value == i +2 for c in first_row)
           if how_many_cards > 0:# filters out the 0 in the counting line above
               hand1.append(how_many_cards)
        hand1.sort()#hand is sorted from largest to smallest numbers for later hand detection purposes
        hand1.reverse()
        first_row_suits.sort()
        first_row_suits.reverse()
        #print(hand1,first_row_suits, '\n', '*********')
        for i in range(13):
           how_many_cards = sum(c.value == i +2 for c in second_row)
           if how_many_cards > 0:
               hand2.append(how_many_cards)
        hand2.sort()
        hand2.reverse()
        second_row_suits.sort()
        second_row_suits.reverse()
        #print(hand2,second_row_suits, '\n', '*********')
        for i in range(13):
           how_many_cards = sum(c.value == i +2 for c in third_row)
           if how_many_cards > 0:
               hand3.append(how_many_cards)
        hand3.sort()
        hand3.reverse()
        third_row_suits.sort()
        third_row_suits.reverse()
        #print(hand3,third_row_suits, '\n', '*********')
        for i in range(13):
           how_many_cards = sum(c.value == i +2 for c in fourth_row)
           if how_many_cards > 0:
               hand4.append(how_many_cards)
        hand4.sort()
        hand4.reverse()
        fourth_row_suits.sort()
        fourth_row_suits.reverse()
        #print(hand4,fourth_row_suits, '\n', '*********')
        for i in range(13):
           how_many_cards = sum(c.value == i +2 for c in fifth_row)
           if how_many_cards > 0:
               hand5.append(how_many_cards) 
        hand5.sort()
        hand5.reverse()
        fifth_row_suits.sort()
        fifth_row_suits.reverse()
        #print(hand5,fifth_row_suits, '\n', '*********')



        if first_row_suits[0] - first_row_suits[4] == 0:# checks for flushes in each row
            first_row_flush = True
            #print('Flush, row 1')
        else:
            first_row_flush = False
        if second_row_suits[0] - second_row_suits[4] == 0:
            second_row_flush = True
            #print('Flush, row 2')
        else:
            second_row_flush = False
        if third_row_suits[0] - third_row_suits[4] == 0:
            third_row_flush = True
            #print('Flush, row 3')
        else:
            third_row_flush = False
        if fourth_row_suits[0] - fourth_row_suits[4] == 0:
            fourth_row_flush = True
            #print('Flush, row 4')
        else:
            fourth_row_flush = False
        if fifth_row_suits[0] - fifth_row_suits[4] == 0:
            fifth_row_flush = True
            #print('Flush, row 5')
            
        if len(hand1) > 4: #essentially if there are 5 unique cards in the row. this checks for straights that occur in each row
            if hand1[0] - hand1[4] == 0:
                if first_row[4].value - first_row[0].value == 4:
                    first_row_straight = True
        if len(hand2) > 4:
            if hand2[0] - hand2[1] == 0:
                if second_row[4].value - second_row[0].value == 4:
                    second_row_straight = True
        if len(hand3) > 4:
            if hand3[0] - hand3[1] == 0:
                if third_row[4].value - third_row[0].value == 4:
                    third_row_straight = True
        if len(hand4) > 4:
            if hand4[0] - hand4[0] == 0:
                if fourth_row[4].value - fourth_row[0].value == 4:
                    fourth_row_straight = True
        if len(hand5) > 4:
            if hand5[0] - hand5[4] == 0:
                if fifth_row[4].value - fifth_row[0].value == 4:
                    fifth_row_straight = True


                    
        #checks for the special "wheel" straight: Ace, 2 , 3, 4, 5
        if first_row[0].value == 2 and first_row[1].value == 3 and first_row[2].value == 4 and first_row[3].value == 5 and first_row[4].value == 14:
            first_row_straight = True
            first_row[0], first_row[4] = first_row[4], first_row[0]
            hand1.sort()
            hand1.reverse()
            pygame.display.update()
        if second_row[0].value == 2 and second_row[1].value == 3 and second_row[2].value == 4 and second_row[3].value == 5 and second_row[4].value == 14:
            second_row_straight = True
        if third_row[0].value == 2 and third_row[1].value == 3 and third_row[2].value == 4 and third_row[3].value == 5 and third_row[4].value == 14:
            third_row_straight = True
        if fourth_row[0].value == 2 and fourth_row[1].value == 3 and fourth_row[2].value == 4 and fourth_row[3].value == 5 and fourth_row[4].value == 14:
            fourth_row_straight = True
        if fifth_row[0].value == 2 and fifth_row[1].value == 3 and fifth_row[2].value == 4 and fifth_row[3].value == 5 and fifth_row[4].value == 14:
            fifth_row_straight = True



        if first_row[0].value == 10 and first_row[1].value == 11 and first_row[2].value == 12 and first_row[3].value == 13 and first_row[4].value == 14:
            first_row_broadway = True
        if second_row[0].value == 10 and second_row[1].value == 11 and second_row[2].value == 12 and second_row[3].value == 13 and second_row[4].value == 14:
            second_row_broadway = True
        if third_row[0].value == 10 and third_row[1].value == 11 and third_row[2].value == 12 and third_row[3].value == 13 and third_row[4].value == 14:
            third_row_broadway = True
        if fourth_row[0].value == 10 and fourth_row[1].value == 11 and fourth_row[2].value == 12 and fourth_row[3].value == 13 and fourth_row[4].value == 14:
            fourth_row_broadway = True
        if fifth_row[0].value == 10 and fifth_row[1].value == 11 and fifth_row[2].value == 12 and fifth_row[3].value == 13 and fifth_row[4].value == 14:
            fifth_row_broadway = True


            
        if hand1[0] == 4:# checks for any non straight or flush hands
            print('Four of a Kind, row 1')
            score += 50
        elif hand1[0] == 3 and hand1[1] == 2:
            print('Full House, row 1')
            score += 30 
        elif hand1[0] == 3:
            print('Three of a Kind, row 1')
            score += 10
        elif hand1[0] == 2 and hand1[1] == 2:
            print('Two Pair, row 1')
            score += 5
        elif hand1[0] == 2:
            print('Pair, row 1')
            score += 2
        elif first_row_flush == True and first_row_straight == True and first_row_broadway == True:
            print('Royal Flush, row 1')
            score += 100
        elif first_row_flush == True and first_row_straight == True:
            print('Straight Flush, row 1')
            score += 75
        elif first_row_flush == True:
            print('Flush, row 1')
            score += 20
        elif first_row_straight == True:
            print('Straight, row 1')
            score += 15
        else:
            print('No points, row 1')
            score += 0

        if hand2[0] == 4:
            print('Four of a kind, row 2')
            score += 50 
        elif hand2[0] == 3 and hand2[1] == 2:
            print('Full House, row 2')
            score += 30
        elif hand2[0] == 3:
            print('Three of a Kind, row 2')
            score += 10
        elif hand2[0] == 2 and hand2[1] == 2:
            print('Two Pair, row 2')
            score += 5
        elif hand2[0] == 2:
            print('Pair, row 2')
            score += 2
        elif second_row_flush == True and second_row_straight == True and second_row_broadway == True:
            print('Royal Flush, row 2')
            score += 100
        elif second_row_flush == True and second_row_straight == True:
            print('Straight Flush, row 2')
            score += 75
        elif second_row_flush == True:
            print('Flush, row 2')
            score += 50
        elif second_row_straight == True:
            print('Straight, row 2')
            score += 15
        else:
            print('no points, row 2')
            score += 0

        if hand3[0] == 4:
            print('Four of a Kind, row 3')
            score += 50
        elif hand3[0] == 3 and hand3[1] == 2:
            print('Full House, row 3')
            score += 30
        elif hand3[0] == 3:
            print('Three of a Kind, row 3')
            score += 10 
        elif hand3[0] == 2 and hand3[1] == 2:
            print('Two Pair, row 3')
            score += 5
        elif hand3[0] == 2:
            print('Pair, row 3')
            score += 2
        elif third_row_flush == True and third_row_straight == True and third_row_broadway == True:
            print('Royal Flush, row 3')
            score += 100
        elif third_row_flush == True and third_row_straight == True:
            print('Straight Flush, row 3')
            score += 75
        elif third_row_flush == True:
            print('Flush, row 3')
            score += 20
        elif third_row_straight == True:
            print('Straight, row 3')
            score += 15
        else:
            print('no points, row 3')
            score += 0

        if hand4[0] == 4:
            print('Four of a Kind, row 4')
            score += 50
        elif hand4[0] == 3 and hand4[1] == 2:
            print('Full House, row 4')
            score += 30
        elif hand4[0] == 3:
            print('Three of a Kind, row 4')
            score += 10
        elif hand4[0] == 2 and hand4[1] == 2:
            print('Two Pair, row 4')
            score += 5
        elif hand4[0] == 2:
            print('Pair, row 4')
            score += 2
        elif fourth_row_flush == True and fourth_row_straight == True and fourth_row_broadway == True:
            print('Royal Flush, row 4')
            score += 100
        elif fourth_row_flush == True and fourth_row_straight == True:
            print('Straight Flush, row 4')
            score += 75
        elif fourth_row_flush == True:
            print('Flush, row 4')
            score += 20
        elif fourth_row_straight == True:
            print('Straight, row 4')
            score += 15
        else:
            print('no points, row 4')
            score += 0

        if hand5[0] == 4:
            print('Four of a Kind, row 5')
            score += 50
        elif hand5[0] == 3 and hand5[1] == 2:
            print('Full House, row 5')
            score += 30
        elif hand5[0] == 3:
            print('Three of a Kind, row 5')
            score += 10
        elif hand5[0] == 2 and hand5[1] == 2:
            print('Two Pair, row 5')
            score += 5
        elif hand5[0] == 2:
            print('Pair, row 5')
            score += 2
        elif fifth_row_flush == True and fifth_row_straight == True and fifth_row_broadway == True:
            print('Royal Flush, row 5')
            score += 100
        elif fifth_row_flush == True and fifth_row_straight == True:
            print('Straight Flush, row 5')
            score += 75
        elif fifth_row_flush == True:
            print('Flush, row 5')
            score += 20
        elif fifth_row_straight == True:
            print('Straight, row 5')
            score += 15
        else:
            print('no points, row 5')
            score += 0
        
        print('\n', 'You scored: ',score)
    
    else:
        gamerunning = 1
        pygame.display.update()
        


