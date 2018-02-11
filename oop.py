#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    total=[]
    player1=[]
    comp=[]
    for i in SUITE:
        for j in RANKS:
            total.append(i+j)
    def shuffle(self):
        shuffle(Deck.total)
    def splitting(self):
        self.player1=Deck.total[:26]
        self.comp=Deck.total[26:]
    dummy=len(total)
    def __str__(self):
        return str(Deck.dummy)

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self):
        self.l=[]
    def check_cards(self):
        return len(self.l)
    def assign_cards(self,card):
        self.l.extend(card)
    def show_card(self):
        return self.l[0]
    def remove(self):
        #print("Before removing cards",self.l)
        cards_removed=[(self.l.pop(0))]
        #print("After removing cards",self.l)
        return cards_removed
    def add(self,cards):
        #print("Before adding cards",self.l)
        self.l.extend(cards)
        #print("After adding cards",self.l)
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self,name,card,h):
        self.name=name
        self.card=card
        self.h=h
        self.h.assign_cards(card)
    def initial_play(self):
        card_shown=self.h.show_card()
        return card_shown
######################
#### GAME PLAY #######
######################
def get_index(p_card,c_card):
    if(p_card[-1] in RANKS):
        index1=RANKS.index(p_card[-1])
    elif(p_card[-2:] in RANKS):
        index1=RANKS.index(p_card[-2:])
    if(c_card[-1] in RANKS):
        index2=RANKS.index(c_card[-1])
    elif(c_card[-2:] in RANKS):
        index2=RANKS.index(c_card[-2:])
    return index1,index2
def compare(index1,index2):
    equal_to=""
    if(index1>index2):
        #print("Person has greater card")
        equal_to='p'
    elif(index2>index1):
        #print("Computer has greater card")
        equal_to='c'
    elif(index1==index2):
        #print("Both has card of same Rank")
        equal_to="Y"
    return equal_to
print("Welcome to War, let's begin...")
d=Deck()
d.shuffle()
d.splitting()
hp=Hand()
hc=Hand()
p=Player("Person",d.player1,hp)
c=Player("Computer",d.comp,hc)
l1=hp.check_cards()
l2=hc.check_cards()
count=0
while(l1>0 and l2>0):
    #print("Show card")
    p_card=p.initial_play()
    c_card=c.initial_play()
    #print(p_card,c_card)
    index1,index2=get_index(p_card,c_card)
    #print(index1,index2)
    played_cards=[]
    played_cards.extend(hp.remove())
    played_cards.extend(hc.remove())
    equal_to=compare(index1,index2)
    if(equal_to=='p'):
        hp.add(played_cards)
    elif(equal_to=='c'):
        hc.add(played_cards)
    else:
        while(equal_to=="Y"):
            for x in range(2):
                played_cards.extend(hp.remove())
                played_cards.extend(hc.remove())
            index1,index2=get_index(played_cards[-2],played_cards[-1])
            equal_to=compare(index1,index2)
        if(equal_to=='p'):
            hp.add(played_cards)
        elif(equal_to=='c'):
            hc.add(played_cards)
    l1=hp.check_cards()
    l2=hc.check_cards()
    count+=1
print(count)
if(hp.check_cards()>hc.check_cards()):
    print("Person has won")
    print(hp.check_cards(),hc.check_cards())
elif(hp.check_cards()<hc.check_cards()):
    print("Computer has won")
    print(hp.check_cards(),hc.check_cards())
elif(hp.check_cards()==hc.check_cards()):
    print("Draw")
    print(hp.check_cards(),hc.check_cards())
# Use the 3 classes along with some logic to play a game of war!
