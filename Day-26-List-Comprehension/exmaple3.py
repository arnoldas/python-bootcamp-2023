# import numbers from example3_file1.txt and example3_file2.txt
# and print the numbers which are in a both files
with open("example3_file1.txt", "r") as f:
    file1_lines = f.readlines()

with open("example3_file2.txt", "r") as f:
    file2_lines = f.readlines()

result = [int(n) for n in file1_lines if n in file2_lines]
print(result)
