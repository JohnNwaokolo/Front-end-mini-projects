#Variable is a container for data values e.g. Strings
#Strings-------------text and numbers in quotation

first_name = "John"
email = "johnnwaokolo81@gmail.com"

print(f"Your name is {first_name} and your email is {email}.")


#Integers---------------Whole Numbers 
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You bought {quantity} bags of rice.")
print(f"There are {num_of_students} students present.")

print("=========================================================================")

#Float-------------------Decimal Values
price = 10.99
gpa = 5.0
distance = 5.5

print(f"The price is ${price}.")
print(f"Your GPA is {gpa} points.")
print(f"The distznce between here and there is {distance}km.")

print("=========================================================================")


#Boolean------------------- True or False

is_student = True

print(f"Are you a student: {is_student}")

print("=========================================================================")


#If Statements under boolean

is_student = False
for_sale = True

if is_student:
    print("You are a student.")

else:
    print("You are not a student, gerrout")


if for_sale:
    print("This item is for sale.")
else:
    print("NOT FOR SALE.")



print("=========================================================================")

