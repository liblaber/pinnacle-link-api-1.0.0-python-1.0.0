# TeaserLinesResponse

**Properties**

| Name           | Type                         | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| :------------- | :--------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status         | TeaserLinesResponseStatus    | ✅       | Status of the request. [VALID = Teaser is valid, PROCESSED_WITH_ERROR = Teaser contains one or more errors]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| legs           | List[TeaserLineLeg]          | ✅       | Collection of Teaser Legs from the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| error_code     | TeaserLinesResponseErrorCode | ❌       | When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. INVALID_LEGS = One or more of the legs is invalid, SAME_EVENT_ONLY_REQUIRED = Teaser specified requires that all legs are from the same event, TEASER_DISABLED = Teaser has been disabled and cannot be bet on, TEASER_DOES_NOT_EXIST = The teaser identifier could not be found, TOO_FEW_LEGS = You do not meet the minimum number of legs requirement for the teaser specified, TOO_MANY_LEGS = You are above the maximum number of legs for the teaser specified, UNKNOWN = An unknown error has occurred |
| price          | float                        | ❌       | Price for the bet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| min_risk_stake | float                        | ❌       | Minimum bet amount for WIN_RISK_TYPE.RISK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| max_risk_stake | float                        | ❌       | Maximum bet amount for WIN_RISK_TYPE.RISK.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| min_win_stake  | float                        | ❌       | Minimum bet amount for WIN_RISK_TYPE.WIN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| max_win_stake  | float                        | ❌       | Maximum bet amount for WIN_RISK_TYPE.WIN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

# TeaserLinesResponseStatus

Status of the request. [VALID = Teaser is valid, PROCESSED_WITH_ERROR = Teaser contains one or more errors]

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| VALID                | str  | ✅       | "VALID"                |
| PROCESSED_WITH_ERROR | str  | ✅       | "PROCESSED_WITH_ERROR" |

# TeaserLinesResponseErrorCode

When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem.

INVALID_LEGS = One or more of the legs is invalid,
SAME_EVENT_ONLY_REQUIRED = Teaser specified requires that all legs are from the same event,  
 TEASER_DISABLED = Teaser has been disabled and cannot be bet on,  
 TEASER_DOES_NOT_EXIST = The teaser identifier could not be found,  
 TOO_FEW_LEGS = You do not meet the minimum number of legs requirement for the teaser specified,  
 TOO_MANY_LEGS = You are above the maximum number of legs for the teaser specified,  
 UNKNOWN = An unknown error has occurred

**Properties**

| Name                     | Type | Required | Description                |
| :----------------------- | :--- | :------- | :------------------------- |
| INVALID_LEGS             | str  | ✅       | "INVALID_LEGS"             |
| SAME_EVENT_ONLY_REQUIRED | str  | ✅       | "SAME_EVENT_ONLY_REQUIRED" |
| TEASER_DISABLED          | str  | ✅       | "TEASER_DISABLED"          |
| TEASER_DOES_NOT_EXIST    | str  | ✅       | "TEASER_DOES_NOT_EXIST"    |
| TOO_FEW_LEGS             | str  | ✅       | "TOO_FEW_LEGS"             |
| TOO_MANY_LEGS            | str  | ✅       | "TOO_MANY_LEGS"            |
| UNKNOWN                  | str  | ✅       | "UNKNOWN"                  |

<!-- This file was generated by liblab | https://liblab.com/ -->
