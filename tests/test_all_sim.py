from tests.flow.flo import Flo

def test_no_for_wanna_play():
    Flo.test('tests/flow/quitter.sim.txt')

def test_yes_for_wanna_play():
    Flo.test('tests/flow/one_and_done.sim.txt')

def test_hot_dice():
    Flo.test('tests/flow/hot_dice.txt')

def test_for_bank_one_roll_then_quit():
    Flo.test("tests/flow/bank_one_roll_then_quit.sim.txt")

def test_for_bank_first_for_two_rounds():
    Flo.test("tests/flow/bank_first_for_two_rounds.sim.txt")
