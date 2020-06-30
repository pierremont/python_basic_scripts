#! /usr/local/bin/python2.7
import sys

##checking the arguments: here you should check if there is an argument and if it's an integer


# print ('number of arguments: ', len(sys.argv), ' arguments')
# print ('argument list: ', str(sys.argv))
# print ('first argument after script name: ', sys.argv[1])

number_of_lines = int(sys.argv[1])


f = open("/root/oasis_provisioning_bot/oasis_log.txt","r")


for line in (f.readlines() [number_of_lines:]):
   print (line)
   




