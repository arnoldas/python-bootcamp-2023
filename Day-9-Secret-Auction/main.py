from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")

continue_bidding = "yes"
participants = {}

while continue_bidding == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    participants[name] = bid
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bidding == "yes":
        clear()

winner_value = 0
winner_name = ""
for name in participants:
    if participants[name] > winner_value:
        winner_name = name
        winner_value = participants[name]

print(f"Auction winner is {winner_name} with a bid ${winner_value}")
    