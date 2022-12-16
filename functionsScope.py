rainfall = [68, 58, 0, 43, 70]
location = "Melbourne"


def print_rainfall(values):
    day = 1
    for value in rainfall:
        print(f"{day} Day : {value}")
        day += 1


def average_rainfall(values):
    import math

    return math.fsum(values) / len(values)


def change_location(new_location):
    global location
    location = new_location
    print(new_location)


print_rainfall(rainfall)
print(average_rainfall(rainfall))

# print(math.fsum(rainfall))

print(location)
change_location("New York")
print(location)
