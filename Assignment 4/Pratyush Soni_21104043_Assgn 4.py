'''Python Assignment 4'''


                                # Q1
# TOWER OF HANOI
print("Question 1")
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# A, B, C are the name of the rods
n = 3
TowerOfHanoi(n,'A','B','C')
print()
print()
print()



                                  # Q2
# PASCAL'S TRIANGLE
print("Question 2")
def pascals_triangle(n):
    """ Defining a function to return an array containing
        the first n rows of PASCAL's TRIANGLE. """

    # If the number of rows = 0 returning an empty list.
    if n == 0:
        return []

    # If number of rows = 1 returning a list containing first row of pascal's triangle.
    elif n == 1:
        return [[1]]

    # Recursive step to add next rows to the array.
    else:
        new_row = [1]
        result = pascals_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row += [1]
        result.append(new_row)
        return result


# Taking input of number of rows from the user.
no_of_rows = int(input("Enter the number of rows you want: "))

# Condition to check if the no of rows entered are positive.
if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

# Printing out the array containing the pascal's triangle as string.
arr = pascals_triangle(no_of_rows)
width = len(str(arr[-1])) - 2

for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

# Iterative Procedure.

print("\n\tIterative Procedure\n")

# Taking input of number of rows from the user.
no_of_rows = int(input("Enter the number of rows you want: "))

# Condition to check if the no of rows entered are positive.
if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

# Creating an initial array containing first row.
arr = [[1]]

# Using while loop to append next 'n-1' rows into the array.
while len(arr) < no_of_rows:

    new_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    arr.append(new_row)

# Printing out the array containing the pascal's triangle as string.
width = len(str(arr[-1])) - 2
for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

print("-" * 80)


        # Q3
# Built - In Functions
print("Question 3")

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

q=a//b
r=a%b
print("The quotient is", q, "and the remainder is", r)

# (a) part
# callable function checks if functions/values are callable or not
print(callable(q))
print(callable(r))

# (b) part
# check if values are non-zero or not
print(q!=0)
print(r!=0)

# (c) part
my_list=[q, r]+[4, 5, 6] # adding elements in list
print(my_list)
my_list=(list(filter(lambda i: i<=4, my_list))) # filters out values  greater than 4
print(my_list)

# (d) part
my_set=set(my_list) # makes set from list
print(my_set)

# (e) part
my_set=frozenset(my_set)        # makes set immutable
print(my_set)

# (f) part
max_num=max(my_set)         # finds max value
print(max_num)
print(hash(max_num))        # finds hash value
print()
print()
print()


                        # Q4
# Class Student
print("Question 4")

class Student:      # class named student
    def __init__(self, name, roll_no):
        self.name=name          # assigns name
        self.roll_no=roll_no        # assigns roll number

s1=Student("Akash", 3080)           # object s1 is created
print("Student's name is", s1.name)
print("Roll number is", s1.roll_no)

del s1          # object s1 is deleted
print()
print()
print()



                        # Q5
# Class Employee
print("Question 5")

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name  # Name of Employee
        self.salary = salary  # Salary of Employee


# Creating Records for Employees.
E1 = Employee("Mehak", 40000)
E2 = Employee("Ashok", 50000)
E3 = Employee("Viren", 60000)

# Making a Table for Employees and their respective salaries.
print(
    "| Employee   <==>   Salary   |\n|   {}    <==>    {}   |\n|   {}    <==>    {}   |\n|   {}    <==>    {}   |".format(
        E1.name, E1.salary,
        E2.name, E2.salary,
        E3.name, E3.salary))

print()
# (a) part
E1.salary = 70000
print("The salary of {} is updated to {}".format(E1.name, E1.salary))
print()

# (b) part
print("{0}'s Record is deleted".format(E3.name))
del E3
print()
print()
print()


                    # Q6
# ANAGRAM TEST
print("Question 6")

george_word=input("Enter George's word: ").strip().lower()
barbie_word=input("Enter Barbie's word: ").strip().lower()


def anagrams(s):             # function to find list of anagrams
    if s=="":
        return [s]
    else:
        ans=[]               # list of anagrams
        for w in anagrams(s[1:]):           # iterates over anagrams of tail of the string
            for pos in range(len(w)+1):             # puts first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

correct_words=anagrams(george_word)
if barbie_word in correct_words:        # checks if Barbie's word is an anagram of George's word
    print("Their friendship is True.")
else:
    print("Their friendship is Fake.")
print()
print()
print()
print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-END OF ASSIGNMENT-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
