import random
import sys

class Guesser(object):
    _maximum_number = None
    _all_possible_variants = []
    _bulls = None
    _cows = None
    _guesser_number = None
    _turn_number = 0

    def debug(self, *kwargs):
        print('INFO: ' + str(kwargs))

    def __init__(self, guess_len=4):
        self.guess_len = guess_len

    @property
    def maximum_number(self):
        """
        The property that has the generated maximum number
        :return: Generated number
        :rtype: int
        """
        if self._maximum_number:
            return self._maximum_number
        else:
            self._maximum_number = self.generate_maximum_number()
            return self._maximum_number

    def generate_maximum_number(self):
        """
        Return the generated maximum number with correct number of zeros
        :return: Generated maximum number
        :rtype: int
        """
        return 10 ** self.guess_len

    @property
    def possible_variants(self):
        """
        Return all possible possible solutions from the minimal number to
        maximum with the same number of digits
        :return: Generated list of possible solutions
        :rtype: list
        """
        permutation = []
        for possible in range(self.maximum_number):
            str_possible = str(possible)
            if len(set(str_possible)) == self.guess_len:
                if len(set(str_possible)) == len(str_possible):
                    permutation.append(int(possible))
        self._all_possible_variants = permutation
        print('all:', self._all_possible_variants)
        return self._all_possible_variants

    def check_by_bulls_and_cows(self):
        """This function remove all unneeded variants from list of
        possibilities if we have the same number of bulls and cows
        when we run the check against the computer guess."""

        self._all_possible_variants.remove(int(self._guesser_number))

        for potentialy_deleted in self._all_possible_variants:
            cows = 0
            bulls = 0
            master_number = str(potentialy_deleted)

            for letter_number in range(len(self._guesser_number)):
                master_letter = master_number[letter_number]
                guesser_letter = str(self._guesser_number[letter_number])
                if master_letter == guesser_letter:
                    bulls += 1
                elif guesser_letter in str(potentialy_deleted):
                    cows += 1

            """Remove numbers with not the same result B and C against our guess"""
            if (bulls != self._bulls) or (cows != self._cows):
                self.debug("Computer will delete this number: ", potentialy_deleted)
                self._all_possible_variants.remove(potentialy_deleted)


    def guess(self, bulls, cows):
        """Ask the computer for a guess, and check it with the
        given function, that gets the guess and returns
        the bulls and cows in a (bulls, cows) representation.
        Print the results to the user.
        Return True if the player won, and False otherwise.
        """
        self._bulls = bulls
        self._cows = cows

        self._turn_number += 1
        self.debug('Turn number: ', self._turn_number)
        self.debug('Possible variants left', len(self._all_possible_variants))

        if bulls == None:
            turn = random.choice(self.possible_variants)
        else:
            self.check_by_bulls_and_cows()
            turn = random.choice(self._all_possible_variants)

        self._guesser_number = str(turn)
        return self._guesser_number
