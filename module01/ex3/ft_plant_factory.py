class Plant:
    """plant with a name, a height and an age"""

    count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        """create a plant

           name :   plant name
           height : height in centimeters
           age :    age in days
        """
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


class Factory:
    """create and store multiple plants at once"""
    def __init__(self) -> None:
        """create and empty factory"""
        self.plants = []

    def add(self, new_plants: list[tuple[str, int, int]]) -> None:
        """create plants from a list

           new_plants : (name, height, age) cf. Plant
        """
        for name, height, age in new_plants:
            self.plants += [Plant(name, height, age)]


def main() -> None:
    """demonstration of the plant factory"""
    f1 = Factory()
    print("=== Plant Factory Output ===")
    f1.add([("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
           ("Sunflower", 80, 45), ("Fern", 15, 120)])
    print(f"\nTotal plants created: {Plant.count}")


if __name__ == "__main__":
    main()
