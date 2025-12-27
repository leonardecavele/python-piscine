class GardenError(Exception):
    """class for garden-related errors"""


class PlantError(GardenError):
    """class for plant-related errors"""


class WaterError(GardenError):
    """class for water-related errors"""


class SunError(GardenError):
    """class for sun-related errors"""


class GardenManager:
    """class with methods to show error handling"""

    def __init__(self) -> None:
        """create a garden manager"""
        self.__plants: dict[str, tuple[int, int]] = {}
        self.__water_tank: int = 42

    def add_plant(
            self,
            plant_name: str,
            water_level: int,
            sunlight_hours: int
            ) -> None:
        """add a plant to the garden or raise a PlantError"""
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        elif plant_name in self.__plants:
            raise PlantError(f"Plant '{plant_name}' already exists!")
        self.__plants[plant_name] = (water_level, sunlight_hours)
        print(f"Added {plant_name} successfully")


    def water_plant(self, amount: int) -> None:
        """water plant with water from the tank or raise WaterError"""
        if amount < 1:
            raise WaterError("Invalid water amount")
        if self.__water_tank < amount:
            raise WaterError("Not enough water in tank")
        self.__water_tank -= amount

    def water_plants(self) -> None:
        """water all plants"""
        print("Opening watering system")
        try:
            if not self.__plants:
                raise PlantError("Error watering plants: No plants to water")
            for plant in self.__plants:
                try:
                    self.water_plant(10)
                    print(f"Watering {plant} - success")
                except WaterError as e:
                    print(f"Error watering {plant}: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str) -> str:
        """check plant health, raise errors if there are invalid values"""
        if plant_name not in self.__plants:
            raise PlantError(
                    f"Error checking {plant_name}: "
                    f"Unknown plant '{plant_name}'"
                    )
        water_level, sunlight_hours = self.__plants[plant_name]
        if water_level > 10:
            raise WaterError(f"Water level {water_level} "
                             "is too high (max 10)"
                             )
        elif water_level < 1:
            raise WaterError(f"Water level {water_level} "
                             "is too low (min 1)"
                             )
        if sunlight_hours > 12:
            raise SunError(f"Sunlight hours {sunlight_hours} "
                           "is too high (max 12)"
                           )
        elif sunlight_hours < 2:
            raise SunError(f"Sunlight hours {sunlight_hours} "
                           "is too low (min 2)"
                           )
        return (
                f"{plant_name}: healthy "
                f"(water: {water_level}, sun: {sunlight_hours})"
                )


def main() -> None:
    """demonstration of the error handling"""
    print("=== Garden Management System ===")
    print()

    manager = GardenManager()
    print("Adding plants to garden...")
    for plant in [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("", 4, 6),
    ]:
        try:
            manager.add_plant(plant[0], plant[1], plant[2])
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    for plant in ["tomato", "lettuce"]:
        try:
            print(manager.check_plant_health(plant))
        except (PlantError, WaterError, SunError) as e:
            print(f"Error checking {plant}: {e}")
    print()

    print("Testing error recovery...")
    try:
        manager.water_plant(999)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
