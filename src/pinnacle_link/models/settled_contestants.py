# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class Outcome(Enum):
    """An enumeration representing different categories.

    :cvar W: "W"
    :vartype W: str
    :cvar L: "L"
    :vartype L: str
    :cvar X: "X"
    :vartype X: str
    :cvar T: "T"
    :vartype T: str
    :cvar Z: "Z"
    :vartype Z: str
    """

    W = "W"
    L = "L"
    X = "X"
    T = "T"
    Z = "Z"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Outcome._member_map_.values()))


@JsonMap({"id_": "id"})
class SettledContestants(BaseModel):
    """Settled Special

    :param id_: Contestant identifier, defaults to None
    :type id_: int, optional
    :param name: Contestant name, defaults to None
    :type name: str, optional
    :param outcome: Contestant outcomes W =  Won, L = Lost,  X = Cancelled, T = Tie, Z = Scratched , defaults to None
    :type outcome: Outcome, optional
    """

    def __init__(self, id_: int = None, name: str = None, outcome: Outcome = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if outcome is not None:
            self.outcome = self._enum_matching(outcome, Outcome.list(), "outcome")
