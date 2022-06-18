games_list = ['minecraft','pes2013']
print(games_list)

games_list[1] = 'pes2017'
print(games_list)

games_list.append('league of legends')
print(games_list)

games_list.insert(2,'wild rift')
print(games_list)

del games_list[3]
print(games_list)

favorite_game = games_list.pop(-1)
print("\nMy favorite game today is " + favorite_game.title() + ".\n")

games_list.remove('pes2017')
print(games_list)

games_list.append('gtav')
games_list.append('mario')
games_list.append('contra')
print(games_list)

print("\nSorted list:")
print(sorted(games_list))

print("\nReverse Sorted list: ")
print(sorted(games_list,reverse=True))

games_list.reverse()
print("\nReverse list: ")
print(games_list)

games_list.reverse()
print("\nThe original list:")
print(games_list)

games_list.sort()
print("\nSort list:")
print(games_list)

games_list.sort(reverse=True)
print("\nReverse sort list:")
print(games_list)

# print(games_list[5]) erro de índice.

