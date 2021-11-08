from game_of_greed.game_logic import GameLogic

from game_of_greed.banker import Banker

class Game:

    def __init__(self,roller=None):
        self.roller=roller
        self.round_num=0
        self.banker=Banker()
        
        
        
        

    def play(self):
        
        print('Welcome to Game of Greed')
        inputChoice=input('Wanna play? ')
        if inputChoice == "n":
            print('OK. Maybe another time')

        else:
            flage=True
            
            while flage:
                self.round_num+=1
                print(f'Starting round {self.round_num}')
                print('Rolling 6 dice...')
                roll_dice=self.roller(6)
                numbers = [ str(x) for x in roll_dice]
                print(','.join(numbers))
                dice_key=input('Enter dice to keep (no spaces), or (q)uit: ')
                num_dice=6
                while num_dice>0:
                    
                    if dice_key=="q":
                        if self.banker.balance:
                            print(f'Total score is {self.banker.balance} points')
                            
                        print(f'Thanks for playing. You earned {self.banker.balance} points')
                        flage=False
                        break
                        
                    
                    elif dice_key=='b':
                        print(f'You banked {self.banker.shelved} points in round {self.round_num}')
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')
                        break
                        

                    else:
                        unbank_point=GameLogic.calculate_score(dice_key)
                        # print(unbank_point)
                        shelf_point=self.banker.shelf(unbank_point)
                        # print(shelf_point)
                        num_dice-=len(dice_key)
                        print(f'You have {shelf_point} unbanked points and {num_dice} dice remaining')
                        dice_key=input('(r)oll again, (b)ank your points or (q)uit ')
                    




            


if __name__=="__main__":
    game = Game(GameLogic.roll_dice)
    game.play()



        

