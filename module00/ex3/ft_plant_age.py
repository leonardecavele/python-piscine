# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 11:16:05 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/16 11:18:42 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
    if int(input("Enter plant age in days: ")) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
