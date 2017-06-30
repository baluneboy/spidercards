#!/usr/bin/env python

import random
import numpy as np

ALPHAMAP = {
'A':('TTT',[0,0,0]),
'B':('TTM',[0,0,1]),
'C':('TTB',[0,0,2]),
'D':('TMT',[0,1,0]),
'E':('TMM',[0,1,1]),
'F':('TMB',[0,1,2]),
'G':('TBT',[0,2,0]),
'H':('TBM',[0,2,1]),
'I':('TBB',[0,2,2]),
'J':('MTT',[1,0,0]),
'K':('MTM',[1,0,1]),
'L':('MTB',[1,0,2]),
'M':('MMT',[1,1,0]),
'N':('MMM',[1,1,1]),
'O':('MMB',[1,1,2]),
'P':('MBT',[1,2,0]),
'Q':('MBM',[1,2,1]),
'R':('MBB',[1,2,2]),
'S':('BTT',[2,0,0]),
'T':('BTM',[2,0,1]),
'U':('BTB',[2,0,2]),
'V':('BMT',[2,1,0]),
'W':('BMM',[2,1,1]),
'X':('BMB',[2,1,2]),
'Y':('BBT',[2,2,0]),
'Z':('BBM',[2,2,1])
}

def get_list(L, zero_pad=False):
    if zero_pad:
        fmtstr = '{:>03}'
    else:
        fmtstr = '{:>3}'
    return ' '.join(map(fmtstr.format, L))

def baseN(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

#print get_list( ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-'] )
#print get_list( [baseN(i, 3) for i in range(27)], zero_pad=True )
#raise SystemExit

def get_card_and_letter(L):
    # raw_input returns the empty string for "enter"
    print get_list(L)
    choice = raw_input('Choose a card from list above: ').upper()
    if choice in L:
        return choice
    else:
        print "You did not pick a card in set, try again:"
        return get_card_and_letter(L)

class Cards(object):

    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
        suites = ['H', 'S', 'C', 'D']
        self.deck = [j + i for j in values for i in suites]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, n_players, n_cards):
        n_cards_used = n_players * n_cards
        if n_cards_used > len(self.deck):
            raise Exception('Not enough cards in deck for %d players, %d cards each.' % (n_players,n_cards))
        self.used = self.deck[0:n_cards_used]
        self.hands = [self.used[i::n_players] for i in range(0, n_players)]
        self.n_players = n_players
        self.n_cards = n_cards

    def show_hands(self):
        hand_num = 0
        for h in self.hands:
            print 'hand #%d' % hand_num,
            print get_list(h)
            hand_num += 1

class TrickCards(Cards):

    def __init__(self):
        Cards.__init__(self)
        self.shuffle()
        n_players = 3
        n_cards = 9 # for each player
        self.deal(n_players, n_cards)

    def pile_numbers(self, r):
        """return pile numbers based which round, r, this is"""
        a = np.array([0,1,2])
        if r in a:
            x = 3**r
            return np.tile(a, [x,9/x]).transpose().reshape(1,27).squeeze()
        else:
            raise Exception('r must be in %s' % str(a))

    def show_cards(self, r):
        """show cards horizontally, and nicely based on round, r"""
        print get_list(self.pile_numbers(r))
        print get_list(self.used)
        print '-'*len(get_list(self.used))
        
    def show_piles(self, r):
        #self.used = self.hands[0] + self.hands[1] + self.hands[2]
        print 'ROUND #%d:' % (r+1),
        print get_list(self.hands[0]), ' | ', get_list(self.hands[1]), ' | ', get_list(self.hands[2])

    def tricky_restack(self, r, order):
        """this is where the magic happens, restack based on round and ternary encoding of favorite letter"""
        victim_points_to = int(raw_input('Which stack is it in [0, 1, 2]: '))
        #print 'tricky restack put pile ', victim_points_to, ' in position ', order[r]
        new_order = [x for x in [0,1,2] if x!=victim_points_to]
        new_order.insert(order[r], victim_points_to)
        self.hands[0], self.hands[1], self.hands[2] = self.hands[new_order[0]], self.hands[new_order[1]], self.hands[new_order[2]]
        #print get_list(self.hands[0]), ' | ', get_list(self.hands[1]), ' | ', get_list(self.hands[2])
        #print ''
        self.used = self.hands[0] + self.hands[1] + self.hands[2]

    def do_the_trick(self):
        fav_letter = 'K'
        mtb = ALPHAMAP[fav_letter][0]
        order = ALPHAMAP[fav_letter][1]
        my_card = get_card_and_letter(self.used)
        print '\nFor debug, your card is "%s" and fav_letter is "%s". >> %s <<\n' % (my_card, fav_letter, mtb)
        for r in range(3):
            self.show_piles(r)
            self.tricky_restack(r,order)
            self.hands = [self.used[i::self.n_players] for i in range(0, self.n_players)]
        ind_your_card = ( order[0]*(3**2) + order[1]*(3**1) + order[2]*(3**0) )
        print 'your card is:', self.used[ind_your_card]       

def non_gui_trick():
    tc = TrickCards()
    tc.do_the_trick()

if __name__ == '__main__':
    non_gui_trick()
