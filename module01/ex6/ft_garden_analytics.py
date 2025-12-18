class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.__name: str = name
        self.__height: int = Plant.valid_height(height)

    def grow(self) -> None:
        self.__height += 1
        print(f"{self.__name} grew 1cm")

    @staticmethod
    def valid_height(height: int) -> int:
        if height > 0:
            return height
        else:
            return 1

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> int:
        return self.__height

    def __str__(self) -> str:
        return f"- {self.__name}: {self.__height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str,
                 blooming: bool) -> None:
        super().__init__(name, height)
        self.__color = color
        self.__blooming = blooming

    def __str__(self) -> str:
        return (
            super().__str__()
            + f", {self.__color} flowers"
            + f" ({'blooming' if self.__blooming else 'not blooming'})"
            )


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, color, blooming)
        self.__prize_points = prize_points

    def __str__(self) -> str:
        return (
            super().__str__()
            + f", Prize points: {self.__prize_points}"
            )

    @property
    def prize_points(self) -> int:
        return self.__prize_points


class Garden:
    def __init__(self, name: str) -> None:
        self.__plants: list[Plant] = []
        self.__name: str = name
        self.__total_growth = 0
        self.__total_prize_points = 0
        self.__total_blooming = 0
        self.__plant_count = 0
        self.__plant_types = [0, 0, 0]

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
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
        self.__total_growth += 1

    def report(self) -> None:
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
        if plant is PrizeFlower:
            return 2
        if plant is FloweringPlant:
            return 1
        return 0

    @property
    def total_growth(self) -> int:
        return self.__total_growth

    @property
    def total_blooming(self) -> int:
        return self.__total_blooming

    @property
    def total_prize_points(self) -> int:
        return self.__total_prize_points

    @property
    def name(self) -> str:
        return self.__name

    @property
    def plants(self) -> list[Plant]:
        return self.__plants

    @property
    def plant_count(self) -> int:
        return self.__plant_count

    @property
    def plant_types(self) -> list[int, int, int]:
        return self.__plant_types


class GardenManager:
    __managers: list["GardenManager"] = []

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__gardens: dict[str, Garden] = {}
        self.__stats = GardenManager.GardenStats(self)
        GardenManager.__managers += [self]

    def add(self, gardens: list[Garden]) -> None:
        for garden in gardens:
            self.__gardens[garden.name] = garden

    def help_grow(self) -> None:
        print(f"{self.__name} is helping all plants grow...")
        for garden_name in self.__gardens:
            garden = self.__gardens[garden_name]
            for plant in garden.plants:
                plant.grow()
                garden.increment_total_growth()

    def report(self) -> None:
        print(f"=== {self.__name} Report ===")
        for garden_name in self.__gardens:
            print(f"Plants in {garden_name}:")
            plants = self.__gardens[garden_name].plants
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
        manager = cls(manager_name)
        gardens: list[Garden] = []
        for garden_name in gardens_spec:
            garden = Garden(garden_name)
            garden.add(gardens_spec[garden_name])
            gardens += [garden]
        manager.add(gardens)
        return manager

    @property
    def name(self) -> str:
        return self.__name

    @property
    def managers(self) -> list["GardenManager"]:
        return self.__managers

    @property
    def gardens(self) -> dict[str, Garden]:
        return self.__gardens

    @property
    def stats(self) -> "GardenManager.GardenStats":
        return self.__stats

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:
            self.__manager: GardenManager = manager

        def plant_types(self) -> tuple[int, int, int]:
            regular_plant = 0
            flowering = 0
            prize_flower = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                garden = self.__manager.gardens[name]
                regular_plant += garden.plant_types[0]
                flowering += garden.plant_types[1]
                prize_flower += garden.plant_types[2]
            return (regular_plant, flowering, prize_flower)

        def count_plants(self) -> int:
            count: int = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                garden = self.__manager.gardens[name]
                count += garden.plant_count
            return count

        def count_growth(self) -> int:
            count: int = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                garden = self.__manager.gardens[name]
                count += garden.total_growth
            return count

        def garden_score(self) -> None:
            score: int = -1
            managers: list["GardenManager"] = self.__manager.managers
            print("Garden scores - ", end='')
            for manager in managers:
                if score != -1:
                    print(", ", end='')
                score = 0
                print(f"{manager.name}: ", end='')
                garden_names = manager.gardens
                for name in garden_names:
                    score += manager.gardens[name].total_prize_points * 3
                    score += manager.gardens[name].total_growth * 2
                    score += manager.gardens[name].total_blooming * 5
                print(f"{score}", end='')
            print()

        def height_validation(self) -> None:
            correct_height: bool = True
            managed_gardens: int = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                managed_gardens += 1
                garden = self.__manager.gardens[name]
                for plant in garden.plants:
                    if plant.height < 1:
                        correct_height = False
            print(f"Height validation test: {correct_height}")

        def gardens_managed(self) -> None:
            managed_gardens: int = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                managed_gardens += 1
            print(f"Total gardens managed: {managed_gardens}")


def main() -> None:
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
