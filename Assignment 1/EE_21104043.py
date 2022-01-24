#Program to find average of three numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

avg = (a+b+c)/3

print("The average of three numbers is: ", avg)

print()
print()
print()

#Compute a person's income tax- 

gross_inc = float(input("Enter gross income $"))
dependents = int(input("Enter the number of dependents "))
dep_deduction = 3000
std_deduction = 10000
tax_rate = (20/100)

taxable_inc = gross_inc - std_deduction-(dep_deduction*dependents)
tax = taxable_inc*tax_rate
print("The tax is $", tax)

print()
print()
print()

#Storing details of students in a list-

SID = int(input("Enter your SID: "))
Name = str(input("Enter your name: "))
Gender = str(input("Enter your gender(F-female, M-male, U-unknown): ")) 
Course_Name = str(input("Enter your course name: "))
CGPA = float(input("Enter your CGPA: "))

List = [SID, Name, Gender, Course_Name, CGPA]

print("Student Info", List)

print()
print()
print()

#Marks of 5 students-

Student1 = float(input("Enter marks of student 1: "))
Student2 = float(input("Enter marks of student 2: "))
Student3 = float(input("Enter marks of student 3: "))
Student4 = float(input("Enter marks of student 4: "))
Student5 = float(input("Enter marks of student 5: "))

Marks = [Student1, Student2, Student3, Student4, Student5]

Marks.sort()
print(Marks)

print()
print()
print()

#List of colors - 

List = ["Red", "Green", "White", "Black", "Pink", "Yellow"]

del List[3]
print("Color", List)

List1 = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
List1[3:5]=["Purple"]
print(List1)

print()
print()
print()


print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")



