# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f" Current Date and Time: {formatted_date}")
    return current_date


def calculate_future_date(days: int):
    """
    Calculates the future date by adding the given number of days
    to the current date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f" Future Date after {days} days: {formatted_future}")
    return future_date


if __name__ == "__main__":
    # Part 1: Display current datetime
    display_current_datetime()

    # Part 2: Ask user for number of days and calculate future date
    try:
        days_input = int(input("Enter number of days to add: "))
        calculate_future_date(days_input)
    except ValueError:
        print(" Please enter a valid integer for days.")

