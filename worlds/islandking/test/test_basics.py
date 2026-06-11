

from . import IslandKingTestBase

from worlds.islandking.data_locations import all_locations


class TestBasics(IslandKingTestBase):
    options = {}

    def test_can_reach_ending(self):
        self.collect_all_but([])
        self.assertTrue(self.can_reach_region("Economics Room"), "Player should be able to reach Economics Room with all items collected")
        self.assertTrue(self.can_reach_region("Town Shop"), "Player should be able to reach Town Shop with all items collected")
        self.assertTrue(self.can_reach_region("Backyard"), "Player should be able to reach Backyard with all items collected")
        self.assertTrue(self.can_reach_region("Basement"), "Player should be able to reach Basement with all items collected")
        self.assertTrue(self.can_reach_region("Town Center"), "Player should be able to reach Town Center with all items collected")
        self.assertTrue(self.can_reach_region("Intensive Research"), "Player should be able to reach Intensive Research with all items collected")
        self.assertTrue(self.can_reach_region("The Button"), "Player should be able to reach The Button with all items collected")
        self.assertTrue(self.can_reach_region("Bigger Bunker"), "Player should be able to reach Bigger Bunker with all items collected")
        self.assertTrue(self.can_reach_region("Expansion Island"), "Player should be able to reach Expansion Island with all items collected")
        self.assertTrue(self.can_reach_region("Farming Island"), "Player should be able to reach Farming Island with all items collected")
        self.assertTrue(self.can_reach_region("Fortified Island"), "Player should be able to reach Fortified Island with all items collected")
        self.assertTrue(self.can_reach_region("Mysterious Island"), "Player should be able to reach Mysterious Island with all items collected")
        self.assertTrue(self.can_reach_location("The Grand Finale"), "Player should be able to reach The Grand Finale with all items collected")
    
    def test_can_reach_locations(self):
        self.collect_all_but([])
        for location in all_locations.keys():
            self.assertTrue(self.can_reach_location(location), f"Player should be able to reach {location} with all items collected")