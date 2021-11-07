from collections import Counter
import random

a = {"1":{"1":100,"2":200,"3":1000,"4":2000,"5":3000,"6":4000},
"2":{"1":0,"2":0,"3":200,"4":400,"5":600,"6":800},
"3":{"1":0,"2":0,"3":300,"4":600,"5":900,"6":1200},
"4":{"1":0,"2":0,"3":400,"4":800,"5":1200,"6":1600},
"5":{"1":50,"2":100,"3":500,"4":1000,"5":1500,"6":2000},
"6":{"1":0,"2":0,"3":600,"4":1200,"5":1800,"6":2400}
}
class GameLogic :
    def __init__(self) :
        pass
    @staticmethod
    def calculate_score(dice):
        score=0
        counter = Counter(dice)
        print(counter)
        cont = counter.most_common()
        print(cont)
        if len(cont) == 6:
           score = 1500

        elif list(counter.values()) == [2,2,2]:
            score = 1500
     
        else:   
            for i in cont:              
                score += a[str(i[0])][str(i[1])]
        print(score)               
        return score
GameLogic.calculate_score((1,1,1,2,3,3))




