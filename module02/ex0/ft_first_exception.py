def check_temperature(temp_str: str) -> int | None:
    """convert a string to a valid temperature for plants"""
    temperature: int = 0
    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temperature > 40:
        print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
        return None
    elif temperature < 0:
        print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
        return None
    print(f"Temperature {temperature}°C is perfect for plants!")
    return temperature


def test_temperature_input() -> None:
    """use the check_temperature function with valid and invalid inputs"""
    print("=== Garden Temperature Checker ===")
    print()

    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Unexpected error: {e}")
