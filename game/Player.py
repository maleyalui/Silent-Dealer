import random
import time


class Player():
    def __init__(self,name="",type="pc",cards=[],chips_bet=0,chips=0):
        
        self.name = name
        self.type = type
        self.cards = cards
        self.chips_bet = chips_bet
        self.chips = chips
        
    @property   
    def bet(self):
        return self.chips_bet 
    
    @bet.setter
    def bet(self,amount):
        
        if amount > self.chips:
            print("Not enough chips to bet")
            return
        self.chips_bet = self.chips_bet + amount
        self.chips = self.chips - amount
           
    def place_initial_bet(self):
        
        while True:
            chips = input(f"{self.name}, Balance is {self.chips} chips: place your initial bet: ")
            
            if chips.isdigit():
                n = int(chips)
                if n > 0 and n <= self.chips:
                    self.chips = self.chips - n
                    return n
            
                print("Invalid amount of chips entered")
                print("Please enter a valid amount of chips to bet")

            else:
                print(f"Enter a number as valid amount of chips between 1 and {self.chips}")
                
    def call_fold_rasie(self,player):
        choice = input("Press 1 to call \nPress 2 to fold \nPress 3 to raise: ")  
        if choice == "1":
            return self.call(player)
        
        if choice == "2":
            return self.fold(player)
        
        if choice == "3":
            return self.raise_stake(player)
        print(f"{choice} is incorrect. ")
        self.call_fold_rasie(player)
        
    def call(self,player):
        print("Chips bet is: ",player.chips_bet)
        diff  = self.chips_bet - player.chips_bet
        if diff > 0:
            return True
        
        diff = abs(diff)
        
        if self.chips >= diff:
            print("Cannot call. Not enough chips.")
            return "l"
        
        self.bet = diff
        print(f"You called with {diff} chips, remaining chips {self.chips}")
        
    def fold(self,player):
        print("I Fold") 
        return "l"
       
    def raise_stake(self,player):
        raise_chips = input("Enter the amount of chips you want to raise: ")   
        raise_chips = int(raise_chips)
        
        if raise_chips > self.chips:
            print("Restart the game ")
            self.raise_stake(player)
            return  
        
        self.chips = self.chips - raise_chips
        print(f"You raise with {raise_chips} chips, remaining chips {self.chips}")
        return raise_chips      
    
    def auto_match_or_rasie(self,chips):
        print("Pc thinking...")
        time.sleep(2)
        to_do = random.randint(1,2)
        raise_chips = chips + random.randint(10,250)
        
        if raise_chips > self.chips:
            to_do = 1
            
        #1 is a match
        if to_do == 1:
            if self.chips > chips:
                self.chips = self.chips - chips
                print(f"Pc matched with {chips} chips")
                return chips
            else:
                return "l"
        
        self.chips = self.chips - raise_chips
        print(f"I have a good feeling. I raise with, {raise_chips} chips")
        return raise_chips
    
    def update_chips_bet(self,amount):
        self.chips_bet = self.chips_bet + amount
        
    def reset_chips_bet(self):
        self.chips_bet = 0
        