# THE MYSTIC FOREST ADVENTURE
# A simple text-based game to learn conditional statements (if/elif/else)

print("=" * 50)
print("    🌲 THE MYSTIC FOREST ADVENTURE 🌲")
print("=" * 50)
print()
print("You wake up in a dark, mysterious forest with no memory of how you got here.")
print("Strange sounds echo through the trees, and an eerie mist surrounds you.")
print("Your goal is to find your way out safely...")
print()

# Initialize player stats
health = 100
energy = 100

print("--- Your Stats ---")
print(f"Health: {health}")
print(f"Energy: {energy}")
print("------------------")
print()

# FIRST MAJOR DECISION POINT
print("🌲 FOREST ENTRANCE")
print("You see three paths ahead:")
print("1. A well-lit path with singing birds")
print("2. A dark, narrow trail with glowing mushrooms") 
print("3. A rocky path leading uphill")
print()


# Get player choice
path_choice = input("Which path do you choose? (1, 2, or 3): ")

# First conditional branch - this teaches if/elif/else
if path_choice == "1":
    print()
    print("🐦 You chose the well-lit path...")
    print("The birds guide you safely, but you feel tired from the long walk.")
    energy = energy - 20  # Show how conditions can affect variables
    print("You lose 20 energy but stay safe.")
    chosen_path = "bright"
    
elif path_choice == "2":
    print()
    print("🍄 You chose the dark trail...")
    print("The glowing mushrooms are beautiful but emit strange spores.")
    health = health - 15  # Conditional effect on health
    energy = energy + 10  # But gain some magical energy
    print("You lose 15 health but gain 10 energy from the magical mushrooms.")
    chosen_path = "dark"
    
elif path_choice == "3":
    print()
    print("🗻 You chose the rocky uphill path...")
    print("The climb is exhausting but you get a great view of the area.")
    energy = energy - 30  # Conditional effect on energy
    print("You lose 30 energy from the difficult climb.")
    chosen_path = "mountain"
    
else:
    # Input validation using else
    print()
    print("Invalid choice! You stand confused and a friendly squirrel guides you to the bright path.")
    energy = energy - 10
    print("You lose 10 energy from confusion.")
    chosen_path = "bright"

print()
print("--- Your Stats ---")
print(f"Health: {health}")
print(f"Energy: {energy}")
print("------------------")
print()

# SECOND MAJOR DECISION POINT - Different scenarios based on first choice
# This shows how previous conditions affect future options

if chosen_path == "bright":
    print("🌞 THE BRIGHT PATH")
    print("You reach a clearing with a sparkling fountain and a friendly hermit.")
    print("The hermit offers you a choice:")
    print("1. Drink from the magical fountain")
    print("2. Ask the hermit for directions")
    print("3. Rest by the fountain")
    
    action_choice = input("What do you do? (1, 2, or 3): ")
    
    if action_choice == "1":
        print()
        print("💧 You drink from the fountain...")
        # Nested conditional - outcome depends on current health
        if health >= 80:
            print("The water tastes amazing! You feel completely refreshed.")
            health = 100
            energy = 100
            print("Your health and energy are fully restored!")
        else:
            print("The water helps, but you needed more healing.")
            health = health + 30
            energy = energy + 20
            print("You gain 30 health and 20 energy.")
        ending_type = "fountain"
        
    elif action_choice == "2":
        print()
        print("🧙 You ask the hermit for help...")
        print("The hermit gives you a map and some advice about avoiding dangers.")
        energy = energy + 15
        print("You gain 15 energy from the helpful advice.")
        ending_type = "hermit"
        
    else:
        print()
        print("😴 You rest by the fountain...")
        energy = energy + 25
        print("You gain 25 energy from the peaceful rest.")
        ending_type = "rest"

elif chosen_path == "dark":
    print("🌙 THE DARK TRAIL")
    print("You encounter a mysterious creature blocking your path!")
    print("It doesn't seem hostile, but it's watching you carefully.")
    print("1. Try to communicate with the creature")
    print("2. Sneak around it quietly")
    print("3. Offer it some food from your backpack")
    
    creature_choice = input("What do you do? (1, 2, or 3): ")
    
    if creature_choice == "1":
        print()
        print("🗣️ You try to communicate...")
        # Conditional outcome based on current health
        if health >= 70:
            print("Your strong presence impresses the creature!")
            print("It leads you to a secret exit from the forest.")
            ending_type = "creature_ally"
        else:
            print("The creature senses your weakness and growls.")
            print("You back away slowly and find another path.")
            health = health - 10
            ending_type = "alternative"
            
    elif creature_choice == "2":
        print()
        print("🤫 You sneak around quietly...")
        # Energy affects stealth success
        if energy >= 60:
            print("You successfully sneak past! The creature never noticed.")
            energy = energy - 20
            ending_type = "stealth"
        else:
            print("You're too tired to sneak properly and step on a branch!")
            print("The creature notices but lets you pass peacefully.")
            energy = energy - 10
            ending_type = "peaceful"
            
    else:
        print()
        print("🍞 You offer food to the creature...")
        print("The creature accepts your gift gratefully!")
        energy = energy - 5
        ending_type = "friendship"

else:  # chosen_path == "mountain"
    print("⛰️ THE MOUNTAIN PATH")
    print("From the mountain top, you see the entire forest spread below you.")
    print("You spot three possible ways down:")
    print("1. A steep but direct path down")
    print("2. A winding path through caves")
    print("3. Wait for help (you saw smoke from a distant cabin)")
    
    descent_choice = input("What do you choose? (1, 2, or 3): ")
    
    if descent_choice == "1":
        print()
        print("⬇️ You take the steep path...")
        # Energy determines if you can handle the steep descent
        if energy >= 40:
            print("You carefully make your way down without injury.")
            energy = energy - 20
            ending_type = "safe_descent"
        else:
            print("You're too tired and slip, injuring yourself.")
            health = health - 25
            energy = energy - 15
            ending_type = "injured_descent"
            
    elif descent_choice == "2":
        print()
        print("🕳️ You enter the caves...")
        print("The caves are dark but lead to an underground river.")
        energy = energy - 15
        ending_type = "cave_river"
        
    else:
        print()
        print("🏠 You wait for help...")
        print("A friendly ranger finds you and escorts you to safety.")
        energy = energy - 10
        ending_type = "rescue"

print()
print("--- Final Stats ---")
print(f"Health: {health}")
print(f"Energy: {energy}")
print("-------------------")
print()

# DIFFERENT ENDINGS BASED ON PLAYER CHOICES
# This shows how multiple conditions can lead to different outcomes

print("🎉 GAME ENDING")
print("=" * 50)

# Multiple if statements to determine ending message
if ending_type == "fountain":
    if health >= 90 and energy >= 90:
        print("⭐ MAGICAL RESTORATION ENDING - BEST!")
        print("The fountain's magic has transformed you!")
        print("You not only find your way out but gain magical abilities!")
        print("You become a guardian of the forest.")
    else:
        print("🌟 MAGICAL HEALING ENDING - GOOD!")
        print("The fountain helped you recover enough to find your way home.")
        print("You escape the forest safely!")

elif ending_type == "hermit":
    print("🌟 WISE GUIDANCE ENDING - GOOD!")
    print("Following the hermit's advice, you navigate the forest expertly.")
    print("You not only escape but help other lost travelers!")

elif ending_type == "rest":
    print("🌟 PEACEFUL REST ENDING - GOOD!")
    print("Well-rested, you calmly find your way out of the forest.")
    print("Sometimes the best choice is to rest and think!")

elif ending_type == "creature_ally":
    print("⭐ MYSTICAL ALLY ENDING - BEST!")
    print("The creature becomes your friend and shows you forest secrets!")
    print("You leave with magical knowledge and a new ally!")

elif ending_type == "alternative":
    if health >= 60:
        print("🌟 ALTERNATIVE PATH ENDING - GOOD!")
        print("You find another way out and escape safely!")
    else:
        print("😅 SURVIVED ENDING - OKAY!")
        print("You barely make it out, but you're safe!")

elif ending_type == "stealth":
    print("🌟 STEALTH MASTER ENDING - GOOD!")
    print("Your stealth skills helped you avoid danger completely!")
    print("You escape undetected like a forest ninja!")

elif ending_type == "peaceful":
    print("🌟 PEACEFUL ENCOUNTER ENDING - GOOD!")
    print("Even though you were caught, the creature was peaceful.")
    print("You learned that not all scary things are dangerous!")

elif ending_type == "friendship":
    print("⭐ FRIENDSHIP ENDING - BEST!")
    print("Your kindness earned you a magical friend!")
    print("The creature guides you home and visits you often!")

elif ending_type == "safe_descent":
    print("🌟 MOUNTAIN MASTER ENDING - GOOD!")
    print("Your careful descent brought you safely down the mountain!")
    print("You exit the forest with new climbing skills!")

elif ending_type == "injured_descent":
    if health >= 40:
        print("😅 TOUGH SURVIVOR ENDING - OKAY!")
        print("Despite your injury, you made it out!")
        print("You're tougher than you thought!")
    else:
        print("😰 BARELY SURVIVED ENDING - CLOSE CALL!")
        print("You're badly injured but alive!")
        print("You'll recover, but this was a close call!")

elif ending_type == "cave_river":
    print("⭐ UNDERGROUND EXPLORER ENDING - BEST!")
    print("The underground river led you to a hidden village!")
    print("You discovered a secret community!")

elif ending_type == "rescue":
    print("🌟 RESCUED ENDING - GOOD!")
    print("The ranger brings you safely back to civilization!")
    print("Sometimes waiting for help is the smartest choice!")

print()
print("=" * 50)
print("Thanks for playing The Mystic Forest Adventure!")
print("Your choices shaped your unique story!")
print("=" * 50)

# Educational summary for students
print()
print("📚 PROGRAMMING CONCEPTS USED:")
print("• if/elif/else statements for decision making")
print("• Variables to track player stats (health, energy)")
print("• String input and comparison")
print("• Nested conditionals (if statements inside if statements)")
print("• Multiple conditions with 'and' operator")
print("• Input validation with else statements")
print("🎉 TOUGH SURVIVOR ENDING")
print("="*50)

print()
print("--- Final Stats ---")
print(f"Health: {health}")
print(f"Energy: {energy}")
print("-------------------")
print()

# Different message based on remaining health
if health >= 40:
    print("Despite your injury, you made it out!")
    print("You're tougher than you thought! 😅 SURVIVED ENDING!")
else:
    print("You're badly injured but alive!")
    print("You'll recover, but this was a close call! 😰 BARELY SURVIVED!")


print()
print("--- Final Stats ---")
print(f"Health: {health}")
print(f"Energy: {energy}")
print("-------------------")
print()

print("\n" + "="*50)
print("Thanks for playing The Mystic Forest Adventure!")
print("Your choices shaped your unique story!")
print("="*50)
