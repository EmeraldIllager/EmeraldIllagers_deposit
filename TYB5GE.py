
 import random   
#game_name = "A Youthful Book -5: Groundegde"
 print(f"\n{'='*len(game_name)}")
 print(game_name)
 print(f"{'='*len(game_name)}")

# Player attributes
player_health = 100
player_boredom = 0
player_coins = 10

# Locations
locations = ["Blackwalk", "Company", "Staleboot"]

# Main game loop
while True:
    print("\nYou are in " + random.choice(locations))
    print("Player Health:", player_health)
    print("Player Boredom:", player_boredom)
    print("Player Coins:", player_coins)
... 
...     # Random encounter
...     if random.randint(1, 5) == 1:
...         print("You encounter a remarkably uninteresting situation!")
...         event = random.randint(1, 3)
...         if event == 1:
...             print("A local poet wants to recite their epic poem. You can listen for a fee of 2 coins.")
...             choice = input("Do you want to listen? (yes/no): ")
...             if choice.lower() == "yes":
...                 player_coins -= 2
...                 print("You endured the monotony.")
...                 player_boredom -= 10
...             else:
...                 print("You continue on your way.")
...                 player_boredom += 5
...         elif event == 2:
...             print("You accidentally step on a sleepy caterpillar. It doesn't seem to mind.")
...             player_boredom += 2
...         elif event == 3:
...             print("You find a job offer. You can earn 5 coins for a day's work of counting pebbles.")
...             choice = input("Do you want to take the job? (yes/no): ")
...             if choice.lower() == "yes":
...                 player_coins += 5
...                 print("You counted pebbles for the day and earned 5 coins.")
...                 player_boredom -= 20
...             else:
...                 print("You continue on your way.")
...                 player_boredom += 10
... 
...     # Boredom check
...     if player_boredom >= 100:
...         print("\nYou have become overwhelmingly bored and have decided to retire to your monotonous life. Game over!")
...         break
... 
...     input("\nPress Enter to continue...")
