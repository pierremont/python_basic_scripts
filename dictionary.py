

info = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}

'''printing'''
# print(info) #prints the whole dictionary
# print(info['James'])    #prints the value for the specified key
# print(info.get('Jame')) #the get method insures that if the key doesnt exist, it will print "None" instead of an error
# print(info.get('Jame', 'not found')) #displays a default value if key not found
# print(len(info))
# print(info.keys())  #print the keys
# print(info.values()) #print the values
# print(info.items()) #print the key value pairs

'''updating'''
info['phone'] = '555-5555'  #adds a new key-value or overwrites an existing one
info.update({'James': ['Jacob', 'Bill'], 'Peter':'Lucy', 'new_item':'ok'}) #updates the dictionary, takes a dictionary as argument

del info['new_item']    #deletes a key value pair

phone = info.pop('phone') #removes a record from the dictionary and passes the value to a variable

'''looping'''
# for i in info: print(i) #loops through the keys only
for i, j in info.items(): print(i, j) #loops through the keys and values