from Game import Game

def play_game():
    game = Game()
    
    human = game.human
    pc = game.pc
    
    game.turn = human
    
    #request to make bet
    human_amount = human.place_initial_bet()
    #human.update_chips_bet(human_amount)
    human.chips_bet = human_amount
    
    pc_amount = pc.auto_match_or_rasie(human_amount)
    #pc.update_chips_bet(human_amount)
    
    pc.chips_bet = pc_amount
    
    
    if pc_amount == "l":
        print("Human wins")
        return
    
    game.turn = human
    #game.pot = human_amount + pc_amount
    
    k = 0
    print("========================")
    print("Starting round...")
    print("========================")
    
    while True:
        print("Showdown, Round ", k)
        print("============================")
        
        if k>=1 and pc.chips_bet == human.chips_bet:
            print("Both players have the same bet. Showdown time!")
            break
        k = k + 1
        
        human_choice = human.call_fold_rasie(player=pc)
        
        if human_choice == "l":
            print("PC WON THE GAME!!!")
            return
        
        print("============================")
        print('Human amount', human.chips)
        print('Human bet amount', human.chips_bet)
        
        pc_choice = pc.auto_call_raise(player=human,k=k)
        
        if pc_choice == "l":
            print("HUMAN WON!!!")
            return
        
        print("============================")
        print('pc amount', pc.chips)
        print('pc bet amount', pc.chips_bet)
        
    #Round 2
    print("============================")
    print("Complete round ", k)
    print("============================")
    deck = game.deck
    deck.burnCard()
    game.community_cards.append(deck.giveCard())
    game.community_cards.append(deck.giveCard())
    game.community_cards.append(deck.giveCard())
    game.print_community_cards()
    print("============================")
    game.pot += human.chips_bet + pc.chips_bet
    human.reset_chips_bet()
    pc.reset_chips_bet()
    
    print("All chips are in the pot. Pot Amount: ", game.pot)
    print("============================")
    
    print("=============================")
    print("Showdown, Round ", k)
    print("=============================")
    
    k = 0
    while True:
        if k>0 and pc.chips_bet == human.chips_bet:
            print("All bets are equal. End the betting round")
            break
        k = k + 1
        
        human_choice = human.call_fold_rasie(player=pc)
        
        if human_choice == "l":
            print("PC WON THE GAME!!!")
            return
        
        print("=========================")
        print ("Human amount ", human.chips)
        print ("Human bet amount ", human.chips_bet)
        
        pc_choice = pc.auto_call_raise(player=human,k=k)
        
        if pc_choice == "l":
            print("HUMAN WON THE GAME!!!")
            return
        
        print("Pc amount", pc.chips)
        print("Pc bet amount", pc.chips_bet)
        print("========================")
            
    print("=========================")
    print("Complete Round ", k)
    print("=========================")
    deck = game.deck
    deck.burnCard()
    game.community_cards.append(deck.giveCard())
    game.print_community_cards()
    print("=========================")
    game.pot += human.chips_bet + pc.chips_bet
    human.reset_chips_bet()
    pc.reset_chips_bet()
    
    print("All chips are in the pot. Pot Amount: ", game.pot)
    print("=========================")
    
    print("==========================")
    print("Showdown, Final Round ")
        
    k=0
    while True:
        if k>0 and pc.chips_bet == human.chips_bet:
            print("All bets are equal. End the betting round")
            break
        k = k + 1
        
        human_choice = human.call_fold_rasie(player=pc)
        
        if human_choice == "l":
            print("PC WON THE GAME!!!")
            return
        
        print("==========================")
        print ("Human amount ", human.chips)
        print ("Human bet amount ", human.chips_bet)
        
        pc_choice = pc.auto_call_raise(player=human,k=k)
        
        if pc_choice == "l":
            print("HUMAN WON THE GAME!!!")
            return
        
        print("Pc amount", pc.chips)
        print("Pc bet amount", pc.chips_bet)
        print("==========================")
            
    print("==========================")
    print("Complete 3rd Round ")
    print("==========================")
    
    deck = game.deck
    deck.burnCard()
    game.community_cards.append(deck.giveCard())
    game.print_community_cards()
    print("==========================")
    game.pot += human.chips_bet + pc.chips_bet
    human.reset_chips_bet()
    pc.reset_chips_bet()
    
    print("All chips are in the pot. Pot Amount: ", game.pot)
    print("==========================")
    
    print("==========================")
    print("Showdown, Final Round ")
    print("==========================")
    
    #check for the winner
    print("==========================")
    print("FINAL RESULT")
    winner = game.check_winner()
    print("Winner:", winner)
    
    
    
    
play_game()