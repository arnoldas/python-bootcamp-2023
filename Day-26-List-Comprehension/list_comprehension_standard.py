numbers = [1, 2, 3]
new_list = []
for n in numbers:
    n += 1
    new_list.append(n)
print(new_list)

# or we can do in one line:
new_list2 = [n + 1 for n in numbers]
print(new_list2)
