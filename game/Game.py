from Deck import Deck  
from Player import Player
from Card import Card

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
        self.community_cards = []
       
    @property    
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self,player):
        
        if isinstance(player,Player):
            self._turn = player
            
        else:
            raise ValueError ("The turn must be assigned to a player object") 
         
    def print_community_cards(self):
        print("Community cards: ")
        for card in self.community_cards:
            print(card.printCard())
            print('------------------')
    
    def check_winner(self):
        #Combine community cards with  each players cards
        human_cards = self.community_cards + self.human.cards
        pc_cards = self.community_cards + self.pc.cards
            # Check for each hand type in order of rank
        hand_checks = [
            self.check_royal_flush,
            self.check_straight_flush,
            self.check_four_of_a_kind,
            self.check_full_house,
            self.check_flush,
            self.check_straight,
            self.check_three_of_a_kind,
            self.check_two_pair,
            self.check_one_pair,
            self.high_card
        ]
        
        # go through each hand type
        for check in hand_checks:
            #see if player has this card
            result = check(human_cards)
            if result:
                return result
            #see if the pc has which hand
            result = check(pc_cards)
            if result:
                return result
                
        return None

    
    def check_rank_card(self,cards,rank):
        for card in cards:
            if card.rank == rank:
                return card
        return None
    
    def check_royal_flush(self,cards):# A, K, Q, J, 10, all of the same suit
        royal = ["A", "K", "Q", "J", "10"]
        checked_cards = []
        
        for rank in royal:
            card = self.check_rank_card(cards=cards,rank=rank)
            if card:
                checked_cards.append(card)
            else:
                return None 
            
        
        for i,rank in enumerate(royal):
            found = False
            for j,card in enumerate(cards):
                if card.rank == rank:
                    found = True
                    checked_cards.append(card)
                    break
                
            if found == True:
                continue
            else:
                return None
            
        suite = checked_cards[0].suite
        for card in checked_cards:
            if card.suite != suite:
                return None
        return True
    
    
    def check_straight_flush(self,cards):
        # Five cards in sequence of the same suit
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        # Check for straight flush by checking for both straight and royal flush
        if self.check_royal_flush(cards=pc_cards) and self.check_straight(cards=pc_cards):
            return ("PC WON THE GAME BY A STRAIGHT FLUSH!!!")

        if self.check_royal_flush(cards=human_cards) and self.check_straight(cards=human_cards):
            return ("HUMAN WON THE GAME BY A STRAIGHT FLUSH!!!")
        
        return None
    
    def check_four_of_a_kind(self,cards):
        # Four cards of the same rank
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        for rank in Card.RANK:
            # Check if there are 4 cards of the same rank for either player
            if sum(1 for card in pc_cards if card.rank == rank) == 4:
                return ("PC WON THE GAME BY A FOUR OF A KIND!!!")
            
            if sum(1 for card in human_cards if card.rank == rank) == 4:
                return ("HUMAN WON THE GAME BY A FOUR OF A KIND!!!")
            
        return None
    
    def check_full_house(self,cards):
        # Three of a kind and a pair
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        for rank in Card.RANK:
            # Check if there are 3 cards of the same rank
            if sum(1 for card in pc_cards if card.rank == rank) == 3:
                
                for rank2 in Card.RANK:
                    # check if there are 2 cards of the same rank for the full house
                    if sum(1 for card in pc_cards if card.rank == rank2) == 2:
                        return ("PC WON THE GAME BY A FULL HOUSE!!!")
            
            if sum(1 for card in human_cards if card.rank == rank) == 3:
                for rank2 in Card.RANK:
                    if sum(1 for card in human_cards if card.rank == rank2) == 2:
                        return ("HUMAN WON THE GAME BY A FULL HOUSE!!!")
            
        return None
    
    def check_flush(self,cards): 
        # Five cards of the same suit
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        pc_suites = {}
        human_suites = {}
        
        # counts suits in both players cards
        # using bubble sort to count the suits
        for card in pc_cards:
            if card.suite in pc_suites:
                # If the suit is already in the dictionary, increment the count
                pc_suites[card.suite] = pc_suites[card.suite] + 1
            else:
                pc_suites[card.suite] = 1
                
        for card in human_cards:
            if card.suite in human_suites:
                human_suites[card.suite] = human_suites[card.suite] + 1
            else:
                human_suites[card.suite] = 1
                
        for suite in pc_suites:
            if pc_suites[suite] >= 5:
                return ("PC WON THE GAME BY A FLUSH!!!")
            
        for suite in human_suites:
            if human_suites[suite] >= 5:
                return ("HUMAN WON THE GAME BY A FLUSH!!!")
            
        return None
    
    def check_straight(self,cards): # Five cards in sequence
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        # Create sets of ranks for both players to check for straights
        pc_ranks = set()
        human_ranks = set()
        
        for card in pc_cards: 
            pc_ranks.add(card.rank)
            
        for card in human_cards:
            human_ranks.add(card.rank)
            
        for i in range(len(Card.RANK) - 4):
            # Check for sequences of 5 ranks
            values = [Card.RANK.index(card.rank) for car in pc_cards]
            
            # Check if all 5 ranks in the sequence are present in the player's cards
            if all( Card.RANK[i + j] in pc_ranks for j in range(5)):
                return ("PC WON THE GAME BY A STRAIGHT!!!")
            
            
            if all( Card.RANK[i + j] in human_ranks for j in range(5)):
                return ("HUMAN WON THE GAME BY A STRAIGHT!!!")
            
    def check_three_of_a_kind(self,cards):
        # Three cards of the same rank
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        for rank in Card.RANK:
            if sum(1 for card in pc_cards if card.rank == rank) == 3:
                return ("PC WON THE GAME BY A THREE OF A KIND!!!")
            
            if sum(1 for card in human_cards if card.rank == rank) == 3:
                return ("HUMAN WON THE GAME BY A THREE OF A KIND!!!")
        
        return None
    
    def check_two_pair(self,cards): 
        # Two different pairs
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        pc_pairs = 0
        human_pairs = 0
        
        for rank in Card.RANK:
            # Check if there are 2 cards of the same rank for either player and count the number of pairs
            if sum(1 for card in pc_cards if card.rank == rank) == 2:
                pc_pairs += 1
            
            if sum(1 for card in human_cards if card.rank == rank) == 2:
                human_pairs += 1
                
        if pc_pairs >= 2:
            return ("PC WON THE GAME BY A TWO PAIR!!!")
        
        if human_pairs >= 2:
            return ("HUMAN WON THE GAME BY A TWO PAIR!!!")
        
        return None
    
    def check_one_pair(self,cards):
        # Two cards of the same rank
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        for rank in Card.RANK:
            if sum(1 for card in pc_cards if card.rank == rank) == 2:
                return ("PC WON THE GAME BY A ONE PAIR!!!")
            
            if sum(1 for card in human_cards if card.rank == rank) == 2:
                return ("HUMAN WON THE GAME BY A ONE PAIR!!!")
        
        return None
    
    def high_card(self,cards): 
        
        # Highest card when no other hand is made
        pc_cards = self.community_cards + self.pc.cards
        human_cards = self.community_cards + self.human.cards
        
        pc_high = None
        human_high = None
        
        for rank in Card.RANK:
            if any(card.rank == rank for card in pc_cards):
                pc_high = rank
            
            if any(card.rank == rank for card in human_cards):
                human_high = rank
                
        if pc_high and human_high:
            if Card.RANK.index(pc_high) > Card.RANK.index(human_high):
                return ("PC WON THE GAME BY A HIGH CARD!!!")
            elif Card.RANK.index(human_high) > Card.RANK.index(pc_high):
                return ("HUMAN WON THE GAME BY A HIGH CARD!!!")
        
        return None
            
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
    