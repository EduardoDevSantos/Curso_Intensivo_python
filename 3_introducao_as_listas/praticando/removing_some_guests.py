guests = ['grandfather','mother','father']
print("\nHi " + guests[0].title() + " do you want to go a dinner's family?")
print("Hi " + guests[1].title() + " do you want to go a dinner's family?")
print("Hi " + guests[2].title() + " do you want to go a dinner's family?")
print("I am inviting " + str(len(guests)) + " peoples to dinner.")
print("Oh, the " +guests[0].title()+ " don't can go to the dinner.")

guests[0] = 'aunt'
print("\nHi " + guests[0].title() + " do you want to go a dinner's family?")
print("Hi " + guests[1].title() + " do you want to go a dinner's family?")
print("Hi " + guests[2].title() + " do you want to go a dinner's family?")
print("Hey, i find a large table for this dinner!")
print("I am inviting " + str(len(guests)) + " peoples to dinner.")

guests.insert(0,'cousin')
guests.insert(0,'uncle')
guests.append('grandmother')
print("\nHi " + guests[0].title() + " do you want to go a dinner's family?")
print("Hi " + guests[1].title() + " do you want to go a dinner's family?")
print("Hi " + guests[2].title() + " do you want to go a dinner's family?")
print("Hi " + guests[3].title() + " do you want to go a dinner's family?")
print("Hi " + guests[4].title() + " do you want to go a dinner's family?")
print("Hi " + guests[5].title() + " do you want to go a dinner's family?")
print("Hey family, i'm so sorry,but i can to invite only two peoples for this dinner,the table is for three.")
print("I am inviting " + str(len(guests)) + " peoples to dinner.")

sorry = guests.pop(-1).title()
print("\nIm so sorry " + sorry + ", i promisse, the next time i'll invite you.")
sorry = guests.pop(0).title()
print("Im so sorry " + sorry + ", i promisse, the next time i'll invite you.")
sorry = guests.pop(0).title()
print("Im so sorry " + sorry + ", i promisse, the next time i'll invite you.")
sorry = guests.pop(0).title()
print("Im so sorry " + sorry + ", i promisse, the next time i'll invite you.")
print("I am inviting " + str(len(guests)) + " peoples to dinner.")

print("\nHi, " + guests[0].title() + ", you still in this dinner.")
print("Hi, " + guests[1].title() + ", you still in this dinner.")

del guests[0]
del guests[0]
print(guests)