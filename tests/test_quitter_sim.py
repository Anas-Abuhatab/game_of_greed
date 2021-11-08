from game_of_greed.game import Game

from tests.flow.flo import Flo

def test_no_for_wanna_play():
    Flo.test('tests/flow/quitter.sim.txt')

def test_one_done_sim():
    Flo.test('tests/flow/one_and_done.sim.txt')

def test_bank_one_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.sim.txt')

def test_bank_first_Two_rounds():
    Flo.test('tests/flow/bank_first_for_two_rounds.sim.txt')