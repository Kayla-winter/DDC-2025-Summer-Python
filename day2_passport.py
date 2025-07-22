# 🧃 Juice Bar Recommender

"""
🍓🥭 Welcome to the Code Island Juice Bar! 🏝️🍹

Today’s mission: Become a juice engineer and create a drink just for your customer.

🔍 What you’ll practice:
- input() to ask questions
- if/elif/else to make decisions
- Creative logic to match mood + flavor to a drink

🧪 Your Job:
1. Ask your customer (user) some questions.
2. Use logic to recommend the perfect drink.
3. Keep it fun, personal, and colorful!

🎨 Remix Challenges (do at least 3):
✅ Add 2–3 new moods and drink combos
✅ Let customers choose an extra topping (boba, glitter, etc)
✅ Print a receipt with name, order, and fake total price
✅ Add a secret VIP code that gives a mystery drink
✅ Add emoji art or a creative title
✅ Show a funny message if someone picks a weird fruit like “pickle”

🧠 Bonus Challenge (for fast coders):
- Add a surprise drink using random.choice()
- Let users build their own drink from 3 ingredients
- Use a loop to serve multiple customers in a row

📸 When You Finish:
- Screenshot your funniest or best drink output
- Write 1–2 sentences about what you changed
- Submit your .py file or Replit link to the class page
"""

print("🍓🥭 Welcome to the Code Island Juice Bar! 🏝️🍹")
print("We make magical smoothies based on your mood, taste, and style.\n")

# Ask customer details
name = input("👤 What's your name? ")
age = int(input("🎂 How old are you? "))
mood = input("😎 How are you feeling today? (happy, sleepy, lit, chill, ecstatic, sad): ").lower()
sweet = input("🍬 Do you want something sweet? (yes/no): ").lower()
fruit = input("🍉 What's your favorite fruit? (mango, strawberry, banana, etc): ").lower()
toppings = input("what topping would you like? (boba, oreos, cereal, etc): ").lower()
# Logic for drink recommendation
print("\n🧪 Mixing your ingredients...\n")

if age < 10:
    drink = "Baby Banana Bash with extra sprinkles 🍌✨"
elif sweet == "yes" and mood == "happy":
    drink = "Super Strawberry Sunshine with rainbow jelly 🍓🌈"
elif sweet == "no" and mood == "sleepy":
    drink = "Calm Coconut Chill – with low sugar 🥥😴"
elif fruit == "mango":
    drink = "Mango Mystery Blast – only for the bold 🥭🔥"
elif mood == "lit":
    drink = "Electric Energy Elixir – caffeine + sparkle ⚡💥"
else:
    drink = f"Classic {fruit.title()} Cooler 🍹"

# Output the result
print("🥤 Here's your personalized drink:")
print(f"{name}, we recommend: {drink}")
print("Enjoy and come back soon!\n")

# Add a signature stamp
print("🔖 Juice Bar Stamp: ✅ 🍍 Served with love.")
