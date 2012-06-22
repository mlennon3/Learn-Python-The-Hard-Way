#grabs arguments from terminal input
#from sys import argv

#there will be two arguments, script and filename
#script, filename = argv

#the variable txt is the opened file given into terminal
#txt = open(filename)

# prints the name of the file
#print "Here's your file %r:" %filename
#reads the open file in the variable txt, prints it
#print txt.read()

print "Type the filename again:"
#makes new variable file_again, which is filled from raw_input
file_again = raw_input("> ")

#txt_again is the opened file typed into on line 17
txt_again = open(file_again)

#reads and prints the file given by user on line 18
print txt_again.read()

txt_again.close()
