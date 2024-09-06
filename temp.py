def greet(name):
    """
    Greet a person by name.
    """
    return f"Hello, {name}!"

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    return length * width

def is_even(number):
    """
    Check if a number is even.
    """
    return number % 2 == 0

# Example usage
if __name__ == "__main__":
    print(greet("Alice"))
    print(f"Area of rectangle: {calculate_area(5, 3)}")
    print(f"Is 4 even? {is_even(4)}")
