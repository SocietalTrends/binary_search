# -*- coding: utf-8 -*-

searchlist = [0,1,2,3,4,5,6,7,8,9]
value  = int(input("Please enter number you want to search: \n"))
number = -1

left = 0
right = len(searchlist)-1


print(searchlist)
while left <= right:
    center = int((left + right)/2)
    if searchlist[center] == value:
        number = center + 1
        break
    elif searchlist[center] < value:
        left = center + 1
    else:
        right = center - 1

if number == -1:
    print("{} は見つかりませんでした。".format(value))
else:
    print(" {} は {} 番目に見つかりました。".format(value, number))
