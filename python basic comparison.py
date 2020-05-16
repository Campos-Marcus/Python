name = input("Type your name: ")
name_size = len(str(name))
 
if name_size < 3:
    print("name must be at least 3 characters")
elif name_size >= 50:
    print ("Names must be lesser than 50 characters")
else:
    print('your name looks good ')
