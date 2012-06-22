#assigns the variable x to the following string, adding 10 in for the %d
x = "There are %d types of people." % 10
#variable binary is the string "binary"
binary = "binary"
#see above
do_not = "don't"
#string inside string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#string inside string
print "I said: %r." % x
#string inside string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
