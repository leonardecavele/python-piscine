def garden_operations(operation: int) -> None:
    if operation == 0:
        int("ValueError")
    elif operation == 1:
        _ = 42 / 0
    elif operation == 2:
        with open("missing.txt", "r") as f:
            pass
    elif operation == 3:
        plants = {}
        _ = plants["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()

    print("Testing ValueError...")
    try:
        garden_operations(0)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations(1)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations(2)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        garden_operations(3)
    except KeyError:
        print(f"Caught KeyError: 'missing\\_plant'") 
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations(1)
        garden_operations(2)
        garden_operations(3)
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    try:
        test_error_types()
    except Exception as e:
        print(f"Unexpected error: {e}")
