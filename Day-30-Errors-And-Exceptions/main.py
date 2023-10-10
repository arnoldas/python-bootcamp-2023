# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["non_existing_key"]
#except: # Catching all exceptions
except FileNotFoundError: # Catching specific error
    print("There was an error[FileNotFoundError]")
    file = open("a_file.txt", "w") # creating file if not exist
    file.write("testing text")
except KeyError as error_message:
    print(f"[KeyError] The key {error_message} does not exist.")
else: #executing if there were no exceptions in TRY block
    content = file.read()
    print(content)
finally: # this block executes always, no matter exception was or not
    file.close()
    print("Finally block")
    # raising our own Exceptions
    #raise KeyError
    raise TypeError("This is an error that I made up.")


# KeyError: 'non_existing_key'
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

#IndexError: list index out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 4)
