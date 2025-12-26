def water_plants(plant_list: list[str | None]) -> None:
    """water the plants and handle errors"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
        print("Watering completed successfully!")
    except:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """call the 'water_plants' function with both valid and invalid inputs"""
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print()

    print("Testing with error...")
    water_plants(["tomato", None])
    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    try:
        test_watering_system()
    except Exception as e:
        print(f"Unexpected error: {e}")
