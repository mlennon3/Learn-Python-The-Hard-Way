the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricotss']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first kind of for loop goes through a list
for number in the_count:
    print "This is the count %d" % number

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# alse we can go thorugh mixed lists too
# notice we have to use %r because we don't know whats in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then we use the range function to do 0 to 5 counts
elements.append(range(0, 6))
print "Adding %r to the element list." % i
# append is a function that lists understand


#now we can print them out too
for i in elements:
    print "Element was %r" % i
