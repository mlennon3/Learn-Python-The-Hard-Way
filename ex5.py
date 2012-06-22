name = 'Michael Lennon'
age = 23
height = 73
weight = 175
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_m = height * .0254
weight_kg = weight * 0.454

print "Let's talk about %s." % name
print "He's %d meters tall." % height_m
print "He's %d kgs heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)
    
