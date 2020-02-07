#prints out characters from a word separated by commas

list = []
word = 5823423
z = 0

for i in str(word):
    z = z + 1
    if z != len(str(word)):
        print (i, end = ',')
        list.append(int(i))
        #list.append(",")
    else:
        print(i)


