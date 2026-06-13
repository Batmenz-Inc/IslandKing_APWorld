
from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Entrance, Region
from rule_builder.rules import *

if TYPE_CHECKING:
    from .world import IslandKingWorld

def create_and_connect_regions(world: "IslandKingWorld") -> None:
    ##################
    # CREATE REGIONS #
    ##################

    castle = Region("Castle", world.player, world.multiworld)
    main_island = Region("Main Island", world.player, world.multiworld)
    economics_room = Region("Economics Room", world.player, world.multiworld)
    town_shop = Region("Town Shop", world.player, world.multiworld)
    backyard = Region("Backyard", world.player, world.multiworld)
    basement = Region("Basement", world.player, world.multiworld)
    town_center = Region("Town Center", world.player, world.multiworld)
    intensive_research = Region("Intensive Research", world.player, world.multiworld)
    the_button = Region("The Button", world.player, world.multiworld)
    bigger_bunker = Region("Bigger Bunker", world.player, world.multiworld)
    expansion_island = Region("Expansion Island", world.player, world.multiworld)
    farming_island = Region("Farming Island", world.player, world.multiworld)
    fortified_island = Region("Fortified Island", world.player, world.multiworld)
    mysterious_island = Region("Mysterious Island", world.player, world.multiworld)

    regions = [
        castle,
        main_island,
        economics_room,
        town_shop,
        backyard,
        basement,
        town_center,
        intensive_research,
        the_button,
        bigger_bunker,
        expansion_island,
        farming_island,
        fortified_island,
        mysterious_island,
    ]

    world.multiworld.regions += regions

    ###################
    # CONNECT REGIONS #
    ###################

    castle.connect(main_island)
    main_island.connect(town_shop, "Open Shop", Or(Has("Open Shop"), Has("Open Shop (King)")))
    castle.connect(economics_room, "Economics Room", Has("Economics Room"))
    castle.connect(backyard, "Castle Backyard Door", Has("Unlock Backyard"))
    backyard.connect(basement, "Backyard Basement Door", Has("Unlock Basement"))
    basement.connect(town_center, "Town Center Upgrade", Has("Town Center Upgrade"))
    town_center.connect(intensive_research, "Intensive Research", Has("Intensive Research"))
    town_center.connect(the_button, "The Button", Has("The Button"))
    the_button.connect(bigger_bunker, "Bigger Bunker", Has("Bigger Bunker"))
    bigger_bunker.connect(expansion_island, "Expansion Island", Has("Expansion Island"))
    expansion_island.connect(farming_island, "Farming Island", Has("Farming Island"))
    farming_island.connect(fortified_island, "Fortified Island", Has("Fortified Island"))
    fortified_island.connect(mysterious_island, "Mysterious Island", Has("Mysterious Island"))