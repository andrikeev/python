class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ""
        for word in self.words:
            if len(line) == 0:
                line = word
            elif len(line) + len(word) < self.width:
                line += " "
                line += word
            else:
                print(line)
                line = word
        print(line)
        self.words = []


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ""
        for word in self.words:
            if len(line) == 0:
                line = word
            elif len(line) + len(word) < self.width:
                line += " "
                line += word
            else:
                self._print(line)
                line = word
        self._print(line)
        self.words = []

    def _print(self, line):
        for i in range(len(line), self.width):
            line = " " + line
        print(line)


if __name__ == '__main__':
    rp = RightParagraph(2)
    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.add_word('e')
    rp.add_word('fg')
    rp.add_word('hi')
    rp.add_word('j')
    rp.add_word('k')
    rp.add_word('l')
    rp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()

    lp = LeftParagraph(2)
    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.add_word('e')
    lp.add_word('fg')
    lp.add_word('hi')
    lp.add_word('j')
    lp.add_word('k')
    lp.add_word('l')
    lp.end()
    print()

    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()

    rp = RightParagraph(2)
    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.add_word('e')
    rp.add_word('fg')
    rp.add_word('hi')
    rp.add_word('j')
    rp.add_word('k')
    rp.add_word('l')
    rp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()

    lp = LeftParagraph(2)
    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.add_word('e')
    lp.add_word('fg')
    lp.add_word('hi')
    lp.add_word('j')
    lp.add_word('k')
    lp.add_word('l')
    lp.end()
    print()

    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()

    rp = RightParagraph(2)
    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.add_word('e')
    rp.add_word('fg')
    rp.add_word('hi')
    rp.add_word('j')
    rp.add_word('k')
    rp.add_word('l')
    rp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()

    lp = LeftParagraph(2)
    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.add_word('e')
    lp.add_word('fg')
    lp.add_word('hi')
    lp.add_word('j')
    lp.add_word('k')
    lp.add_word('l')
    lp.end()
    print()

    lp.add_word('a')
    lp.add_word('bc')
    lp.add_word('d')
    lp.end()
    print()

    rp.add_word('a')
    rp.add_word('bc')
    rp.add_word('d')
    rp.end()
    print()
