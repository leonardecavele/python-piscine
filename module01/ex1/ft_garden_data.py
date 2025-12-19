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

    def get_info(self) -> None:
        """print a description of the plant"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """create some plants and displey them"""
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    p1.get_info()
    p2.get_info()
    p3.get_info()


if __name__ == "__main__":
    main()

