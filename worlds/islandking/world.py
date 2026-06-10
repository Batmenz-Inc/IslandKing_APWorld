from collections.abc import Mapping
from typing import Any, List, Set
# Imports of base Archipelago modules must be absolute.
from BaseClasses import Item, Location
from worlds.AutoWorld import World
from rule_builder.rules import *

class IslandKingWorld(World):
    """
    Island King is a 2D top-down co-op roguelite game developed for the Archipelago Game Jam 2026.
    """

    game = "Island King"

    # Set the Web World
    # web = web_world.

    # Set the Options
    options_dataclass = 
    options:  # type: ignore

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    # location_name_to_id = locations.LOCATION_NAME_TO_ID
    # item_name_to_id = items.ITEM_NAME_TO_ID

    # Technically, Simon starts in the Entrance Hall, but for lore reasons, Starting at The Campsite is also acceptable, and is not a "room"
    origin_region_name = "Castle"

    # # Our world class must have certain functions ("steps") that get called during generation.
    # # The main ones are: create_regions, set_rules, create_items.
    # # For better structure and readability, we put each of these in their own file.
    def create_regions(self) -> None:
        pass

    def set_rules(self) -> None:
        self.set_completion_rule(CanReachLocation("The Grand Finale", "Mysterious Island")) # true urban win condition

    def create_items(self) -> None:
        pass

    # def create_item(self, name: str) -> items.IslandKingItem:
    #     return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return "Nothing"
        # return items.get_random_filler_item_name(self)
    
    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        slot_data = self.options.as_dict(
            
        )
        return slot_data