"""
Test suite for Game Sentinel
Author: T. Landone Love
"""

import unittest
from game_sentinel import Game, CharacterClass, GameState

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.start_new_game(CharacterClass.WARRIOR)

    def test_game_initialization(self):
        self.assertEqual(self.game.state, GameState.PLAYING)
        self.assertEqual(self.game.character.char_class, CharacterClass.WARRIOR)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.current_level, 1)

    def test_character_classes(self):
        # Test Warrior stats
        warrior_game = Game()
        warrior_game.start_new_game(CharacterClass.WARRIOR)
        self.assertEqual(warrior_game.character.strength, 15)
        self.assertEqual(warrior_game.character.magic, 5)
        
        # Test Mage stats
        mage_game = Game()
        mage_game.start_new_game(CharacterClass.MAGE)
        self.assertEqual(mage_game.character.magic, 15)
        self.assertEqual(mage_game.character.strength, 5)
        
        # Test Rogue stats
        rogue_game = Game()
        rogue_game.start_new_game(CharacterClass.ROGUE)
        self.assertEqual(rogue_game.character.agility, 15)

    def test_game_actions(self):
        actions = ["attack", "defend", "collect_item", "use_item"]
        for action in actions:
            with self.subTest(action=action):
                result = self.game.perform_action(action)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_item_system(self):
        # Test item collection
        result = self.game.perform_action("collect_item")
        self.assertIn("Collected", result)
        self.assertEqual(len(self.game.character.inventory), 1)
        
        # Test item usage
        result = self.game.perform_action("use_item")
        self.assertIn("Used", result)
        self.assertEqual(len(self.game.character.inventory), 0)

    def test_game_progression(self):
        # Force score increase to trigger level up
        self.game.score = 99
        result = self.game.perform_action("attack")
        self.assertIn("Advanced to level", result)
        self.assertEqual(self.game.current_level, 2)
        self.assertGreater(self.game.character.max_health, 100)

    def test_game_statistics(self):
        self.game.perform_action("attack")
        self.game.perform_action("collect_item")
        self.game.quit_game()
        
        self.assertGreater(self.game.stats.get_session_duration(), 0)
        self.assertEqual(self.game.stats.actions_performed, 2)
        self.assertEqual(self.game.stats.items_collected, 1)

    def test_game_states(self):
        self.assertEqual(self.game.pause_game(), "Game paused")
        self.assertEqual(self.game.state, GameState.PAUSED)
        
        self.assertEqual(self.game.resume_game(), "Game resumed")
        self.assertEqual(self.game.state, GameState.PLAYING)
        
        self.assertEqual(self.game.quit_game(), "Game quit")
        self.assertEqual(self.game.state, GameState.GAME_OVER)


if __name__ == "__main__":
    unittest.main()
