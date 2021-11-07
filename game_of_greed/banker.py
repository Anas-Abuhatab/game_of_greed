class Banker:
    """
    this class for storing the player point :
    it will take two values:
    balance=0
    shelved=0

    - store unbanked point in the shelf method

    - reset the shelved point to 0

    - stored the point in the method bank 
    
    """


    def __init__(self):

        self.balance=0
        self.shelved=0
        
     
    def shelf(self,value):
        
        self.shelved+=value

        return self.shelved

    def clear_shelf(self):

        self.shelved=0

    def bank(self):
        
        self.balance+=self.shelved
        self.clear_shelf()

        return self.balance


    
