
class User:
    pass
user1 = User()  #create an object
user1.first_name = "Dave" #attach a field to the object

###############
import datetime
class User2:
    '''test class'''    #doc string. Can be called with the command help(User2)
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday    #yyyymmdd

        #extract first and last names
        name_pieces = full_name.split(" ")   #creates a list from the full name pieces
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        '''Return the age of the user in years'''
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)   #date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User2("dave bowman", "19710315")
print("user age is", user.age())
print()



user2 = User2("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

#help(User2)