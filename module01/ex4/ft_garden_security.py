class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.__height = 0
        self.set__height(height)
        self.__age = 0
        self.set__age(age)

    def set__height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set__age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get__height(self) -> int:
        return self.__height

    def get__age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"Current plant: {self.name} ", end='')
        print(f"({self.__height}cm, {self.__age} days)")


def main() -> None:
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print()
    p1.set__height(-5)
    print()
    p1.get_info()


if __name__ == "__main__":
    main()
