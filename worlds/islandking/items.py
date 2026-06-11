
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .constants import *
from .data_items import all_items

if TYPE_CHECKING:
    from .world import IslandKingWorld

ITEM_NAME_TO_ID = {
    "50 Coins": 1,

} | {
    k: v[ITEM_ID_KEY] for k, v in all_items.items()
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "50 Coins": ItemClassification.filler,

} | {
    k: v[ITEM_ITEM_CLASSIFICATION_KEY] for k, v in all_items.items()
}

class IslandKingItem(Item):
    game: str = "Island King"

def get_random_filler_item_name(world: "IslandKingWorld") -> str:
    return "50 Coins"

def create_item_with_correct_classification(world: "IslandKingWorld", name: str) -> IslandKingItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return IslandKingItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

# Create the items For the world
def create_all_items(world: "IslandKingWorld") -> None:

    itempool: list[Item] = []
    to_precollect: list[Item] = []

    exclude = [item for item in world.multiworld.precollected_items[world.player]]

    # 
    # Add Items
    # 

    itempool += [world.create_item(k) for k in all_items]

    # remove any items that are in starting inventory
    for item in to_precollect.copy():
        if item in exclude:
            exclude.remove(item)
        else:
            world.push_precollected(item)

    for item in itempool.copy():
        if item in exclude:
            exclude.remove(item)
            itempool.remove(item)

    #
    # Add Filler Stuff
    #

    # Get Number of Existing Items.
    number_of_items = len(itempool)

    # Get number of unfilled locations.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Determine Number Of Filler Items To Create
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Append Filler Items To Item Pool
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Add Itempool to world itempool
    world.multiworld.itempool += itempool