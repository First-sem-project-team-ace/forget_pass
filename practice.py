#to check whether number is prime or not
# def is_prime(number):
#     # Check if the number is less than 2
#     if number <= 1:
#         return False
#     # Check if the number is 2
#     if number == 2:
#         return True
#     # Check if the number is greater than 2 and even
#     if number % 2 == 0:
#         return False
#     # Check for factors from 3 to the square root of the number
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# # Example usage
# print(is_prime(1))   # Output: False
# print(is_prime(2))   # Output: True
# print(is_prime(17))  # Output: True
# print(is_prime(18))  # Output: False



# def num(n):
#     a=0
#     b=1
#     if(n<0):
#         print("number is invalid")
#     elif(n==1):
#         print(a)
#     else:
#         print(0)
#         print(1)
#         c=0
#         for i in range(2,n):
#             c = a + b
#             if(c<25):
#                 a=b
#                 b=c
#                 print(c)

# num(25)


# def count_is_occurrences(file_path):
#     try:
#         # Initialize a counter for occurrences of the word "is"
#         is_count = 0
        
#         # Open the file and read its content
#         with open(file_path, 'r') as file:
#             for line in file:
#                 # Split each line into words and count occurrences of "is"
#                 words = line.split()
#                 is_count += words.count("is")
        
#         # Display the total count of "is"
#         print(f'The word "is" occurs {is_count} times in the file.')
    
#     except FileNotFoundError:
#         print(f"The file {file_path} does not exist.")

# # Example usage
# count_is_occurrences("softwarica.txt")

#factorial number
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     elif n == 1 or n == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result

# # Example usage:
# number = int(input("Enter a number: "))
# print(factorial(number))

# a=[1,2,3]
# a.append(4)
# print(a)
# def div(a,b):
#     assert b!=0, "Divisor cannot be zero"
#     return a/b
# print(div(10,2))