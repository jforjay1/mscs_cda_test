#Write a program that prints the values for the formula a^2x - a^x + 1 for a given input a and x ranging from 1 to a by an increment of 1.
a = int(input("Enter the value of a: "))
for i in range(1,a+1):
    print(" ")
    print(a**(2*i) - (a**i) + 1)