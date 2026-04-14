import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice (Rock, Paper, Scissor) = ")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
if user_choice == comp_choice:
    print("It's a tie!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer wins!")
    else:
        print("Rock smashes Scissors = User wins!")
    
elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers Rock = User wins!")
    else:
        print("Scissor cuts Paper = Computer wins!")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissors = Computer wins!")
    else:
        print("Scissor cuts Paper = User wins!")