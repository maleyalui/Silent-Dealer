from Deck import Deck  
from Player import Player

class Game():
    def __init__(self):
        self.pot = 0 
        deck = Deck()
        deck.shuffle()
        deck.shuffle()
        human_card = [deck.giveCard(), deck.giveCard()]
        pc_card = [deck.giveCard(), deck.giveCard()]
        self.human = Player(type="human",
                           cards=human_card,
                           chips_bet=0,
                           name="Luie",chips=1000)
        self.pc = Player(type="pc",
                           cards=pc_card,
                           chips_bet=0,
                           name="John",chips=1000)
        
        self._turn = self.human
        self.deck = deck
       
    @property    
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):
        
        if isinstance(player,Player):
            self._turn = player
            
        else:
            raise ValueError ("The turn must be assigned to a player object") 
         
# if __name__ == "__main__":
#     game = Game()
#     game.deck.printDeck()
#     print("This is the Deck")
#     print("Pc cards: ")
#     print(game.pc.cards[0].printCard())
#     print(game.pc.cards[1].printCard())
#     print("Human cards:")
#     print(game.human.cards[0].printCard())
#     print(game.human.cards[1].printCard())
    