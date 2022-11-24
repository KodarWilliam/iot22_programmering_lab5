from yahtzee import YahtzeeMainClass
from die import Die

import pytest


def test_is_yahtzee_when_all_dice_matches():
    dice = [Die(), Die(), Die(), Die(), Die()]

    for die in dice:
        die.value = 6

    y = YahtzeeMainClass(dice)
    assert y.check_yahtzee() is True


def test_is_not_yahtzee_when_all_dice_not_matching_each_other():
    dice = [Die(), Die(), Die(), Die(), Die()]

    for die in dice:
        die.value = 6

    dice[0].value = 2

    y = YahtzeeMainClass(dice)
    assert y.check_yahtzee() is not True


if __name__ == '__main__':
    pytest.main()
