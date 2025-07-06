# THE MYSTIC FOREST ADVENTURE - GUI EDITION
# A standalone GUI text-based adventure game using tkinter

import random
import time

# Try to import tkinter with error handling
try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext, ttk
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("⚠️  Tkinter is not available on this system.")
    print("📝 This is common on macOS with Homebrew Python installations.")
    print("🔧 To fix this, you can:")
    print("   1. Install tkinter: brew install python-tk")
    print("   3. Or run the CLI version instead")
    print()

# GAME DATA STRUCTURES
ITEMS_DATABASE = {
    "healing_potion": {
        "name": "Healing Potion",
        "effect": {
            "health": 25
        },
        "description": "A red vial filled with healing magic"
    },
    "energy_crystal": {
        "name": "Energy Crystal",
        "effect": {
            "energy": 20
        },
        "description": "A glowing crystal that restores energy"
    },
    "ancient_coin": {
        "name": "Ancient Coin",
        "effect": {},
        "description": "A mysterious coin with strange symbols"
    },
    "shadow_essence": {
        "name": "Shadow Essence",
        "effect": {
            "energy": 15
        },
        "description": "Dark energy from a defeated creature"
    }
}

class GameState:
    """Class to manage game state and statistics"""
    def __init__(self, player_name="Adventurer"):
        self.player_name = player_name
        self.health = 100
        self.max_health = 100
        self.energy = 100
        self.max_energy = 100
        self.inventory = []
        self.score = 0
        self.locations_visited = []
        self.choices_made = []
        self.battles_won = 0
        self.items_found = 0
        self.puzzles_solved = 0
        self.current_location = "Forest Entrance"
        self.game_complete = False
        self.ending_type = "incomplete"

class AdventureGameGUI:
    """Main GUI class for the adventure game"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌲 Mystic Forest Adventure - GUI Edition")
        self.root.geometry("900x700")
        self.root.configure(bg='#2d4a2d')
        
        # Game state
        self.game_state = None
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI components"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="🌲 THE MYSTIC FOREST ADVENTURE 🌲",
            font=("Arial", 20, "bold"),
            bg='#2d4a2d',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="GUI Edition - Interactive Adventure Game",
            font=("Arial", 12, "italic"),
            bg='#2d4a2d',
            fg='lightgray'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Main content frame
        self.main_frame = tk.Frame(self.root, bg='#2d4a2d')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Story text area with frame
        story_frame = tk.LabelFrame(
            self.main_frame,
            text="Adventure Story",
            font=("Arial", 12, "bold"),
            bg='#2d4a2d',
            fg='white',
            bd=2,
            relief='groove'
        )
        story_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.story_text = scrolledtext.ScrolledText(
            story_frame,
            height=18,
            width=80,
            font=("Arial", 11),
            bg='#f0f8f0',
            fg='#2d4a2d',
            wrap=tk.WORD,
            state=tk.DISABLED,
            padx=10,
            pady=10
        )
        self.story_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Stats frame
        stats_frame = tk.LabelFrame(
            self.main_frame,
            text="Player Stats",
            font=("Arial", 10, "bold"),
            bg='#2d4a2d',
            fg='white',
            bd=2,
            relief='groove'
        )
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.stats_inner_frame = tk.Frame(stats_frame, bg='#2d4a2d')
        self.stats_inner_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Stats labels
        self.health_label = tk.Label(self.stats_inner_frame, text="Health: --", bg='#2d4a2d', fg='white', font=("Arial", 10, "bold"))
        self.health_label.pack(side=tk.LEFT, padx=10)
        
        self.energy_label = tk.Label(self.stats_inner_frame, text="Energy: --", bg='#2d4a2d', fg='white', font=("Arial", 10, "bold"))
        self.energy_label.pack(side=tk.LEFT, padx=10)
        
        self.score_label = tk.Label(self.stats_inner_frame, text="Score: --", bg='#2d4a2d', fg='white', font=("Arial", 10, "bold"))
        self.score_label.pack(side=tk.LEFT, padx=10)
        
        self.location_label = tk.Label(self.stats_inner_frame, text="Location: --", bg='#2d4a2d', fg='white', font=("Arial", 10, "bold"))
        self.location_label.pack(side=tk.LEFT, padx=10)
        
        # Choice buttons frame
        choice_frame = tk.LabelFrame(
            self.main_frame,
            text="Actions",
            font=("Arial", 10, "bold"),
            bg='#2d4a2d',
            fg='white',
            bd=2,
            relief='groove'
        )
        choice_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.choice_frame = tk.Frame(choice_frame, bg='#2d4a2d')
        self.choice_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Start with welcome screen
        self.show_welcome_screen()
        
    def add_story_text(self, text):
        """Add text to the story display"""
        self.story_text.config(state=tk.NORMAL)
        self.story_text.insert(tk.END, text + "\n")
        self.story_text.see(tk.END)
        self.story_text.config(state=tk.DISABLED)
        
    def clear_story_text(self):
        """Clear the story display"""
        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete(1.0, tk.END)
        self.story_text.config(state=tk.DISABLED)
        
    def clear_choice_buttons(self):
        """Clear all choice buttons"""
        for widget in self.choice_frame.winfo_children():
            widget.destroy()
            
    def update_stats_display(self):
        """Update the stats display"""
        if self.game_state:
            self.health_label.config(text=f"Health: {self.game_state.health}/{self.game_state.max_health}")
            self.energy_label.config(text=f"Energy: {self.game_state.energy}/{self.game_state.max_energy}")
            self.score_label.config(text=f"Score: {self.game_state.score}")
            self.location_label.config(text=f"Location: {self.game_state.current_location}")
            
    def show_welcome_screen(self):
        """Display the welcome screen"""
        self.clear_story_text()
        self.clear_choice_buttons()
        
        welcome_text = """
Welcome to the Mystic Forest Adventure!

This is an interactive text-based adventure game where your choices determine your fate. 
You'll explore a mysterious forest, solve puzzles, collect items, and face various challenges.

Features:
🎮 Interactive GUI interface
🌲 Multiple story paths and endings
🎒 Inventory and item management
⚔️ Combat encounters
🧩 Puzzle challenges
📊 Detailed statistics tracking

Your goal is to escape the mysterious forest safely while scoring as many points as possible!

Good luck, brave adventurer!
"""
        
        self.add_story_text(welcome_text)
        
        # Get player name
        name_frame = tk.Frame(self.choice_frame, bg='#2d4a2d')
        name_frame.pack(pady=20)
        
        tk.Label(
            name_frame, 
            text="Enter your adventurer name:", 
            bg='#2d4a2d', 
            fg='white',
            font=("Arial", 12, "bold")
        ).pack(pady=(0, 10))
        
        self.name_entry = tk.Entry(
            name_frame, 
            width=25,
            font=("Arial", 12),
            justify='center'
        )
        self.name_entry.pack(pady=(0, 10))
        self.name_entry.insert(0, "Adventurer")
        self.name_entry.focus()
        
        # Buttons frame
        button_frame = tk.Frame(name_frame, bg='#2d4a2d')
        button_frame.pack(pady=10)
        
        start_btn = tk.Button(
            button_frame,
            text="🎮 Start Adventure!",
            command=self.start_new_game,
            bg='#4a7c59',
            fg='white',
            font=("Arial", 14, "bold"),
            width=20,
            height=2,
            cursor='hand2'
        )
        start_btn.pack(side=tk.LEFT, padx=10)
        
        demo_btn = tk.Button(
            button_frame,
            text="📊 View Demo Stats",
            command=self.show_demo_stats,
            bg='#4a4a7c',
            fg='white',
            font=("Arial", 14, "bold"),
            width=20,
            height=2,
            cursor='hand2'
        )
        demo_btn.pack(side=tk.LEFT, padx=10)
        
        # Bind Enter key to start game
        self.name_entry.bind('<Return>', lambda e: self.start_new_game())
        
    def start_new_game(self):
        """Start a new adventure game"""
        player_name = self.name_entry.get().strip() or "Adventurer"
        self.game_state = GameState(player_name)
        self.clear_choice_buttons()
        self.clear_story_text()
        
        self.add_story_text(f"🌲 Welcome to the Mystic Forest, {player_name}!")
        self.add_story_text("")
        self.add_story_text("You wake up in a dark, mysterious forest with no memory of how you got here.")
        self.add_story_text("Strange sounds echo through the trees, and an eerie mist surrounds you.")
        self.add_story_text("Your goal is to find your way out safely...")
        self.add_story_text("")
        self.add_story_text("The adventure begins now!")
        
        self.update_stats_display()
        self.root.after(1500, self.show_path_choice)
        
    def show_path_choice(self):
        """Show the initial path choice"""
        self.game_state.current_location = "Forest Entrance"
        self.update_stats_display()
        
        self.add_story_text("🌲 FOREST ENTRANCE")
        self.add_story_text("You see three paths ahead:")
        self.add_story_text("")
        
        choices = [
            ("🐦 Well-lit path with singing birds", lambda: self.choose_path("bright")),
            ("🍄 Dark trail with glowing mushrooms", lambda: self.choose_path("dark")),
            ("🗻 Rocky path leading uphill", lambda: self.choose_path("mountain"))
        ]
        
        self.create_choice_buttons(choices)
        
    def choose_path(self, path_type):
        """Handle path selection"""
        self.game_state.choices_made.append(f"Chose {path_type} path")
        self.clear_choice_buttons()
        
        if path_type == "bright":
            self.add_story_text("🐦 You chose the well-lit path...")
            self.add_story_text("The birds guide you safely, but you feel tired from the long walk.")
            self.modify_stats(energy=-20)
            self.add_story_text("You lose 20 energy but stay safe.")
            self.game_state.current_location = "Sunlit Path"
            
        elif path_type == "dark":
            self.add_story_text("🍄 You chose the dark trail...")
            self.add_story_text("The glowing mushrooms are beautiful but emit strange spores.")
            self.modify_stats(health=-15, energy=10)
            self.add_story_text("You lose 15 health but gain 10 energy from the magical mushrooms.")
            self.game_state.current_location = "Shadow Trail"
            
        else:  # mountain
            self.add_story_text("🗻 You chose the rocky uphill path...")
            self.add_story_text("The climb is exhausting but you get a great view of the area.")
            self.modify_stats(energy=-30)
            self.add_story_text("You lose 30 energy from the difficult climb.")
            self.game_state.current_location = "Mountain Peak"
            
        self.update_stats_display()
        
        # Simulate finding an item
        self.root.after(1500, lambda: self.item_discovery_phase(path_type))
        
    def item_discovery_phase(self, path_type):
        """Handle item discovery"""
        self.add_story_text("")
        self.add_story_text("🔍 EXPLORATION PHASE")
        self.add_story_text("You notice something glinting in the distance...")
        
        # Random item based on path
        path_items = {
            "bright": ["healing_potion", "ancient_coin"],
            "dark": ["shadow_essence", "energy_crystal"],
            "mountain": ["energy_crystal", "ancient_coin"]
        }
        
        found_item = random.choice(path_items[path_type])
        item_data = ITEMS_DATABASE[found_item]
        
        self.add_story_text(f"✨ You found a {item_data['name']}!")
        self.add_story_text(item_data['description'])
        
        self.game_state.inventory.append(found_item)
        self.game_state.items_found += 1
        self.game_state.score += 15
        
        # Apply item effects if it's usable
        if "health" in item_data["effect"]:
            self.modify_stats(health=item_data["effect"]["health"])
            self.add_story_text(f"You use it immediately and gain {item_data['effect']['health']} health!")
        elif "energy" in item_data["effect"]:
            self.modify_stats(energy=item_data["effect"]["energy"])
            self.add_story_text(f"You absorb its power and gain {item_data['effect']['energy']} energy!")
            
        self.update_stats_display()
        
        # Continue to puzzle
        self.root.after(2000, lambda: self.puzzle_challenge(path_type))
        
    def puzzle_challenge(self, path_type):
        """Present a puzzle challenge"""
        self.add_story_text("")
        self.add_story_text("🧩 ANCIENT PUZZLE")
        self.add_story_text("You encounter an ancient stone puzzle that blocks your path.")
        
        # Generate simple math puzzle
        num1 = random.randint(5, 15)
        num2 = random.randint(3, 8)
        correct_answer = num1 + num2
        
        self.add_story_text(f"The puzzle asks: What is {num1} + {num2}?")
        
        # Create input field and button
        puzzle_frame = tk.Frame(self.choice_frame, bg='#2d4a2d')
        puzzle_frame.pack(pady=10)
        
        tk.Label(puzzle_frame, text="Your answer:", bg='#2d4a2d', fg='white').pack(side=tk.LEFT)
        
        answer_entry = tk.Entry(puzzle_frame, width=10)
        answer_entry.pack(side=tk.LEFT, padx=5)
        
        def check_answer():
            try:
                player_answer = int(answer_entry.get())
                self.clear_choice_buttons()
                
                if player_answer == correct_answer:
                    self.add_story_text("✅ Correct! The puzzle glows and moves aside.")
                    self.modify_stats(energy=10)
                    self.game_state.score += 25
                    self.game_state.puzzles_solved += 1
                    self.add_story_text("You gain 10 energy and 25 points!")
                else:
                    self.add_story_text(f"❌ Incorrect. The answer was {correct_answer}.")
                    self.add_story_text("You find another way around the puzzle.")
                    self.modify_stats(energy=-5)
                    
                self.update_stats_display()
                self.root.after(2000, lambda: self.path_adventure(path_type))
                
            except ValueError:
                self.add_story_text("❌ Please enter a valid number.")
                
        submit_btn = tk.Button(
            puzzle_frame,
            text="Submit",
            command=check_answer,
            bg='#4a7c59',
            fg='white'
        )
        submit_btn.pack(side=tk.LEFT, padx=5)
        
        # Focus on entry
        answer_entry.focus()
        answer_entry.bind('<Return>', lambda e: check_answer())
        
    def path_adventure(self, path_type):
        """Handle path-specific adventures"""
        self.add_story_text("")
        
        if path_type == "bright":
            self.bright_path_adventure()
        elif path_type == "dark":
            self.dark_path_adventure()
        else:
            self.mountain_path_adventure()
            
    def bright_path_adventure(self):
        """Handle bright path storyline"""
        self.add_story_text("🌞 THE BRIGHT PATH")
        self.add_story_text("You reach a clearing with a sparkling fountain and a friendly hermit.")
        self.add_story_text("The hermit offers you a choice:")
        self.add_story_text("")
        
        choices = [
            ("💧 Drink from the magical fountain", lambda: self.bright_choice("fountain")),
            ("🧙 Ask the hermit for directions", lambda: self.bright_choice("hermit")),
            ("😴 Rest by the fountain", lambda: self.bright_choice("rest"))
        ]
        
        self.create_choice_buttons(choices)
        
    def bright_choice(self, choice):
        """Handle bright path choices"""
        self.clear_choice_buttons()
        self.game_state.choices_made.append(f"Bright path: {choice}")
        
        if choice == "fountain":
            self.add_story_text("💧 You drink from the fountain...")
            if self.game_state.health >= 80:
                self.add_story_text("The water tastes amazing! You feel completely refreshed.")
                self.game_state.health = self.game_state.max_health
                self.game_state.energy = self.game_state.max_energy
                self.add_story_text("Your health and energy are fully restored!")
            else:
                self.add_story_text("The water helps, but you needed more healing.")
                self.modify_stats(health=30, energy=20)
                self.add_story_text("You gain 30 health and 20 energy.")
            self.game_state.score += 30
            self.game_state.ending_type = "fountain"
            
        elif choice == "hermit":
            self.add_story_text("🧙 You ask the hermit for help...")
            self.add_story_text("The hermit gives you a map and advice about avoiding dangers.")
            self.modify_stats(energy=15)
            self.game_state.inventory.append("hermit_map")
            self.game_state.score += 25
            self.add_story_text("You gain 15 energy and receive a helpful map!")
            self.game_state.ending_type = "hermit"
            
        else:  # rest
            self.add_story_text("😴 You rest by the fountain...")
            self.modify_stats(energy=25)
            self.game_state.score += 20
            self.add_story_text("You gain 25 energy from the peaceful rest.")
            self.game_state.ending_type = "rest"
            
        self.update_stats_display()
        self.root.after(2000, self.complete_adventure)
        
    def dark_path_adventure(self):
        """Handle dark path storyline"""
        self.add_story_text("🌙 THE DARK TRAIL")
        self.add_story_text("You encounter a mysterious creature blocking your path!")
        self.add_story_text("It doesn't seem hostile, but it's watching you carefully.")
        self.add_story_text("")
        
        choices = [
            ("🗣️ Try to communicate", lambda: self.dark_choice("communicate")),
            ("🤫 Sneak around quietly", lambda: self.dark_choice("sneak")),
            ("🍞 Offer food", lambda: self.dark_choice("offer_food"))
        ]
        
        self.create_choice_buttons(choices)
        
    def dark_choice(self, choice):
        """Handle dark path choices"""
        self.clear_choice_buttons()
        self.game_state.choices_made.append(f"Dark path: {choice}")
        
        if choice == "communicate":
            self.add_story_text("🗣️ You try to communicate...")
            if self.game_state.health >= 70:
                self.add_story_text("Your strong presence impresses the creature!")
                self.add_story_text("It leads you to a secret exit from the forest.")
                self.game_state.score += 40
                self.game_state.ending_type = "creature_ally"
            else:
                self.add_story_text("The creature senses your weakness but remains peaceful.")
                self.add_story_text("You find another path around it.")
                self.modify_stats(energy=-10)
                self.game_state.score += 15
                self.game_state.ending_type = "alternative"
                
        elif choice == "sneak":
            self.add_story_text("🤫 You sneak around quietly...")
            if self.game_state.energy >= 60:
                self.add_story_text("You successfully sneak past! The creature never noticed.")
                self.modify_stats(energy=-15)
                self.game_state.score += 35
                self.game_state.ending_type = "stealth"
            else:
                self.add_story_text("You're too tired to sneak properly but the creature is understanding.")
                self.modify_stats(energy=-10)
                self.game_state.score += 20
                self.game_state.ending_type = "peaceful"
                
        else:  # offer_food
            self.add_story_text("🍞 You offer food to the creature...")
            self.add_story_text("The creature accepts your gift gratefully!")
            self.modify_stats(energy=-5)
            self.game_state.inventory.append("creature_blessing")
            self.game_state.score += 45
            self.game_state.ending_type = "friendship"
            
        self.update_stats_display()
        
        # Potential combat encounter
        if choice == "communicate" and self.game_state.health < 70:
            self.root.after(2000, self.combat_encounter)
        else:
            self.root.after(2000, self.complete_adventure)
            
    def mountain_path_adventure(self):
        """Handle mountain path storyline"""
        self.add_story_text("⛰️ THE MOUNTAIN PATH")
        self.add_story_text("From the mountain top, you see the entire forest spread below you.")
        self.add_story_text("You spot three possible ways down:")
        self.add_story_text("")
        
        choices = [
            ("⬇️ Take the steep direct path", lambda: self.mountain_choice("steep")),
            ("🕳️ Enter the winding caves", lambda: self.mountain_choice("caves")),
            ("🏠 Wait for help", lambda: self.mountain_choice("wait"))
        ]
        
        self.create_choice_buttons(choices)
        
    def mountain_choice(self, choice):
        """Handle mountain path choices"""
        self.clear_choice_buttons()
        self.game_state.choices_made.append(f"Mountain path: {choice}")
        
        if choice == "steep":
            self.add_story_text("⬇️ You take the steep path...")
            if self.game_state.energy >= 40:
                self.add_story_text("You carefully make your way down without injury.")
                self.modify_stats(energy=-20)
                self.game_state.score += 30
                self.game_state.ending_type = "safe_descent"
            else:
                self.add_story_text("You're tired and slip, but manage to recover.")
                self.modify_stats(health=-15, energy=-15)
                self.game_state.score += 15
                self.game_state.ending_type = "difficult_descent"
                
        elif choice == "caves":
            self.add_story_text("🕳️ You enter the caves...")
            self.add_story_text("The caves are dark but lead to an underground river.")
            self.modify_stats(energy=-10)
            self.game_state.score += 35
            self.game_state.ending_type = "cave_river"
            
        else:  # wait
            self.add_story_text("🏠 You wait for help...")
            self.add_story_text("A friendly ranger finds you and escorts you to safety.")
            self.modify_stats(energy=-5)
            self.game_state.score += 25
            self.game_state.ending_type = "rescue"
            
        self.update_stats_display()
        self.root.after(2000, self.complete_adventure)
        
    def combat_encounter(self):
        """Handle a combat encounter"""
        self.add_story_text("")
        self.add_story_text("⚔️ COMBAT ENCOUNTER")
        self.add_story_text("The creature becomes aggressive and attacks!")
        
        enemy_health = 25
        self.combat_round(enemy_health)
        
    def combat_round(self, enemy_health):
        """Handle a single combat round"""
        if self.game_state.health <= 0:
            self.add_story_text("💀 You have been defeated...")
            self.game_state.ending_type = "defeat"
            self.complete_adventure()
            return
            
        if enemy_health <= 0:
            self.add_story_text("🎉 Victory! You defeated the creature!")
            self.game_state.battles_won += 1
            self.game_state.score += 50
            self.game_state.inventory.append("victory_trophy")
            self.update_stats_display()
            self.root.after(2000, self.complete_adventure)
            return
            
        self.add_story_text(f"Your Health: {self.game_state.health} | Enemy Health: {enemy_health}")
        self.add_story_text("Choose your action:")
        
        choices = [
            ("⚔️ Attack", lambda: self.combat_action("attack", enemy_health)),
            ("🧪 Use healing item", lambda: self.combat_action("heal", enemy_health)),
            ("🏃 Try to flee", lambda: self.combat_action("flee", enemy_health))
        ]
        
        self.create_choice_buttons(choices)
        
    def combat_action(self, action, enemy_health):
        """Handle combat actions"""
        self.clear_choice_buttons()
        
        if action == "attack":
            damage = random.randint(8, 15)
            enemy_health -= damage
            self.add_story_text(f"⚔️ You deal {damage} damage!")
            
        elif action == "heal":
            healing_items = [item for item in self.game_state.inventory if "healing" in item]
            if healing_items:
                self.game_state.inventory.remove(healing_items[0])
                self.modify_stats(health=25)
                self.add_story_text("🧪 You use a healing item and recover 25 health!")
            else:
                self.add_story_text("❌ You don't have any healing items!")
                
        elif action == "flee":
            if random.random() > 0.4:  # 60% chance to flee
                self.add_story_text("🏃 You successfully escape!")
                self.modify_stats(energy=-10)
                self.game_state.ending_type = "fled"
                self.update_stats_display()
                self.root.after(2000, self.complete_adventure)
                return
            else:
                self.add_story_text("❌ You couldn't escape!")
                
        # Enemy attacks
        if enemy_health > 0:
            enemy_damage = random.randint(5, 12)
            self.modify_stats(health=-enemy_damage)
            self.add_story_text(f"👹 The creature attacks for {enemy_damage} damage!")
            
        self.update_stats_display()
        self.root.after(1500, lambda: self.combat_round(enemy_health))
        
    def complete_adventure(self):
        """Complete the adventure and show results"""
        self.game_state.game_complete = True
        self.add_story_text("")
        self.add_story_text("🎉 ADVENTURE COMPLETE!")
        self.add_story_text("=" * 40)
        
        # Calculate final score
        location_bonus = len(self.game_state.locations_visited) * 10
        health_bonus = self.game_state.health // 2
        self.game_state.score += location_bonus + health_bonus
        
        self.add_story_text(f"Final Score: {self.game_state.score}")
        self.add_story_text(f"Items Found: {self.game_state.items_found}")
        self.add_story_text(f"Puzzles Solved: {self.game_state.puzzles_solved}")
        self.add_story_text(f"Battles Won: {self.game_state.battles_won}")
        
        # Show ending based on score and choices
        if self.game_state.score >= 150:
            self.add_story_text("⭐ LEGENDARY EXPLORER ENDING!")
            self.add_story_text("You mastered the forest and became a legend!")
        elif self.game_state.score >= 100:
            self.add_story_text("🌟 EXPERT ADVENTURER ENDING!")
            self.add_story_text("You navigated the forest with great skill!")
        elif self.game_state.score >= 50:
            self.add_story_text("😊 SUCCESSFUL ESCAPE ENDING!")
            self.add_story_text("You made it out safely!")
        else:
            self.add_story_text("😅 SURVIVOR ENDING!")
            self.add_story_text("You barely escaped, but you're alive!")
            
        self.update_stats_display()
        
        # Show final buttons
        button_frame = tk.Frame(self.choice_frame, bg='#2d4a2d')
        button_frame.pack(pady=20)
        
        stats_btn = tk.Button(
            button_frame,
            text="📊 Detailed Statistics",
            command=self.show_detailed_stats,
            bg='#4a4a7c',
            fg='white',
            font=("Arial", 12, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        stats_btn.pack(side=tk.LEFT, padx=10)
        
        restart_btn = tk.Button(
            button_frame,
            text="🔄 New Adventure",
            command=self.show_welcome_screen,
            bg='#4a7c59',
            fg='white',
            font=("Arial", 12, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        restart_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(
            button_frame,
            text="❌ Quit Game",
            command=self.root.quit,
            bg='#7c4a4a',
            fg='white',
            font=("Arial", 12, "bold"),
            width=18,
            height=2,
            cursor='hand2'
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
    def show_detailed_stats(self):
        """Show detailed game statistics in a new window"""
        stats_window = tk.Toplevel(self.root)
        stats_window.title(f"📊 Adventure Statistics - {self.game_state.player_name}")
        stats_window.geometry("600x500")
        stats_window.configure(bg='#f0f8f0')
        
        # Title
        title_label = tk.Label(
            stats_window,
            text=f"🎮 {self.game_state.player_name}'s Adventure Report",
            font=("Arial", 16, "bold"),
            bg='#f0f8f0',
            fg='#2d4a2d'
        )
        title_label.pack(pady=10)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(stats_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Basic Stats Tab
        basic_frame = tk.Frame(notebook, bg='#f0f8f0')
        notebook.add(basic_frame, text="📊 Basic Stats")
        
        basic_text = tk.Text(basic_frame, height=15, width=70, bg='white', fg='#2d4a2d')
        basic_text.pack(padx=10, pady=10)
        
        basic_stats = f"""
🎯 FINAL RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Final Score: {self.game_state.score} points
Ending Type: {self.game_state.ending_type.replace('_', ' ').title()}

🏃‍♂️ PLAYER STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Health: {self.game_state.health}/{self.game_state.max_health}
Energy: {self.game_state.energy}/{self.game_state.max_energy}
Final Location: {self.game_state.current_location}

🎒 INVENTORY & DISCOVERIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Items Found: {self.game_state.items_found}
Items in Inventory: {len(self.game_state.inventory)}
Inventory Contents: {', '.join(self.game_state.inventory) if self.game_state.inventory else 'Empty'}

⚔️ COMBAT & CHALLENGES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Battles Won: {self.game_state.battles_won}
Puzzles Solved: {self.game_state.puzzles_solved}
Locations Visited: {len(self.game_state.locations_visited)}

🎲 PERFORMANCE RATING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        if self.game_state.score >= 150:
            basic_stats += "★★★★★ LEGENDARY (150+ points)\n"
        elif self.game_state.score >= 100:
            basic_stats += "★★★★☆ EXPERT (100+ points)\n"
        elif self.game_state.score >= 50:
            basic_stats += "★★★☆☆ SKILLED (50+ points)\n"
        else:
            basic_stats += "★★☆☆☆ NOVICE (<50 points)\n"
            
        basic_text.insert(tk.END, basic_stats)
        basic_text.config(state=tk.DISABLED)
        
        # Choices Tab
        choices_frame = tk.Frame(notebook, bg='#f0f8f0')
        notebook.add(choices_frame, text="🎯 Choices Made")
        
        choices_text = tk.Text(choices_frame, height=15, width=70, bg='white', fg='#2d4a2d')
        choices_text.pack(padx=10, pady=10)
        
        choices_summary = "🎯 DECISION HISTORY\n" + "="*50 + "\n\n"
        for i, choice in enumerate(self.game_state.choices_made, 1):
            choices_summary += f"{i}. {choice}\n"
            
        choices_text.insert(tk.END, choices_summary)
        choices_text.config(state=tk.DISABLED)
        
        # Tips Tab
        tips_frame = tk.Frame(notebook, bg='#f0f8f0')
        notebook.add(tips_frame, text="💡 Tips & Analysis")
        
        tips_text = tk.Text(tips_frame, height=15, width=70, bg='white', fg='#2d4a2d')
        tips_text.pack(padx=10, pady=10)
        
        tips_content = """
💡 PERFORMANCE ANALYSIS & TIPS
═══════════════════════════════════════════════════════════════

📈 SCORE BREAKDOWN:
• Base adventure completion: Varies by choices
• Items found bonus: +15 points each
• Puzzles solved bonus: +25 points each
• Combat victories: +50 points each
• Health preservation: +1 point per 2 health remaining
• Location exploration: +10 points per location

🎯 STRATEGIES FOR HIGHER SCORES:
• Explore thoroughly to find more items
• Solve puzzles when encountered (+25 points each)
• Maintain high health for bonus points
• Make strategic choices based on current stats
• Combat can be rewarding but risky

🎮 REPLAYABILITY FEATURES:
• Multiple story paths with different outcomes
• Random elements ensure unique experiences
• Various difficulty levels based on choices
• Hidden bonus points for specific combinations

💪 CHALLENGE YOURSELF:
• Try different path combinations
• Aim for 150+ points (Legendary status)
• Experiment with risk vs. safety choices
• See how many different endings you can discover
"""
        
        tips_text.insert(tk.END, tips_content)
        tips_text.config(state=tk.DISABLED)
        
    def show_demo_stats(self):
        """Show demo statistics window"""
        # Create a sample completed game state for demo
        demo_state = GameState("Demo Player")
        demo_state.score = 165
        demo_state.health = 75
        demo_state.energy = 60
        demo_state.inventory = ["healing_potion", "ancient_coin", "shadow_essence", "victory_trophy"]
        demo_state.items_found = 4
        demo_state.puzzles_solved = 1
        demo_state.battles_won = 1
        demo_state.locations_visited = ["Forest Entrance", "Shadow Trail", "Dark Cave", "Crystal Chamber"]
        demo_state.choices_made = ["Chose dark path", "Dark path: communicate", "Fought creature bravely"]
        demo_state.ending_type = "legendary_hero"
        demo_state.game_complete = True
        
        # Temporarily replace current game state
        original_state = self.game_state
        self.game_state = demo_state
        
        # Show detailed stats
        self.show_detailed_stats()
        
        # Restore original state
        self.game_state = original_state
        
    def create_choice_buttons(self, choices):
        """Create choice buttons from a list of (text, command) tuples"""
        self.clear_choice_buttons()
        
        for i, (text, command) in enumerate(choices):
            btn = tk.Button(
                self.choice_frame,
                text=f"{i+1}. {text}",
                command=command,
                bg='#4a7c59',
                fg='white',
                font=("Arial", 11),
                width=50,
                height=2,
                wraplength=400,
                cursor='hand2',
                relief='raised',
                bd=2
            )
            btn.pack(pady=5)
            
            # Add hover effects
            def on_enter(e, button=btn):
                button.config(bg='#5d8f6c')
            def on_leave(e, button=btn):
                button.config(bg='#4a7c59')
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            
    def modify_stats(self, health=0, energy=0):
        """Modify player stats with bounds checking"""
        if health != 0:
            self.game_state.health = max(0, min(self.game_state.max_health, self.game_state.health + health))
        if energy != 0:
            self.game_state.energy = max(0, min(self.game_state.max_energy, self.game_state.energy + energy))
            
    def run(self):
        """Start the GUI main loop"""
        # Center the window on screen
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.root.mainloop()

def main():
    """Main function to start the GUI application"""
    if not TKINTER_AVAILABLE:
        print("❌ GUI mode is not available due to missing tkinter.")
        print("🎮 Starting CLI mode instead...")
        print()
        
        # Try to import and run the CLI version
        try:
            import sys
            import os
            
            # Get the directory where this script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))
            functions_file = os.path.join(script_dir, "mystic_codex_functions.py")
            
            if os.path.exists(functions_file):
                # Import and run the functions version
                sys.path.insert(0, script_dir)
                from mystic_codex_functions import main as cli_main
                cli_main()
            else:
                print("❌ CLI version not found. Running simplified text adventure...")
                run_simple_text_adventure()
                
        except ImportError as e:
            print(f"❌ Could not import CLI version: {e}")
            print("🎮 Running simplified text adventure instead...")
            run_simple_text_adventure()
    else:
        try:
            app = AdventureGameGUI()
            app.run()
        except Exception as e:
            print(f"❌ Error starting the GUI application: {e}")
            print("🎮 Running simplified text adventure instead...")
            run_simple_text_adventure()

def run_simple_text_adventure():
    """Simple text-based adventure game fallback"""
    print("🌲 THE MYSTIC FOREST ADVENTURE - TEXT EDITION 🌲")
    print("="*50)
    print()
    
    # Simple game state
    health = 100
    energy = 100
    inventory = []
    score = 0
    
    print("You wake up in a dark, mysterious forest...")
    print("Your goal is to find your way out safely!")
    print()
    
    # Path choice
    print("🌲 You see three paths ahead:")
    print("1. 🐦 Well-lit path with singing birds")
    print("2. 🍄 Dark trail with glowing mushrooms")
    print("3. 🗻 Rocky path leading uphill")
    print()
    
    while True:
        choice = input("Which path do you choose? (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("❌ Please enter 1, 2, or 3")
    
    if choice == '1':
        print("\n🐦 You chose the well-lit path...")
        print("The birds guide you safely, but you feel tired.")
        energy -= 20
        score += 20
        print("You lose 20 energy but gain 20 points for safety.")
        
    elif choice == '2':
        print("\n🍄 You chose the dark trail...")
        print("The glowing mushrooms emit strange spores.")
        health -= 15
        energy += 10
        score += 30
        print("You lose 15 health but gain 10 energy and 30 points for bravery.")
        
    else:
        print("\n🗻 You chose the rocky uphill path...")
        print("The climb is exhausting but gives a great view.")
        energy -= 30
        score += 25
        print("You lose 30 energy but gain 25 points for perseverance.")
    
    # Item discovery
    print(f"\n🔍 You search the area...")
    items = ["healing potion", "energy crystal", "ancient coin"]
    found_item = random.choice(items)
    inventory.append(found_item)
    print(f"✨ You found a {found_item}!")
    
    if found_item == "healing potion":
        health = min(100, health + 25)
        print("You drink it and gain 25 health!")
    elif found_item == "energy crystal":
        energy = min(100, energy + 20)
        print("You absorb its power and gain 20 energy!")
    
    score += 15
    
    # Simple puzzle
    print(f"\n🧩 You encounter an ancient puzzle...")
    num1 = random.randint(5, 15)
    num2 = random.randint(3, 8)
    correct = num1 + num2
    
    print(f"What is {num1} + {num2}?")
    
    try:
        answer = int(input("Your answer: "))
        if answer == correct:
            print("✅ Correct! You solve the puzzle!")
            energy += 10
            score += 25
        else:
            print(f"❌ Incorrect. The answer was {correct}.")
            energy -= 5
    except ValueError:
        print("❌ Invalid input. You skip the puzzle.")
        energy -= 5
    
    # Final results
    print("\n" + "="*50)
    print("🎉 ADVENTURE COMPLETE!")
    print("="*50)
    print(f"Final Health: {health}")
    print(f"Final Energy: {energy}")
    print(f"Items Found: {len(inventory)}")
    print(f"Final Score: {score}")
    
    if score >= 70:
        print("\n⭐ EXCELLENT ADVENTURER!")
        print("You mastered the forest!")
    elif score >= 50:
        print("\n🌟 SKILLED EXPLORER!")
        print("You navigated well!")
    else:
        print("\n😊 BRAVE SURVIVOR!")
        print("You made it out alive!")
    
    print("\n📚 This simplified version demonstrates:")
    print("• Basic input/output operations")
    print("• Conditional statements (if/elif/else)")
    print("• Random number generation")
    print("• Error handling with try/except")
    print("• Simple game state management")
    print()
    print("👉 To run the full GUI version, install tkinter:")
    print("   brew install python-tk")
    print("👉 Or run the CLI version:")
    print("   python3 mystic_codex_functions.py")

if __name__ == "__main__":
    print("🌲 Starting Mystic Forest Adventure...")
    if TKINTER_AVAILABLE:
        print("🖱️  GUI mode available - starting graphical interface...")
    else:
        print("⌨️  GUI mode unavailable - running text mode...")
    print()
    print("📚 This version demonstrates:")
    if TKINTER_AVAILABLE:
        print("• GUI programming with tkinter")
        print("• Event-driven programming")
        print("• Object-oriented design")
        print("• User interface design principles")
        print("• Real-time statistics display")
        print("• Interactive storytelling")
    else:
        print("• Error handling and graceful fallbacks")
        print("• Import error management")
        print("• Alternative execution paths")
        print("• Simple game logic implementation")
    print()
    main()
