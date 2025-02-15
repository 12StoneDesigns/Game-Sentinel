"""
Author: T. Landone Love
Company: 12Stone Designs
Contact: 12stonedesigns@gmail.com

A sophisticated game testing framework that simulates a fantasy RPG game environment
with multiple character classes, inventory system, and complex game mechanics.
"""

from enum import Enum
from typing import Dict, List, Optional
import random
import time


class CharacterClass(Enum):
    WARRIOR = "warrior"
    MAGE = "mage"
    ROGUE = "rogue"


class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    VICTORY = "victory"


class Item:
    def __init__(self, name: str, power: int, durability: int):
        self.name = name
        self.power = power
        self.durability = durability
        self.is_broken = False

    def use(self) -> bool:
        if self.is_broken:
            return False
        self.durability -= 1
        if self.durability <= 0:
            self.is_broken = True
        return True


class Character:
    def __init__(self, char_class: CharacterClass):
        self.char_class = char_class
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.experience = 0
        self.inventory: List[Item] = []
        
        # Class-specific stats
        if char_class == CharacterClass.WARRIOR:
            self.strength = 15
            self.magic = 5
            self.agility = 8
        elif char_class == CharacterClass.MAGE:
            self.strength = 5
            self.magic = 15
            self.agility = 8
        else:  # ROGUE
            self.strength = 8
            self.magic = 5
            self.agility = 15

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        
        if self.char_class == CharacterClass.WARRIOR:
            self.strength += 3
            self.magic += 1
            self.agility += 1
        elif self.char_class == CharacterClass.MAGE:
            self.strength += 1
            self.magic += 3
            self.agility += 1
        else:  # ROGUE
            self.strength += 1
            self.magic += 1
            self.agility += 3


class GameStatistics:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.actions_performed = 0
        self.items_collected = 0
        self.enemies_defeated = 0
        self.levels_completed = 0
        self.high_score = 0

    def start_session(self):
        self.start_time = time.time()

    def end_session(self):
        self.end_time = time.time()

    def get_session_duration(self) -> float:
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0.0

    def update_high_score(self, score: int):
        if score > self.high_score:
            self.high_score = score
            return True
        return False


class Game:
    def __init__(self):
        self.state = GameState.MENU
        self.character: Optional[Character] = None
        self.score = 0
        self.current_level = 1
        self.max_level = 5
        self.stats = GameStatistics()
        self.available_items = [
            Item("Sword", 10, 5),
            Item("Staff", 8, 8),
            Item("Dagger", 6, 10),
            Item("Health Potion", 20, 1),
            Item("Magic Scroll", 15, 3)
        ]

    def start_new_game(self, char_class: CharacterClass) -> str:
        self.character = Character(char_class)
        self.state = GameState.PLAYING
        self.score = 0
        self.current_level = 1
        self.stats = GameStatistics()
        self.stats.start_session()
        return f"Started new game with {char_class.value} class"

    def perform_action(self, action: str) -> str:
        if self.state != GameState.PLAYING:
            return f"Cannot perform action: Game is in {self.state.value} state"

        self.stats.actions_performed += 1
        action_result = ""

        if action == "attack":
            damage = self._calculate_damage()
            self.score += damage
            action_result = f"Performed attack dealing {damage} damage"
        elif action == "defend":
            self.character.health = min(self.character.max_health,
                                     self.character.health + 10)
            action_result = "Defended and recovered 10 health"
        elif action == "collect_item":
            if len(self.available_items) > 0:
                item = random.choice(self.available_items)
                self.character.inventory.append(item)
                self.stats.items_collected += 1
                action_result = f"Collected {item.name}"
            else:
                action_result = "No items available to collect"
        elif action == "use_item":
            if len(self.character.inventory) > 0:
                item = self.character.inventory.pop()
                if item.use():
                    self.score += item.power
                    action_result = f"Used {item.name} for {item.power} power"
                else:
                    action_result = f"{item.name} is broken"
            else:
                action_result = "No items in inventory"

        # Check for level completion
        if self.score >= self.current_level * 100:
            self._advance_level()
            action_result += f"\nAdvanced to level {self.current_level}"

        return action_result

    def _calculate_damage(self) -> int:
        base_damage = 0
        if self.character.char_class == CharacterClass.WARRIOR:
            base_damage = self.character.strength * 2
        elif self.character.char_class == CharacterClass.MAGE:
            base_damage = self.character.magic * 2
        else:  # ROGUE
            base_damage = self.character.agility * 2

        return base_damage + random.randint(1, 10)

    def _advance_level(self):
        self.current_level += 1
        self.character.level_up()
        self.stats.levels_completed += 1
        
        if self.current_level > self.max_level:
            self.complete_game()

    def complete_game(self) -> str:
        self.state = GameState.VICTORY
        self.stats.end_session()
        high_score_beaten = self.stats.update_high_score(self.score)
        
        result = (
            f"Game completed!\n"
            f"Final score: {self.score}\n"
            f"Time played: {self.stats.get_session_duration():.2f} seconds\n"
            f"Actions performed: {self.stats.actions_performed}\n"
            f"Items collected: {self.stats.items_collected}\n"
            f"Levels completed: {self.stats.levels_completed}"
        )
        
        if high_score_beaten:
            result += f"\nNew high score achieved!"
        
        return result

    def pause_game(self) -> str:
        if self.state == GameState.PLAYING:
            self.state = GameState.PAUSED
            return "Game paused"
        return f"Cannot pause: Game is in {self.state.value} state"

    def resume_game(self) -> str:
        if self.state == GameState.PAUSED:
            self.state = GameState.PLAYING
            return "Game resumed"
        return f"Cannot resume: Game is in {self.state.value} state"

    def quit_game(self) -> str:
        self.state = GameState.GAME_OVER
        self.stats.end_session()
        return "Game quit"
