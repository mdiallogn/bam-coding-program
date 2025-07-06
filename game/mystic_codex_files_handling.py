# THE MYSTIC FOREST ADVENTURE - FILE HANDLING EDITION
# A text-based game to learn file operations, data persistence, and error handling

import random
import json
import os
import datetime
from pathlib import Path

# FILE PATHS - Using Path objects for cross-platform compatibility
GAME_DATA_DIR = Path("game_data")
SAVE_FILES_DIR = GAME_DATA_DIR / "saves"
CONFIG_FILE = GAME_DATA_DIR / "config.json"
HIGHSCORES_FILE = GAME_DATA_DIR / "highscores.json"
PLAYER_PROFILES_FILE = GAME_DATA_DIR / "player_profiles.json"
GAME_HISTORY_FILE = GAME_DATA_DIR / "game_history.txt"

# Ensure directories exist
GAME_DATA_DIR.mkdir(exist_ok=True)
SAVE_FILES_DIR.mkdir(exist_ok=True)

# GAME DATABASE - Using dictionaries to store structured game data
ITEMS_DATABASE = {
    "healing_potion": {
        "name": "Healing Potion",
        "description": "A red vial filled with healing magic",
        "effect": {"health": 25, "energy": 0},
        "value": 50,
        "usable": True
    },
    "energy_crystal": {
        "name": "Energy Crystal", 
        "description": "A glowing crystal that restores energy",
        "effect": {"health": 0, "energy": 20},
        "value": 40,
        "usable": True
    },
    "ancient_coin": {
        "name": "Ancient Coin",
        "description": "A mysterious coin with strange symbols",
        "effect": {"health": 0, "energy": 0},
        "value": 100,
        "usable": False
    },
    "shadow_essence": {
        "name": "Shadow Essence",
        "description": "Dark energy captured from a defeated creature", 
        "effect": {"health": 0, "energy": 15},
        "value": 75,
        "usable": True
    }
}

# DEFAULT GAME CONFIGURATION
DEFAULT_CONFIG = {
    "difficulty": "normal",
    "sound_enabled": True,
    "auto_save": True,
    "player_name": "Adventurer",
    "max_save_slots": 5,
    "display_hints": True
}

# FILE OPERATIONS FUNCTIONS

def load_json_file(filepath, default_data=None):
    """Load JSON data from file with error handling"""
    try:
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(f"✅ Loaded data from {filepath.name}")
                return data
        else:
            print(f"📄 File {filepath.name} not found, using defaults")
            return default_data if default_data is not None else {}
    except json.JSONDecodeError as e:
        print(f"❌ Error reading {filepath.name}: Invalid JSON format")
        print(f"   Details: {e}")
        return default_data if default_data is not None else {}
    except PermissionError:
        print(f"❌ Permission denied accessing {filepath.name}")
        return default_data if default_data is not None else {}
    except Exception as e:
        print(f"❌ Unexpected error loading {filepath.name}: {e}")
        return default_data if default_data is not None else {}

def save_json_file(filepath, data):
    """Save data to JSON file with error handling"""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"✅ Saved data to {filepath.name}")
        return True
    except PermissionError:
        print(f"❌ Permission denied writing to {filepath.name}")
        return False
    except Exception as e:
        print(f"❌ Error saving to {filepath.name}: {e}")
        return False

def append_to_text_file(filepath, text):
    """Append text to file with timestamp"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"[{timestamp}] {text}\n")
        return True
    except Exception as e:
        print(f"❌ Error writing to {filepath.name}: {e}")
        return False

# CONFIGURATION MANAGEMENT

def load_config():
    """Load game configuration from file"""
    config = load_json_file(CONFIG_FILE, DEFAULT_CONFIG.copy())
    
    # Ensure all required keys exist
    for key, value in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = value
    
    return config

def save_config(config):
    """Save game configuration to file"""
    return save_json_file(CONFIG_FILE, config)

def update_config_setting(key, value):
    """Update a single configuration setting"""
    config = load_config()
    config[key] = value
    save_config(config)
    print(f"⚙️ Updated {key} to {value}")

# PLAYER PROFILE MANAGEMENT

def load_player_profiles():
    """Load all player profiles"""
    return load_json_file(PLAYER_PROFILES_FILE, {})

def save_player_profiles(profiles):
    """Save all player profiles"""
    return save_json_file(PLAYER_PROFILES_FILE, profiles)

def create_player_profile(player_name):
    """Create a new player profile"""
    profiles = load_player_profiles()
    
    if player_name not in profiles:
        profiles[player_name] = {
            "name": player_name,
            "games_played": 0,
            "total_score": 0,
            "best_score": 0,
            "achievements": [],
            "total_playtime": 0,
            "created_date": datetime.datetime.now().isoformat(),
            "last_played": None
        }
        save_player_profiles(profiles)
        print(f"👤 Created new profile for {player_name}")
    
    return profiles[player_name]

def update_player_profile(player_name, game_stats):
    """Update player profile with game results"""
    profiles = load_player_profiles()
    
    if player_name not in profiles:
        create_player_profile(player_name)
    
    profile = profiles[player_name]
    profile["games_played"] += 1
    profile["total_score"] += game_stats.get("score", 0)
    profile["best_score"] = max(profile["best_score"], game_stats.get("score", 0))
    profile["last_played"] = datetime.datetime.now().isoformat()
    
    # Add new achievements
    new_achievements = game_stats.get("achievements", [])
    for achievement in new_achievements:
        if achievement not in profile["achievements"]:
            profile["achievements"].append(achievement)
    
    profiles[player_name] = profile
    save_player_profiles(profiles)

# HIGH SCORE MANAGEMENT

def load_highscores():
    """Load high scores from file"""
    default_scores = {"scores": []}
    return load_json_file(HIGHSCORES_FILE, default_scores)

def save_highscores(highscores):
    """Save high scores to file"""
    return save_json_file(HIGHSCORES_FILE, highscores)

def add_highscore(player_name, score, difficulty, date=None):
    """Add a new high score entry"""
    if date is None:
        date = datetime.datetime.now().isoformat()
    
    highscores = load_highscores()
    
    new_score = {
        "player": player_name,
        "score": score,
        "difficulty": difficulty,
        "date": date
    }
    
    highscores["scores"].append(new_score)
    
    # Sort by score (descending) and keep top 10
    highscores["scores"].sort(key=lambda x: x["score"], reverse=True)
    highscores["scores"] = highscores["scores"][:10]
    
    save_highscores(highscores)
    print(f"🏆 Added high score: {score} points")

def display_highscores():
    """Display the high scores leaderboard"""
    highscores = load_highscores()
    scores = highscores.get("scores", [])
    
    print("\n" + "="*50)
    print("🏆 HIGH SCORES LEADERBOARD 🏆")
    print("="*50)
    
    if not scores:
        print("No high scores yet! Be the first to set a record!")
        return
    
    print(f"{'Rank':<4} {'Player':<15} {'Score':<8} {'Difficulty':<10} {'Date':<12}")
    print("-" * 55)
    
    for i, score in enumerate(scores, 1):
        date_str = score["date"][:10] if len(score["date"]) > 10 else score["date"]
        print(f"{i:<4} {score['player']:<15} {score['score']:<8} {score['difficulty']:<10} {date_str:<12}")

# SAVE GAME MANAGEMENT

def get_save_slots():
    """Get list of available save slots"""
    save_files = list(SAVE_FILES_DIR.glob("save_*.json"))
    slots = {}
    
    for save_file in save_files:
        try:
            slot_num = int(save_file.stem.split("_")[1])
            save_data = load_json_file(save_file)
            if save_data:
                slots[slot_num] = {
                    "filename": save_file.name,
                    "player_name": save_data.get("player_name", "Unknown"),
                    "save_date": save_data.get("save_date", "Unknown"),
                    "location": save_data.get("current_location", "Unknown"),
                    "level": save_data.get("level", 1),
                    "score": save_data.get("score", 0)
                }
        except (ValueError, IndexError):
            continue
    
    return slots

def save_game(game_state, slot_number):
    """Save game state to specified slot"""
    save_file = SAVE_FILES_DIR / f"save_{slot_number}.json"
    
    # Add metadata
    save_data = game_state.copy()
    save_data["save_date"] = datetime.datetime.now().isoformat()
    save_data["save_slot"] = slot_number
    
    if save_json_file(save_file, save_data):
        print(f"💾 Game saved to slot {slot_number}")
        return True
    return False

def load_game(slot_number):
    """Load game state from specified slot"""
    save_file = SAVE_FILES_DIR / f"save_{slot_number}.json"
    
    if not save_file.exists():
        print(f"❌ Save slot {slot_number} is empty")
        return None
    
    save_data = load_json_file(save_file)
    if save_data:
        print(f"📁 Loaded game from slot {slot_number}")
        return save_data
    return None

def delete_save(slot_number):
    """Delete a save file"""
    save_file = SAVE_FILES_DIR / f"save_{slot_number}.json"
    
    try:
        if save_file.exists():
            save_file.unlink()
            print(f"🗑️ Deleted save slot {slot_number}")
            return True
        else:
            print(f"❌ Save slot {slot_number} doesn't exist")
            return False
    except Exception as e:
        print(f"❌ Error deleting save slot {slot_number}: {e}")
        return False

# GAME STATISTICS AND EXPORT

def export_player_statistics(player_name):
    """Export player statistics to a text file"""
    profiles = load_player_profiles()
    
    if player_name not in profiles:
        print(f"❌ No profile found for {player_name}")
        return False
    
    profile = profiles[player_name]
    export_file = GAME_DATA_DIR / f"{player_name}_stats.txt"
    
    try:
        with open(export_file, 'w', encoding='utf-8') as file:
            file.write(f"PLAYER STATISTICS REPORT\n")
            file.write(f"========================\n\n")
            file.write(f"Player Name: {profile['name']}\n")
            file.write(f"Profile Created: {profile['created_date'][:10]}\n")
            file.write(f"Last Played: {profile.get('last_played', 'Never')[:10]}\n")
            file.write(f"Games Played: {profile['games_played']}\n")
            file.write(f"Total Score: {profile['total_score']}\n")
            file.write(f"Best Score: {profile['best_score']}\n")
            file.write(f"Average Score: {profile['total_score'] / max(1, profile['games_played']):.1f}\n")
            file.write(f"\nAchievements Unlocked:\n")
            
            if profile['achievements']:
                for achievement in profile['achievements']:
                    file.write(f"• {achievement}\n")
            else:
                file.write("• No achievements yet\n")
            
            file.write(f"\nReport generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        print(f"📊 Statistics exported to {export_file.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error exporting statistics: {e}")
        return False

def log_game_event(event_text):
    """Log game events to history file"""
    return append_to_text_file(GAME_HISTORY_FILE, event_text)

# UTILITY FUNCTIONS

def display_header(title):
    """Display a formatted header for different game sections"""
    print("\n" + "=" * 50)
    print(f"    {title}")
    print("=" * 50)

def create_player_stats(player_name="Adventurer"):
    """Create initial player stats dictionary"""
    return {
        "player_name": player_name,
        "health": 100,
        "max_health": 100,
        "energy": 100,
        "max_energy": 100,
        "strength": 10,
        "luck": 5,
        "experience": 0,
        "level": 1,
        "current_location": "forest_entrance",
        "inventory": {},
        "visited_locations": [],
        "game_history": [],
        "achievements": [],
        "score": 0,
        "start_time": datetime.datetime.now().isoformat()
    }

def validate_input(prompt, valid_choices):
    """Get valid input from player with error handling"""
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid choice! Please try again.")

# MAIN MENU AND GAME MANAGEMENT

def show_file_management_menu():
    """Show file management options"""
    while True:
        display_header("📁 FILE MANAGEMENT")
        print("1. Manage Save Games")
        print("2. View High Scores")
        print("3. Player Profiles")
        print("4. Game Settings")
        print("5. Export Statistics")
        print("6. View Game History")
        print("7. Reset All Data")
        print("8. Back to Main Menu")
        
        choice = validate_input("Choose option (1-8): ", [str(i) for i in range(1, 9)])
        
        if choice == "1":
            manage_save_games()
        elif choice == "2":
            display_highscores()
        elif choice == "3":
            manage_player_profiles()
        elif choice == "4":
            manage_game_settings()
        elif choice == "5":
            export_statistics_menu()
        elif choice == "6":
            view_game_history()
        elif choice == "7":
            reset_all_data()
        elif choice == "8":
            break

def manage_save_games():
    """Manage save game slots"""
    while True:
        display_header("💾 SAVE GAME MANAGEMENT")
        
        slots = get_save_slots()
        config = load_config()
        max_slots = config.get("max_save_slots", 5)
        
        print("Save Slots:")
        for i in range(1, max_slots + 1):
            if i in slots:
                slot_info = slots[i]
                print(f"{i}. {slot_info['player_name']} - Level {slot_info['level']} - {slot_info['save_date'][:10]}")
            else:
                print(f"{i}. [Empty Slot]")
        
        print(f"\n{max_slots + 1}. Delete a save")
        print(f"{max_slots + 2}. Back to File Management")
        
        choice = validate_input("Choose option: ", [str(i) for i in range(1, max_slots + 3)])
        choice_num = int(choice)
        
        if 1 <= choice_num <= max_slots:
            if choice_num in slots:
                slot_info = slots[choice_num]
                print(f"\nSave Slot {choice_num}:")
                print(f"Player: {slot_info['player_name']}")
                print(f"Date: {slot_info['save_date'][:19]}")
                print(f"Location: {slot_info['location']}")
                print(f"Level: {slot_info['level']}")
                print(f"Score: {slot_info['score']}")
            else:
                print(f"\nSave slot {choice_num} is empty")
        elif choice_num == max_slots + 1:
            delete_slot = validate_input("Enter slot number to delete (or 'cancel'): ", 
                                       [str(i) for i in range(1, max_slots + 1)] + ["cancel"])
            if delete_slot != "cancel":
                delete_save(int(delete_slot))
        elif choice_num == max_slots + 2:
            break

def manage_player_profiles():
    """Manage player profiles"""
    display_header("👤 PLAYER PROFILES")
    
    profiles = load_player_profiles()
    
    if not profiles:
        print("No player profiles found.")
        return
    
    print("Player Profiles:")
    for name, profile in profiles.items():
        print(f"\n👤 {name}")
        print(f"   Games Played: {profile['games_played']}")
        print(f"   Best Score: {profile['best_score']}")
        print(f"   Total Score: {profile['total_score']}")
        print(f"   Achievements: {len(profile['achievements'])}")
        print(f"   Last Played: {profile.get('last_played', 'Never')[:10]}")

def manage_game_settings():
    """Manage game configuration settings"""
    config = load_config()
    
    while True:
        display_header("⚙️ GAME SETTINGS")
        
        print(f"1. Difficulty: {config['difficulty']}")
        print(f"2. Sound Enabled: {config['sound_enabled']}")
        print(f"3. Auto Save: {config['auto_save']}")
        print(f"4. Default Player Name: {config['player_name']}")
        print(f"5. Max Save Slots: {config['max_save_slots']}")
        print(f"6. Display Hints: {config['display_hints']}")
        print("7. Reset to Defaults")
        print("8. Back to File Management")
        
        choice = validate_input("Choose option (1-8): ", [str(i) for i in range(1, 9)])
        
        if choice == "1":
            difficulty = validate_input("Choose difficulty (easy/normal/hard): ", ["easy", "normal", "hard"])
            config["difficulty"] = difficulty
        elif choice == "2":
            config["sound_enabled"] = not config["sound_enabled"]
        elif choice == "3":
            config["auto_save"] = not config["auto_save"]
        elif choice == "4":
            name = input("Enter default player name: ").strip()
            if name:
                config["player_name"] = name
        elif choice == "5":
            try:
                slots = int(input("Enter max save slots (1-10): "))
                if 1 <= slots <= 10:
                    config["max_save_slots"] = slots
            except ValueError:
                print("❌ Invalid number")
        elif choice == "6":
            config["display_hints"] = not config["display_hints"]
        elif choice == "7":
            config = DEFAULT_CONFIG.copy()
            print("⚙️ Settings reset to defaults")
        elif choice == "8":
            break
        
        if choice != "8":
            save_config(config)

def export_statistics_menu():
    """Menu for exporting statistics"""
    display_header("📊 EXPORT STATISTICS")
    
    profiles = load_player_profiles()
    
    if not profiles:
        print("No player profiles found to export.")
        return
    
    print("Available players:")
    players = list(profiles.keys())
    for i, player in enumerate(players, 1):
        print(f"{i}. {player}")
    
    print(f"{len(players) + 1}. Export All Players")
    print(f"{len(players) + 2}. Cancel")
    
    choice = validate_input("Choose option: ", [str(i) for i in range(1, len(players) + 3)])
    choice_num = int(choice)
    
    if 1 <= choice_num <= len(players):
        export_player_statistics(players[choice_num - 1])
    elif choice_num == len(players) + 1:
        for player in players:
            export_player_statistics(player)
        print("📊 Exported statistics for all players")

def view_game_history():
    """View game history log"""
    display_header("📜 GAME HISTORY")
    
    try:
        if GAME_HISTORY_FILE.exists():
            with open(GAME_HISTORY_FILE, 'r', encoding='utf-8') as file:
                history = file.readlines()
            
            if history:
                print("Recent game events (last 20):")
                for line in history[-20:]:
                    print(line.strip())
            else:
                print("No game history recorded yet.")
        else:
            print("No game history file found.")
    except Exception as e:
        print(f"❌ Error reading game history: {e}")

def reset_all_data():
    """Reset all game data with confirmation"""
    display_header("🗑️ RESET ALL DATA")
    
    print("⚠️ WARNING: This will delete ALL game data including:")
    print("• Save games")
    print("• Player profiles")  
    print("• High scores")
    print("• Configuration")
    print("• Game history")
    
    confirm = validate_input("Are you sure? Type 'DELETE ALL' to confirm: ", ["delete all", "cancel"])
    
    if confirm == "delete all":
        try:
            # Delete all files
            for file_path in [CONFIG_FILE, HIGHSCORES_FILE, PLAYER_PROFILES_FILE, GAME_HISTORY_FILE]:
                if file_path.exists():
                    file_path.unlink()
            
            # Delete save files
            for save_file in SAVE_FILES_DIR.glob("save_*.json"):
                save_file.unlink()
            
            # Delete exported statistics
            for stats_file in GAME_DATA_DIR.glob("*_stats.txt"):
                stats_file.unlink()
            
            print("🗑️ All game data has been deleted.")
            
        except Exception as e:
            print(f"❌ Error deleting data: {e}")
    else:
        print("❌ Reset cancelled.")

# MAIN GAME FUNCTIONS (simplified versions with file handling)
# Note: These functions are simplified for demonstration purposes and do not run the full game logic.

def start_new_game():
    """Start a new adventure game"""
    config = load_config()
    
    # Get player name
    default_name = config.get("player_name", "Adventurer")
    player_name = input(f"Enter your name (or press Enter for '{default_name}'): ").strip()
    if not player_name:
        player_name = default_name
    
    # Create player profile
    create_player_profile(player_name)
    
    # Initialize game state
    game_state = create_player_stats(player_name)
    
    # Log game start
    log_game_event(f"New game started by {player_name}")
    
    # Simple game simulation
    print(f"\n🌲 Welcome to the Mystic Forest, {player_name}!")
    print("You wake up in a mysterious forest...")
    
    # Simulate some gameplay
    game_state["score"] = random.randint(50, 200)
    game_state["achievements"] = ["first_game"]
    if game_state["score"] > 150:
        game_state["achievements"].append("high_scorer")
    
    # Auto-save if enabled
    if config.get("auto_save", True):
        save_game(game_state, 1)
    
    # Update player profile
    update_player_profile(player_name, game_state)
    
    # Add to high scores
    add_highscore(player_name, game_state["score"], config["difficulty"])
    
    # Log game completion
    log_game_event(f"Game completed by {player_name} with score {game_state['score']}")
    
    print(f"\n🎉 Game completed! Final score: {game_state['score']}")

def load_existing_game():
    """Load an existing game"""
    slots = get_save_slots()
    
    if not slots:
        print("❌ No saved games found.")
        return
    
    display_header("📁 LOAD GAME")
    print("Available save games:")
    
    for slot_num, slot_info in slots.items():
        print(f"{slot_num}. {slot_info['player_name']} - Level {slot_info['level']} - {slot_info['save_date'][:10]}")
    
    choice = validate_input("Choose save slot (or 'cancel'): ", 
                           list(map(str, slots.keys())) + ["cancel"])
    
    if choice == "cancel":
        return
    
    game_state = load_game(int(choice))
    if game_state:
        print(f"🎮 Resuming game for {game_state['player_name']}")
        log_game_event(f"Game loaded by {game_state['player_name']} from slot {choice}")
        
        # Continue game simulation
        print("Continuing your adventure...")
        game_state["score"] += random.randint(20, 80)
        
        # Save progress
        save_game(game_state, int(choice))
        update_player_profile(game_state["player_name"], game_state)
        
        print(f"🎉 Adventure continues! Current score: {game_state['score']}")

def main_game_loop():
    """Main game loop with file handling capabilities"""
    display_header("🌲 THE MYSTIC FOREST ADVENTURE - FILE HANDLING EDITION 🌲")
    
    # Load configuration
    config = load_config()
    print(f"⚙️ Game difficulty: {config['difficulty']}")
    
    while True:
        print("\n🎮 MAIN MENU")
        print("1. Start New Adventure")
        print("2. Load Saved Game")
        print("3. File Management")
        print("4. View High Scores")
        print("5. Exit Game")
        
        choice = validate_input("Choose option (1-5): ", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            start_new_game()
        elif choice == "2":
            load_existing_game()
        elif choice == "3":
            show_file_management_menu()
        elif choice == "4":
            display_highscores()
        elif choice == "5":
            print("\n👋 Thanks for playing!")
            log_game_event("Game session ended")
            break
    
    print("\n📚 FILE HANDLING CONCEPTS DEMONSTRATED:")
    print("• JSON file reading and writing for structured data")
    print("• Text file operations for logs and exports")
    print("• Error handling for file operations")
    print("• Data persistence across game sessions")
    print("• Configuration management")
    print("• Save/load game functionality")
    print("• High score tracking and leaderboards")
    print("• Player profile management")
    print("• Data export and import capabilities")
    print("• File path management with Path objects")

if __name__ == "__main__":
    main_game_loop()
