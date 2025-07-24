# 🐶 Day 4: Virtual Pet Simulator

"""
👾 Welcome to Code Island’s Virtual Pet Challenge!

Today you’ll build a pet simulator where players can take care of a digital pet.
They’ll feed it, play with it, and keep it alive and happy using Python code!

🔍 What you’ll practice:
- Using variables to track your pet’s status (like hunger or happiness)
- Using loops to keep your program running
- Using `if` statements to react to the player’s actions

🐾 Game Idea:
You adopt a virtual pet — a dog, cat, alien, or anything silly!
Players must keep it alive by choosing actions like FEED, PLAY, or REST.
If they ignore it or make bad choices, the pet gets sad or runs away!

🎨 Remix Challenges (do at least 2–3):
✅ Let the user choose their pet’s name and type
✅ Add a “happiness” or “energy” meter
✅ Add a timer (limited rounds)
✅ Use `random.choice()` to add surprises (like "Your pet found a toy!")
✅ Add ASCII art or emoji to show how the pet feels 🥹😎🥴
✅ Add a restart or game over loop

📸 When You Finish:
- Let someone else try to take care of your pet
- Show off your best pet survival record
- Submit your `.py` file or Replit link
"""

# 🐾 Starter Code
print("🐾 Welcome to the Virtual Pet Game!")
name = input("What would you like to name your pet? ")
pet_type = input("What kind of pet is it? (dog, cat, alien, etc): ")

hunger = 5  # 0 is full, 10 is starving
happiness = 5  # 0 is sad, 10 is super happy

print(f"\nYou adopted a {pet_type} named {name}! Take good care of it.")

# Game loop (runs for 5 turns)
for turn in range(5):
    print("\nWhat would you like to do?")
    print("1 - Feed")
    print("2 - Play")
    print("3 - Do nothing")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        hunger = max(0, hunger - 2)
        print(f"You fed {name}. Hunger is now {hunger}.")
    elif choice == "2":
        happiness = min(10, happiness + 2)
        hunger = min(10, hunger + 1)  # playing makes it hungry
        print(f"You played with {name}. Happiness is now {happiness}, but hunger is now {hunger}.")
    elif choice == "3":
        hunger = min(10, hunger + 2)
        happiness = max(0, happiness - 2)
        print(f"You did nothing. {name} looks bored and hungry... 😢")
    else:
        print("Invalid choice. Nothing happens.")

# End of game
print("\n🧾 Game Over!")
if hunger >= 10:
    print(f"{name} was too hungry and ran away in search of snacks. 🍟")
elif happiness <= 0:
    print(f"{name} got too sad and hid in its pet bed. 🐾")
else:
    print(f"You did a great job taking care of {name}! 🎉")
