class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


class WordList(object):
    def __init__(self, word_list):
        self.word_list = word_list

    def peek(self):
        if self.word_list:
            word = self.word_list[0]
            return word[0]
        else:
            return None

            
    def match(self, expecting):
        if self.word_list:
            word = self.word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None


    def skip(self, word_type):
        while self.peek() == word_type:
            match(self.word_list, word_type)
        
    def parse_verb(self):
        self.skip('stop')

        if self.peek() == 'verb':
            return self.match('verb')
        else:
            raise ParserError("Expected a verb next.")


    def parse_object(self):
        self.skip('stop')
        next = self.peek()

        if next == 'noun':
            return self.match('noun')
        if next == 'direction':
            return self.match('direction')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, subj):
        verb = self.parse_verb()
        obj = self.parse_object()

        return Sentence(subj, verb, obj)


    def parse_sentence(self):
        self.skip('stop')

        start = self.peek()

        if start == 'noun':
            subj = self.match('noun')
            return self.parse_subject(subj)
        elif start == 'verb':
            # assume the subject is the player then
            return self.parse_subject(('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not : %s" %start)
