# ex 1
def reverse_string(my_str):
    return my_str[::-1]


print(reverse_string("1234abcd"))
print("\n")


# ex 2 #WHY IT PRINT NONE
def get_integer(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("n1")
    if n2 > n3 and n2 > n1:
        print("n2")
    if n3 > n1 and n3 > n2:
        print("n3")


print(get_integer(3, 2, 1))
print("\n")


def unique(list):
    unique_list = []
    # עבור כל תו ברשימה
    for x in list:
        # אם תו זה אינו קיים ברשימה החדשה
        if x not in unique_list:
            # הכנס לי אותו לרשימה החדשה
            unique_list.append(x)

    for x in unique_list:
        print(str(x) + " ", end="")


list = [1, 2, 1, 1, 3, 4, 3, 3, 5]
unique(list)
print("\n")


def my_factorial(n, fact):
    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of " + str(n) + " is : ", end="")
    print(fact)


my_factorial(5, 1)
print("\n")

