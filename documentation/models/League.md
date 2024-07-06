# League

**Properties**

| Name                  | Type | Required | Description                                                                                  |
| :-------------------- | :--- | :------- | :------------------------------------------------------------------------------------------- |
| id\_                  | int  | ❌       | League Id.                                                                                   |
| name                  | str  | ❌       | Name of the league.                                                                          |
| home_team_type        | str  | ❌       | Specifies whether the home team is team1 or team2. You need this information to place a bet. |
| has_offerings         | bool | ❌       | Whether the league currently has events or specials.                                         |
| container             | str  | ❌       | Represents grouping for the league, usually a region/country                                 |
| allow_round_robins    | bool | ❌       | Specifies whether you can place parlay round robins on events in this league.                |
| league_specials_count | int  | ❌       | Indicates how many specials are in the given league.                                         |
| event_specials_count  | int  | ❌       | Indicates how many game specials are in the given league.                                    |
| event_count           | int  | ❌       | Indicates how many events are in the given league.                                           |

<!-- This file was generated by liblab | https://liblab.com/ -->