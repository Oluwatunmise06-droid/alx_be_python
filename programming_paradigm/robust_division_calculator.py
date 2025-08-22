def safe_divide(numerator, denominator):
    try:
        # try to convert to float
        num = float(numerator)
        den = float(denominator)

        # try to divide
        result = num / den
        return f"Result: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please provide numbers only."
