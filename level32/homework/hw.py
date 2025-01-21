

list = [1, 2, 3, 4, 5]


while len(list) > 0:
    list.pop()
i = 5
while len(list) < 5:
    list.append(i)
    i -= 1

print(list)
