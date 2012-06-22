def sayings(word1, word2, word3, word4, word5):
    print "%s %s %s %s %s" % (word1, word2, word3, word4, word5)


sayings("hello", "how", "are", "you", "today")

word1 = "ballers"
word2 = "are"
word3 = "not"
word4 = "born"
word5 = "everyday"

sayings(word1, word2, word3, word4, word5)

sayings(word4 + word1, word3 + word2, word5 + word5, word4, word1)

def sayings(word6):
    print "Now I'm all just about word 6\n"
    print "Which is: %s" % word6
    sayings(word4)

word6 = "green"

sayings(word6)
