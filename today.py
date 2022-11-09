#print(chr(1024))

str='technology'

print('original string '+str)

hindex = int(len(str)/2)

str1 = str[0:hindex]

str1+= str[hindex:len(str)].upper()

print(str1)