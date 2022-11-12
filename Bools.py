raining = True
daytime = True
hot_outside= True

raining = not raining
hot_outside = not hot_outside

if daytime and not raining and not hot_outside:
    print('It\'s and nice day let\'s go out')

if not hot_outside and raining:
    print('Let\'s stay in')

if raining and hot_outside:
    print('Let\'s dance')