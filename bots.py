import builtins
import re
from abc import abstractmethod
from collections import Counter

from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class BasePlayer:
    def __init__(self):
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print # Methods overriding
        builtins.input = self._mock_input # Methods overriding
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input

    # The default behaviour
    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)

    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)

    @classmethod
    def play(cls, num_games=1):

        mega_total = 0

        for i in range(num_games):
            player = cls()
            game = Game() # doesn't pass a mock roller
            try:
                game.play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass
            player.total_score = game.banker.balance
            mega_total += player.total_score
            player.reset()
        print(
            f"Congrats! {num_games} games (maybe) played with average score of {mega_total // num_games}"
        )


class AmmanBot(BasePlayer):
  
    def _mock_print(self, *args):
        self.old_print(*args)
        printed_data = str(args[0])
        if printed_data[0].isdigit():
            self.rolled_dice = tuple(int(ch) for ch in printed_data.split(','))
            # '2,3,1,2,6,4' ==> (2,3,1,2,6,4)

    def _mock_input(self, *args):
        self.old_print(*args)
        if args[0].startswith('Wanna play'):
            return 'y'
        elif args[0].startswith('Enter dice'):
            self.counter = Counter(self.rolled_dice)
            # count = counter.most_common()
            if list(self.counter.values()) == [2,2,2] or list(self.counter.values()) == [1,1,1,1,1,1]:
                self.bot_input = "".join([str(i) for i in self.rolled_dice])
                return self.bot_input
            else:
                self.bot_input=''
                for i in self.rolled_dice:
                    if i ==1 or i == 5:
                        self.bot_input += f"{i}"
                    elif self.counter[i]> 2:
                        self.bot_input +=f"{i}"
                return self.bot_input


            # if 1 in self.rolled_dice:
            #     return '1'
            # elif 5 in self.rolled_dice:
            #     return '5'
            # else:
            #     return 'q'
        elif args[0].startswith('(r)oll again, (b)ank your points or (q)ui'):
            if (len(self.rolled_dice) - len(self.bot_input))>3 or list(self.counter.values()) == [2,2,2] or list(self.counter.values()) == [1,1,1,1,1,1] :
            
                return "r"
            else:
                return 'b'
        else:
            return 'q'




if __name__=="__main__":
    # bot1 = BasePlayer()
    # bot1.play()
    amman_bot = AmmanBot()
    amman_bot.play(10)