#!/usr/bin/env python
import sys


class StopGame(Exception):
    pass


class Game(object):
    bulls = None
    cows = None

    def __init__(self, master_type, guesser_type, guess_len=4):
        self.master = master_type(guess_len)
        self.guesser = guesser_type(guess_len)
        self.guess_len = guess_len

    def __iter__(self):
        return self

    def next(self):
        guess_number = self.guesser.guess(self.bulls, self.cows)
        if guess_number == 'exit':
            raise StopIteration
        self.bulls, self.cows = self.master.number_bulls_cows(guess_number)
        return guess_number, self.bulls, self.cows

    def main(self):
        for turn in self:
            guess_number, self.bulls, self.cows = turn
            guess_number = ''.join(map(str, guess_number))
            print('Guesser said: Number: %s' % guess_number)
            print('Master said: Bulls: %d Cows: %d' % (self.bulls, self.cows))
            if self.bulls == self.guess_len:
                raise StopGame


def load_class(cls_path):
    module_name, class_name = cls_path.rsplit('.', 1)
    __import__(module_name)
    module = sys.modules[module_name]
    return getattr(module, class_name)

if __name__ == '__main__':

    guess_len = 4

    if len(sys.argv) != 3:
        print >>sys.stderr, \
            "Syntax: ./game.py mod.master.Master mod.human.Human for Human Player\n" \
            "or ./game.py mod.master.Master mod.comp.Guesser for Computer"
        sys.exit(1)

    master_type = load_class(sys.argv[1])
    guesser_type = load_class(sys.argv[2])
    game = Game(master_type, guesser_type, guess_len)
    try:
        game.main()
    except StopGame:
        print('You won!')
