
from typing import TYPE_CHECKING

from BaseClasses import CollectionState, Entrance, Region
from rule_builder.rules import *

if TYPE_CHECKING:
    from .world import IslandKingWorld

def create_and_connect_regions(world: IslandKingWorld) -> None:
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

    regions = [
        castle,
        main_island,
        economics_room,
        town_shop,
        backyard,
        basement,
        town_center
    ]

    world.multiworld.regions += regions

    ###################
    # CONNECT REGIONS #
    ###################

    castle.connect(main_island)
    main_island.connect(town_shop, "Open Shop", Has("Town Shop"))
    castle.connect(economics_room, "Economics Room", Has("Economics Room"))
    castle.connect(backyard, "Castle Backyard Door", Has("Unlock Backyard"))
    backyard.connect(basement, "Backyard Basement Door", Has("Unlock Basement"))
    basement.connect(town_center, "Town Center Upgrade", Has("Town Center Upgrade"))