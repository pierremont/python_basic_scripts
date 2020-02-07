#written for python 3. In python 2 use raw_input

number = input("enter ")
try:
    if type(int(number)) == int and int(number) >= 0:
        print("correct integer and positive")
        print(number)
    else:
        print("integer, but negative")
except:
    print("incorrect integer")