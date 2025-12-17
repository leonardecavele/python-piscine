class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        print(f"Plant created: {self.name}")
        self.height = 0
        self.set_height(height)
        self.age = 0
        self.set_age(age)

    def set_height(self, height: int):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = age
            print(f"Age updated: {age} days [OK]")

    def get_info(self):
        print(f"Current plant: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print()
    p1.set_height(-5)
    print()
    p1.get_info()


if __name__ == "__main__":
    main()
