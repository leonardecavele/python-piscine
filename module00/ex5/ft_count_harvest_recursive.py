# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 11:29:42 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/16 11:37:37 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive() -> None:
    days: int = None
    if not days:
        day: int = 0
        days = int(input("Days until harvest: "))
    day += 1
    print(f"Day {day}")
    if day == days:
        print("Harvest time!")
    else:
        ft_count_harvest_recursive()
