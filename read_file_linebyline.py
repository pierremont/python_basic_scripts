#! /bin/python3.6

f = open("testfile.txt","r")
#if f.mode == "r":
content = f.readlines()
for x in content:
    print(x)