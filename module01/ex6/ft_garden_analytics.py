class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.__name: str = name
        self.__height: int = height

    def grow(self) -> None:
        self.__height += 1
        print(f"{self.__name} grew 1cm")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def height(self) -> int:
        return self.__height

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height}cm"


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


class Garden:
    def __init__(self, name: str) -> None:
        self.__plants: list[Plant] = []
        self.__name: str = name
        self.__plant_count = 0
        self.__plant_types = (0, 0, 0)

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
        for plant, *args in new_plants:
            self.__plants += [plant(*args)]
            self.__plant_count += 1
            print(f"Added {args[0]} to {self.__name}")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def plants(self) -> list[Plant]:
        return self.__plants


class GardenManager:
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__gardens: dict[str, Garden] = {}
        self.__stats = GardenManager.GardenStats(self)

    def add(self, gardens: list[Garden]) -> None:
        for garden in gardens:
            self.__gardens[garden.name] = garden

    def help_grow(self) -> None:
        print(f"{self.__name} is helping all plants grow...")
        for garden_name in self.__gardens:
            garden = self.__gardens[garden_name]
            for plant in garden.plants:
                plant.grow()
                self.__stats.increment_total_growth()

    def create_garden_network() -> None:
        pass

    @property
    def gardens(self) -> dict[str, Garden]:
        return self.__gardens

    @property
    def stats(self) -> "GardenManager.GardenStats":
        return self.__stats

    class GardenStats:
        def __init__(self, manager: "GardenManager") -> None:
            self.__manager: GardenManager = manager
            self.__total_growth = 0

        def plant_types(self) -> tuple[int, int, int]:
            regular_plant = 0
            flowering = 0
            prize_flower = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                garden = self.__manager.gardens[name]
                for plant in garden.plants:
                    if plant.__class__ is PrizeFlower:
                        prize_flower += 1
                    elif plant.__class__ is FloweringPlant:
                        flowering += 1
                    elif plant.__class__ is Plant:
                        regular_plant += 1
            return (regular_plant, flowering, prize_flower)

        def count_plants(self) -> int:
            count: int = 0
            garden_names = self.__manager.gardens
            for name in garden_names:
                garden = self.__manager.gardens[name]
                for plant in garden.plants:
                    count += 1
            return count

        def increment_total_growth(self) -> None:
            self.__total_growth += 1

        @property
        def total_growth(self) -> int:
            return self.__total_growth


def main() -> None:
    manager = GardenManager("Alice")

    g1 = Garden("South garden")
    g1.add([(Plant, "Basil", 25), (FloweringPlant, "Rose", 60, "Red", 0),
           (PrizeFlower, "Orchid", 120, "White", 1, 9)])

    g2 = Garden("North Garden")
    g2.add([(Plant, "Oak", 3000), (FloweringPlant, "Tulip", 40, "Yellow", 0)])

    manager.add([g1, g2])
    manager.help_grow()
    manager.help_grow()

    print(manager.stats.count_plants())
    print(manager.stats.total_growth)
    print(manager.stats.plant_types())


if __name__ == "__main__":
    main()
