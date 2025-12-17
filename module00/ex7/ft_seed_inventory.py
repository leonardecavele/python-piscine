def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets" or unit == "grams" or unit == "area":
        print(f"{seed_type.capitalize()} seeds: {quantity} ", end="")
        if unit == "packets":
            print("available")
        elif unit == "grams":
            print("total")
        elif unit == "area":
            print("square meters")
    else:
        print("Unknown unit type.")
