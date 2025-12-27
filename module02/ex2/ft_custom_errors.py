class GardenError(Exception):
    """class for garden-related errors"""


class PlantError(GardenError):
    """class for plant-related errors"""


class WaterError(GardenError):
    """class for water-related errors"""


def plant_error() -> None:
    """trigger a PlantError error"""
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    """trigger a WaterError error"""
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    """use error functions to show all custom errors"""
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    for function_error in (plant_error, water_error):
        try:
            function_error()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
