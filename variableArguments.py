def function_variable_arguments(*args):
    total = 0
    for var in args:
        total += var
    print(total)


function_variable_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
