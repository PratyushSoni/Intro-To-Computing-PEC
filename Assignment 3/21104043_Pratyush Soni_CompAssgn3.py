                             #Question 1
'''Counting the number of occurences of each word or character'''

string = str(input("Input the string : "))
list = string.split() 
dict = {} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")
print()
print()
print()

                                #Question 2
'''Print next date of input date'''

Month_30 = [4, 6, 9, 11]                     #Months which have 30 days
Month_31 = [1, 3, 5, 7, 8, 10, 12]           #Months which have 31 days
def input_date():
    global day
    global month
    global year
    day = int(input("Enter the Day of the Month: "))
    month = int(input("Enter the Month of the Year: "))
    year = int(input("Enter The Year: "))
    if day > 28 and month == 2 and year%4 != 0:
        print("Please enter a valid date")
        input_date()
    if year>2025 or year<1800 or month<1 or month>12 or day<1 or day>31:
        print("Please enter a valid date")
    
    elif ((day > 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
        print("Please enter a valid date")
        input_date()
    elif day > 30 and month in Month_30:
        print("Please enter a valid date")
        input_date()
input_date()
if day == 28 and month == 2 and year%4 != 0:
    day = 1
    month = 3
elif ((day == 28 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day += 1
elif ((day == 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day = 1
    month = 3
elif day == 30 and month in Month_30:
    day = 1
    month += 1
elif day == 31:
    day = 1
    month += 1
else:
    day += 1
if month == 13:
    month = 1
    year += 1
print("Next Date Is: ", day,'/',month,'/',year)

print()
print()
print()

                #Question 3
'''Finding the square of numbers'''

list = (input("Enter Some Numbers: ")).split()
print("list = ", list)
tuple = [(int(x),int(x)**2) for x in list]
print("Output: ", tuple)

print()
print()
print()

                    #Question 4
'''Grades and Performance'''

grade=int(input("Enter the grade between 4 to 10: "))
if(grade>10 or grade<4):
    print("Please enter the correct grade: ")
elif(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")

print()
print()
print()

        #Question 5
'''Printing pattern in python'''

pyramid = 6
for i in range(pyramid):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(pyramid-i)-1):
        print(chr(65 + j), end='')  
    print()
print("\n")
print()
print()
print()

                                    # Question 6.
'''Program to add student details in a dictionary and performing operations on that dictionary.'''


# Question 6 -  a  python  script  that  repeatedly  ask  user  to  enter  name  and  SID and then performing further functions on them as follows:
print("Question-6\n")

SID = int(input("Enter SID: "))
Name = input("Enter Name: ")
Students = {SID:Name}

while True:
    UserInput = input("Do you want to enter another student details(y or n): ").upper()
    if UserInput == 'Y':
        SID = int(input("Enter SID: "))
        Name = input("Enter Name: ")
        Students[SID] = Name
    elif UserInput == 'N':
        break
    else:
     print('Input Is Invalid!')

#a-part

print("\n(a) Student Details: " ,Students)

#b-part

print("\n(b) Stuident Details Sorted By Names: " ,{k:v for k,v in sorted(Students.items(), key= lambda x:x[1])})

#c-part

print("\n(c) Stuident Details Sorted By SID: " ,{k:v for k,v in sorted(Students.items())})

#d-part

Search = int(input("\nPlease Enter SID Of The Student You Want To Search: " ))
print("\n(d) Student With The Given SID Is: " ,Students[Search])


print()
print()
print()

                        #Question 7
'''Fibonacci series and average of it'''
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input("Enter The Number Of Terms In The Series: "))
if (terms <= 0):    
   print("Please enter a positive integer")
else:
   print("Resultant Fibonacci sequence: ")
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg = float(sum/terms)
print("Average Of The Resultant Fibonacci Series is = ",avg)

print()
print()
print()

                                            #Question 8
'''Performing operations on sets'''

Set_1 ={1,2,3,4,5}
Set_2 ={2,4,6,8}
Set_3 ={1,5,9,13,17}

#part (a)
Set_union = Set_1.union(Set_2)
Set_int = Set_1.intersection(Set_2)
A_Part = Set_union - Set_int
print("(a)-> ", A_Part)

#part (b)
B_Part = Set_1.union(Set_2.union(Set_3)) - Set_1.intersection(Set_2) - Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print("(b)-> ", B_Part)

#part (c)
C_Part=((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3)))) - (Set_1.intersection(Set_2.intersection(Set_3)))
print("(c)-> ", C_Part)

#part (d)
D_Part=set()
for i in range(1,11):
    if i not in Set_1:
        D_Part.add(i)
print("(d)-> ", D_Part)


#part e
E_Part=set()
for i in range(1,11):
    E_Part.add(i)
set_e = E_Part - (Set_1 | Set_2 | Set_3)
print("(e)-> ",set_e)

print()
print()
print()

