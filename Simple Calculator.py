class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y == 0:
            return "Error: Cannot divide by zero."
        return x/y
if __name__=="__main__":
    calc=Calculator()
    num1=float(input("Enter First Number: "))
    num2=float(input("Enter Second Number: "))
    op=input("Choose Operation(+,-,*,/) or 'q' to quit: ")
    if op=="q":
        print("Goodbye!")
    elif op == "+":
        print("Addition:",calc.add(num1,num2))
    elif op=="-":
        print("Subtraction:",calc.subtract(num1,num2))
    elif op=="*":
        print("Multiplication:",calc.multiply(num1,num2))
    elif op=="/":
        print("Division:",calc.divide(num1,num2))
    else:
        print("Invalid operator")