# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldecavel <ldecavel@student.42lyon.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 18:08:34 by ldecavel          #+#    #+#              #
#    Updated: 2025/12/08 18:08:54 by ldecavel         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area() -> None:
    length: int = int(input("Enter length: "))
    width: int = int(input("Enter width: "))
    print(f"Plot area: {length * width}")
