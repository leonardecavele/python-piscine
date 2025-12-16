# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 11:19:32 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/16 11:20:59 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None:
    if int(input("Days since last watering: ")) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine.")
