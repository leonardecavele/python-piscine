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


class Flower(Plant):
    """a flower with a given color"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """create a flower

           name, height, age : cf. Plant
           color :  flower color
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """print a blooming message"""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """print the flower information"""
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")


class Tree(Plant):
    """a tree with a trunk diameter that can produce shade"""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """create a tree

           name, height, age :  cf. Plant
           trunk_diameter :     tree trunk diameter 
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """print a shade message"""
        print(f"{self.name} provides 78 square meters of shade")

    def get_info(self) -> None:
        """print the tree information"""
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    """a vegetable with harvest season and nutritional value"""

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """create a vegetable

           name, height, age :  cf. Plant
           harvest_season :     harvest season
           nutrional_value :    nutrional value
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        """print the vegetable information"""
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main() -> None:
    """demonstration of the different plant types"""
    print("=== Garden Plant Types ===\n")
    Flower("Tulip", 20, 15, "yellow")
    f1 = Flower("Rose", 25, 30, "red")
    f1.get_info()
    f1.bloom()
    print()
    Tree("Pine", 800, 2500, 40)
    t1 = Tree("Oak", 500, 1825, 50)
    t1.get_info()
    t1.produce_shade()
    print()
    Vegetable("Carrot", 30, 70, "autumn", "vitamin A")
    v1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    v1.get_info()


if __name__ == "__main__":
    main()
