# ex 1
x = 2.5
y = 3.5

if x > y:
    print(x)
else:
    print(y)
print("\n")

# ex 2
my_list = [2, 5, 9]

if my_list[0] > my_list[1]:
    print("first one is bigger")
elif my_list[0] < my_list[1]:
    print("second one is bigger")
elif my_list[0] == my_list[1]:
    print("both are equal")
print("\n")

# ex 3
for i in range(10):
    print(i + 1)
print("\n")

i = 0
while i < 10:
    print(i + 1)
    i += 1
print("\n")

for k in range(50):
    if k >= 30:
        if k % 2 == 0:
            print(k)
print("\n")

for k in range(40):
    if k >= 20:
        if k % 2 != 0:
            print(k)
print("\n")

# ex 4
my_country_list = ["Israel", "Peru", "Canada", "Germany", "Austria"]
for a in range(len(my_country_list)):
    print(my_country_list[a])
print("\n")

for b in range(len(my_country_list)):
    if my_country_list[b] == "Israel":
        print(my_country_list[b])
print("\n")

for c in range(len(my_country_list)):
    if my_country_list[c] == "China":
        print("Yes it is there")
    elif c == len(my_country_list) - 1:
        print("No, Sorry...")
    else:
        continue
print("\n")

for d in range(len(my_country_list)):
    if my_country_list[d] == "Israel":
        for country in my_country_list[d]:
            print("letter:" + country)
print("\n")

# ex 5
n = int(input("Enter a number: "))
if 0 <= n <= 6:
    print("Go to Kindergarten")
elif 7 <= n <= 18:
    print("Go to School")
elif 19 <= n <= 67:
    print("Go to Work")
elif 68 <= n <= 120:
    print("Collecting Pension")
print("\n")

# ex 6
# Teacher = 5,000 , Bank Teller = 10,000 , QA = 15,000 , Average Salary = 9,100
profession = str(input("Enter a profession: "))

if profession == "Teacher":
    print("5,000")
elif profession == "Bank Teller":
    print("10,000")
elif profession == "QA":
    print("15,000")
elif profession == "Average Salary":
    print("9,100")
print("\n")

# ex 7
my_dictionary = {1: 12345, 2: 45678, 3: 54321, "a": "Yoni", "b": "Moshe", "c": "David"}

print("ID: ", my_dictionary.get(1))
print("ID: ", my_dictionary.get(2))
print("ID: ", my_dictionary.get(3))

print("NAME: ", my_dictionary.get("a"))
print("NAME: ", my_dictionary.get("b"))
print("NAME: ", my_dictionary.get("c"))
print("\n")

# ex 8
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for specific_set in my_set:
    if specific_set % 3 == 0 or specific_set % 5 == 0:
        print(specific_set)
print("\n")

# ex 9
my_hello_list = ["o", "l", "l", "e", "H"]

length = len(my_hello_list)
s = length

new_list = [None] * length

for item in my_hello_list:
    s = s - 1
    new_list[s] = item

print(new_list)
print("\n")

# ex 10
my_numbers_list = [7, 20, 36, 2, 15]

if my_numbers_list[0] > my_numbers_list[1]:
    if my_numbers_list[0] <my_numbers_list[2]:
        print(my_numbers_list[0])
    else:
        print(my_numbers_list[2])

elif my_numbers_list[1] > my_numbers_list[2]:
    print(my_numbers_list[1])
else:
    print(my_numbers_list[2])

max = my_numbers_list[0]
for item in my_numbers_list:
    if max < item:
        max = item
print(max)

sum = 0
for item in my_numbers_list:
        sum += item
print(sum)
print("\n")


# ex 11
num = 29
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

print("\n")

