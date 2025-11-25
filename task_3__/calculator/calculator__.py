class Calculator:
    def __init__(self):
        # Constructor, no inputs yet
        pass

    def calculate(self, a, b, operation):
        try:
            a = float(a)
            b = float(b)

            if operation == "+":
                return self.add(a, b)
            elif operation == "-":
                return self.subtract(a, b)
            elif operation == "*":
                return self.multiply(a, b)
            elif operation == "/":
                return self.divide(a, b)
            else:
                raise ValueError("Invalid operation selected.")

        except ValueError as e:
          return str(e)

        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        except Exception as e:
            return f"Unexpected error occurred: {str(e)}"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b


# ----------- MAIN FUNCTION ------------
def main():
    print("✨ Smart Calculator using Classes and Exception Handling ✨")
    print("Available operations: + , - , * , / , exit")

    calc = Calculator()

    while True:
        operation = input("\nEnter operation: ").lower().strip()

        if operation == "exit":
            print("Exiting Calculator. Goodbye")
            break

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        result = calc.calculate(a, b, operation)
        print("Result:", result,"\n-----------------------------------")


if __name__ == "__main__":
    main()
