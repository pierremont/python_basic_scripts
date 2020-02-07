#! /bin/python3.6

def get_initial(name,force_uppercase=True):  #passing a default variable
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

nume = input("enter surname: ")
litera_mare = input("vwould you like it to be capsed? ")
initiala_nume = get_initial(nume,int(litera_mare))      #positional notation
#initiala_nume = get_initial(name=nume,force_uppercase=int(litera_mare))        #named notation
#initiala_nume = get_initial(name=nume,force_uppercase=True)        #named notation

prenume = input ("enter name: ")
litera_mare2 = input("would you like it to be capsed? ")
initiala_prenume = get_initial(prenume,int(litera_mare2))

print("initials are " + initiala_nume + initiala_prenume)

#shorter version - nested:
#print("initials are " \
#+ get_initial(nume) \
#+ get_initial(prenume))