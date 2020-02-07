#! /bin/python3.6

def get_initial(name, force_uppercase=True):  #passing a default variable, positional notation
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

nume = input("enter surname: ")
initiala_nume = get_initial(nume)

prenume = input ("enter name: ")
initiala_prenume = get_initial(prenume)

print("initials are " + initiala_nume + initiala_prenume)

#shorter version - nested:
#print("initialele sunt " \
#+ get_initial(nume) \
#+ get_initial(prenume))