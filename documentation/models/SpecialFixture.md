# SpecialFixture

**Properties**

| Name        | Type                             | Required | Description                                                                                                                                                                                                                                                                                                                                       |
| :---------- | :------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_        | int                              | ❌       | Unique Id                                                                                                                                                                                                                                                                                                                                         |
| bet_type    | SpecialFixtureBetType            | ❌       | The type [MULTI_WAY_HEAD_TO_HEAD, SPREAD, OVER_UNDER]                                                                                                                                                                                                                                                                                             |
| name        | str                              | ❌       | Name of the special.                                                                                                                                                                                                                                                                                                                              |
| date\_      | str                              | ❌       | Date of the special in UTC.                                                                                                                                                                                                                                                                                                                       |
| cutoff      | str                              | ❌       | Wagering cutoff date in UTC.                                                                                                                                                                                                                                                                                                                      |
| category    | str                              | ❌       | The category that the special falls under.                                                                                                                                                                                                                                                                                                        |
| units       | str                              | ❌       | Measurment in the context of the special. This is applicable to specials bet type spead and over/under. In a hockey special this could be goals.                                                                                                                                                                                                  |
| status      | SpecialFixtureStatus             | ❌       | Status of the Special O = This is the starting status. It means that the lines are open for betting, H = This status indicates that the lines are temporarily unavailable for betting, I = This status indicates that one or more lines have a red circle (a lower maximum bet amount)                                                            |
| event       | SpecialsFixturesEvent            | ❌       | Optional event asscoaited with the special.                                                                                                                                                                                                                                                                                                       |
| contestants | List[SpecialsFixturesContestant] | ❌       | ContestantLines available for wagering.                                                                                                                                                                                                                                                                                                           |
| live_status | SpecialFixtureLiveStatus         | ❌       | When a special is linked to an event, we will return live status of the event, otherwise it will be 0. 0 = No live betting will be offered on this event, 1 = Live betting event, 2 = Live betting will be offered on this match, but on a different event. Please note that live delay is applied when placing bets on special with LiveStatus=1 |

# SpecialFixtureBetType

The type [MULTI_WAY_HEAD_TO_HEAD, SPREAD, OVER_UNDER]

**Properties**

| Name                   | Type | Required | Description              |
| :--------------------- | :--- | :------- | :----------------------- |
| MULTI_WAY_HEAD_TO_HEAD | str  | ✅       | "MULTI_WAY_HEAD_TO_HEAD" |
| SPREAD                 | str  | ✅       | "SPREAD"                 |
| OVER_UNDER             | str  | ✅       | "OVER_UNDER"             |

# SpecialFixtureStatus

Status of the Special

O = This is the starting status. It means that the lines
are open for betting,

H = This status indicates that the lines are temporarily unavailable
for betting,

I = This status indicates that one or more lines have a red circle
(a lower maximum bet amount)

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| O    | str  | ✅       | "O"         |
| H    | str  | ✅       | "H"         |
| I    | str  | ✅       | "I"         |

# SpecialFixtureLiveStatus

When a special is linked to an event, we will return live status of the event, otherwise it will be 0.
0 = No live betting will be offered on this event,
1 = Live betting event,
2 = Live betting will be offered on this match, but on a different event.  
Please note that live delay is applied when placing bets on special with LiveStatus=1

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_0  | int  | ✅       | 0           |
| \_1  | int  | ✅       | 1           |
| \_2  | int  | ✅       | 2           |

<!-- This file was generated by liblab | https://liblab.com/ -->
