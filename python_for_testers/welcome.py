# ex1: introduction
print("Gil")
print("Almuly")
print("27")
print("Gil ", end="")
print("Almuly ", end="")
print(" 27")
print("---------------------------------------------")

# ex2: variables
my_f_name = "Gil"
my_l_name = "Almuly"
my_age = "27"

print(my_f_name)
print(my_l_name)
print(my_age)
print("---------------------------------------------")


# ex3:data types: String_1
my_f_name = "Gil"
my_l_name = "Almuly"
my_age = str(27)

print(my_f_name.upper())
print(my_l_name.lower())
print(my_f_name[1:3])
print(my_l_name[0:5])
print("---------------------------------------------")


# ex3:data types: String_2
sentence_num_one = "Python is a general purpose computer programming language"
print(sentence_num_one.count("computer"))
print(sentence_num_one.index("computer"))
print(sentence_num_one.replace(" ", ""))
print("---------------------------------------------")


# ex3:data types: String_3
sentence_num_two = "Hello World"
print(sentence_num_two[6:11])
print("---------------------------------------------")


# ex3:data types: List
country_list = ["Greece", "Barcelona", "Seattle", "Israel", "India", "Australia"]
# 1
print(country_list[0:3])
# 2
country_list.insert(0, "Barcelona")
country_list.insert(1, "Greece")
country_list.pop(2)
country_list.pop(2)
print(country_list)
# 3
country_list.sort()
print(country_list)
# 4
print(country_list[len(country_list) - 1:])
# 5
len = len(country_list) / 2
country_list.insert(int(len), "Brazil")
print(country_list)
print("---------------------------------------------")


# ex3:data types: List
family = {1: 'gil', 2: 'noam', 3: 'ishay', 4: 'michal', 5: 'sivan'}
print(family)
count = 0
for i in family:
    count += 1
print(count)
print("---------------------------------------------")


# ex4 operators: 1
n = int(input("Enter a number: "))
print(n % 2 == 0)
print("---------------------------------------------")

# ex4 operators: 2
# 4 2 true true  false true true
x = 3
x += 1
print(x)
x /= 2
print(x)
print(x <= 2)
print(x >= 2)
x *= 3
y = 10
print(x != 5 and y < 10)
print(x != 5 or y < 10)
print(x != 5 and y >= 10)



