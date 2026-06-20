#print the factorial of a numbers using while loop
n=int(input("Enter the number: "))
fact=1
while n>1:
    fact=fact * n
    n = n-1
    print(f"the factorial of a number is {fact}")
