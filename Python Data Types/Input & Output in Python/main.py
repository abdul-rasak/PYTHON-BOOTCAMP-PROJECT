my_file = open('docs.txt')
# print(my_file.read())
my_file.seek(0)
# print(my_file.readlines())

my_file.close()

#avoiding error
with open('docs.txt',) as main_file:
    my_file = main_file.read()

print(my_file)
