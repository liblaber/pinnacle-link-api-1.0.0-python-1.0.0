# Fixture

**Properties**

| Name                              | Type              | Required | Description                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------- | :---------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_                              | int               | ❌       | Event id.                                                                                                                                                                                                                                                                                                                                                       |
| parent_id                         | int               | ❌       | If event is linked to another event, parentId will be populated. Live event would have pre game event as parent id.                                                                                                                                                                                                                                             |
| starts                            | str               | ❌       | Start time of the event in UTC.                                                                                                                                                                                                                                                                                                                                 |
| home                              | str               | ❌       | Home team name.                                                                                                                                                                                                                                                                                                                                                 |
| away                              | str               | ❌       | Away team name.                                                                                                                                                                                                                                                                                                                                                 |
| rot_num                           | str               | ❌       | Team1 rotation number. Please note that in the next version of /fixtures, rotNum property will be decommissioned. ParentId can be used instead to group the related events.                                                                                                                                                                                     |
| live_status                       | FixtureLiveStatus | ❌       | Indicates live status of the event. 0 = No live betting will be offered on this event, 1 = Live betting event, 2 = Live betting will be offered on this match, but on a different event. Please note that [pre-game and live events are different](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-find-associated-events) . |
| status                            | FixtureStatus     | ❌       | This is deprecated parameter, please check period's `status` in the `/odds` endpoint to see if it's open for betting. O = This is the starting status of a game. H = This status indicates that the lines are temporarily unavailable for betting, I = This status indicates that one or more lines have a red circle (lower maximum bet amount).               |
| parlay_restriction                | ParlayRestriction | ❌       | &nbsp;Parlay status of the event. 0 = Allowed to parlay, without restrictions, 1 = Not allowed to parlay this event, 2 = Allowed to parlay with the restrictions. You cannot have more than one leg from the same event in the parlay. All events with the same rotation number are treated as same event.                                                      |
| alt_teaser                        | bool              | ❌       | Whether an event is offer with alternative teaser points. Events with alternative teaser points may vary from teaser definition.                                                                                                                                                                                                                                |
| resulting_unit                    | str               | ❌       | Specifies based on what the event will be resulted, e.g. Corners, Bookings                                                                                                                                                                                                                                                                                      |
| version                           | float             | ❌       | Fixture version, goes up when there is a change in the fixture.                                                                                                                                                                                                                                                                                                 |
| same_event_parlay_periods_enabled | List[int]         | ❌       | Contains a list of period numbers that are allowed to be parlayed together.                                                                                                                                                                                                                                                                                     |

# FixtureLiveStatus

Indicates live status of the event.

0 = No live betting will be offered on this event,
1 = Live betting event,
2 = Live betting will be offered on this match, but on a different event. Please note that [pre-game and live events are different](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-find-associated-events) .

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_0  | int  | ✅       | 0           |
| \_1  | int  | ✅       | 1           |
| \_2  | int  | ✅       | 2           |

# FixtureStatus

This is deprecated parameter, please check period's `status` in the
`/odds` endpoint to see if it's open for betting.

O = This is the starting status of a game.

H = This status indicates that the lines are temporarily unavailable
for betting,

I = This status indicates that one or more lines have a red circle
(lower maximum bet amount).

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| O    | str  | ✅       | "O"         |
| H    | str  | ✅       | "H"         |
| I    | str  | ✅       | "I"         |

# ParlayRestriction

Parlay status of the event.

0 = Allowed to parlay, without restrictions,
1 = Not allowed to parlay this event,
2 = Allowed to parlay with the restrictions. You cannot have more than one leg from the same event in the parlay. All events with the same rotation number are treated as same event.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_0  | int  | ✅       | 0           |
| \_1  | int  | ✅       | 1           |
| \_2  | int  | ✅       | 2           |

<!-- This file was generated by liblab | https://liblab.com/ -->
