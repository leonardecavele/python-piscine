class Plant:
    def __init__(
                self,
                name: str,
                height: int,
                age: int
                ) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(
                self,
                name: str,
                height: int,
                age: int,
                color: str
                ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    def __init__(
                self,
                name: str,
                height: int,
                age: int,
                trunk_diameter: int
                ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides 78 square meters of shade")

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(
                self,
                name: str,
                height: int,
                age: int,
                harvest_season: str,
                nutritional_value: str
                ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.__class__.__name__}): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest\n"
            f"{self.name} is rich in {self.nutritional_value}"
        )


def main() -> None:
    print("=== Garden Plant Types ===\n")
    Flower("Tulip", 20, 15, "yellow")
    f1 = Flower("Rose", 25, 30, "red")
    print(f1)
    f1.bloom()
    print()
    Tree("Pine", 800, 2500, 40)
    t1 = Tree("Oak", 500, 1825, 50)
    print(t1)
    t1.produce_shade()
    print()
    Vegetable("Carrot", 30, 70, "autumn", "vitamin A")
    print(Vegetable("Tomato", 80, 90, "summer", "vitamin C"))


if __name__ == "__main__":
    main()
