#print the sum of all even number from 1 upto n 
n = int(input("Enter the number: "))
sum=0
num=2
while num<=n:
    sum=sum+num
    num=num+2
    print(f"sum of all natural number from 1 to n is: {sum}")