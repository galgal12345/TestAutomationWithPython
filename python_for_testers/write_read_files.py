def write_into_txt(my_file_name):
    file1 = open(my_file_name, "w+")
    file1.write("i am a new txt in an existing file in my project")
    file1.close()


write_into_txt(r"C:\Users\GIL\PycharmProjects\TestAutomationWithPython\my txt files\New Text Document.txt")


def read_from_txt(my_file_name):
    file1 = open(my_file_name, "r")
    print(str(file1.read()))


read_from_txt(r"C:\Users\GIL\PycharmProjects\TestAutomationWithPython\my txt files\New Text Document.txt")
