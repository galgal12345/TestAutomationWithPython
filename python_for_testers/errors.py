def print_massage(arg):
    try:
        print("OK " + arg)
    except TypeError:
        print("Casting issue need to correct code")


print_massage("gil")


