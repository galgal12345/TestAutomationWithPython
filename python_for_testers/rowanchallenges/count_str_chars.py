my_dictionary = {}  # Initializing empty dictionary
my_string = "Hello World".replace(" ", "")  # removing spaces from my string
for the_char in my_string:  # for every char in my string

    # check if the char exist in my dictionary
    if the_char in my_dictionary:
        # if it exist increase
        # the specific val
        # in my dictionary by one
        my_dictionary[the_char] += 1
    else:
        # In any other case
        # initialize a new val
        # in my dictionary
        my_dictionary[the_char] = 1

# at the end of the process print Sorted keys dictionary
print(sorted(my_dictionary.items()))
