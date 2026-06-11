from BaseClasses import Item, ItemClassification
from .constants import *


path_unlocks = {
    "Town Center": {
        ITEM_ID_KEY: 1001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "The Button": {
        ITEM_ID_KEY: 1002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    }
}

path_progress = {
    "Unlock Backyard": {
        ITEM_ID_KEY: 2001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Unlock Basement": {
        ITEM_ID_KEY: 2002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Intensive Research": {
        ITEM_ID_KEY: 2003,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Bigger Bunker": {
        ITEM_ID_KEY: 2004,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Expansion Island": {
        ITEM_ID_KEY: 2005,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Farming Island": {
        ITEM_ID_KEY: 2006,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Fortified Island": {
        ITEM_ID_KEY: 2007,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Mysterious Island": {
        ITEM_ID_KEY: 2008,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
}

player_progress_unlock = {
    "Shop Unlock": {
        ITEM_ID_KEY: 5001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    "Shop Unlock (King)": {
        ITEM_ID_KEY: 5002,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    },
    # "Housing": {
    #     ITEM_ID_KEY: 5003,
    #     ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.useful
    # },
}

general_upgrades = {
    "Economics Room": {
        ITEM_ID_KEY: 6001,
        ITEM_ITEM_CLASSIFICATION_KEY: ItemClassification.progression
    }
}

all_items = general_upgrades | path_unlocks | path_progress | player_progress_unlock