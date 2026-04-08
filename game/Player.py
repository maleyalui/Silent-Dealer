class Player():
    def __init__(self,name,type="pc",cards=[],chips_bet=0,chips=0):
        
        self.name = name
        self.type = type
        self.cards = cards
        self.chips_bet = chips_bet
        self.chips = chips
        