import parser
import lexicon


stuff = raw_input('>   ')
#words = stuff.split()
direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = {}


class Word(object):
    def __init__(self, name):
        self.name = name
        self.word_type = ''
        
    def find_word_type(self):
        if self.name in direction_words:
            self.word_type = 'direction'
        elif self.name in verbs:
            self.word_type = 'verb'
        elif self.name in stop_words:
            self.word_type = 'stop'
        elif self.name in nouns:
            self.word_type = 'noun'
        elif convert_number(self.name):
            self.word_type = 'number'
        else:
            self.word_type = 'error'

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


"""inputted_word = words[0]
inputted_word = Word(inputted_word)
inputted_word.find_word_type()
print inputted_word.word_type
"""


def scanner():
    sentence = []
    for each_word in words:
        each_word = Word(each_word)
        each_word.find_word_type()
        tuple = each_word.word_type, each_word.name
        sentence.append(tuple)
    return sentence

scanned = lexicon.scan(stuff)
parsed = parser.parse_sentence(scanned)
print parsed.show()


        
        
