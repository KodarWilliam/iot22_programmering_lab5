from die import Die


class YahtzeeMainClass:
    def __init__(self, dice_list=None):
        if dice_list is None:
            dice_list = [Die(), Die(), Die(), Die(), Die()]

        self.dice_list = dice_list
        self.keepItGoing = True
        self.turn = 0
        self.yahtzee = None
        self.throwAgain = None
        self.playAgain = None

    def play(self):
        while self.keepItGoing:
            print("Welcome to Yahtzee")
            self.dice_throws()
            if self.yahtzee is not True:
                self.throw_again()
            else:
                print(f"You got YAHTZEE! in {self.dice_list[0].value}'s")

            while self.turn < 3:
                self.throw_again()
                self.play_again()

    def dice_throws(self):
        while self.turn < 3:
            print(f"Starting turn: {self.turn + 1} of 3, rolling dice")
            for dice_number, die_value in enumerate(self.dice_list):
                die_value.die_roll()
                print(f"{dice_number + 1}:{die_value}")
            break
        self.check_yahtzee()

    def check_yahtzee(self):
        while self.turn < 3:
            self.yahtzee = True
            for i in range(1, 5):
                if self.dice_list[i].value != self.dice_list[i - 1].value:
                    self.yahtzee = False
            return self.yahtzee

    def throw_again(self):
        self.throwAgain = input("Want to throw again? (y for yes, anything else for no) ")

        if self.throwAgain == "y":
            self.turn += 1
            self.dice_throws()
        else:
            self.keepItGoing = False
            self.turn = 3

    def play_again(self):
        self.playAgain = input("Game over! Want to play again? (y/n): ")

        if self.playAgain == "y":
            self.turn = 0
            self.play()
        else:
            self.keepItGoing = False
            self.turn = 3


def main():
    y = YahtzeeMainClass()
    y.play()


if __name__ == '__main__':
    main()
