numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number)+"st",end=" ")
    elif number == 2:
        print(str(number)+"nd",end=' ')
    elif number == 3:
        print(str(number)+"rd",end=' ')
    else:
        print(str(number)+"th",end=' ')