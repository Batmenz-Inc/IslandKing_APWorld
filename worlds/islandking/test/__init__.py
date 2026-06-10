from typing import ClassVar

from rule_builder.rules import Rule
from test.bases import WorldTestBase

class IslandKingTestBase(WorldTestBase):
    game = "Island King"
    player: ClassVar[int] = 1