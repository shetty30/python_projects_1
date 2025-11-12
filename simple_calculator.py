def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):  
    return a * b            
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    print("Simple Calculator")
    print("Type 'exit' anytime to quit.\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == "exit":
            break

        num2 = input("Enter second number: ")
        if num2.lower() == "exit":
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.\n")
            continue

        operator = input("Choose operation (+, -, *, /): ")

        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            print("🚫 Invalid operator. Try again.\n")
            continue

        print(f"Result: {result}\n")

    print("Calculator closed. 👋")


if __name__ == "__main__":
    main()