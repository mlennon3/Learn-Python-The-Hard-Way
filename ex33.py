def number_loop(j, k):
    i = 0
    numbers = []

    for i in range (0, j, k):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers is now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num

number_loop(input("What number do you want?") + 1, input("How many should it jump by?"))
