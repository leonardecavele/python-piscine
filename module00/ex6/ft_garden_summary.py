# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/16 11:51:31 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/16 11:51:31 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary() -> None:
    name: str = input("Enter garden name: ")
    plants: str = input("Enter number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {plants}")
    print("Status: Growing well!")
