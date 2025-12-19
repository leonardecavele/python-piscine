class SecurePlant:
    """secured plant with a name, a valid height and a valid age"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """create a secured plant

           name :   plant name
           height : height in centimeters
           age :    age in days
        """
        self.__name = name
        print(f"Plant created: {self.__name}")
        self.__height = 0
        self.set_height(height)
        self.__age = 0
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """safely update height"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """safely update age"""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """get the height"""
        return self.__height

    def get_age(self) -> int:
        """get the age"""
        return self.__age

    def get_info(self) -> None:
        """print the plant information"""
        print(f"Current plant: {self.__name} ", end='')
        print(f"({self.__height}cm, {self.__age} days)")


def main() -> None:
    """demonstration of the garden security system"""
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print()
    p1.set_height(-5)
    print()
    p1.get_info()


if __name__ == "__main__":
    main()
