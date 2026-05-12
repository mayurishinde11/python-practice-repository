# print(''' Hello My Name Is Mayuri
#           My Age Is 26.
#           And i am  Software Engineer ''')


# 📌 Mini Exercise
# Write a program that:

# Takes user age as input
# Prints whether the user is an adult (18+) or not

# age=int(input("Enter Your Age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Not Adult")

# Create a program that:

# Takes two numbers
# Performs all arithmetic operations
# Checks which number is greater
# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# print("Addition:",num1+num2)
# print("Subtraction:",num1-num2)
# print("Multiplication:",num1*num2)
# print("Division:",num1/num2)    
# if num1>num2:
#     print(num1,"is greater than",num2)
# elif num2>num1:
#     print(num2,"is greater than",num1)  
# else:    
#     print("Both numbers are equal")
# i = 10

# # Checking if i is greater than 15
# if i > 15:
#     print("10 is less than 15")



# #Write a python program to check year is laep or not
# Year=int(input("Enter The Year "))
# if(Year%4==0):
#   if(Year%100==0):
#     if(Year%400==0):
#       print(Year,"Year Is Leap")
#     else:
#       print(Year,"Year Is not Leap")
#   else:
#     print(Year,"Year Is Leap")
# else:
#   print(Year,"Year Is Not Leap")




# year = int(input("Enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")



#1. Positive or Negative Number or Zero

# number = float(input("Enter The nNumber..."))
# if number >0:
#     print(number,"Is Positive")
# elif number < 0:
#     print(number,"is negative")
# else:
#     print(number,"is zero")


# 3. Largest Among Three Numbers
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if num1 >= num2 and num1 >=num3:
#     print(num1, "is the largest number.") 
# elif num2 >= num1 and num2 >= num3:
#     print(num2, "is the largest number.")
# else:
#     print(num3, "is the largest number.")



# Create a program that:

# Takes student marks
# Prints grade using if-elif-else

# marks=float(input("Enter Student Marks: "))
# if marks >=80 :
#     print("Grade A")
# elif marks>=60 and marks<=79.99:
#     print("Grade B")
# elif marks>=40 and marks<=59.99: 
#     print("Grade C")
# elif marks>=35 and marks<=39.99:   
#     print("Grade D")
# else:
#     print("FAIL")


# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# i = 1

# while i <= 5:
#     print(i)
#     i += 1


# for i in range(10):
#     if i == 5:
#         break
#     print(i)



# for i in range(5):
#     pass
# print("This is a placeholder for future code.")




# num = int(input("Enter a number to calculate its factorial: "))
# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(fact)



# # Sum of Numbers
# sum=0
# for i in range(10):
#     sum=sum+i
# print(sum)



# 3️⃣ Reverse Number


# num = int(input())
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# print(rev)

# n = int(input())

# a, b = 0, 1

# for i in range(n):
#     print(a)
#     a, b = b, a + b


# for i in range(1, 6):
#     for j in range(1, 11):
#         print(i, "x", j, "=", i*j)
#     print()


# text="Python"
# print(text[0:5:2])


# text="Python"
# print(text[0:5:2])
# print(text[0:5:3])
# print(text[0:5:4])
# print(text[0:5:5])
# print(text[0:5:6])







# text="Python is a programming language"
# print(text.split())
# print("python".find("a") )



# text = "Python"

# print("p" in text)


# first = "Hello"
# second = "World"

# print(first + second)


#palindrome string

str=input()
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")