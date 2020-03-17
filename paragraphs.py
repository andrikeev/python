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

    def _print(self, line):
        for i in range(len(line), self.width):
            line = " " + line
        print(line)


if __name__ == '__main__':
    paragraph = RightParagraph(8)
    paragraph.add_word("abc")
    paragraph.add_word("abc2")
    paragraph.add_word("ab2")
    paragraph.add_word("a1231bc")
    paragraph.add_word("ab31c")
    paragraph.end()
