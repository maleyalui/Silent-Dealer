class Card():
    
    def __init__(self,suite,rank):
        
        acceptedRanks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        acceptedSuites = ['Hearts','Diamonds','Clubs','Spades']
        
        if not isinstance(suite,str):
            raise TypeError('Suite must be a string')
        if not isinstance(rank,str):
            raise TypeError('Rank must be a string')
        
        if suite not in acceptedSuites:
            raise ValueError('Suite must be one of the following: ' + ', '.join(acceptedSuites))
        
        if rank not in acceptedRanks:
            raise ValueError('Rank must be one of the following: '+ ', '.join(acceptedRanks))
        
        self.suite = suite
        self.rank = rank
        
    def printCard(self):
            return self.rank + ' of ' + self.suite
        

if __name__ == '__main__':
    card1 = Card('Diamonds','4')
    print(card1.printCard())