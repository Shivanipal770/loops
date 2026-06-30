num = int(input("Enter the number : "))
count = 0

# Optional: Handle negative numbers
num = abs(num)

# Edge case: If the number is 0, it has 1 digit
if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10 
        count += 1

print("Total number of digits:", count)