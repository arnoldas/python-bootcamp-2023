import pandas

#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# while True:
#     try:
#         result = [nato_dictionary[letter] for letter in input("Enter a word: ").upper()]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         print(result)
#         break

# or we can achieve this by using function:
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # Calling the same function again if there was an error
    else:
        print(result)

generate_phonetic()
