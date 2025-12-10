# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 18:24:18 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/08 18:31:17 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    total: int = 0
    total += int(input("Day 1 harvest: "))
    total += int(input("Day 2 harvest: "))
    total += int(input("Day 3 harvest: "))
    print(f"Total harvest: {total}")
