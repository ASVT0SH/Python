import time

print('Can i please have a number')

num = input()
num = int(num)

prime = True

tic = time.clock()

for i in range(2,num):
    if num%i==0:
        prime=False
        break
    
if prime:
    print('prime')
else:
    print('not prime')

toc = time.clock()

print("time taken= "+(toc-tic)+" seconds")