filename = raw_input("What filename do you want to read?")

txt = open(filename)
print txt.read()
txt.close()
