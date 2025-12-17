def ft_count_harvest_recursive(day: int = None, days: int = None) -> None:
    if not days:
        days = int(input("Days until harvest: "))
    if not day:
        day = 0
    day += 1
    print(f"Day {day}")
    if day == days:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive(day, days)
