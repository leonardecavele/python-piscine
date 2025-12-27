def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hours: int
                       ) -> str:
    """raise an error if a value given to this function is incorrect"""
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError("Error: "
                         f"Water level {water_level} is too high (max 10)"
                         )
    elif water_level < 1:
        raise ValueError("Error: "
                         f"Water level {water_level} is too low (min 1)"
                         )
    if sunlight_hours > 12:
        raise ValueError("Error: "
                         f"Sunlight hours {sunlight_hours} is too high (max 12)"
                         )
    elif sunlight_hours < 2:
        raise ValueError("Error: "
                         f"Sunlight hours {sunlight_hours} is too low (min 2)"
                         )
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """call 'check_plant_health' with correct and incorrect values""" 
    print("=== Garden Plant Health Checker ===")
    print()

    print("Testing good values...")
    print(check_plant_health("tomato", 4, 2))
    print()

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 4, 2))
    except ValueError as e:
        print(f"{e}")
    print()

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 2))
    except ValueError as e:
        print(f"{e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 4, 0))
    except ValueError as e:
        print(f"{e}")
    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    try:
        test_plant_checks()
    except Exception as e:
        print(f"Unexpected error: {e}")
