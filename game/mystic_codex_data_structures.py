# THE MYSTIC FOREST ADVENTURE - DATA STRUCTURES EDITION
# A text-based game to learn data structures (lists, dictionaries, arrays)

import random
import time

# GAME DATABASE - Using dictionaries to store structured game data

# ITEMS DATABASE - Dictionary of dictionaries for item properties
ITEMS_DATABASE = {
    "healing_potion": {
        "name": "Healing Potion",
        "description": "A red vial filled with healing magic",
        "effect": {"health": 25, "energy": 0},
        "value": 50,
        "usable": True,
        "stackable": True
    },
    "energy_crystal": {
        "name": "Energy Crystal",
        "description": "A glowing crystal that restores energy",
        "effect": {"health": 0, "energy": 20},
        "value": 40,
        "usable": True,
        "stackable": True
    },
    "magic_rope": {
        "name": "Magic Rope",
        "description": "A rope that can extend to any length needed",
        "effect": {"health": 0, "energy": 0},
        "value": 30,
        "usable": False,
        "stackable": False
    },
    "ancient_coin": {
        "name": "Ancient Coin",
        "description": "A mysterious coin with strange symbols",
        "effect": {"health": 0, "energy": 0},
        "value": 100,
        "usable": False,
        "stackable": True
    },
    "forest_map": {
        "name": "Forest Map",
        "description": "A detailed map of the forest paths",
        "effect": {"health": 0, "energy": 5},
        "value": 25,
        "usable": False,
        "stackable": False
    },
    "shadow_essence": {
        "name": "Shadow Essence",
        "description": "Dark energy captured from a defeated creature",
        "effect": {"health": 0, "energy": 15},
        "value": 75,
        "usable": True,
        "stackable": True
    },
    "hermit_map": {
        "name": "Hermit's Map",
        "description": "A wise hermit's guide to safe forest paths",
        "effect": {"health": 0, "energy": 10},
        "value": 60,
        "usable": False,
        "stackable": False
    },
    "creature_blessing": {
        "name": "Creature's Blessing",
        "description": "A magical blessing from a forest creature",
        "effect": {"health": 15, "energy": 10},
        "value": 80,
        "usable": True,
        "stackable": False
    }
}

# LOCATIONS DATABASE - Dictionary of game locations with properties
LOCATIONS_DATABASE = {
    "forest_entrance": {
        "name": "Forest Entrance",
        "description": "A misty entrance to the mysterious forest",
        "available_actions": ["choose_path", "examine_area", "check_stats"],
        "connected_areas": ["bright_path", "dark_path", "mountain_path"],
        "items": ["forest_map"],
        "danger_level": 0
    },
    "bright_path": {
        "name": "Sunlit Path",
        "description": "A well-lit path with singing birds guiding your way",
        "available_actions": ["continue_forward", "rest", "search_area"],
        "connected_areas": ["hermit_clearing"],
        "items": ["energy_crystal"],
        "danger_level": 1
    },
    "dark_path": {
        "name": "Shadow Trail",
        "description": "A dark trail with glowing mushrooms and mysterious creatures",
        "available_actions": ["sneak_forward", "communicate", "search_area"],
        "connected_areas": ["hermit_clearing", "crystal_cave"],
        "items": ["shadow_essence", "ancient_coin"],
        "danger_level": 4
    },
    "mountain_path": {
        "name": "Rocky Mountain Path",
        "description": "A steep path leading to a mountain overlook",
        "available_actions": ["climb_up", "rest", "survey_area"],
        "connected_areas": ["hermit_clearing", "ancient_grove"],
        "items": ["magic_rope"],
        "danger_level": 3
    },
    "hermit_clearing": {
        "name": "Hermit's Clearing",
        "description": "A peaceful clearing with a sparkling fountain",
        "available_actions": ["drink_fountain", "talk_hermit", "rest"],
        "connected_areas": ["crystal_cave", "ancient_grove"],
        "items": ["healing_potion", "hermit_map"],
        "danger_level": 0
    },
    "crystal_cave": {
        "name": "Crystal Cave",
        "description": "A beautiful cave filled with energy-giving crystals",
        "available_actions": ["harvest_crystals", "explore_deeper", "rest"],
        "connected_areas": ["ancient_grove", "mystical_spring"],
        "items": ["energy_crystal", "energy_crystal"],
        "danger_level": 2
    },
    "ancient_grove": {
        "name": "Ancient Grove",
        "description": "A grove of wise, ancient trees",
        "available_actions": ["seek_wisdom", "rest", "search_area"],
        "connected_areas": ["mystical_spring"],
        "items": ["ancient_coin", "creature_blessing"],
        "danger_level": 1
    },
    "mystical_spring": {
        "name": "Mystical Spring",
        "description": "A spring with magical healing waters",
        "available_actions": ["drink_water", "rest", "explore_area"],
        "connected_areas": [],  # This is the final destination
        "items": ["healing_potion"],
        "danger_level": 0
    }
}

# PLAYER PROGRESSION SYSTEM - Dictionary to track player advancement
PLAYER_PROGRESSION = {
    "level": 1,
    "experience": 0,
    "experience_to_next_level": 100,
    "skill_points": 0,
    "achievements": [],
    "stats_bonuses": {"health": 0, "energy": 0, "strength": 0, "luck": 0}
}

# GAME STATE MANAGEMENT - Lists and dictionaries for game state
GAME_HISTORY = []  # List to track all player actions
AVAILABLE_ACTIONS = []  # List of current available actions
QUEST_LOG = []  # List of active quests/objectives

# UTILITY FUNCTIONS - Enhanced with data structure operations

def display_header(title):
    """Display a formatted header for different game sections"""
    print("\n" + "=" * 50)
    print(f"    {title}")
    print("=" * 50)

def create_player_stats():
    """Create initial player stats dictionary"""
    return {
        "health": 100,
        "max_health": 100,
        "energy": 100,
        "max_energy": 100,
        "strength": 10,
        "luck": 5,
        "experience": 0,
        "level": 1,
        "current_location": "forest_entrance",
        "inventory": {},  # Dictionary to track item quantities
        "visited_locations": [],  # List of visited locations
        "game_history": [],  # List of player actions
        "achievements": [],  # List of earned achievements
        "score": 0
    }

def display_stats(player_stats):
    """Display current player stats using dictionary access"""
    print("\n--- Player Stats ---")
    print(f"Health: {player_stats['health']}/{player_stats['max_health']}")
    print(f"Energy: {player_stats['energy']}/{player_stats['max_energy']}")
    print(f"Strength: {player_stats['strength']}")
    print(f"Luck: {player_stats['luck']}")
    print(f"Level: {player_stats['level']} (XP: {player_stats['experience']})")
    print(f"Location: {LOCATIONS_DATABASE[player_stats['current_location']]['name']}")
    print(f"Score: {player_stats['score']}")
    print("--------------------")

def display_inventory(player_stats):
    """Display inventory using dictionary operations"""
    inventory = player_stats['inventory']
    if not inventory:
        print("📦 Your inventory is empty.")
        return
    
    print("\n📦 Your Inventory:")
    print("-" * 30)
    total_value = 0
    
    # Sort items by value (using dictionary comprehension and sorting)
    sorted_items = sorted(inventory.items(), key=lambda x: ITEMS_DATABASE[x[0]]['value'], reverse=True)
    
    for item_id, quantity in sorted_items:
        item_data = ITEMS_DATABASE[item_id]
        print(f"• {item_data['name']} x{quantity}")
        print(f"  {item_data['description']}")
        print(f"  Value: {item_data['value']} each")
        total_value += item_data['value'] * quantity
        print()
    
    print(f"Total Inventory Value: {total_value} coins")
    print("-" * 30)

def add_item_to_inventory(player_stats, item_id, quantity=1):
    """Add items to inventory using dictionary operations"""
    if item_id in ITEMS_DATABASE:
        if item_id in player_stats['inventory']:
            player_stats['inventory'][item_id] += quantity
        else:
            player_stats['inventory'][item_id] = quantity
        
        item_name = ITEMS_DATABASE[item_id]['name']
        print(f"✨ Added {quantity}x {item_name} to inventory!")
        
        # Add to game history
        player_stats['game_history'].append(f"Found {item_name}")
        return True
    return False

def remove_item_from_inventory(player_stats, item_id, quantity=1):
    """Remove items from inventory using dictionary operations"""
    if item_id in player_stats['inventory']:
        if player_stats['inventory'][item_id] >= quantity:
            player_stats['inventory'][item_id] -= quantity
            if player_stats['inventory'][item_id] == 0:
                del player_stats['inventory'][item_id]
            return True
    return False

def use_item(player_stats, item_id):
    """Use an item and apply its effects"""
    if item_id not in player_stats['inventory']:
        print("❌ You don't have that item!")
        return False
    
    item_data = ITEMS_DATABASE[item_id]
    if not item_data['usable']:
        print(f"❌ {item_data['name']} cannot be used!")
        return False
    
    # Apply item effects
    effects = item_data['effect']
    for stat, value in effects.items():
        if stat in player_stats:
            if stat == "health":
                player_stats[stat] = min(player_stats['max_health'], player_stats[stat] + value)
            elif stat == "energy":
                player_stats[stat] = min(player_stats['max_energy'], player_stats[stat] + value)
            else:
                player_stats[stat] += value
    
    # Remove item from inventory
    remove_item_from_inventory(player_stats, item_id)
    
    print(f"✅ Used {item_data['name']}!")
    if effects['health'] > 0:
        print(f"  Restored {effects['health']} health!")
    if effects['energy'] > 0:
        print(f"  Restored {effects['energy']} energy!")
    
    return True

def validate_input(prompt, valid_choices):
    """Get valid input from player with error handling"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid choice! Please try again.")

def get_available_actions(player_stats):
    """Get available actions for current location using dictionary lookup"""
    current_location = player_stats['current_location']
    location_data = LOCATIONS_DATABASE[current_location]
    return location_data['available_actions'].copy()

def add_experience(player_stats, exp_amount):
    """Add experience and handle level ups"""
    player_stats['experience'] += exp_amount
    print(f"📈 Gained {exp_amount} experience!")
    
    # Check for level up
    exp_needed = player_stats['level'] * 100
    if player_stats['experience'] >= exp_needed:
        player_stats['level'] += 1
        player_stats['experience'] -= exp_needed
        player_stats['max_health'] += 10
        player_stats['max_energy'] += 10
        player_stats['strength'] += 2
        player_stats['health'] = player_stats['max_health']
        player_stats['energy'] = player_stats['max_energy']
        print(f"🎉 LEVEL UP! You are now level {player_stats['level']}!")
        print("💪 Your stats have increased!")

def check_achievements(player_stats):
    """Check and award achievements based on player actions"""
    achievements = []
    
    # Achievement: First Steps
    if len(player_stats['visited_locations']) >= 3 and "explorer" not in player_stats['achievements']:
        achievements.append("explorer")
        print("🏆 Achievement Unlocked: Explorer - Visit 3 different locations")
    
    # Achievement: Collector
    if len(player_stats['inventory']) >= 5 and "collector" not in player_stats['achievements']:
        achievements.append("collector")
        print("🏆 Achievement Unlocked: Collector - Collect 5 different items")
    
    # Achievement: Survivor
    if player_stats['health'] <= 20 and "survivor" not in player_stats['achievements']:
        achievements.append("survivor")
        print("🏆 Achievement Unlocked: Survivor - Survive with low health")
    
    # Add new achievements to player stats
    player_stats['achievements'].extend(achievements)
    return achievements

def search_location_for_items(player_stats):
    """Search current location for items using list operations"""
    current_location = player_stats['current_location']
    location_data = LOCATIONS_DATABASE[current_location]
    available_items = location_data['items'].copy()
    
    if not available_items:
        print("🔍 You search the area but find nothing of interest.")
        return
    
    print("🔍 You search the area carefully...")
    
    # Random chance to find items based on luck
    search_success = random.randint(1, 10) <= (player_stats['luck'] + 3)
    
    if search_success and available_items:
        found_item = random.choice(available_items)
        add_item_to_inventory(player_stats, found_item)
        add_experience(player_stats, 10)
        
        # Remove item from location (simulating that it's been taken)
        location_data['items'].remove(found_item)
    else:
        print("🚫 Your search yields nothing useful.")

def move_to_location(player_stats, new_location):
    """Move player to a new location and update history"""
    if new_location in LOCATIONS_DATABASE:
        old_location = player_stats['current_location']
        player_stats['current_location'] = new_location
        
        # Add to visited locations if not already visited
        if new_location not in player_stats['visited_locations']:
            player_stats['visited_locations'].append(new_location)
            add_experience(player_stats, 15)
        
        # Add to game history
        location_name = LOCATIONS_DATABASE[new_location]['name']
        player_stats['game_history'].append(f"Moved to {location_name}")
        
        print(f"🚶 You move to {location_name}")
        print(f"📖 {LOCATIONS_DATABASE[new_location]['description']}")
        
        return True
    else:
        print(f"❌ Location '{new_location}' not found!")
        return False

def show_location_info(player_stats):
    """Display current location information"""
    current_location = player_stats['current_location']
    location_data = LOCATIONS_DATABASE[current_location]
    
    print(f"\n🌍 Current Location: {location_data['name']}")
    print(f"📖 {location_data['description']}")
    print(f"⚠️ Danger Level: {location_data['danger_level']}/5")
    
    # Show available actions
    actions = get_available_actions(player_stats)
    print(f"🎯 Available Actions: {', '.join(actions)}")
    
    # Show connected areas
    connected = location_data['connected_areas']
    if connected:
        print(f"🗺️ Connected Areas: {', '.join(connected)}")

def combat_system(player_stats, enemy_data):
    """Enhanced combat system using dictionaries for enemy data"""
    print(f"\n⚔️ Combat with {enemy_data['name']}!")
    print(f"📖 {enemy_data['description']}")
    
    enemy_health = enemy_data['health']
    battle_round = 0
    
    while player_stats['health'] > 0 and enemy_health > 0:
        battle_round += 1
        print(f"\n🥊 Battle Round {battle_round}")
        print(f"Your Health: {player_stats['health']} | Enemy Health: {enemy_health}")
        
        # Available combat actions
        combat_actions = ["attack", "use_item", "flee"]
        print("\nCombat Actions:")
        print("1. Attack")
        print("2. Use Item")
        print("3. Try to Flee")
        
        choice = validate_input("Choose action (1-3): ", ["1", "2", "3"])
        
        if choice == "1":
            # Attack calculation using player strength
            base_damage = random.randint(5, 10)
            strength_bonus = player_stats['strength'] // 2
            total_damage = base_damage + strength_bonus
            
            enemy_health -= total_damage
            print(f"⚔️ You deal {total_damage} damage!")
            add_experience(player_stats, 5)
            
        elif choice == "2":
            # Show usable items
            usable_items = [item for item in player_stats['inventory'] 
                          if ITEMS_DATABASE[item]['usable']]
            
            if not usable_items:
                print("❌ No usable items!")
                continue
            
            print("\nUsable Items:")
            for i, item in enumerate(usable_items, 1):
                print(f"{i}. {ITEMS_DATABASE[item]['name']}")
            
            try:
                item_choice = int(input("Choose item (number): ")) - 1
                if 0 <= item_choice < len(usable_items):
                    use_item(player_stats, usable_items[item_choice])
                else:
                    print("❌ Invalid item choice!")
                    continue
            except ValueError:
                print("❌ Invalid input!")
                continue
                
        elif choice == "3":
            # Flee chance based on luck and danger level
            flee_chance = (player_stats['luck'] + 5) / 20
            if random.random() < flee_chance:
                print("🏃 You successfully flee from battle!")
                player_stats['energy'] = max(0, player_stats['energy'] - 15)
                return "fled"
            else:
                print("❌ You couldn't escape!")
        
        # Check if enemy is defeated
        if enemy_health <= 0:
            print(f"\n🎉 Victory! You defeated the {enemy_data['name']}!")
            
            # Rewards
            exp_reward = enemy_data.get('exp_reward', 25)
            add_experience(player_stats, exp_reward)
            
            # Item drops
            if 'item_drops' in enemy_data:
                for item in enemy_data['item_drops']:
                    add_item_to_inventory(player_stats, item)
            
            player_stats['score'] += enemy_data.get('score_reward', 50)
            return "victory"
        
        # Enemy attack
        if enemy_health > 0:
            enemy_damage = random.randint(enemy_data['min_damage'], enemy_data['max_damage'])
            player_stats['health'] = max(0, player_stats['health'] - enemy_damage)
            print(f"👹 {enemy_data['name']} attacks for {enemy_damage} damage!")
            
            if player_stats['health'] <= 0:
                print(f"\n💀 You have been defeated by the {enemy_data['name']}...")
                return "defeat"
    
    return "ongoing"

def puzzle_challenge(player_stats):
    """Enhanced puzzle system with multiple types"""
    puzzles = [
        {
            "type": "math",
            "question": lambda: f"What is {random.randint(5, 15)} + {random.randint(5, 15)}?",
            "answer": lambda q: eval(q.split("What is ")[1].split("?")[0])
        },
        {
            "type": "logic",
            "question": lambda: "What comes next in the sequence: 2, 4, 8, 16, ?",
            "answer": lambda q: 32
        },
        {
            "type": "riddle",
            "question": lambda: "I have cities, but no houses. I have mountains, but no trees. What am I?",
            "answer": lambda q: "map"
        }
    ]
    
    puzzle = random.choice(puzzles)
    question = puzzle["question"]()
    
    print(f"\n🧩 Puzzle Challenge!")
    print(f"📝 {question}")
    
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\n🔢 Attempt {attempts}/{max_attempts}")
        
        try:
            if puzzle["type"] == "math":
                player_answer = int(input("Your answer: "))
                correct_answer = puzzle["answer"](question)
            else:
                player_answer = input("Your answer: ").lower().strip()
                correct_answer = puzzle["answer"](question)
            
            if player_answer == correct_answer:
                print("✅ Correct! Well done!")
                add_experience(player_stats, 20)
                player_stats['score'] += 30
                return True
            else:
                print(f"❌ Incorrect!")
                if attempts < max_attempts:
                    print("Try again...")
                    
        except ValueError:
            print("❌ Invalid input!")
            attempts -= 1
    
    print("🔨 You couldn't solve the puzzle, but you find another way forward.")
    player_stats['energy'] = max(0, player_stats['energy'] - 10)
    return False

def main_game_loop():
    """Main game loop with enhanced data structure management"""
    display_header("🌲 THE MYSTIC FOREST ADVENTURE - DATA STRUCTURES EDITION 🌲")
    
    # Main menu loop
    while True:
        print("\n🎮 MAIN MENU")
        print("1. Start New Adventure")
        print("2. View Game Statistics")
        print("3. Exit Game")
        
        choice = validate_input("Choose option (1-3): ", ["1", "2", "3"])
        
        if choice == "1":
            # Initialize new game
            player_stats = create_player_stats()
            
            # Game introduction
            print("\n🌲 Welcome to the Mystic Forest!")
            print("You wake up in a mysterious forest with no memory of how you got here.")
            print("Use your wits and the items you find to escape safely...")
            
            # Main game loop
            game_active = True
            while game_active:
                # Display current status
                show_location_info(player_stats)
                display_stats(player_stats)
                
                # Check achievements
                check_achievements(player_stats)
                
                # Get available actions for current location
                actions = get_available_actions(player_stats)
                actions.extend(["inventory", "stats", "history", "quit"])
                
                print("\n🎯 What would you like to do?")
                print("1. Explore/Move")
                print("2. Search Area")
                print("3. Use Item")
                print("4. View Inventory")
                print("5. Check Stats")
                print("6. View History")
                print("7. Quit Game")
                
                choice = validate_input("Choose action (1-7): ", ["1", "2", "3", "4", "5", "6", "7"])
                
                if choice == "1":
                    # Movement system
                    current_location = player_stats['current_location']
                    connected_areas = LOCATIONS_DATABASE[current_location]['connected_areas']
                    
                    if connected_areas:
                        print("\n🗺️ Available destinations:")
                        for i, area in enumerate(connected_areas, 1):
                            # Check if the area exists before accessing it
                            if area in LOCATIONS_DATABASE:
                                print(f"{i}. {LOCATIONS_DATABASE[area]['name']}")
                            else:
                                print(f"{i}. {area} (Under Construction)")
                        
                        try:
                            dest_choice = int(input("Choose destination: ")) - 1
                            if 0 <= dest_choice < len(connected_areas):
                                new_location = connected_areas[dest_choice]
                                if new_location in LOCATIONS_DATABASE:
                                    move_to_location(player_stats, new_location)
                                    
                                    # Random events based on danger level
                                    danger = LOCATIONS_DATABASE[new_location]['danger_level']
                                    if danger > 0 and random.random() < (danger / 10):
                                        print("\n⚠️ You encounter danger!")
                                        
                                        # Example enemy encounter
                                        enemy = {
                                            "name": "Shadow Creature",
                                            "description": "A dark creature emerges from the shadows",
                                            "health": 25,
                                            "min_damage": 3,
                                            "max_damage": 8,
                                            "exp_reward": 30,
                                            "score_reward": 40,
                                            "item_drops": ["shadow_essence"]
                                        }
                                        
                                        combat_result = combat_system(player_stats, enemy)
                                        if combat_result == "defeat":
                                            print("💀 Game Over!")
                                            game_active = False
                                            break
                                else:
                                    print("❌ That area is not accessible yet!")
                            else:
                                print("❌ Invalid destination!")
                        except ValueError:
                            print("❌ Invalid input!")
                    else:
                        print("🚫 No available destinations from here.")
                        if player_stats['current_location'] == "mystical_spring":
                            print("🎉 Congratulations! You've reached the end of the forest!")
                            print("You've successfully escaped!")
                            game_active = False
                
                elif choice == "2":
                    search_location_for_items(player_stats)
                
                elif choice == "3":
                    if player_stats['inventory']:
                        display_inventory(player_stats)
                        usable_items = [item for item in player_stats['inventory'] 
                                      if ITEMS_DATABASE[item]['usable']]
                        
                        if usable_items:
                            print("\nUsable items:")
                            for i, item in enumerate(usable_items, 1):
                                print(f"{i}. {ITEMS_DATABASE[item]['name']}")
                            
                            try:
                                item_choice = int(input("Choose item to use: ")) - 1
                                if 0 <= item_choice < len(usable_items):
                                    use_item(player_stats, usable_items[item_choice])
                                else:
                                    print("❌ Invalid item choice!")
                            except ValueError:
                                print("❌ Invalid input!")
                        else:
                            print("❌ No usable items in inventory!")
                    else:
                        print("📦 Your inventory is empty!")
                
                elif choice == "4":
                    display_inventory(player_stats)
                
                elif choice == "5":
                    display_stats(player_stats)
                    print(f"\n🏆 Achievements: {', '.join(player_stats['achievements']) if player_stats['achievements'] else 'None'}")
                
                elif choice == "6":
                    print("\n📜 Game History:")
                    for i, action in enumerate(player_stats['game_history'][-10:], 1):
                        print(f"{i}. {action}")
                    if len(player_stats['game_history']) > 10:
                        print(f"... and {len(player_stats['game_history']) - 10} more actions")
                
                elif choice == "7":
                    print("👋 Thanks for playing!")
                    game_active = False
                
                # Check win condition
                if player_stats['current_location'] == "mystical_spring":
                    print("\n🎉 Congratulations! You've reached the mystical spring!")
                    print("You've successfully escaped the forest!")
                    print(f"Final Score: {player_stats['score']}")
                    print(f"Level Reached: {player_stats['level']}")
                    print(f"Locations Visited: {len(player_stats['visited_locations'])}")
                    game_active = False
                
                # Check game over conditions
                if player_stats['health'] <= 0:
                    print("\n💀 Your health has reached zero!")
                    print("Game Over!")
                    game_active = False
                
                if player_stats['energy'] <= 0:
                    print("\n😴 You're too exhausted to continue!")
                    print("Game Over!")
                    game_active = False
        
        elif choice == "2":
            print("\n📊 GAME STATISTICS")
            print(f"Total Items in Database: {len(ITEMS_DATABASE)}")
            print(f"Total Locations: {len(LOCATIONS_DATABASE)}")
            print("\nItem Categories:")
            
            # Group items by type using dictionary comprehension
            usable_items = {k: v for k, v in ITEMS_DATABASE.items() if v['usable']}
            print(f"• Usable Items: {len(usable_items)}")
            
            valuable_items = {k: v for k, v in ITEMS_DATABASE.items() if v['value'] > 50}
            print(f"• Valuable Items (>50 value): {len(valuable_items)}")
            
        elif choice == "3":
            print("\n👋 Thanks for playing!")
            break
    
    print("\n📚 DATA STRUCTURES CONCEPTS DEMONSTRATED:")
    print("• Dictionaries for structured game data (items, locations, player stats)")
    print("• Lists for inventory management and game history")
    print("• Dictionary comprehensions for data filtering")
    print("• Nested data structures for complex game objects")
    print("• List operations (append, remove, sort)")
    print("• Dictionary operations (get, update, delete)")
    print("• Data structure iteration and manipulation")
    print("• Structured data organization and access")

if __name__ == "__main__":
    main_game_loop()
