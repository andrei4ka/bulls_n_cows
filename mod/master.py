import random


class Master(object):
    _master_number = None

    def debug(self, message):
        print('DEBUG: ' + str(message))

    def __init__(self, guess_len=4):
        """
        :param guess_len: The length of the secret number
        :type guess_len: int
        """
        self.number_length = guess_len

    @property
    def master_number(self):
        """
        Return the generated master number
        :return: Generated number
        :rtype: str
        """
        if self._master_number:
            return self._master_number
        else:
            self._master_number = self.generate_number()
            return self._master_number

    def generate_number(self):
        """
        Generate a new number-counted secret
        :return: The generated number
        :rtype: str
        """
        while True:
            result = ''
            for i in range(self.number_length):
                result += "%d" % random.randint(0, 9)
            if self.check_no_duplicates(result):
                return result

    @staticmethod
    def check_no_duplicates(master_number):
        """
        Check that the generated number contains no duplicates
        :return: The result of the check
        :rtype: bool
        """
        used_digits = set()
        for digit in master_number:
            if digit in used_digits:
                return False
            else:
                used_digits.add(digit)
        return True

    def number_bulls_cows(self, guesser_number):
        """
        Get the number of bulls and cows for the number
        given by the guesser.
        :param guesser_number: The number provided by the guesser
        :type guesser_number: str
        :return:
        """
        # self.debug("Call: number_bulls_cows(%s)" % guesser_number)
        self.debug("Master number is: %s" % self.master_number)
        cows = 0
        bulls = 0

        for letter_number in range(len(self.master_number)):
            master_letter = str(self.master_number[letter_number])
            guesser_letter = str(guesser_number[letter_number])

            # self.debug("Compare: %s with %s" % (master_letter, guesser_letter))
            if master_letter == guesser_letter:
                bulls += 1
            else:
                if guesser_letter in self.master_number:
                    cows += 1
        return bulls, cows
