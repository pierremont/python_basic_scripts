
#python 2 and 3, windows script
import os
#os.getcwd() #gets the current directory

os.chdir('E:\\petrus\\VAS\\howto_technology\\devops\\python')

#file = open("test.txt", "w+") #overwrites the file
file = open("test.txt", "a")
file.write ("added line \n")
file.close()