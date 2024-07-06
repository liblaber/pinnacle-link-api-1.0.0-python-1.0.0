# LineService

A list of all methods in the `LineService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                               |
| :-------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| [line_straight_v1_get](#line_straight_v1_get) | Returns latest line.                                                                                      |
| [line_parlay_v2_post](#line_parlay_v2_post)   | Returns parlay lines and calculate odds. For placing round robin bets, must be used with /v2/bets/parlay. |
| [line_teaser_v1_post](#line_teaser_v1_post)   | Validates a teaser bet prior to submission. Returns bet limit and price on success.                       |
| [line_special_v1_get](#line_special_v1_get)   | Returns special lines and calculate odds.                                                                 |

## line_straight_v1_get

Returns latest line.

- HTTP Method: `GET`
- Endpoint: `/v1/line`

**Parameters**

| Name          | Type                                                                    | Required | Description                                                                                                                       |
| :------------ | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| league_id     | int                                                                     | ✅       | League Id.                                                                                                                        |
| handicap      | float                                                                   | ✅       | This is needed for SPREAD, TOTAL_POINTS and TEAM_TOTAL_POINTS bet types                                                           |
| odds_format   | [LineStraightV1GetOddsFormat](../models/LineStraightV1GetOddsFormat.md) | ✅       | Format in which we return the odds. Default is American.                                                                          |
| sport_id      | int                                                                     | ✅       | Sport identification                                                                                                              |
| event_id      | int                                                                     | ✅       | Event identification                                                                                                              |
| period_number | int                                                                     | ✅       | This represents the period of the match. Please check Get Periods endpoint for the list of currently supported periods per sport. |
| bet_type      | [LineStraightV1GetBetType](../models/LineStraightV1GetBetType.md)       | ✅       | Bet Type                                                                                                                          |
| team          | [LineStraightV1GetTeam](../models/LineStraightV1GetTeam.md)             | ❌       | Chosen team type. This is needed only for SPREAD, MONEYLINE and TEAM_TOTAL_POINTS bet types                                       |
| side          | [LineStraightV1GetSide](../models/LineStraightV1GetSide.md)             | ❌       | Chosen side. This is needed only for TOTAL_POINTS and TEAM_TOTAL_POINTS                                                           |

**Return Type**

`LineResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import LineStraightV1GetOddsFormat, LineStraightV1GetBetType, LineStraightV1GetTeam, LineStraightV1GetSide

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.line.line_straight_v1_get(
    league_id=1,
    handicap=4.58,
    odds_format="American",
    sport_id=0,
    event_id=1,
    period_number=0,
    bet_type="SPREAD",
    team="Team1",
    side="OVER"
)

print(result)
```

## line_parlay_v2_post

Returns parlay lines and calculate odds. For placing round robin bets, must be used with /v2/bets/parlay.

- HTTP Method: `POST`
- Endpoint: `/v2/line/parlay`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [ParlayLinesRequest](../models/ParlayLinesRequest.md) | ✅       | The request body. |

**Return Type**

`ParlayLinesResponseV2`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import ParlayLinesRequest

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = ParlayLinesRequest(
    odds_format="American",
    legs=[
        {
            "unique_leg_id": "uniqueLegId",
            "event_id": 0,
            "period_number": 3,
            "leg_bet_type": "SPREAD",
            "team": "Team1",
            "side": "OVER",
            "handicap": 8.22
        }
    ]
)

result = sdk.line.line_parlay_v2_post(request_body=request_body)

print(result)
```

## line_teaser_v1_post

Validates a teaser bet prior to submission. Returns bet limit and price on success.

- HTTP Method: `POST`
- Endpoint: `/v1/line/teaser`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [LinesRequestTeaser](../models/LinesRequestTeaser.md) | ✅       | The request body. |

**Return Type**

`TeaserLinesResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import LinesRequestTeaser

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = LinesRequestTeaser(
    teaser_id=6,
    odds_format="American",
    legs=[
        {
            "leg_id": "legId",
            "event_id": 1,
            "period_number": 7,
            "bet_type": "SPREAD",
            "team": "Team1",
            "side": "OVER",
            "handicap": 0.14
        }
    ]
)

result = sdk.line.line_teaser_v1_post(request_body=request_body)

print(result)
```

## line_special_v1_get

Returns special lines and calculate odds.

- HTTP Method: `GET`
- Endpoint: `/v1/line/special`

**Parameters**

| Name          | Type                                                                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :------------ | :-------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| odds_format   | [LineSpecialV1GetOddsFormat](../models/LineSpecialV1GetOddsFormat.md) | ✅       | Format the odds are returned in. [American, Decimal, HongKong, Indonesian, Malay]                                                                                                                                                                                                                                                                                                                                                      |
| special_id    | int                                                                   | ✅       | Id of the special.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| contestant_id | int                                                                   | ✅       | Id of the contestant.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| handicap      | int                                                                   | ❌       | handicap of the contestant. As contestant's handicap is a mutable property, it may happened that line/special returns status:SUCCESS, but with the different handicap from the one that client had at the moment of calling the line/special. One can specify handicap parameter in the request and if the contestant's handicap changed, it would return status:NOT_EXISTS. This way line/special is more aligned to how /line works. |

**Return Type**

`SpecialLineResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import LineSpecialV1GetOddsFormat

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.line.line_special_v1_get(
    odds_format="American",
    special_id=4,
    contestant_id=2,
    handicap=5
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
