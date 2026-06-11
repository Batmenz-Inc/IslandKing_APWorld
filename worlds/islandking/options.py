from dataclasses import dataclass

from Options import (
    Choice,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    Toggle,
    Visibility,
    OptionCounter,
)

# Filler Options.
class FillerItemDistribution(OptionCounter):
    """
    This option allows the user to set the weight chance of any particular item to show up as a filler item.
    """

    rich_text_doc = True

    min = 0
    max = 100

    default = {
        "50 Coins": 50,
    }

    valid_keys = default.keys()

class DeathLink(Toggle):
    """
    Toggles Deathlink
    """

    display_name = "Deathlink"

    default = False

    visibility = Visibility.all

# Goal Options
class GoalType(Choice):
    """

    This selection determines what goal the player needs to aim for.

    - **count:** Complete GoalEnding number of unique endings [Not Implemented]
    - **urban:** Complete any urban ending once
    - **true_urban:** Complete true urban ending once

    """

    display_name = "Goal"

    rich_text_doc = True
    option_count = 0
    option_urban = 1
    option_true_urban = 2

    default = 2

class GoalEndings(Range):
    """
    GoalEndings is the number of unique endings that need to be completed if goal is set to count
    """

    display_name = "Goal: Endings"

    range_start = 1
    range_end = 9
    default = 1

    visibility = Visibility.none

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class IslandKingOptions(PerGameCommonOptions):
    # Extra item options.
    filler_item_distribution: FillerItemDistribution

    deathlink: DeathLink

    goal_type: GoalType
    goal_endings: GoalEndings