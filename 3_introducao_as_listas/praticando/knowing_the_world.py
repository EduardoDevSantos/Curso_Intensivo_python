places = ['florianopolis','são paulo','canadá','estados unidos','rio grande do sul']
print("\nHere is the places i want to visite: ")
print(places)

print("\nAnd here the places sorted:")
print(sorted(places))

print("\nBut the original list continue here:")
print(places)

print("\nHere is my list inverse sorted:")
print(sorted(places,reverse=True))

print("\nBut the original list continues here:")
print(places)

places.reverse()
print("\nI changed my list, it's reverse now!")
print(places)

places.reverse()
print("\nI give up, my list will back to original form again: ")
print(places)

places.sort()
print("\nNow I'm going to change my list, it's arranged in alphabetical order:")
print(places)

places.sort(reverse=True)
print("\nI am soo crazy, and i arranged my list in reverse alphabetical order:")
print(places)