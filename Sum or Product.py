def sum_or_product(a,b):
    product=a*b
    if product<=1000:
        return product
    else:
        return a+b

a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))

result=sum_or_product(a,b)
print(f"The result is {result}")