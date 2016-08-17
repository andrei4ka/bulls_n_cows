class Human(object):
    def __init__(self, guess_len=4):
        self.guess_len = guess_len

    def is_legal(self, guesser_number):
        if len(guesser_number) != self.guess_len:
            return False
        if len(set(guesser_number)) != self.guess_len:
            return False
        return True

    def guess(self, bulls, cows):
        """Ask the user for a guess, and check it with the
        given function, that gets the guess and returns
        the bulls and cows in a (bulls, cows) representation.
        Print the results to the user.
        Return True if the player won, and False otherwise.
        """
        while True:
            inp = raw_input('Enter a guess: ')
            try:
                guesser_number = inp
            except ValueError:
                pass
            else:
                if self.is_legal(guesser_number):
                    break
            print("The number should consist of %d different digits "
                  "and the first digit can't be 0. \nOr type exit to exit." % self.guess_len)
        # print(guesser_number)
        return guesser_number
