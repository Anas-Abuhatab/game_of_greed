import random

class GameLogic:

    def __init__(self,dice_num=6):
        
        self.dice_num=dice_num


    def calculate_score():
        pass

    @staticmethod    
    def roll_dice(dice_num):
        """
        this function will take random number in range 0-6 time and return them in tuple
        
        """
        newArr=[]
       
        for i in range(dice_num):
            randomNum=random.randint(1,6)
            newArr.append(randomNum)
            
        return tuple(newArr)    
   
  
