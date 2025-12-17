class Plant:
    count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.count += 1
        print(f"Created: {name} ({height}cm, {age} days)")


def main() -> None:
    print("=== Plant Factory Output ===")
    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)
    Plant("Fern", 15, 120)
    print(f"\nTotal plants created: {Plant.count}")


if __name__ == "__main__":
    main()
