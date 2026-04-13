class Card():
    
    RANK = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    SUITE = ['Hearts','Diamonds','Clubs','Spades']
    def __init__(self,suite,rank):
        
        
        if not isinstance(suite,str):
            raise TypeError('Suite must be a string')
        if not isinstance(rank,str):
            raise TypeError('Rank must be a string')
        
        if suite not in Card.SUITE:
            raise ValueError('Suite must be one of the following: ' + ', '.join(Card.SUITE))
        
        if rank not in Card.RANK:
            raise ValueError('Rank must be one of the following: '+ ', '.join(Card.RANK))
        
        self.suite = suite
        self.rank = rank
        
    def printCard(self):
            return self.rank + ' of ' + self.suite
        

# if __name__ == '__main__':
#     card1 = Card('Diamonds','4')
#     print(card1.printCard())