def fancy_name_plate(name):
    """Prints a fancy name plate with the name in the middle"""

    print("#" * 20)
    print("##" + "-" * 16 + "##")
    print("##" + name.center(16, "-") + "##")
    print("##" + "-" * 16 + "##")
    print("#" * 20)


name = input("Enter your name: ")
fancy_name_plate(name)
