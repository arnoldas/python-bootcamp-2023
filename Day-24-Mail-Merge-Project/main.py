#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    default_content = letter_file.read()

for name in names_list:
    name = name.strip()
    new_content = default_content.replace("[name]", name)
    print(new_content)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as new_letter:
        new_letter.write(new_content)
