"""
Demo script to showcase the Game Testing Framework functionality
Author: T. Landone Love
"""

from game_testing_framework import Game, CharacterClass
import time

def display_character_stats(character):
    print(f"\nCharacter Stats:")
    print(f"Class: {character.char_class.value}")
    print(f"Level: {character.level}")
    print(f"Health: {character.health}/{character.max_health}")
    print(f"Strength: {character.strength}")
    print(f"Magic: {character.magic}")
    print(f"Agility: {character.agility}")
    print(f"Items in inventory: {len(character.inventory)}")

def run_demo():
    print("=== Game Testing Framework Demo ===\n")
    
    # Create game instances for each character class
    games = {
        "Warrior": Game(),
        "Mage": Game(),
        "Rogue": Game()
    }
    
    # Test each character class
    for class_name, game in games.items():
        print(f"\n=== Testing {class_name} Class ===")
        
        # Start new game with character class
        result = game.start_new_game(CharacterClass[class_name.upper()])
        print(result)
        
        # Display initial stats
        display_character_stats(game.character)
        time.sleep(0.5)  # Add delay for more realistic session duration
        
        # Perform various actions
        print("\nPerforming actions:")
        
        # Collect some items
        for _ in range(2):
            result = game.perform_action("collect_item")
            print(f"- {result}")
            time.sleep(0.3)  # Add delay between actions
        
        # Perform attacks
        for _ in range(3):
            result = game.perform_action("attack")
            print(f"- {result}")
            time.sleep(0.3)
        
        # Use collected items
        for _ in range(2):
            result = game.perform_action("use_item")
            print(f"- {result}")
            time.sleep(0.3)
        
        # Test game state changes
        print("\nTesting game states:")
        print(f"- {game.pause_game()}")
        time.sleep(0.3)
        print(f"- {game.resume_game()}")
        time.sleep(0.3)
        
        # Display final stats
        display_character_stats(game.character)
        
        # End game and show statistics
        print("\nGame Statistics:")
        print(game.quit_game())
        print(f"Session duration: {game.stats.get_session_duration():.2f} seconds")
        print(f"Actions performed: {game.stats.actions_performed}")
        print(f"Items collected: {game.stats.items_collected}")
        print(f"Current score: {game.score}")
        print("\n" + "="*40)
        
        # Add delay between character tests for readability
        time.sleep(1)

if __name__ == "__main__":
    run_demo()
