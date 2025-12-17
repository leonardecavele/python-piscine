class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.__name = name
        self.__height = height
        self.__age = age

    def grow(self) -> None:
        self.__height += 1
        self.__age += 1

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height}cm, {self.__age} days old"  # to do


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 blooming: bool) -> None:
        super().__init__(name, height, age)
        self.__color = color
        self.__blooming = blooming

    def __str__(self) -> str:
        return super().__str__()  # to do


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        super().__init__(name, height, age, color, blooming)
        self.__prize_points = prize_points

    def __str__(self) -> str:
        return super().__str__()  # to do


class Garden:
    def __init__(self, name: str) -> None:
        self.__plants = []
        self.__name = name

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
        for plant, *args in new_plants:
            self.__plants += [plant(*args)]
            print(f"Added {args[0]} to {self.__name}")

    def get_info(self) -> None:
        print()


# instance methods, class-level methods, utility functions
# each garden should track plant collections and statistics
# use nested statistics helepr to calculate analytics
class GardenManager:
    def __init__(self) -> None:
        self._gardens: dict[str, Garden] = {}
        self._stats = GardenManager.GardenStats()

    def add(self, garden: Garden) -> None:
        self._gardens[garden.name] = garden

    class GardenStats:
        pass  # functions for calculating statistics

    def create_garden_network() -> None:
        pass


def main() -> None:
    manager = GardenManager()

    g1 = Garden("South garden")
    g1.add(("Basil", 18, 25), ("Rose", 35, 60, "Red"), ("Orchid", 22, 120, "White", 9))

    g2 = Garden("North Garden")
    g2.add(("Oak", 500, 3000), ("Tulip", 28, 40, "Yellow"))

    manager.add(g1)
    manager.add(g2)


if __name__ == "__main__":
    main()
