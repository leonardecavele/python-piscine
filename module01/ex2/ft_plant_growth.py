class Plant:
    """plant with a name, a height and an age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """create a plant

           name :   plant name
           height : height in centimeters
           age :    age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        """grow the plant by 1cm and age it by 1 day"""
        self.height += 1
        self.age += 1

    def get_info(self) -> None:
        """print the plant information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """one-week growth simulation for a plant"""
    p1 = Plant("Rose", 25, 30)

    tmp: int = p1.height
    day: int = 1
    print(f"=== Day {day} ===")
    p1.get_info()
    while day < 7:
        p1.grow()
        day += 1
    print(f"=== Day {day} ===")
    p1.get_info()
    print(f"Growth this week: +{p1.height - tmp}cm")


if __name__ == "__main__":
    main()
