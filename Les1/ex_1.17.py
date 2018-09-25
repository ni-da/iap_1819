# Exercise 1.17. Write a program that asks for the size of teams t and a number
# of participants p, and then calculates how many teams can be formed. Print
# out the number of teams and the number of participants left over. For example,
# if t = 4 and p = 11, then we have 2 teams and 3 remaining participants.

t = int(input("Size of teams: "))
p = int(input("Number of participants: "))

print("Teams: ", p // t, ", leftover paerticipants: ", p % t)
