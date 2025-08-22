class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers"""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers"""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage (you can remove or comment this when importing in another script)
if __name__ == "__main__":
    # Using static method
    print("Addition:", Calculator.add(5, 3))

    # Using class method
    print("Multiplication:", Calculator.multiply(5, 3))
