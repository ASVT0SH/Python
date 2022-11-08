flower = []

while True:
    print('Enter a flower')

    str = input()
    if str in flower:
            print('Flower already present in list')
    if str not in flower:
        print('Flower not present in list')
    if str!="":
        flower=flower+[str]
    else:
        break

print('Flowers entered  by you')
print(flower)

for str in flower:
    print(str)