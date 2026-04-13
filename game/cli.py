from Game import Game

def play_game():
    game = Game()
    
    human = game.human
    pc = game.pc
    
    game.turn = human
    
    #request to make bet
    human_amount = human.place_initial_bet()
    human.update_chips_bet(human_amount)
    
    pc_amount = pc.auto_match_or_rasie(human_amount)
    pc.update_chips_bet(human_amount)
    
    
    
    if pc_amount == "l":
        print("Human wins")
        return
    
    game.turn = human
    game.pot = human_amount + pc_amount
    
    k = 0
    print("========================")
    print("Starting round...")
    print("========================")
    
    while True:
        if k>=1 and pc.chips_bet == human.chips_bet:
            ##print("Showdown")
            break
        k = k + 1
        
    print('Human amount', human.chips)
    print('Human bet amount', human.chips_bet)
    human.call_fold_rasie(player=pc)
play_game()