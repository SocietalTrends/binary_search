# -*- coding: utf-8 -*-

searchlist = [0,1,2,3,4,5,6,7,8,9]
value = 4
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

print(" {} は {} 番目に見つかりました。".format(value, number))
