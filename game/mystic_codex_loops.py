# THE MYSTIC FOREST ADVENTURE - LOOPS EDITION
# A text-based game to learn loops (while/for) and repetition

import random

# MAIN GAME LOOP - This allows players to restart the game
playing = True
while playing:
    print("=" * 50)
    print("    🌲 THE MYSTIC FOREST ADVENTURE 🌲")
    print("=" * 50)
    print()
    
    # MAIN MENU LOOP - Keep showing menu until valid choice
    menu_choice = ""
    while menu_choice not in ["1", "2", "3"]:
        print("🎮 MAIN MENU")
        print("1. Start New Adventure")
        print("2. View High Scores")
        print("3. Exit Game")
        print()
        menu_choice = input("Choose an option (1-3): ")
        
        if menu_choice == "2":
            print("\n📊 HIGH SCORES")
            print("Best Adventure: Mountain Explorer - 95 points")
            print("Most Lives Saved: Forest Guardian - 12 travelers")
            print("Fastest Escape: Speed Runner - 23 minutes")
            print()
            menu_choice = ""  # Reset to show menu again
        elif menu_choice == "3":
            print("\n👋 Thanks for playing! Goodbye!")
            playing = False
            break
        elif menu_choice != "1":
            print("❌ Invalid choice! Please try again.\n")
    
    # If player chose to exit, break out of main loop
    if not playing:
        break
    
    # GAME INITIALIZATION
    print("\nYou wake up in a dark, mysterious forest with no memory of how you got here.")
    print("Strange sounds echo through the trees, and an eerie mist surrounds you.")
    print("Your goal is to find your way out safely...\n")
    
    # Initialize player stats
    health = 100
    energy = 100
    inventory = []  # List to store collected items
    score = 0
    
    print("--- Your Stats ---")
    print(f"Health: {health}")
    print(f"Energy: {energy}")
    print(f"Inventory: {inventory}")
    print("------------------\n")
    
    # FIRST MAJOR DECISION POINT
    print("🌲 FOREST ENTRANCE")
    print("You see three paths ahead:")
    print("1. A well-lit path with singing birds")
    print("2. A dark, narrow trail with glowing mushrooms")
    print("3. A rocky path leading uphill")
    print()
    
    # INPUT VALIDATION LOOP - Keep asking until valid input
    path_choice = ""
    while path_choice not in ["1", "2", "3"]:
        path_choice = input("Which path do you choose? (1, 2, or 3): ")
        if path_choice not in ["1", "2", "3"]:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")
    
    # Process path choice with conditionals
    if path_choice == "1":
        print("\n🐦 You chose the well-lit path...")
        print("The birds guide you safely, but you feel tired from the long walk.")
        energy = energy - 20
        print("You lose 20 energy but stay safe.")
        chosen_path = "bright"
        
    elif path_choice == "2":
        print("\n🍄 You chose the dark trail...")
        print("The glowing mushrooms are beautiful but emit strange spores.")
        health = health - 15
        energy = energy + 10
        print("You lose 15 health but gain 10 energy from the magical mushrooms.")
        chosen_path = "dark"
        
    else:  # path_choice == "3"
        print("\n🗻 You chose the rocky uphill path...")
        print("The climb is exhausting but you get a great view of the area.")
        energy = energy - 30
        print("You lose 30 energy from the difficult climb.")
        chosen_path = "mountain"
    
    print(f"\n--- Stats After Path Choice ---")
    print(f"Health: {health}, Energy: {energy}")
    print("--------------------------------\n")
    
    # ITEM COLLECTION LOOP - Players can explore and gather items
    print("🔍 EXPLORATION PHASE")
    print("You notice several items scattered around the area...")
    
    # List of possible items to find
    possible_items = ["healing potion", "energy crystal", "magic rope", "ancient coin", "forest map"]
    
    # FOR LOOP - Check each possible item location
    for i in range(3):  # Player can find up to 3 items
        print(f"\n📍 Search location {i + 1}:")
        search_choice = input("Do you want to search this area? (y/n): ").lower()
        
        if search_choice == "y":
            # Random chance to find an item
            if random.random() > 0.3:  # 70% chance to find something
                found_item = random.choice(possible_items)
                inventory.append(found_item)
                print(f"✨ You found a {found_item}!")
                
                # Item effects
                if found_item == "healing potion":
                    health = min(100, health + 20)
                    print("You drink it immediately and gain 20 health!")
                elif found_item == "energy crystal":
                    energy = min(100, energy + 15)
                    print("You absorb its power and gain 15 energy!")
                
                score += 10
            else:
                print("🚫 You found nothing here.")
        else:
            print("⏭️ You skip searching this area.")
    
    print(f"\n--- After Exploration ---")
    print(f"Health: {health}, Energy: {energy}")
    print(f"Inventory: {inventory}")
    print(f"Score: {score}")
    print("---------------------------\n")
    
    # PUZZLE SOLVING SECTION - Multiple attempts using loops
    print("🧩 ANCIENT PUZZLE")
    print("You encounter an ancient stone puzzle that blocks your path.")
    print("The puzzle has mystical numbers that must be solved...")
    
    # Generate a simple math puzzle
    puzzle_num1 = random.randint(5, 15)
    puzzle_num2 = random.randint(3, 8)
    correct_answer = puzzle_num1 + puzzle_num2
    
    attempts = 0
    max_attempts = 3
    puzzle_solved = False
    
    # WHILE LOOP - Give player multiple attempts
    while attempts < max_attempts and not puzzle_solved:
        attempts += 1
        print(f"\n🔢 Attempt {attempts}/{max_attempts}")
        print(f"What is {puzzle_num1} + {puzzle_num2}?")
        
        try:
            player_answer = int(input("Enter your answer: "))
            
            if player_answer == correct_answer:
                print("✅ Correct! The puzzle glows and moves aside.")
                puzzle_solved = True
                energy += 10
                score += 20
                print("You gain 10 energy and 20 points for solving the puzzle!")
            else:
                print(f"❌ Incorrect. The correct answer was {correct_answer}.")
                if attempts < max_attempts:
                    print("The puzzle gives you another chance...")
                
        except ValueError:
            print("❌ Please enter a valid number.")
            attempts -= 1  # Don't count invalid input as an attempt
    
    if not puzzle_solved:
        print("\n🔨 The puzzle remains unsolved, but you find a way around it.")
        energy -= 5
        print("You lose 5 energy finding an alternate path.")
    
    # COMBAT SYSTEM - While loop for battle rounds
    if chosen_path == "dark":
        print("\n⚔️ COMBAT ENCOUNTER")
        print("A shadow creature emerges from the darkness!")
        
        enemy_health = 30
        player_won = False
        battle_round = 0
        
        # COMBAT LOOP - Battle continues until someone is defeated
        while health > 0 and enemy_health > 0:
            battle_round += 1
            print(f"\n🥊 Battle Round {battle_round}")
            print(f"Your Health: {health} | Enemy Health: {enemy_health}")
            
            # Player's turn
            print("\nChoose your action:")
            print("1. Attack (deal 8-12 damage)")
            print("2. Use healing potion (if you have one)")
            print("3. Try to flee")
            
            action = input("What do you do? (1-3): ")
            
            if action == "1":
                damage = random.randint(8, 12)
                enemy_health -= damage
                print(f"⚔️ You deal {damage} damage to the creature!")
                
            elif action == "2":
                if "healing potion" in inventory:
                    inventory.remove("healing potion")
                    health = min(100, health + 25)
                    print("🧪 You drink a healing potion and recover 25 health!")
                else:
                    print("❌ You don't have any healing potions!")
                    continue  # Skip enemy turn since player's turn was wasted
                    
            elif action == "3":
                if random.random() > 0.5:  # 50% chance to flee
                    print("🏃 You successfully escape from the battle!")
                    energy -= 10
                    break
                else:
                    print("❌ You couldn't escape! The creature blocks your path.")
            
            # Check if enemy is defeated
            if enemy_health <= 0:
                print("\n🎉 Victory! You defeated the shadow creature!")
                player_won = True
                score += 50
                print("You gain 50 points for winning the battle!")
                break
            
            # Enemy's turn
            if enemy_health > 0:
                enemy_damage = random.randint(5, 10)
                health -= enemy_damage
                print(f"👹 The creature attacks you for {enemy_damage} damage!")
                
                if health <= 0:
                    print("\n💀 You have been defeated...")
                    break
        
        # Battle aftermath
        if health > 0 and player_won:
            print("The creature drops a magical artifact!")
            inventory.append("shadow essence")
            energy += 5
    
    # LOCATION REVISIT SYSTEM - Players can explore multiple areas
    locations_visited = []
    exploration_continues = True
    
    print(f"\n🗺️ EXPLORATION SYSTEM")
    print("You can now explore different areas of the forest...")
    
    # EXPLORATION LOOP - Continue until player chooses to stop
    while exploration_continues and energy > 10:
        print("\n🌲 Available Locations:")
        print("1. Crystal Cave")
        print("2. Ancient Grove")
        print("3. Mystical Spring")
        print("4. Continue to Exit")
        
        location_choice = input("Where do you want to explore? (1-4): ")
        
        if location_choice == "1":
            if "Crystal Cave" not in locations_visited:
                print("\n💎 You discover a beautiful crystal cave!")
                print("The crystals energize you!")
                energy += 20
                score += 15
                locations_visited.append("Crystal Cave")
            else:
                print("\n💎 You revisit the crystal cave.")
                print("The crystals still provide some energy.")
                energy += 5
            
        elif location_choice == "2":
            if "Ancient Grove" not in locations_visited:
                print("\n🌳 You find an ancient grove with wise trees!")
                print("The trees share their wisdom with you.")
                if "ancient coin" in inventory:
                    print("Your ancient coin glows! The trees are impressed.")
                    score += 25
                else:
                    score += 10
                locations_visited.append("Ancient Grove")
            else:
                print("\n🌳 You return to the ancient grove.")
                print("The trees nod in recognition.")
                energy += 3
                
        elif location_choice == "3":
            if "Mystical Spring" not in locations_visited:
                print("\n🌊 You discover a mystical spring!")
                print("The water heals your wounds.")
                health = min(100, health + 30)
                score += 20
                locations_visited.append("Mystical Spring")
            else:
                print("\n🌊 You return to the mystical spring.")
                print("The water still provides some healing.")
                health = min(100, health + 10)
                
        elif location_choice == "4":
            print("\n➡️ You decide to head toward the forest exit.")
            exploration_continues = False
            
        else:
            print("❌ Invalid choice! Please try again.")
            continue
        
        # Each exploration costs energy
        energy -= 5
        
        # Check if player wants to continue exploring
        if exploration_continues and energy > 10:
            continue_exploring = input("\nDo you want to continue exploring? (y/n): ").lower()
            if continue_exploring != "y":
                exploration_continues = False
    
    # FINAL STATS AND ENDING
    print("\n" + "="*50)
    print("🎉 ADVENTURE COMPLETE!")
    print("="*50)
    print(f"Final Health: {health}")
    print(f"Final Energy: {energy}")
    print(f"Items Collected: {len(inventory)}")
    print(f"Locations Visited: {len(locations_visited)}")
    print(f"Final Score: {score}")
    
    # ENDING DETERMINATION - Based on performance
    if score >= 100:
        print("\n⭐ LEGENDARY EXPLORER ENDING!")
        print("You mastered the forest and became a legend!")
    elif score >= 70:
        print("\n🌟 EXPERT ADVENTURER ENDING!")
        print("You navigated the forest with great skill!")
    elif score >= 40:
        print("\n😊 SUCCESSFUL ESCAPE ENDING!")
        print("You made it out safely with some discoveries!")
    else:
        print("\n😅 SURVIVOR ENDING!")
        print("You barely escaped, but you're alive!")
    
    print("\n📚 LOOP CONCEPTS DEMONSTRATED:")
    print("• while loop for main game loop (restart capability)")
    print("• while loop for menu system (input validation)")
    print("• for loop for item collection (fixed iterations)")
    print("• while loop for puzzle attempts (condition-based)")
    print("• while loop for combat system (battle rounds)")
    print("• while loop for exploration (player choice)")
    print("• break statements to exit loops early")
    print("• continue statements to skip loop iterations")
    print("• Loop counters for tracking attempts and rounds")
    
    # ASK IF PLAYER WANTS TO PLAY AGAIN
    print("\n" + "="*50)
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        playing = False
        print("👋 Thanks for playing The Mystic Forest Adventure!")

print("\n🎮 Game ended. See you next time!")
