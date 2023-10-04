def add(*args):
    #print(type(args)) # Tuple
    #print(args[0]) # prints the first argument value
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum


print(add(1, 3, 5))
print(add(1, 3, 5, 8, 15))