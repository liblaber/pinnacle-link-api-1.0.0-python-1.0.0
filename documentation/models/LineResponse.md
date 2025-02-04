# LineResponse

**Properties**

| Name                   | Type               | Required | Description                                                                                                                                                              |
| :--------------------- | :----------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status                 | LineResponseStatus | ❌       | If the value is NOT_EXISTS, than this will be the only parameter in the response. All other params would be empty. [SUCCESS = OK, NOT_EXISTS = Line not offered anymore] |
| price                  | float              | ❌       | Latest price.                                                                                                                                                            |
| line_id                | int                | ❌       | Line identification needed to place a bet.                                                                                                                               |
| alt_line_id            | int                | ❌       | This would be needed to place the bet if the handicap is on alternate line, otherwise it will not be populated in the response.                                          |
| team1_score            | int                | ❌       | Team 1 score for the period 0. Applicable to soccer only.                                                                                                                |
| team2_score            | int                | ❌       | Team 2 score for the period 0. Applicable to soccer only.                                                                                                                |
| team1_red_cards        | int                | ❌       | Team 1 red cards for the period 0. Applicable to soccer only.                                                                                                            |
| team2_red_cards        | int                | ❌       | Team 2 red cards for the period 0. Applicable to soccer only.                                                                                                            |
| max_risk_stake         | float              | ❌       | Maximum bettable risk amount.                                                                                                                                            |
| min_risk_stake         | float              | ❌       | Minimum bettable risk amount.                                                                                                                                            |
| max_win_stake          | float              | ❌       | Maximum bettable win amount.                                                                                                                                             |
| min_win_stake          | float              | ❌       | Minimum bettable win amount.                                                                                                                                             |
| effective_as_of        | str                | ❌       | Line is effective as of this date and time in UTC.                                                                                                                       |
| period_team1_score     | int                | ❌       | Team 1 score for the supported periods. Applicable to soccer only.                                                                                                       |
| period_team2_score     | int                | ❌       | Team 2 score for the supported periods. Applicable to soccer only.                                                                                                       |
| period_team1_red_cards | int                | ❌       | Team 1 red cards for the supported periods. Applicable to soccer only.                                                                                                   |
| period_team2_red_cards | int                | ❌       | Team 2 red cards for the supported periods. Applicable to soccer only.                                                                                                   |

# LineResponseStatus

If the value is NOT_EXISTS, than this will be the only parameter in the response. All other params would be empty. [SUCCESS = OK, NOT_EXISTS = Line not offered anymore]

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| SUCCESS    | str  | ✅       | "SUCCESS"    |
| NOT_EXISTS | str  | ✅       | "NOT_EXISTS" |

<!-- This file was generated by liblab | https://liblab.com/ -->
