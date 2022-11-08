#for given list num 25 22 14 65 97 72
#write a py prgoram to replace all integers divisible by 3 with ppp divisible by 5 with qqq and divisible by 3 and 5 with pppqqq

from os import remove


myNums = [25,22,14,65,97,72]

for iter in range(len(myNums)):
    if myNums[iter]%3==0 and myNums[iter]%5==0:
        myNums[iter] = 'pppqqq'
    elif myNums[iter]%3==0:
        myNums[iter]='ppp'
    elif myNums[iter]%5==0:
        myNums[iter]='qqq'

print(myNums)

remove [22] in myNums