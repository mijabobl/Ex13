
lines = ["He can take in his beak, \n", "Enough food for a week, \n" "But im dammed if i see how the helican. \n"]

with open('pelican.txt', 'a') as theF:
    theF.write('A wonderful bird is the pelican, \n')
    theF.write('His bill holds more than his belican, \n')
    theF.writelines(lines)

