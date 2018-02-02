q = int(input("day of the month: "))
m = int(input("month (January = 13, February = 14, March = 3): "))
k = int(input("year of century (20[18]<--): "))
j = int(input("zero based century (-->[20]18): "))

if m == 14 or m == 13:
    k = k - 1

h = (q + (13 * (m + 1)) // 5 + k +( k // 4) + ( j // 4 ) - 2 * j) % 7

if  h == 0:
    h = "Saturday"
elif h == 1:
    h = "Sunday"
elif h == 2:
    h = "Monday"
elif h == 3:
    h = "Tuesday"
elif h == 4:
    h = "Wednesday"
elif h == 5:
    h = "Thursday"
elif h == 6:
    h = "Friday"

#// = floor division (eg: 11/2 = 5)

print(h)