
from typing import TYPE_CHECKING, List, Optional
from BaseClasses import CollectionState, ItemClassification, Location, LocationProgressType, Region, Region
from .constants import *
from .data_locations import all_locations

if TYPE_CHECKING:
    from .world import IslandKingWorld

LOCATION_NAME_TO_ID = {
    location_name: location_data[LOCATION_ID_KEY] for location_name, location_data in all_locations.items()
}

class IslandKingLocation(Location):
    game: str = "Island King"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: "IslandKingWorld") -> None:
    
    for location_name, location_data in all_locations.items():
        locs = get_location_names_with_ids([location_name])
        world.get_region(location_data[LOCATION_PARENT_REGION_KEY]).add_locations(locs, IslandKingLocation)

        if LOCATION_RULE_KEY in location_data:
            world.set_rule(world.get_location(location_name), location_data[LOCATION_RULE_KEY])