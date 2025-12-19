class Plant:
    """plant with a name and a height"""

    def __init__(self, name: str, height: int) -> None:
        """create a plant

           name :   plant name
           height : height in centimeters
        """
        self.__name: str = name
        self.__height: int = Plant.valid_height(height)

    def grow(self) -> None:
        """grow the plant by 1cm and print a message"""
        self.__height += 1
        print(f"{self.__name} grew 1cm")

    @staticmethod
    def valid_height(height: int) -> int:
        """validate a given height value

           height : height in centimeters

        returns :
           a positive height or 1 if height <= 0
        """
        if height > 0:
            return height
        else:
            return 1

    def get_name(self) -> str:
        """get the Plant name"""
        return self.__name

    def get_height(self) -> int:
        """get the Plant height"""
        return self.__height

    def get_info(self) -> None:
        """print the Plant information"""
        print(f"- {self.__name}: {self.__height}cm")


class FloweringPlant(Plant):
    """a plant with flowers, a given color and a blooming status"""

    def __init__(self, name: str, height: int, color: str,
                 blooming: bool) -> None:
        """create a flowering plant

           name, height :   cf. Plant
           color :      flower color
           blooming :   true if the plant is currently blooming
        """
        super().__init__(name, height)
        self.__color = color
        self.__blooming = blooming

    def get_info(self) -> None:
        """print the flower information"""
        print(
            f"- {self.get_name()}: {self.get_height()}cm"
            f", {self.__color} flowers"
            f" ({'blooming' if self.__blooming else 'not blooming'})"
        )


class PrizeFlower(FloweringPlant):
    """a flowering plant with prize points"""

    def __init__(self, name: str, height: int, color: str,
                 blooming: bool, prize_points: int) -> None:
        """create a prize flower

           name, height, color, blooming :  cf. FloweringPlant
           prize_points :   points awarded by the plant
        """
        super().__init__(name, height, color, blooming)
        self.__prize_points = prize_points

    def get_prize_points(self) -> int:
        """get the prize points value"""
        return self.__prize_points

    def get_info(self) -> None:
        """print the prize flower information"""
        print(
            f"- {self.get_name()}: {self.get_height()}cm"
            f", {self._FloweringPlant__color} flowers"
            f" ({'blooming' if self._FloweringPlant__blooming else 'not blooming'})"
            f", Prize points: {self.__prize_points}"
        )


class Garden:
    """a list of plants that holds their statistics"""

    def __init__(self, name: str) -> None:
        """create an empty garden.

           name: garden name
        """
        self.__plants: list[Plant] = []
        self.__name: str = name
        self.__total_growth = 0
        self.__total_prize_points = 0
        self.__total_blooming = 0
        self.__plant_count = 0
        self.__plant_types = [0, 0, 0]

    def add(self, new_plants: list[tuple[type[Plant]], object]) -> None:
        """add new plants to the garden

           new_plants : [(PlantClass, arg1, arg2, ...), ...]
        """
        for plant, *args in new_plants:
            self.__plants += [plant(*args)]
            self.__plant_count += 1
            index: int = Garden.type_index(plant)
            self.__plant_types[index] += 1
            if index == 1:
                if args[-1]:
                    self.__total_blooming += 1
            if index == 2:
                self.__total_prize_points += args[-1]
                if args[-2]:
                    self.__total_blooming += 1
            print(f"Added {args[0]} to {self.__name}")

    def increment_total_growth(self) -> None:
        """increment total_growth by 1cm"""
        self.__total_growth += 1

    def report(self) -> None:
        """print a report on the garden contents and its statistics"""
        print(f"=== {self.__name} Report ===")
        print("Plants in garden:")
        for plant in self.__plants:
            plant.get_info()
        print()
        print(
            f"Plants added: {self.__plant_count}, ",
            f"Total growth: {self.__total_growth}cm"
            )
        print(
            f"Plant types: {self.__plant_types[0]} regular,",
            f"{self.__plant_types[1]} flowering,",
            f"{self.__plant_types[2]} prize flowers"
            )

    @staticmethod
    def type_index(plant: type[Plant]) -> int:
        """return the type index for the plant_types list

           plant :  Plant class or a Plant child class

        returns :
           0 for Plant, 1 for FloweringPlant, 2 for PrizeFlower
        """
        if plant is PrizeFlower:
            return 2
        if plant is FloweringPlant:
            return 1
        return 0

    def get_total_growth(self) -> int:
        """get the total growth value"""
        return self.__total_growth

    def get_total_blooming(self) -> int:
        """get the count of flowers in blooming state"""
        return self.__total_blooming

    def get_total_prize_points(self) -> int:
        """get the total prize points"""
        return self.__total_prize_points

    def get_name(self) -> str:
        """get the Garden name"""
        return self.__name

    def get_plants(self) -> list[Plant]:
        """get the list of Plant instances"""
        return self.__plants

    def get_plant_count(self) -> int:
        """get the number of Plant instances"""
        return self.__plant_count

    def get_plant_types(self) -> list[int]:
        """get type counts as [regular, flowering, prize]"""
        return self.__plant_types


class GardenManager:
    """manage multiple gardens and print statistics"""

    __managers: list["GardenManager"] = []

    def __init__(self, name: str) -> None:
        """create a garden manager.

           name :   manager name
        """
        self.__name: str = name
        self.__gardens: dict[str, Garden] = {}
        self.__stats = GardenManager.GardenStats(self)
        GardenManager.__managers += [self]

    def add(self, gardens: list[Garden]) -> None:
        """register gardens under this manager

           gardens :    gardens to manage
        """
        for garden in gardens:
            self.__gardens[garden.get_name()] = garden

    def help_grow(self) -> None:
        """make every plant in every managed garden grow"""
        print(f"{self.__name} is helping all plants grow...")
        for garden_name in self.__gardens:
            garden = self.__gardens[garden_name]
            for plant in garden.get_plants():
                plant.grow()
                garden.increment_total_growth()

    def report(self) -> None:
        """print a full report of all managed gardens"""
        print(f"=== {self.__name} Report ===")
        for garden_name in self.__gardens:
            print(f"Plants in {garden_name}:")
            plants = self.__gardens[garden_name].get_plants()
            for plant in plants:
                plant.get_info()
            print()
        print(
            f"Plants added: {self.__stats.count_plants()}, ",
            f"Total growth: {self.__stats.count_growth()}cm"
            )
        print(
            f"Plant types: {self.__stats.plant_types()[0]} regular,",
            f"{self.__stats.plant_types()[1]} flowering,",
            f"{self.__stats.plant_types()[2]} prize flowers"
            )
        print()
        self.__stats.height_validation()
        self.__stats.garden_score()
        self.__stats.gardens_managed()

    @classmethod
    def create_garden_network(cls,
                              manager_name: str,
                              gardens_spec:
                              dict[str, list[tuple[type[Plant], object]]],
                              ) -> "GardenManager":
        """factory to build a manager and its gardens

           manager_name :   cf. GardenManager
           gardens_spec :   cf. Garden

        returns :
           an initialized garden manager with initialized Garden
           instances registered
        """
        manager = cls(manager_name)
        gardens: list[Garden] = []
        for garden_name in gardens_spec:
            garden = Garden(garden_name)
            garden.add(gardens_spec[garden_name])
            gardens += [garden]
        manager.add(gardens)
        return manager

    def get_name(self) -> str:
        """get the manager name"""
        return self.__name

    def get_managers(self) -> list["GardenManager"]:
        """get the list of all GardenManager instances"""
        return self.__managers

    def get_gardens(self) -> dict[str, Garden]:
        """get the Garden instances managed by this GardenManager"""
        return self.__gardens

    def get_stats(self) -> "GardenManager.GardenStats":
        """get the stats helper of this GardenManager"""
        return self.__stats

    class GardenStats:
        """compute statistics of a GardenManager associated gardens"""

        def __init__(self, manager: "GardenManager") -> None:
            """create a stats helper bound to a manager

               manager :    GardenManager to bound with
            """
            self.__manager: GardenManager = manager

        def plant_types(self) -> tuple[int, int, int]:
            """count plant types across all managed gardens

            returns:
               a tuple (regular, flowering, prize)
            """
            regular_plant = 0
            flowering = 0
            prize_flower = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                regular_plant += garden.get_plant_types()[0]
                flowering += garden.get_plant_types()[1]
                prize_flower += garden.get_plant_types()[2]
            return (regular_plant, flowering, prize_flower)

        def count_plants(self) -> int:
            """count total number of plants across all managed gardens"""
            count: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                count += garden.get_plant_count()
            return count

        def count_growth(self) -> int:
            """count total growth across all managed gardens"""
            count: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                garden = self.__manager.get_gardens()[name]
                count += garden.get_total_growth()
            return count

        def garden_score(self) -> None:
            """print a score for each manager

            score rules:
                prize_points * 3
                total_growth * 2
                total_blooming * 5
            """
            score: int = -1
            managers: list["GardenManager"] = self.__manager.get_managers()
            print("Garden scores - ", end='')
            for manager in managers:
                if score != -1:
                    print(", ", end='')
                score = 0
                print(f"{manager.get_name()}: ", end='')
                garden_names = manager.get_gardens()
                for name in garden_names:
                    score += manager.get_gardens()[name].get_total_prize_points() * 3
                    score += manager.get_gardens()[name].get_total_growth() * 2
                    score += manager.get_gardens()[name].get_total_blooming() * 5
                print(f"{score}", end='')
            print()

        def height_validation(self) -> None:
            """check if all plants have a valid height"""
            correct_height: bool = True
            managed_gardens: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                managed_gardens += 1
                garden = self.__manager.get_gardens()[name]
                for plant in garden.get_plants():
                    if plant.get_height() < 1:
                        correct_height = False
            print(f"Height validation test: {correct_height}")

        def gardens_managed(self) -> None:
            """print how many gardens are managed by the manager"""
            managed_gardens: int = 0
            garden_names = self.__manager.get_gardens()
            for name in garden_names:
                managed_gardens += 1
            print(f"Total gardens managed: {managed_gardens}")


def main() -> None:
    """demonstration of the garden management system"""
    print("=== Garden Management System Demo ===")
    print()

    m1 = GardenManager.create_garden_network(
        "Jean",
        {
            "Eath garden": [
                (Plant, "Spruce", 450),
            ],
        },
    )
    m2 = GardenManager.create_garden_network(
        "Eude",
        {
            "South garden": [
                (Plant, "Baobab", 250),
                (FloweringPlant, "Dandelion", 35, "white", True),
                (PrizeFlower, "Daisy", 45, "purple", False, 7),
            ],
            "North garden": [
                (Plant, "Bamboo", 180),
                (FloweringPlant, "Tulip", 20, "red", False),
            ],
        },
    )
    print()

    m2.help_grow()
    print()

    m2.report()


if __name__ == "__main__":
    main()
