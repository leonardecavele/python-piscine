class Plant:
    count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1


class Garden:
    def __init__(self) -> None:
        self.plants = []

    def add(self, new: Plant) -> None:
        self.plants += [Plant]
        print(f"Created: {new.name} ({new.height}cm, {new.age} days)")


def main() -> None:
    g1 = Garden()
    print("=== Plant Factory Output ===")
    g1.add(Plant("Rose", 25, 30))
    g1.add(Plant("Oak", 200, 365))
    g1.add(Plant("Cactus", 5, 90))
    g1.add(Plant("Sunflower", 80, 45))
    g1.add(Plant("Fern", 15, 120))
    print(f"\nTotal plants created: {Plant.count}")


if __name__ == "__main__":
    main()
