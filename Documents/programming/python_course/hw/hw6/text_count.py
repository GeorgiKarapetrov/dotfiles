class WordCount():
    """Counts the number of words in a text and the longest wod"""

    def __init__(self):
        lines = []
        lines.append(input('Enter some text, followed by two empty lines:'))
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        self.text = '\n'.join(lines)

    @staticmethod
    def counter(text):
        word_list = text.split()
        longest = 0
        for _ in word_list:
            if len(_) > longest:
                longest = len(_)
        print(f'The text contains {len(word_list)} words.')
        print(f'The longest word contains {longest} characters.')


test1 = WordCount()
WordCount.counter(test1.text)
