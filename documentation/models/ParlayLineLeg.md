# ParlayLineLeg

**Properties**

| Name            | Type                   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------- | :--------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status          | ParlayLineLegStatus    | ✅       | Status of the request. [VALID = Valid leg, PROCESSED_WITH_ERROR = Processed with error]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| leg_id          | str                    | ✅       | Echo of the legId from the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| error_code      | ParlayLineLegErrorCode | ❌       | When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. CORRELATED - The leg is correlated with another one, CANNOT_PARLAY_LIVE_GAME - The wager is placed on Live game, EVENT_NO_LONGER_AVAILABLE_FOR_BETTING - The event is no longer offered for Parlays, EVENT_NOT_OFFERED_FOR_PARLAY - The event is not offered for Parlays, LINE_DOES_NOT_BELONG_TO_EVENT - LineId does not match the EventId specified in the request, WAGER_TYPE_NO_LONGER_AVAILABLE_FOR_BETTING - Wager Type no longer available for betting, WAGER_TYPE_NOT_VALID_FOR_PARLAY - Wager Type not valid for parlay, WAGER_TYPE_CONFLICTS_WITH_OTHER_LEG - Wager Type conflicts with other leg SAME_EVENT_PERIODS_ARE_DISALLOWED - It's not allowed to parlay selected periods of the same event. |
| line_id         | int                    | ❌       | Line identification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| alt_line_id     | int                    | ❌       | If alternate Line was requested, the Id of that line will be returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| price           | float                  | ❌       | Price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| correlated_legs | List[str]              | ❌       | If errorCode is CORRELATED will contain legIds of all correlated legs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

# ParlayLineLegStatus

Status of the request. [VALID = Valid leg, PROCESSED_WITH_ERROR = Processed with error]

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| VALID                | str  | ✅       | "VALID"                |
| PROCESSED_WITH_ERROR | str  | ✅       | "PROCESSED_WITH_ERROR" |

# ParlayLineLegErrorCode

When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem.

CORRELATED - The leg is correlated with another one,  
 CANNOT_PARLAY_LIVE_GAME - The wager is placed on Live game,  
 EVENT_NO_LONGER_AVAILABLE_FOR_BETTING - The event is no longer offered for Parlays,  
 EVENT_NOT_OFFERED_FOR_PARLAY - The event is not offered for Parlays,  
 LINE_DOES_NOT_BELONG_TO_EVENT - LineId does not match the EventId specified in the request,  
 WAGER_TYPE_NO_LONGER_AVAILABLE_FOR_BETTING - Wager Type no longer available for betting,
WAGER_TYPE_NOT_VALID_FOR_PARLAY - Wager Type not valid for parlay,  
 WAGER_TYPE_CONFLICTS_WITH_OTHER_LEG - Wager Type conflicts with other leg
SAME_EVENT_PERIODS_ARE_DISALLOWED - It's not allowed to parlay selected periods of the same event.

**Properties**

| Name                                       | Type | Required | Description                                  |
| :----------------------------------------- | :--- | :------- | :------------------------------------------- |
| CORRELATED                                 | str  | ✅       | "CORRELATED"                                 |
| CANNOT_PARLAY_LIVE_GAME                    | str  | ✅       | "CANNOT_PARLAY_LIVE_GAME"                    |
| EVENT_NO_LONGER_AVAILABLE_FOR_BETTING      | str  | ✅       | "EVENT_NO_LONGER_AVAILABLE_FOR_BETTING"      |
| EVENT_NOT_OFFERED_FOR_PARLAY               | str  | ✅       | "EVENT_NOT_OFFERED_FOR_PARLAY"               |
| LINE_DOES_NOT_BELONG_TO_EVENT              | str  | ✅       | "LINE_DOES_NOT_BELONG_TO_EVENT"              |
| WAGER_TYPE_NO_LONGER_AVAILABLE_FOR_BETTING | str  | ✅       | "WAGER_TYPE_NO_LONGER_AVAILABLE_FOR_BETTING" |
| WAGER_TYPE_NOT_VALID_FOR_PARLAY            | str  | ✅       | "WAGER_TYPE_NOT_VALID_FOR_PARLAY"            |
| WAGER_TYPE_CONFLICTS_WITH_OTHER_LEG        | str  | ✅       | "WAGER_TYPE_CONFLICTS_WITH_OTHER_LEG"        |
| SAME_EVENT_PERIODS_ARE_DISALLOWED          | str  | ✅       | "SAME_EVENT_PERIODS_ARE_DISALLOWED"          |

<!-- This file was generated by liblab | https://liblab.com/ -->
