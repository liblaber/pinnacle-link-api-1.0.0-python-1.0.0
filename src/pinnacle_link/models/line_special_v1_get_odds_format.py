# This file was generated by liblab | https://liblab.com/

from enum import Enum


class LineSpecialV1GetOddsFormat(Enum):
    """An enumeration representing different categories.

    :cvar AMERICAN: "American"
    :vartype AMERICAN: str
    :cvar DECIMAL: "Decimal"
    :vartype DECIMAL: str
    :cvar HONGKONG: "HongKong"
    :vartype HONGKONG: str
    :cvar INDONESIAN: "Indonesian"
    :vartype INDONESIAN: str
    :cvar MALAY: "Malay"
    :vartype MALAY: str
    """

    AMERICAN = "American"
    DECIMAL = "Decimal"
    HONGKONG = "HongKong"
    INDONESIAN = "Indonesian"
    MALAY = "Malay"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LineSpecialV1GetOddsFormat._member_map_.values())
        )
