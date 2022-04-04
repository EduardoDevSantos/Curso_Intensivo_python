#! /usr/bin/env python3
positions = [1,2,3,4,5,6,7,8,9]
for position in positions:
    if position == 1:
        print(str(position) + "st")
    elif position == 2:
        print(str(position) + "nd")
    elif position == 3:
        print(str(position) + "rd")
    else:
        print(str(position) + "th")