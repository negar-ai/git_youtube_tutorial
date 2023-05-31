Fibonacci Sequence: Write a program that prints the first n numbers in the Fibonacci sequence, where n is entered by the user.

# Program to display the Fibonacci sequence up to n-th term while receives "n" from client interactively.
num_terms = int(input("How many terms of Fibonacci Sequence do you want? "))

# first two terms that is fixed
n1, n2 = 0, 1

# check if the number of terms is valid
count = 0
if num_terms <= 0:
    print("Please enter a positive integer")
    
# if there is only one term, return n1
elif num_terms == 1:
    print("Fibonacci sequence up to", num_terms, ":")
    print(n1)
    
# generate the Fibonacci sequence
else:
    print("Fibonacci sequence up to", num_terms, ":")
    while count < num_terms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
