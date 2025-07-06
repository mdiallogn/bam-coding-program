# THE MYSTIC FOREST ADVENTURE - FUNCTIONS EDITION
# A text-based game to learn functions while incorporating conditions and loops

import random

# UTILITY FUNCTIONS - These handle common tasks throughout the game

def display_header(title):
    """Display a formatted header for different game sections"""
    print("\n" + "=" * 50)
    print(f"    {title}")
    print("=" * 50)

def display_stats(health, energy, inventory=None, score=0):
    """Display current player stats in a formatted way"""
    print("\n--- Your Stats ---")
    print(f"Health: {health}/100")
    print(f"Energy: {energy}/100")
    if inventory is not None:
        print(f"Inventory: {inventory}")
    if score > 0:
        print(f"Score: {score}")
    print("------------------")

def validate_input(prompt, valid_choices):
    """Get valid input from player with error handling - uses loops"""
    while True:  # Loop until valid input
        choice = input(prompt).strip()
        # Use conditions to check if input is valid
        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid choice! Please try again.")

def show_inventory(inventory):
    """Display inventory contents in a nice format"""
    if not inventory:
        print("📦 Your inventory is empty.")
    else:
        print("📦 Your inventory contains:")
        for i, item in enumerate(inventory, 1):
            print(f"  {i}. {item}")

def calculate_ending_score(health, energy, inventory, locations_visited):
    """Calculate final score based on player performance"""
    score = 0
    score += health // 2  # Health contributes to score
    score += energy // 3  # Energy contributes to score
    score += len(inventory) * 10  # Items are valuable
    score += len(locations_visited) * 15  # Exploration bonus
    return score

# GAME INITIALIZATION AND MENU FUNCTIONS

def show_main_menu():
    """Display the main menu and handle menu selection - uses loops"""
    while True:  # Keep showing menu until valid choice
        display_header("🎮 MAIN MENU")
        print("1. Start New Adventure")
        print("2. View High Scores")
        print("3. Exit Game")
        print()
        
        choice = input("Choose an option (1-3): ")
        
        # Use conditions to handle different menu choices
        if choice == "1":
            return "start"
        elif choice == "2":
            show_high_scores()
            # Continue loop to show menu again
        elif choice == "3":
            return "exit"
        else:
            print("❌ Invalid choice! Please try again.\n")

def show_high_scores():
    """Display high scores - demonstrates a simple display function"""
    print("\n📊 HIGH SCORES")
    print("Best Adventure: Mountain Explorer - 95 points")
    print("Most Lives Saved: Forest Guardian - 12 travelers")
    print("Fastest Escape: Speed Runner - 23 minutes")
    print("Most Items Found: Treasure Hunter - 8 items")
    print()

def initialize_game():
    """Initialize game variables and show introduction"""
    display_header("🌲 THE MYSTIC FOREST ADVENTURE 🌲")
    print("\nYou wake up in a dark, mysterious forest with no memory of how you got here.")
    print("Strange sounds echo through the trees, and an eerie mist surrounds you.")
    print("Your goal is to find your way out safely...\n")
    
    # Return initial game state
    return {
        'health': 100,
        'energy': 100,
        'inventory': [],
        'score': 0,
        'locations_visited': []
    }

# PATH SELECTION AND STORY FUNCTIONS

def choose_initial_path():
    """Handle the first major decision point - uses conditions"""
    display_header("🌲 FOREST ENTRANCE")
    print("You see three paths ahead:")
    print("1. A well-lit path with singing birds")
    print("2. A dark, narrow trail with glowing mushrooms")
    print("3. A rocky path leading uphill")
    
    choice = validate_input("Which path do you choose? (1, 2, or 3): ", ['1', '2', '3'])
    
    # Use conditions to determine path effects
    if choice == '1':
        print("\n🐦 You chose the well-lit path...")
        print("The birds guide you safely, but you feel tired from the long walk.")
        print("You lose 20 energy but stay safe.")
        return "bright", -20, 0  # path_type, energy_change, health_change
    elif choice == '2':
        print("\n🍄 You chose the dark trail...")
        print("The glowing mushrooms are beautiful but emit strange spores.")
        print("You lose 15 health but gain 10 energy from the magical mushrooms.")
        return "dark", 10, -15
    else:  # choice == '3'
        print("\n🗻 You chose the rocky uphill path...")
        print("The climb is exhausting but you get a great view of the area.")
        print("You lose 30 energy from the difficult climb.")
        return "mountain", -30, 0

def bright_path_adventure(game_state):
    """Handle the bright path storyline - uses conditions"""
    display_header("🌞 THE BRIGHT PATH")
    print("You reach a clearing with a sparkling fountain and a friendly hermit.")
    print("The hermit offers you a choice:")
    print("1. Drink from the magical fountain")
    print("2. Ask the hermit for directions")
    print("3. Rest by the fountain")
    
    choice = validate_input("What do you do? (1, 2, or 3): ", ['1', '2', '3'])
    
    # Use nested conditions for different outcomes
    if choice == '1':
        print("\n💧 You drink from the fountain...")
        if game_state['health'] >= 80:
            print("The water tastes amazing! You feel completely refreshed.")
            game_state['health'] = 100
            game_state['energy'] = 100
            print("Your health and energy are fully restored!")
        else:
            print("The water helps, but you needed more healing.")
            game_state['health'] = min(100, game_state['health'] + 30)
            game_state['energy'] = min(100, game_state['energy'] + 20)
            print("You gain 30 health and 20 energy.")
        game_state['score'] += 25
        return "fountain"
    elif choice == '2':
        print("\n🧙 You ask the hermit for help...")
        print("The hermit gives you a map and some advice about avoiding dangers.")
        game_state['energy'] = min(100, game_state['energy'] + 15)
        game_state['inventory'].append("hermit's map")
        game_state['score'] += 20
        print("You gain 15 energy and receive a helpful map!")
        return "hermit"
    else:
        print("\n😴 You rest by the fountain...")
        game_state['energy'] = min(100, game_state['energy'] + 25)
        game_state['score'] += 15
        print("You gain 25 energy from the peaceful rest.")
        return "rest"

def dark_path_adventure(game_state):
    """Handle the dark path storyline - uses conditions"""
    display_header("🌙 THE DARK TRAIL")
    print("You encounter a mysterious creature blocking your path!")
    print("It doesn't seem hostile, but it's watching you carefully.")
    print("1. Try to communicate with the creature")
    print("2. Sneak around it quietly")
    print("3. Offer it some food from your backpack")
    
    choice = validate_input("What do you do? (1, 2, or 3): ", ['1', '2', '3'])
    
    # Conditions based on current stats
    if choice == '1':
        print("\n🗣️ You try to communicate...")
        if game_state['health'] >= 70:
            print("Your strong presence impresses the creature!")
            print("It leads you to a secret exit from the forest.")
            game_state['score'] += 30
            return "creature_ally"
        else:
            print("The creature senses your weakness and growls menacingly.")
            print("It attacks! You barely escape but are badly injured.")
            if apply_stat_changes(game_state, -25, -15):
                return "game_over"
            return "barely_escaped"
            
    elif choice == '2':
        print("\n🤫 You sneak around quietly...")
        if game_state['energy'] >= 60:
            print("You successfully sneak past! The creature never noticed.")
            game_state['energy'] -= 20
            game_state['score'] += 25
            return "stealth"
        else:
            print("You're too tired to sneak properly and step on a branch!")
            print("The creature notices and chases you! You run but trip and fall.")
            if apply_stat_changes(game_state, -20, -20):
                return "game_over"
            print("You manage to get away but are hurt and exhausted.")
            return "failed_stealth"
    else:
        print("\n🍞 You offer food to the creature...")
        print("The creature accepts your gift gratefully!")
        game_state['energy'] = max(0, game_state['energy'] - 5)
        game_state['inventory'].append("creature's blessing")
        game_state['score'] += 35
        return "friendship"

def mountain_path_adventure(game_state):
    """Handle the mountain path storyline - uses conditions"""
    display_header("⛰️ THE MOUNTAIN PATH")
    print("From the mountain top, you see the entire forest spread below you.")
    print("You spot three possible ways down:")
    print("1. A steep but direct path down")
    print("2. A winding path through caves")
    print("3. Wait for help (you saw smoke from a distant cabin)")
    
    choice = validate_input("What do you choose? (1, 2, or 3): ", ['1', '2', '3'])
    
    # Energy-dependent outcomes with real consequences
    if choice == '1':
        print("\n⬇️ You take the steep path...")
        if game_state['energy'] >= 40:
            print("You carefully make your way down without injury.")
            game_state['energy'] -= 20
            game_state['score'] += 20
            return "safe_descent"
        else:
            print("You're too tired and slip badly, tumbling down the rocky slope!")
            print("You hit your head on a rock and lose consciousness...")
            if apply_stat_changes(game_state, -40, -25):
                return "game_over"
            print("You wake up battered and bleeding but somehow still alive.")
            return "dangerous_fall"
            
    elif choice == '2':
        print("\n🕳️ You enter the caves...")
        if game_state['energy'] >= 20:
            print("The caves are dark but lead to an underground river.")
            game_state['energy'] -= 15
            game_state['score'] += 30
            return "cave_river"
        else:
            print("You're too exhausted to navigate the dark caves safely.")
            print("You get lost in the darkness and panic, using up your remaining energy.")
            if apply_stat_changes(game_state, -10, -15):
                return "game_over"
            print("You eventually find your way out, but you're in terrible condition.")
            return "lost_in_caves"
    else:
        print("\n🏠 You wait for help...")
        print("A friendly ranger finds you and escorts you to safety.")
        game_state['energy'] = max(0, game_state['energy'] - 10)
        game_state['score'] += 25
        return "rescue"

# EXPLORATION AND COLLECTION FUNCTIONS

def item_collection_phase(game_state):
    """Handle item collection using loops"""
    display_header("🔍 EXPLORATION PHASE")
    print("You notice several items scattered around the area...")
    
    possible_items = ["healing potion", "energy crystal", "magic rope", "ancient coin", "forest map"]
    
    # FOR LOOP - Check each possible item location
    for i in range(3):  # Player can search 3 locations
        print(f"\n📍 Search location {i + 1}:")
        search_choice = validate_input("Do you want to search this area? (y/n): ", ['y', 'n'])
        
        if search_choice == 'y':
            # Use conditions with random chance
            if random.random() > 0.3:  # 70% chance to find something
                found_item = random.choice(possible_items)
                game_state['inventory'].append(found_item)
                print(f"✨ You found a {found_item}!")
                
                # Apply item effects using conditions
                if found_item == "healing potion":
                    game_state['health'] = min(100, game_state['health'] + 20)
                    print("You drink it immediately and gain 20 health!")
                elif found_item == "energy crystal":
                    game_state['energy'] = min(100, game_state['energy'] + 15)
                    print("You absorb its power and gain 15 energy!")
                
                game_state['score'] += 10
            else:
                print("🚫 You found nothing here.")
        else:
            print("⏭️ You skip searching this area.")

def solve_puzzle(game_state):
    """Handle puzzle solving with multiple attempts - uses loops"""
    display_header("🧩 ANCIENT PUZZLE")
    print("You encounter an ancient stone puzzle that blocks your path.")
    print("The puzzle has mystical numbers that must be solved...")
    
    # Generate puzzle
    puzzle_num1 = random.randint(5, 15)
    puzzle_num2 = random.randint(3, 8)
    correct_answer = puzzle_num1 + puzzle_num2
    
    attempts = 0
    max_attempts = 3
    
    # WHILE LOOP - Multiple attempts
    while attempts < max_attempts:
        attempts += 1
        print(f"\n🔢 Attempt {attempts}/{max_attempts}")
        print(f"What is {puzzle_num1} + {puzzle_num2}?")
        
        try:
            player_answer = int(input("Enter your answer: "))
            
            # Use conditions to check answer
            if player_answer == correct_answer:
                print("✅ Correct! The puzzle glows and moves aside.")
                game_state['energy'] = min(100, game_state['energy'] + 10)
                game_state['score'] += 30
                print("You gain 10 energy and 30 points for solving the puzzle!")
                return True
            else:
                print(f"❌ Incorrect. The correct answer was {correct_answer}.")
                if attempts < max_attempts:
                    print("The puzzle gives you another chance...")
                    
        except ValueError:
            print("❌ Please enter a valid number.")
            attempts -= 1  # Don't count invalid input
    
    print("\n🔨 The puzzle remains unsolved, but you find a way around it.")
    game_state['energy'] = max(0, game_state['energy'] - 5)
    print("You lose 5 energy finding an alternate path.")
    return False

def combat_encounter(game_state):
    """Handle combat system using loops and conditions"""
    display_header("⚔️ COMBAT ENCOUNTER")
    print("A shadow creature emerges from the darkness!")
    
    enemy_health = 35  # Made slightly stronger
    battle_round = 0
    
    # WHILE LOOP - Battle continues until someone is defeated
    while game_state['health'] > 0 and enemy_health > 0:
        battle_round += 1
        print(f"\n🥊 Battle Round {battle_round}")
        print(f"Your Health: {game_state['health']} | Enemy Health: {enemy_health}")
        
        print("\nChoose your action:")
        print("1. Attack (deal 8-12 damage)")
        print("2. Use healing potion (if you have one)")
        print("3. Try to flee")
        
        action = validate_input("What do you do? (1-3): ", ['1', '2', '3'])
        
        # Use conditions to handle different actions
        if action == '1':
            damage = random.randint(8, 12)
            enemy_health -= damage
            print(f"⚔️ You deal {damage} damage to the creature!")
            
        elif action == '2':
            if "healing potion" in game_state['inventory']:
                game_state['inventory'].remove("healing potion")
                game_state['health'] = min(100, game_state['health'] + 25)
                print("🧪 You drink a healing potion and recover 25 health!")
            else:
                print("❌ You don't have any healing potions!")
                print("You waste your turn searching your inventory!")
                # Enemy gets extra attack for wasted turn
                enemy_damage = random.randint(8, 15)
                game_state['health'] = max(0, game_state['health'] - enemy_damage)
                print(f"👹 The creature takes advantage and deals {enemy_damage} extra damage!")
                if game_state['health'] <= 0:
                    print("\n💀 You have been defeated in battle...")
                    return "combat_death"
                continue
                
        elif action == '3':
            # Flee chance depends on current health and energy
            flee_chance = 0.3 if game_state['health'] < 30 else 0.5
            if random.random() < flee_chance:
                print("🏃 You successfully escape from the battle!")
                game_state['energy'] = max(0, game_state['energy'] - 15)
                return "fled_combat"
            else:
                print("❌ You couldn't escape! The creature blocks your path.")
                print("Your failed escape attempt leaves you vulnerable!")
        
        # Check if enemy is defeated
        if enemy_health <= 0:
            print("\n🎉 Victory! You defeated the shadow creature!")
            game_state['score'] += 50
            game_state['inventory'].append("shadow essence")
            print("You gain 50 points and find a magical artifact!")
            return "combat_victory"
        
        # Enemy's turn - damage increases as battle goes on
        if enemy_health > 0:
            base_damage = random.randint(5, 12)
            # Creature gets more dangerous when wounded
            if enemy_health <= 15:
                base_damage += 3
                print("The creature becomes more vicious as it's wounded!")
            
            game_state['health'] = max(0, game_state['health'] - base_damage)
            print(f"👹 The creature attacks you for {base_damage} damage!")
            
            if game_state['health'] <= 0:
                print("\n💀 You have been defeated in battle...")
                return "combat_death"
    
    return "combat_victory"

def exploration_system(game_state):
    """Handle location exploration using loops"""
    display_header("🗺️ EXPLORATION SYSTEM")
    print("You can now explore different areas of the forest...")
    
    # Check if player has enough energy to explore
    if game_state['energy'] <= 15:
        print("You're too exhausted to explore safely.")
        print("You must find the exit before you collapse!")
        return
    
    available_locations = {
        '1': 'Crystal Cave',
        '2': 'Ancient Grove', 
        '3': 'Mystical Spring'
    }
    
    # WHILE LOOP - Continue exploring until player chooses to stop
    while game_state['energy'] > 15:
        print("\n🌲 Available Locations:")
        for key, location in available_locations.items():
            visited = "✓" if location in game_state['locations_visited'] else ""
            print(f"{key}. {location} {visited}")
        print("4. Continue to Exit")
        
        choice = validate_input("Where do you want to explore? (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '4':
            print("\n➡️ You decide to head toward the forest exit.")
            break
        
        location = available_locations[choice]
        if explore_location(game_state, location):
            return  # Game over occurred
        
        # Each exploration costs energy
        game_state['energy'] = max(0, game_state['energy'] - 8)
        
        # Check for exhaustion
        if game_state['energy'] <= 15:
            print("\n⚠️ You're getting dangerously exhausted!")
            print("You should head to the exit before you collapse!")
            continue_exploring = validate_input("Do you want to risk exploring more? (y/n): ", ['y', 'n'])
            if continue_exploring == 'n':
                break
        elif game_state['energy'] > 15:
            continue_exploring = validate_input("Do you want to continue exploring? (y/n): ", ['y', 'n'])
            if continue_exploring == 'n':
                break

def explore_location(game_state, location):
    """Handle individual location exploration - uses conditions"""
    # Random chance of danger in each location
    danger_chance = 0.2  # 20% chance of dangerous encounter
    
    if random.random() < danger_chance:
        print(f"\n⚠️ Danger in {location}!")
        if location == "Crystal Cave":
            print("A crystal shard falls and cuts you!")
            if apply_stat_changes(game_state, -15, -5):
                return True
        elif location == "Ancient Grove":
            print("Poisonous thorns scratch you as you explore!")
            if apply_stat_changes(game_state, -10, -10):
                return True
        elif location == "Mystical Spring":
            print("You slip on wet rocks and injure yourself!")
            if apply_stat_changes(game_state, -12, -8):
                return True
    
    # Use conditions to handle different locations
    if location == "Crystal Cave":
        if location not in game_state['locations_visited']:
            print("\n💎 You discover a beautiful crystal cave!")
            print("The crystals energize you!")
            game_state['energy'] = min(100, game_state['energy'] + 20)
            game_state['score'] += 15
            game_state['locations_visited'].append(location)
        else:
            print("\n💎 You revisit the crystal cave.")
            print("The crystals still provide some energy.")
            game_state['energy'] = min(100, game_state['energy'] + 5)
            
    elif location == "Ancient Grove":
        if location not in game_state['locations_visited']:
            print("\n🌳 You find an ancient grove with wise trees!")
            print("The trees share their wisdom with you.")
            if "ancient coin" in game_state['inventory']:
                print("Your ancient coin glows! The trees are impressed.")
                game_state['score'] += 25
            else:
                game_state['score'] += 10
            game_state['locations_visited'].append(location)
        else:
            print("\n🌳 You return to the ancient grove.")
            print("The trees nod in recognition.")
            game_state['energy'] = min(100, game_state['energy'] + 3)
            
    elif location == "Mystical Spring":
        if location not in game_state['locations_visited']:
            print("\n🌊 You discover a mystical spring!")
            print("The water heals your wounds.")
            game_state['health'] = min(100, game_state['health'] + 30)
            game_state['score'] += 20
            game_state['locations_visited'].append(location)
        else:
            print("\n🌊 You return to the mystical spring.")
            print("The water still provides some healing.")
            game_state['health'] = min(100, game_state['health'] + 10)
    
    return False

def check_game_over(game_state):
    """Check if the game should end due to low health or energy"""
    if game_state['health'] <= 0:
        display_header("💀 GAME OVER - HEALTH DEPLETED")
        print("Your health has reached zero. You collapse in the forest...")
        print("The mysterious forest claims another victim.")
        print("Your adventure ends here.")
        return True
    elif game_state['energy'] <= 0:
        display_header("😴 GAME OVER - EXHAUSTED")
        print("You are completely exhausted and can no longer continue.")
        print("You sit down to rest and fall into a deep sleep...")
        print("When you wake up, you're back where you started - outside the forest.")
        print("You failed to escape, but at least you're alive.")
        return True
    return False

def apply_stat_changes(game_state, health_change, energy_change):
    """Apply health and energy changes and check for game over"""
    game_state['health'] = max(0, game_state['health'] + health_change)
    game_state['energy'] = max(0, game_state['energy'] + energy_change)
    
    # Check if changes caused game over
    if check_game_over(game_state):
        return True
    return False

# ENDING FUNCTIONS

def determine_ending(game_state, ending_type):
    """Determine and display the appropriate ending - uses conditions"""
    # Check for failure endings first
    if ending_type == "game_over":
        return  # Game over already handled
    
    if ending_type == "combat_death":
        display_header("💀 DEFEAT")
        print("You fought bravely but the shadow creature was too powerful.")
        print("Your adventure ends in the dark forest...")
        print("Better luck next time!")
        return
    
    if ending_type in ["barely_escaped", "failed_stealth", "dangerous_fall", "lost_in_caves"]:
        display_header("😰 NARROW ESCAPE")
        print("You barely survived your ordeal in the forest.")
        print("Though you eventually found your way out, you're badly injured.")
        print("You'll need weeks to recover from this adventure.")
        print("Next time, be more careful with your choices!")
        return
    
    # Calculate final score for successful endings
    final_score = calculate_ending_score(
        game_state['health'], 
        game_state['energy'], 
        game_state['inventory'], 
        game_state['locations_visited']
    )
    game_state['score'] += final_score
    
    display_header("🎉 ADVENTURE COMPLETE!")
    display_stats(game_state['health'], game_state['energy'], game_state['inventory'], game_state['score'])
    print(f"Locations Visited: {len(game_state['locations_visited'])}")
    
    # Use conditions to determine ending quality
    if game_state['score'] >= 150:
        print("\n⭐ LEGENDARY EXPLORER ENDING!")
        print("You mastered the forest and became a legend!")
    elif game_state['score'] >= 100:
        print("\n🌟 EXPERT ADVENTURER ENDING!")
        print("You navigated the forest with great skill!")
    elif game_state['score'] >= 50:
        print("\n😊 SUCCESSFUL ESCAPE ENDING!")
        print("You made it out safely with some discoveries!")
    else:
        print("\n😅 SURVIVOR ENDING!")
        print("You barely escaped, but you're alive!")
    
    # Add specific ending flavor based on story path
    add_story_ending_flavor(ending_type)

def add_story_ending_flavor(ending_type):
    """Add specific story details based on the path taken"""
    story_endings = {
        "fountain": "The fountain's magic will always be with you.",
        "hermit": "The hermit's wisdom guides you even now.",
        "rest": "You learned the value of patience and rest.",
        "creature_ally": "Your new ally watches over the forest.",
        "friendship": "Kindness opened doors that force could not.",
        "stealth": "You've become one with the shadows.",
        "safe_descent": "Your climbing skills are now legendary.",
        "cave_river": "You've discovered secrets few will ever know.",
        "rescue": "Sometimes the best choice is to wait for help.",
        "fled_combat": "Sometimes running away is the smartest choice."
    }
    
    if ending_type in story_endings:
        print(story_endings[ending_type])

def show_programming_concepts():
    """Display the programming concepts demonstrated"""
    print("\n📚 PROGRAMMING CONCEPTS DEMONSTRATED:")
    print("• Functions with parameters and return values")
    print("• Utility functions for common tasks")
    print("• while loops for menus and game flow")
    print("• for loops for item collection")
    print("• if/elif/else statements for decision making")
    print("• Nested conditions for complex logic")
    print("• Function documentation with docstrings")
    print("• Code organization and reusability")
    print("• Parameter passing and state management")

# MAIN GAME FUNCTION

def main():
    """Main game function - coordinates all game systems"""
    display_header("🌲 THE MYSTIC FOREST ADVENTURE - FUNCTIONS EDITION 🌲")
    
    # MAIN GAME LOOP
    while True:
        menu_choice = show_main_menu()
        
        if menu_choice == "exit":
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
        # Initialize new game
        game_state = initialize_game()
        
        # Main game flow
        display_stats(game_state['health'], game_state['energy'], game_state['inventory'])
        
        # Choose initial path
        chosen_path, energy_change, health_change = choose_initial_path()
        if apply_stat_changes(game_state, health_change, energy_change):
            continue  # Game over, restart
        
        display_stats(game_state['health'], game_state['energy'])
        
        # Item collection phase
        item_collection_phase(game_state)
        display_stats(game_state['health'], game_state['energy'], game_state['inventory'], game_state['score'])
        
        # Puzzle solving
        solve_puzzle(game_state)
        
        # Path-specific adventures
        if chosen_path == "bright":
            ending_type = bright_path_adventure(game_state)
        elif chosen_path == "dark":
            ending_type = dark_path_adventure(game_state)
            # Check if game over occurred
            if ending_type == "game_over":
                continue
            # Combat encounter for dark path
            if game_state['health'] > 0:
                combat_result = combat_encounter(game_state)
                if combat_result == "combat_death":
                    ending_type = "combat_death"
        else:  # mountain path
            ending_type = mountain_path_adventure(game_state)
            # Check if game over occurred
            if ending_type == "game_over":
                continue
        
        # Exploration system (only if still alive)
        if game_state['health'] > 0 and ending_type not in ["combat_death", "game_over"]:
            exploration_system(game_state)
        
        # Show final results
        determine_ending(game_state, ending_type)
        show_programming_concepts()
        
        # Ask if player wants to play again
        print("\n" + "="*50)
        play_again = validate_input("Do you want to play again? (y/n): ", ['y', 'n'])
        if play_again == 'n':
            break
    
    print("\n🎮 Thanks for playing The Mystic Forest Adventure!")
    print("You've learned about functions, conditions, and loops!")
    print("Remember: sometimes you lose, but that's how you learn to play better!")

# Run the game
if __name__ == "__main__":
    main()
