#string
my_parrot_name = 'alex'
print(my_parrot_name)

#The '\n' next_line sign
print("What's yoor name? \n My name is AbdulRasak");

#The '\t' tab sign
print("What's up \t I'm good");

#The 'len() function'
print(len(my_parrot_name));

#string slicing
company_name_1 = "Microsoft"
company_name_2 = "Google"

print(company_name_1[:5])
print(company_name_2[:2])
print(company_name_1[5:])
print(company_name_2[1:5])
print(company_name_1[::2])
print(company_name_2[0:5:2])
print(company_name_2[0:5])
#Reverse the string
print(company_name_1[::-1])

#String concatination
my_full_name = 'KamoruAbdulRasakOyinlola'
my_surename = my_full_name[:6]
my_first_name = my_full_name[6:16]
my_last_name = my_full_name[16:]
full_name = my_surename + " " + my_first_name + " " + my_last_name;

print(full_name)

#String methods
print(full_name.upper())
print(full_name.lower())

#String formarting
print("My name is {} {} {}".format('Kamoru', 'AbdulRasak', 'Oyinlola' ))
print("My {T} name is {N}".format(T = "dog", N = "Alex"))

answer = 3.2589643
print("The answer is {a:1.3f}".format(a = answer))

instruction = 'Python rules!'
print(f"Please follow {instruction}")