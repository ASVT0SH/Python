person = 'Jeff'
pet_name = 'Rex'
pet_type = 'dog'
print(person,'has a',pet_type,'and his name is',pet_name,'.')

print(f"{person} has a {pet_type} and his name is {pet_name}.")

message = "{} has a {} and his name is {}." 
print(message.format(person,pet_type,pet_name))

print("%s has a %s and his name is %s." % (person,pet_type,pet_name))