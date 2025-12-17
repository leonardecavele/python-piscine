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

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
        for plant, *args in new_plants:
            self.__plants += [plant(*args)]
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
        self.__stats = GardenManager.GardenStats()

    def add(self, gardens: list[Garden]) -> None:
        for garden in gardens:
            self.__gardens[garden.name] = garden

    class GardenStats:
        pass  # functions for calculating statistics

    def create_garden_network() -> None:
        pass

    def help_grow(self) -> None:
        print(f"{self.__name} is helping all plants grow...")
        for garden_name in self.__gardens:
            garden = self.__gardens[garden_name]
            for plant in garden.plants:
                plant.grow()


def main() -> None:
    manager = GardenManager("Alice")

    g1 = Garden("South garden")
    g1.add([(Plant, "Basil", 25), (FloweringPlant, "Rose", 60, "Red", 0),
           (PrizeFlower, "Orchid", 120, "White", 1, 9)])

    g2 = Garden("North Garden")
    g2.add([(Plant, "Oak", 3000), (FloweringPlant, "Tulip", 40, "Yellow", 0)])

    manager.add([g1, g2])
    manager.help_grow()


if __name__ == "__main__":
    main()
