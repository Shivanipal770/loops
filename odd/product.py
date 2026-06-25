number = int(input("Enter the number :"))
temp = number  # Save the original number for printing
product = 1

# Process digits while the number is greater than 0
while number > 0:
    digit = number % 10          
    product *= digit             
    number = number // 10 

print(f"The product of the digits of {temp} is: {product}")