# Practice 1

# Check if number is:

# positive
# negative
# zero



num=float(input("Enter Number which you have to check: "))
if num >0:
    print(num,"Is positive" )
elif num < 0:
    print(num,"Is negative")
else:
    print(num, "is Zero")


# Practice 2

# Take marks and print:

# A
# B
# C
# Fail


Marks=float(input("Enter The Marks To Check Grade:..."))
if Marks >=80:
    print("Grade A...")
elif Marks >=60:
    print("Grade B...")
elif Marks >=35:
    print("Grade C....")
else:
    print("Fail")


# Practice 3

# Check:

# even or odd


num=float(input("Enter Number To Check If It Is Even Or Odd: "))
if num % 2 == 0:
    print(num,"Is Even..")
else:
    print(num,"Is Odd...")


# Practice 4

# Take username and password.
# Print:

# Login successful
# OR
# Invalid credentials



username=input("Enter Your Username:....")
password=input("Enter Your Password:....")
if username=="Mahi" and password=="Mahi@123":
    print("Login Successful...")
else:
    print("Invalid Credentials...")



# 13. Mini Coding Task
# Movie Ticket Eligibility System

# Requirements:

# Ask age
# If age >= 18:
# print “Adult Ticket”
# Else:
# print “Child Ticket”

# BONUS:
# Add student discount using nested condition.


age=int(input("Enter Your Age To Check Movie Ticket Eligibility: "))
if age >=18:
    print("Adult Ticket....")
    student=input("Aru You Student Please Anser (Yes/No):....")
    if student.lower() == "yes":
        print("Congratulations You Are Eligible For Student Discount...")
    else:
        print("Sorry, You Are Not eligible For student Discount....")
else:
    print("Child Ticket....")
