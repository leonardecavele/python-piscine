class Plant:
    """Basic plant with a name and a height in centimeters."""

    def __init__(self, name: str, height: int) -> None:
        """Create a Plant.

        Args:
            name:   Plant name.
            height: Initial height in centimeters.
        """
        self.__name: str = name
        self.__height: int = Plant.valid_height(height)

    def grow(self) -> None:
        """Increase the plant height by 1 cm and print a message."""
        self.__height += 1
        print(f"{self.__name} grew 1cm")

    @staticmethod
    def valid_height(height: int) -> int:
        """Validate a given height value.

        Args:
            height: Height in centimeters.

        Returns:
            A positive height. If height <= 0, returns 1.
        """
        if height > 0:
            return height
        else:
            return 1

    def get_name(self) -> str:
        """Get the plant name."""
        return self.__name

    def get_height(self) -> int:
        """Get the current plant height."""
        return self.__height

    def __str__(self) -> str:
        """Return a readable description of the plant."""
        return f"- {self.__name}: {self.__height}cm"


class FloweringPlant(Plant):
    """A plant with flowers, a given color and a blooming status."""

    def __init__(self, name: str, height: int, color: str,
                 blooming: bool) -> None:
        """Create a FloweringPlant.

        Args:
            name, height: cf. Plant
            color: Flower color.
            blooming: True if the plant is currently blooming.
        """
        super().__init__(name, height)
        self.__color = color
        self.__blooming = blooming

    def __str__(self) -> str:
        """Return a readable description of the flower."""
        return (
            super().__str__()
            + f", {self.__color} flowers"
            + f" ({'blooming' if self.__blooming else 'not blooming'})"
            )


class PrizeFlower(FloweringPlant):
    """A flowering plant that awards prize points (e.g., for competitions)."""

    def __init__(self, name: str, height: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        """Create a PrizeFlower.

        Args:
            name, height, color, blooming: cf. FloweringPlant
            prize_points: Points awarded by this plant.
        """
        super().__init__(name, height, color, blooming)
        self.__prize_points = prize_points

    def __str__(self) -> str:
        """Return a readable description of the prize flower."""
        return (
            super().__str__()
            + f", Prize points: {self.__prize_points}"
            )

    def get_prize_points(self) -> int:
        """Get the prize points value."""
        return self.__prize_points


class Garden:
    """A list of plants that holds statistics about them."""

    def __init__(self, name: str) -> None:
        """Create an empty garden.

        Args:
            name: Garden name.
        """
        self.__plants: list[Plant] = []
        self.__name: str = name
        self.__total_growth = 0
        self.__total_prize_points = 0
        self.__total_blooming = 0
        self.__plant_count = 0
        self.__plant_types = [0, 0, 0]

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
        """Add new plants to the garden.

        Each item in new_plants is expected to be a tuple like:
        - (PlantClass, arg1, arg2, ...)

        Args:
            new_plants: [(PlantClass, arg1, arg2, ...), ...]

        Notes:
            This method also updates:
            - plant_count
            - plant_types
            - total_blooming
            - total_prize_points
        """
        for plant, *args in new_plants:
            self.__plants += [plant(*args)]
            self.__plant_count += 1
            index: int = Garden.type_index(plant)
            self.__plant_types[index] += 1
            if index == 1:
                if args[-1]:
                    self.__total_blooming += 1
            if index == 2:
                self.__total_prize_points += args[-1]
                if args[-2]:
                    self.__total_blooming += 1
            print(f"Added {args[0]} to {self.__name}")

    def increment_total_growth(self) -> None:
        """Increment total_growth by 1 cm."""
        self.__total_growth += 1

    def report(self) -> None:
        """Print a report of the garden contents and its statistics."""
        print(f"=== {self.__name} Report ===")
        print("Plants in garden:")
        for plant in self.__plants:
            print(plant)
        print()
        print(
            f"Plants added: {self.__plant_count}, ",
            f"Total growth: {self.__total_growth}cm"
            )
        print(
            f"Plant types: {self.__plant_types[0]} regular,",
            f"{self.__plant_types[1]} flowering,",
            f"{self.__plant_types[2]} prize flowers"
            )

    @staticmethod
    def type_index(plant: type[Plant]) -> int:
        """Return the type index for the plant_types count.

        Args:
            plant: Plant class or a Plant child class

        Returns:
            0 for Plant, 1 for FloweringPlant, 2 for PrizeFlower.
        """
        if plant is PrizeFlower:
            return 2
        if plant is FloweringPlant:
            return 1
        return 0

    def get_total_growth(self) -> int:
        """Get the accumulated growth value"""
        return self.__total_growth

    def get_total_blooming(self) -> int:
        """Get how many flowering/prize plants were added in blooming state."""
        return self.__total_blooming

    def get_total_prize_points(self) -> int:
        """Get the total prize points from all added prize flowers."""
        return self.__total_prize_points

    def get_name(self) -> str:
        """Get the garden name."""
        return self.__name

    def get_plants(self) -> list[Plant]:
        """Get the list of plant instances in the garden."""
        return self.__plants

    def get_plant_count(self) -> int:
        """Get the number of plants added to this garden."""
        return self.__plant_count

    def get_plant_types(self) -> list[int]:
        """Get type counts as [regular, flowering, prize]."""
        return self.__plant_types


class GardenManager:
    """Manage multiple gardens and print combined reports and statistics."""

    __managers: list["GardenManager"] = []

    def __init__(self, name: str) -> None:
        """Create a garden manager.

        Args:
            name: Manager name.
        """
        self.__name: str = name
        self.__gardens: dict[str, Garden] = {}
        self.__stats = GardenManager.GardenStats(self)
        GardenManager.__managers += [self]

    def add(self, gardens: list[Garden]) -> None:
        """Register gardens under this manager.

        Args:
            gardens: Gardens to manage.
        """
        for garden in gardens:
            self.__gardens[garden.get_name()] = garden

    def help_grow(self) -> None:
        """Make every plant in every managed garden grow once."""
        print(f"{self.__name} is helping all plants grow...")
        for garden_name in self.__gardens:
            garden = self.__gardens[garden_name]
            for plant in garden.get_plants():
                plant.grow()
                garden.increment_total_growth()

    def report(self) -> None:
        """Print a full report of all managed gardens and global stats."""
        print(f"=== {self.__name} Report ===")
        for garden_name in self.__gardens:
            print(f"Plants in {garden_name}:")
            plants = self.__gardens[garden_name].get_plants()
            for plant in plants:
                print(plant)
            print()
        print(
            f"Plants added: {self.__stats.count_plants()}, ",
            f"Total growth: {self.__stats.count_growth()}cm"
            )
        print(
            f"Plant types: {self.__stats.plant_types()[0]} regular,",
            f"{self.__stats.plant_types()[1]} flowering,",
            f"{self.__stats.plant_types()[2]} prize flowers"
            )
        print()
        self.__stats.height_validation()
        self.__stats.garden_score()
        self.__stats.gardens_managed()

    @classmethod
    def create_garden_network(cls,
                              manager_name: str,
                              gardens_spec:
                              dict[str, list[tuple[type[Plant], object]]],
                              ) -> "GardenManager":
        """Factory to build a manager and its gardens from specifications.

        Args:
            manager_name: cf. GardenManager
            gardens_spec: cf. Garden

        Returns:
            An initialized GardenManager with initialized gardens registered.
        """
        manager = cls(manager_name)
        gardens: list[Garden] = []
        for garden_name in gardens_spec:
            garden = Garden(garden_name)
            garden.add(gardens_spec[garden_name])
            gardens += [garden]
        manager.add(gardens)
        return manager

    def get_name(self) -> str:
        """Get the manager name."""
        return self.__name

    def get_managers(self) -> list["GardenManager"]:
        """Get the list of all GardenManager instances created so far."""
        return self.__managers

    def get_gardens(self) -> dict[str, Garden]:
        """Get the gardens managed by this manager."""
        return self.__gardens

    def get_stats(self) -> "GardenManager.GardenStats":
        """Get the stats helper for this manager."""
        return self.__stats

    class GardenStats:
        """Compute statistics across a manager's gardens."""

        def __init__(self, manager: "GardenManager") -> None:
            """Create a stats helper bound to a manager.

            Args:
                manager: The GardenManager to read data from.
            """
            self.__manager: GardenManager = manager

        def plant_types(self) -> tuple[int, int, int]:
            """Count plant types across all managed gardens.

            Returns:
                A tuple (regular, flowering, prize).
            """
            regular_plant = 0
            flowering = 0
            prize_flower = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                regular_plant += garden.get_plant_types()[0]
                flowering += garden.get_plant_types()[1]
                prize_flower += garden.get_plant_types()[2]
            return (regular_plant, flowering, prize_flower)

        def count_plants(self) -> int:
            """Count total number of plants across all managed gardens."""
            count: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                count += garden.get_plant_count()
            return count

        def count_growth(self) -> int:
            """Count total growth across all managed gardens."""
            count: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                count += garden.get_total_growth()
            return count

        def garden_score(self) -> None:
            """Print a score for each manager based on their gardens.

            Score rules:
            - prize points * 3
            - total growth * 2
            - total blooming * 5
            """
            score: int = -1
            managers: list["GardenManager"] = self.__manager.get_managers()
            print("Garden scores - ", end='')
            for manager in managers:
                if score != -1:
                    print(", ", end='')
                score = 0
                print(f"{manager.get_name()}: ", end='')
                garden_names = manager.get_gardens()
                for name in garden_names:
                    score += manager.get_gardens()[name].get_total_prize_points() * 3
                    score += manager.get_gardens()[name].get_total_growth() * 2
                    score += manager.get_gardens()[name].get_total_blooming() * 5
                print(f"{score}", end='')
            print()

        def height_validation(self) -> None:
            """Check if all plants have a valid height and print the result."""
            correct_height: bool = True
            managed_gardens: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                managed_gardens += 1
                garden = self.__manager.get_gardens()[name]
                for plant in garden.get_plants():
                    if plant.get_height() < 1:
                        correct_height = False
            print(f"Height validation test: {correct_height}")

        def gardens_managed(self) -> None:
            """Print how many gardens are managed by the manager."""
            managed_gardens: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                managed_gardens += 1
            print(f"Total gardens managed: {managed_gardens}")


def main() -> None:
    """Run a demo of the garden management system."""
    print("=== Garden Management System Demo ===")
    print()

    m1 = GardenManager("Alice")

    g1 = Garden("South garden")
    g1.add([(Plant, "Basil", 25), (FloweringPlant, "Rose", 60, "Red", False),
           (PrizeFlower, "Orchid", 120, "White", True, 9)])
    g2 = Garden("North Garden")
    g2.add([(Plant, "Oak", 3000),
            (FloweringPlant, "Tulip", 40, "Yellow", False)])
    m1.add([g1, g2])
    print()

    m1.help_grow()
    print()

    g1.report()
    print()

    m2 = GardenManager.create_garden_network(
        "Jean",
        {
            "East garden": [
                (Plant, "Grass", 30),
                (Plant, "Spruce", 300),
            ],
            "West garden": [
                (Plant, "Basil", 25),
                (FloweringPlant, "Rose", 60, "Red", True),
                (PrizeFlower, "Orchid", 120, "White", True, 9),
            ],
        },
    )
    print()

    m2.help_grow()
    print()

    m1.report()
    print()
    m2.report()


if __name__ == "__main__":
    main()
