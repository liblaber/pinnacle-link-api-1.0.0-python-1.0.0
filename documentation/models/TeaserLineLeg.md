# TeaserLineLeg

**Properties**

| Name       | Type                   | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :--------- | :--------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status     | TeaserLineLegStatus    | ✅       | Status of the request. [VALID = Teaser is valid, PROCESSED_WITH_ERROR = Teaser contains error(s)]                                                                                                                                                                                                                                                                                                                                                  |
| leg_id     | str                    | ✅       | Echo of the unique id for the leg from the request.                                                                                                                                                                                                                                                                                                                                                                                                |
| error_code | TeaserLineLegErrorCode | ❌       | When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. EVENT_NOT_FOUND - The event specified could not be found, POINTS_NO_LONGER_AVAILABLE - The points requested are no longer available. This means that the lines moved, UNKNOWN - An unknown error has occured, WAGER_TYPE_NOT_VALID_FOR_TEASER - The specified wager type is not valid for teasers GAME_TEASER_DISABLED - Teasers are disabled for the event. |
| line_id    | int                    | ❌       | Line identification.                                                                                                                                                                                                                                                                                                                                                                                                                               |

# TeaserLineLegStatus

Status of the request. [VALID = Teaser is valid, PROCESSED_WITH_ERROR = Teaser contains error(s)]

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| VALID                | str  | ✅       | "VALID"                |
| PROCESSED_WITH_ERROR | str  | ✅       | "PROCESSED_WITH_ERROR" |

# TeaserLineLegErrorCode

When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem.

EVENT_NOT_FOUND - The event specified could not be found,  
 POINTS_NO_LONGER_AVAILABLE - The points requested are no longer available. This means that the lines moved,  
 UNKNOWN - An unknown error has occured,  
 WAGER_TYPE_NOT_VALID_FOR_TEASER - The specified wager type is not valid for teasers  
 GAME_TEASER_DISABLED - Teasers are disabled for the event.

**Properties**

| Name                            | Type | Required | Description                       |
| :------------------------------ | :--- | :------- | :-------------------------------- |
| EVENT_NOT_FOUND                 | str  | ✅       | "EVENT_NOT_FOUND"                 |
| POINTS_NO_LONGER_AVAILABLE      | str  | ✅       | "POINTS_NO_LONGER_AVAILABLE"      |
| UNKNOWN                         | str  | ✅       | "UNKNOWN"                         |
| WAGER_TYPE_NOT_VALID_FOR_TEASER | str  | ✅       | "WAGER_TYPE_NOT_VALID_FOR_TEASER" |
| GAME_TEASER_DISABLED            | str  | ✅       | "GAME_TEASER_DISABLED"            |

<!-- This file was generated by liblab | https://liblab.com/ -->