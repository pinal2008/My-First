#first example#
number = 10
if number >0:
    print ("the number is positive.")
    
    #output#
   """ the number is positive."""

#Example :2 check if the user is eligible to vote

age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote.")
if age<18:
    print ("you are not eligible to vote")
    
 #out pur#
   #enter your age17
   # you are not eligible to vote
   #=== Code Execution Successful ===  """


#example :3 check if password contains'@'
password = input("Enter a password:")
if"@" in password:
    print("password contains'@'.")
if"@"not in password:
    print("password dose not contain'@'.")
   
    ''' #out put
Enter a password:pinal
password dose not contain'@'.

Enter a password:pinal@2008
password contains'@'.
=== Code Execution Successful === '''


#Example :4 check if a number is greater than10
number = int(input("Enter a number:"))
if number > 10:
    print(f"the number {number} is greater than 10.")
if number <= 10:
    print(f"the number {number} is not greater than 10.")
  # out put
  # Enter a number:30
  #the number 30 is greater than 10.
  #Enter a number:9
  #the number 9 is not greater than 10.
  #=== Code Execution Successful ===


#Example:5 Display "hello world" if the condition is true
message = input("Enter a message:")
if message == "greet":
    print("Hello world!")
if message != "greet":
    print("you did not greet.")
"""   # [out put]
Enter a message:greet
Hello world!
Enter a message:preet
you did not greet.

=== Code Execution Successful ==
"""


# Else Statement
#Example : 1 Check if a Number is positive
number = int(input("Enter a number"))
if number >= 0:
    print(f"The number {number} is positive.")
else:
    print(f"The number {number} is negative.")
"""    #[out put]
Enter a number4
The number 4 is positive.

Enter a number-5
The number -5 is negative.
=== Code Execution Successful ===
"""


#  Example : 2 validate an Age as English or Ineligible for senior Discounts
age = int(input("Enter your age:"))
if age >=60:
    print("You are eligible for a senior discount.")
else:
    print("youb are not eligible for a seniour discount.")
    
'''    #[out put]
Enter your age:17
youb are not eligible for a seniour discount.
Enter your age:70
You are eligible for a senior discount.

=== Code Execution Successful ===   '''


#Example:3  Check if a Give Temoperature is Too High or Acceptablete
temperature = float(input("enter the temperature in celsius:"))
if temperature > 37.5:
    print("The temperature is too high!")
else:
    print("The temperature is accetable.")
'''    # [out put]
enter the temperature in celsius:36
The temperature is accetable.

enter the temperature in celsius:89
The temperature is too high!
=== Code Execution Successful ===  '''


#Example:4 Return a Message if a Login Attempt Fails
password = input("Enter your password:")
if password == "Admin123":
    print("Login successful!")
else:
    print("Login failed. please try agin.")

""" #[out put]
Enter your password:Admin123
Login successful! 

Enter your password:pinal123
Login failed. please try agin.
=== Code Execution Successful ===  """


#Example : 5 Identify if a Fail Extension Mathches .txt
filename = input("Enter the file name:")
if filename.endswith(".txt"):
    print("The file is a text file.")
else:
    print("The file is not a text file.")
    
"""    #[out put]
Enter the file name:notes.txt
The file is a text file.
Enter the file name:notes
The file is not a text file.

=== Code Execution Successful ===   """


#   [3] Elif Statement
#  Example: 1 Determine if a Number is Positive, zero, or Negative
number = int(input("Enter a number:"))
if number>0:
    print(f"The number {number} is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print(f"The number {numbe} is negative.")
    
"""   #[output]
Enter a number:11
The number 11 is positive.
Enter a number:0
The number is zero.
=== Code Execution Successful ===  """


#Example: 2 Classify Grades
marks = int(input("Enter your marks:"))
if marks>90:
    print("Grade:A")
elif marks>75:
    print("Grade:B")
elif marks>50:
    print("Grade:C")
else:
    print("Grade:F")
""" #[out put]
Enter your marks:92
Grade:A
Enter your marks:79
Grade:B
Enter your marks:65
Grade:C
Enter your marks:45
Grade:F
=== Code Execution Successful  === """

#Example :3 Identify the Types of Triangle
a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    printr("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

"""
Enter the first side:34 
Enter the second side:34
Enter the third side:34
The triangle is equilateral.

Enter the first side:6
Enter the second side:5
Enter the third side:3
The triangle is scalene


=== Code Execution Successful ===  """


#Example : 4 Classify a Day Based on Temperature
temperature = float(input("Enter the temperature in celsius:"))
if temperature > 35:
    print("It's hot.")
elif temperature > 20:
    print("It's wam.")
else:
    print("It's cold")
    
"""  #[out put]
Enter the temperature in celsius:40
It's hot.
Enter the temperature in celsius:30
It's wam.
Enter the temperature in celsius:10
It's cold

=== Code Execution Successful ===   """


#Example : 5 Detect a user's Role
role = input("Enter your role(admin,user,guest);").lower()
if role == "admin":
    print("you have full access.")
elif role == "user":
    print("you have limited access.")
elif role == "guest":
    print("you have guest access.")
else:
    print("Invalid role.")
    
"""
Enter your role(admin,user,guest);admin
you have full access.
Enter your role(admin,user,guest);user
you have limited access.
Enter your role(admin,user,guest);guest
you have guest access.
Enter your role(admin,user,guest);enter
Invalid role.

=== Code Execution Successful ===  """


# Basic Structure of if statement
#include<stdio.h>
int main(){
    int number;
    printf("Enter a number:");
    scanf("%d",&number);
    
    if (number>0){
        printf("the number %d is positive.\n",number);
    }
    return0:
}

#[output]
Enter a number:5
the number 5 is positive.
=== Code Execution Successful ===


# Using If Statement With Else
#include<stdio.h>
int main(){
    int number;
    //Input a number from the user
    printf("Enter a number:");
    scanf("%d",&number);
    
    //Check if the number is positive
    if (number>0){
        printf("The number %d is positive.\n",number);
    }else{
        printf("The number %d is negaive or zero,\n",number);
    }
    return 0;
}
/*    #[out put]
Enter a number:11
The number 11 is positive.
Enter a number:-11
The number -11 is negaive or zero,


=== Code Execution Successful === */


#Structure of Nested If-Else Statements
# example is a grading system that uses nested if-else statments to determine grades based
score = 85
if score>=90:
    print("Grade:A")
elif score>=80:
    print("Grade:B")
    if score>=85:
        print("Good Performance!")
    else:
        print("Keep up the good work!")
elif score>=70:
    print("Grade:C")
else:
    print("Grade:D")
""" #[out put]
Grade:B
Good Performance!

=== Code Execution Successful ===


#Elif Statement (if-elif-else ladder)
score = 85
if score>90:
    print("Excellent performance!")
elif score>75:
    print("Good job!")
    
"""  [out put]
Good job!
=== Code Execution Successful ===
"""


# Combining If, Elif, and Else Example

score = 85

if score >= 90:
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

else:
    print("Grade: D")
"""    [out put]
Grade: B
=== Code Execution Successful ===  """


#Nested If-Elif-Else Statements
score = 85
if score>=70:
    if score>=90:
        print("Grade:A")
    elif score>=80:
        print("Grade:B")
    else:
        print("Grade:C")
else:
        print("Grade:D")
"""  [out put]      
Grade:B

=== Code Execution Successful ===  """


#Logical OPerators
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

"""   [out put]
You can drive.
=== Code Execution Successful ===  """


#user Input Validation : Ensuring that user inputs meet certain criteria before processig them. Example
user_input=input("Enter your age:")
age = int(user_input)

if age<0:
    print("Invalid age!")
elif age<18:
    print("you are a minor.")
else:
    print("you are an adult.")
"""  #[out put]
Enter your age:78
you are an adult.
Enter your age:17
you are a minor.
Enter your age:-10
Invalid age!
=== Code Execution Successful ===

"""

#Menu Selection : providing options to users and executing diffrent code based on thier selection 
choise = input("Enter choise(1,2,3):")

if choise == '1':
    print("you chose option 1.")
elif choise == '2':
    print("you chose option 2.")
elif choise == '3':
    print("you chose option 3.")
else:
    print("Invalid choise!")
    
"""  [out put]
Enter choise(1,2,3):1
you chose option 1.
Enter choise(1,2,3):2
you chose option 2.
Enter choise(1,2,3):3
you chose option 3.
Enter choise(1,2,3):4
Invalid choise!

=== Code Execution Successful ===  """


#For Loop Example
names = ["XYZ" , "PQR" , "STU"]
for name in names:
    print(name)
"""   
XYZ
PQR
STU

=== Code Execution Successful ===     """


#Example : 1 Itreating over a Matrix (2D List)  nested for loops are useful for working with 2D lists (lits of lists) ,like matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
 
for row in matrix:
    for element in row:
         print(element,end='')
    print()
""" output
123
456
789

=== Code Execution Successful ===
"""


#Example :2 Multiplying Element of Two Lists
list1 = [1,2,3]
list2 = [4,5,6]
for i in list1:
    for j in list2:
        print(f"{i} * {j} = {i * j}")
"""   #[out put]
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18

=== Code Execution Successful ===   """


# While loop
count = 1
while count <=5:
    print(count)
    count += 1
"""   #[out put]
1
2
3
4
5

=== Code Execution Successful ===  """



#Breack Statement Example
names = ["XYZ","PQR","STU"]
for name in names:
    if name == "PQR":
        break
    print(name)
    
""" out put 
XYZ
=== Code Execution Successful ===  """


#continue statement 
names = ["XYZ","PQR","STU"]
for name in names:
    if name == "PQR":
            continue
    print(name)
"""  #[out put]
XYZ
STU
=== Code Execution Successful ===
"""

