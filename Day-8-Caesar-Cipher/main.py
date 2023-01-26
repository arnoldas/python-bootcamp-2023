import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(p_text, p_amount, p_direction):
    result_text = ""
    for char in p_text:
        if char not in alphabet:
            result_text += char
        else:
            if p_direction == "encode":
                index = alphabet.index(char) + p_amount
                if index >= len(alphabet):
                    index -= len(alphabet)
            elif p_direction == "decode":
                index = alphabet.index(char) - p_amount
            result_text += alphabet[index]
    print(f"Here's the {p_direction}d result: {result_text}")

print(art.logo)
execute_program = "yes"
while execute_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift % len(alphabet)
    caesar(p_text=text, p_amount=shift, p_direction=direction)
    execute_program = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
print("Goodbye")