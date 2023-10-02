names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Create a list with short names (name has 4 or less letters)
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Create a list with 5 or more letters and names should be in uppercase version
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
