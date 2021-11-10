from game_of_greed.game_logic import GameLogic
from collections import Counter
from game_of_greed.banker import Banker
# from ..bots import BasePlayer
class Game:

    def __init__(self,roller=GameLogic.roll_dice):
        self.roller=roller
        self.round_num=0
        self.banker=Banker()
          

    def play(self):
        
        print('Welcome to Game of Greed')
        inputChoice=input('Wanna play? ')
        if inputChoice == "n":
            print('OK. Maybe another time')

        elif inputChoice == "y":
            flage=True
            did_play = False
            while flage and self.round_num < 20:
                flagedice = True
                self.round_num+=1
                print(f'Starting round {self.round_num}')
                print('Rolling 6 dice...')
                num_dice=6
                roll_dice=self.roller(num_dice)
                numbers = [str(x) for x in roll_dice]
                roll_dice = ','.join(numbers)
                print(roll_dice)
                if GameLogic.calculate_score(numbers)==0:
                    flagedice = False
                    self.banker.clear_shelf() 
                    print("Zilch!!! Round over")
                    print(f"You banked 0 points in round {self.round_num}")
                    print(f'Total score is {self.banker.balance} points')
                else:
                    dice_key=input('Enter dice to keep (no spaces), or (q)uit: ')
                
                while flagedice:
                    not_cheater = True
                    if dice_key=="q":
                        if did_play:
                            print(f'Total score is {self.banker.balance} points')

                        print(f'Thanks for playing. You earned {self.banker.balance} points')
                        flage=False
                        break
                        
                    
                    elif dice_key=='b':
                        print(f'You banked {self.banker.shelved} points in round {self.round_num}')
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')
                        break

                    elif dice_key=='r':
                        print(f'Rolling {num_dice} dice...')
                        roll_dice=self.roller(num_dice)
                        numbers = [str(x) for x in roll_dice]
                        roll_dice = ','.join(numbers)
                        print(roll_dice)
    
                        if GameLogic.calculate_score(numbers)== 0:
                            self.banker.clear_shelf()
                            print("Zilch!!! Round over")
                            print(f"You banked 0 points in round {self.round_num}")
                            print(f'Total score is {self.banker.balance} points')
                            break
                        else:
                            dice_key=input('Enter dice to keep (no spaces), or (q)uit: ')

                    else:
                        did_play = True
                        counter_input = Counter(dice_key)
                        counter_output = Counter(roll_dice)
                        for i in counter_input:
                            if counter_output[i] < counter_input[i]:
                                print("Cheater!!! Or possibly made a typo...")
                                print(roll_dice)
                                dice_key = input("Enter dice to keep (no spaces), or (q)uit: ")
                                not_cheater = False
                                break
                      
                        if not_cheater:
                            unbank_point=GameLogic.calculate_score(dice_key)
                            shelf_point=self.banker.shelf(unbank_point)
                            num_dice-=len(dice_key)
                            print(f'You have {shelf_point} unbanked points and {num_dice} dice remaining')                   
                            if list(counter_input.values()) == [2,2,2] or list(counter_input.values()) == [1,1,1,1,1,1]:
                                num_dice = 6
                            dice_key=input('(r)oll again, (b)ank your points or (q)uit ')
        
    # def zilch():


            


if __name__=="__main__":
    game = Game()
    game.play()



        

