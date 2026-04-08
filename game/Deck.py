from Card import Card
import random

class Deck():
    
    def __init__(self):
        ranks = Card.RANK
        suites = Card.SUITE
        deck = []
        
        for rank in ranks:
            for suite in suites:
                print(rank + ' of ' + suite)
                print('------------------')
                deck.append(Card(suite,rank))
                
        self.deck = deck
                
    def shuffle(self):
        if not self.deck:
            print('Deck is empty')
            return
        
        random.shuffle(self.deck)
        print('Deck shuffled successfully')
        
        # Instead of using random.shuffle, we can also implement our own shuffle algorithm using random.randint and list.pop
        
        # newDeck = []
        # deck = self.deck
        
        # while True:
        #     if len(deck) == 1:
        #         card=deck[0]
        #         newDeck.append(card)
        #         break
        
        #     n = random.randint(0,len(deck)-1)
        #     card = deck[n]
        #     deck.pop(n)
        #     newDeck.append(card)
        
        # for card in newDeck:
        #     card.printCard()
        #     print("--")
        
        # self.deck = newDeck
        
    def printDeck(self):
        for card in self.deck:
            print(card.printCard())
            print('------------------')
                    
    def burnCard(self):
        """" Moving the top card to the bottom of the deck """
        print("Card burned: " + self.deck[0].printCard())
        topCard = self.deck[0]
        self.deck.pop(0)
        self.deck.append(topCard)
    
    def giveCard(self):
        """ Giving the top card to the player and removing it from the deck """
        topCard = self.deck[0]
        self.deck.pop(0)
        return topCard
    
 #Tests   
if __name__ == '__main__':
    d1=Deck()
    d1.shuffle()
    d1.burnCard()
    card = d1.giveCard()
    print('Card given: ' + card.printCard())
    d1.printDeck()
    