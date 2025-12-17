class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> None:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main() -> None:
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print(p1)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()
