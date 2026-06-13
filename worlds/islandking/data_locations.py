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

urban_upgrades = {
    "Crop Fertilizer": {
        LOCATION_ID_KEY: 3001,
        LOCATION_PARENT_REGION_KEY: "Town Center",
    },
    "Faster Processing": {
        LOCATION_ID_KEY: 3002,
        LOCATION_PARENT_REGION_KEY: "Town Center",
    },
    "Intensive Research": {
        LOCATION_ID_KEY: 3003,
        LOCATION_PARENT_REGION_KEY: "Town Center",
        LOCATION_RULE_KEY: Has("Intensive Research")
    },
    "Significantly Cropier Crops": {
        LOCATION_ID_KEY: 3004,
        LOCATION_PARENT_REGION_KEY: "Town Center",
    },
    "Extreme Economy": {
        LOCATION_ID_KEY: 3005,
        LOCATION_PARENT_REGION_KEY: "Intensive Research",
    },
    "Better Return Rates": {
        LOCATION_ID_KEY: 3006,
        LOCATION_PARENT_REGION_KEY: "Intensive Research",
    },
    "Crop Harvesting Technology": {
        LOCATION_ID_KEY: 3007,
        LOCATION_PARENT_REGION_KEY: "Intensive Research",
    },
    "The Button": {
        LOCATION_ID_KEY: 3008,
        LOCATION_PARENT_REGION_KEY: "Town Center",
        LOCATION_RULE_KEY: Has("The Button")
    },
}

true_urban_upgrades = {
    "A Dollar A Dime": {
        LOCATION_ID_KEY: 4001,
        LOCATION_PARENT_REGION_KEY: "The Button",
    },
    "Double City Funding": {
        LOCATION_ID_KEY: 4002,
        LOCATION_PARENT_REGION_KEY: "The Button",
    },
    "Guaranteed Returns": {
        LOCATION_ID_KEY: 4003,
        LOCATION_PARENT_REGION_KEY: "The Button",
    },
    "Better Farmers": {
        LOCATION_ID_KEY: 4004,
        LOCATION_PARENT_REGION_KEY: "The Button",
    },
    "Incredibly Fast Growth": {
        LOCATION_ID_KEY: 4005,
        LOCATION_PARENT_REGION_KEY: "The Button",
    },
    "Bigger Bunker": {
        LOCATION_ID_KEY: 4006,
        LOCATION_PARENT_REGION_KEY: "The Button",
        LOCATION_RULE_KEY: Has("Bigger Bunker")
    },
    "Expansion Island": {
        LOCATION_ID_KEY: 4007,
        LOCATION_PARENT_REGION_KEY: "Bigger Bunker",
        LOCATION_RULE_KEY: Has("Expansion Island")
    },
    "Morale Boost": {
        LOCATION_ID_KEY: 4008,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
    },
    "Lower Shipping Taxes": {
        LOCATION_ID_KEY: 4009,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
    },
    "Even Better Harvesting": {
        LOCATION_ID_KEY: 4010,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
    },
    "Faster Selling": {
        LOCATION_ID_KEY: 4011,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
    },
    "Farming Island": {
        LOCATION_ID_KEY: 4012,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
        LOCATION_RULE_KEY: Has("Farming Island")
    },
    "Deluxe Farm": {
        LOCATION_ID_KEY: 4013,
        LOCATION_PARENT_REGION_KEY: "Farming Island",
    },
    "Quality Control": {
        LOCATION_ID_KEY: 4014,
        LOCATION_PARENT_REGION_KEY: "Farming Island",
    },
    "Better Filters": {
        LOCATION_ID_KEY: 4015,
        LOCATION_PARENT_REGION_KEY: "Farming Island",
    },
    "Fortified Island": {
        LOCATION_ID_KEY: 4016,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
        LOCATION_RULE_KEY: Has("Fortified Island")
    },
    "Mysterious Island": {
        LOCATION_ID_KEY: 4017,
        LOCATION_PARENT_REGION_KEY: "Expansion Island",
        LOCATION_RULE_KEY: Has("Mysterious Island")
    },
    "The Grand Finale": {
        LOCATION_ID_KEY: 4018,
        LOCATION_PARENT_REGION_KEY: "Mysterious Island",
    },
}

town_shop = {

}

all_locations = castle_upgrades | main_island_upgrades | urban_upgrades | true_urban_upgrades | town_shop