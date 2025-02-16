"""
Demo script to showcase the Game Testing Framework functionality
Author: T. Landone Love
"""

from game_sentinel import Game, CharacterClass, GameState
import time
import sys

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
    try:
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
            
            # Perform various actions
            print("\nPerforming actions:")
            
            # Test all available actions
            actions = ["attack", "defend", "collect_item", "use_item"]
            for action in actions:
                result = game.perform_action(action)
                print(f"- {result}")
            
            # Demonstrate level progression
            print("\nDemonstrating level progression:")
            while game.current_level < 3:  # Progress through 2 levels
                result = game.perform_action("attack")
                if "Advanced to level" in result:
                    print(f"- {result}")
                    display_character_stats(game.character)
            
            # Test game state changes
            print("\nTesting game states:")
            print(f"- {game.pause_game()}")
            print(f"- {game.resume_game()}")
            
            # Display final stats
            display_character_stats(game.character)
            
            # End game and show statistics
            print("\nGame Statistics:")
            print(game.quit_game())
            print(f"Session duration: {game.stats.get_session_duration():.2f} seconds")
            print(f"Actions performed: {game.stats.actions_performed}")
            print(f"Items collected: {game.stats.items_collected}")
            print(f"Current score: {game.score}")
            print(f"Levels completed: {game.stats.levels_completed}")
            print("\n" + "="*40)

    except KeyboardInterrupt:
        print("\nDemo interrupted by user")
        # Ensure proper cleanup
        for game in games.values():
            if game.state != GameState.GAME_OVER:
                game.quit_game()
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_demo()
