var='This is global'

def func():
    v = 'This is local'
    print(v)

func()
print(var)