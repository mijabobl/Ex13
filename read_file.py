#read file and print what type the data is
infile = open('pelican.txt', 'r')
buffer = infile.read()
print(type(buffer))
print(buffer)

#read file and print out a line
infile = open('pelican.txt', 'r')
line = infile.readline()
print(line)

#read file in to a list, display the type and how many list items there are
listlines = open('pelican.txt').read().splitlines()
print(listlines)
print(type(listlines))
print(len(listlines))

#same but shows the new lines.....\n
listlines = open('pelican.txt').readlines()
print(listlines)
print(type(listlines))
print(len(listlines))

#loop displaying all data sripping out blank lines (and \n, not sure how to keep these in)
with open('pelican.txt', 'r') as inF:

    for line in inF:
        print(line.rstrip(), end="")
        