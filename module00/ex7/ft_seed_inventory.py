# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 11:57:30 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/16 12:00:10 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
