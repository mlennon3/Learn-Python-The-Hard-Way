direction_words = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

class Word(object):
    def __init__(self, name):
        self.name = name
        self.word_type = ''
        
    def find_word_type(self):
        if self.name.lower() in direction_words:
            self.word_type = 'direction'
        elif self.name.lower() in verbs:
            self.word_type = 'verb'
        elif self.name.lower() in stop_words:
            self.word_type = 'stop'
        elif self.name.lower() in nouns:
            self.word_type = 'noun'
        elif convert_number(self.name):
            self.word_type = 'number'
            self.name = convert_number(self.name)
        else:
            self.word_type = 'error'

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    sentence = []
    for each_word in words:
        each_word = Word(each_word)
        each_word.find_word_type()
        tuple = each_word.word_type, each_word.name
        sentence.append(tuple)
    return sentence



        
        
