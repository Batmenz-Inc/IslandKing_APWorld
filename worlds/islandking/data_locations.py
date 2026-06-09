from BaseClasses import Item, ItemClassification
from rule_builder.rules import *
from .constants import *

castle_upgrades = {
    "Economics Room": {
        LOCATION_ID_KEY: 1001,
        LOCATION_PARENT_REGION_KEY: "Castle",
        LOCATION_RULE_KEY: Has("Economics Room")
    },
    "Unlock Backyard": {
        LOCATION_ID_KEY: 1002,
        LOCATION_PARENT_REGION_KEY: "Castle",
        LOCATION_RULE_KEY: Has("Unlock Backyard")
    },
    "Unlock Basement": {
        LOCATION_ID_KEY: 1003,
        LOCATION_PARENT_REGION_KEY: "Backyard",
        LOCATION_RULE_KEY: Has("Unlock Basement")
    },
    "Town Center Upgrade": {
        LOCATION_ID_KEY: 1004,
        LOCATION_PARENT_REGION_KEY: "Basement",
        LOCATION_RULE_KEY: Has("Town Center Upgrade")
    },
    "Faster Money Generation": {
        LOCATION_ID_KEY: 1005,
        LOCATION_PARENT_REGION_KEY: "Economics Room",
    },
    "Better Sell Deals": {
        LOCATION_ID_KEY: 1006,
        LOCATION_PARENT_REGION_KEY: "Economics Room",
    },
}

main_island_upgrades = {
    "Open Shop": {
        LOCATION_ID_KEY: 2001,
        LOCATION_PARENT_REGION_KEY: "Main Island",
        LOCATION_RULE_KEY: Has("Open Shop")
    },
    "Open Shop (King)": {
        LOCATION_ID_KEY: 2002,
        LOCATION_PARENT_REGION_KEY: "Main Island",
        LOCATION_RULE_KEY: Has("Open Shop (King)")
    },
    "Faster Crop Spawn Rate": {
        LOCATION_ID_KEY: 2003,
        LOCATION_PARENT_REGION_KEY: "Main Island"
    }
}

town_shop = {

}

all_locations = castle_upgrades | main_island_upgrades | town_shop