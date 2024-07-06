# OddsService

A list of all methods in the `OddsService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                            |
| :-------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [odds_straight_v1_get](#odds_straight_v1_get) | Returns straight odds for all non-settled events. Please note that it is possible that the event is in Get Fixtures response but not in Get Odds. This happens when the odds are not currently available for wagering. |
| [odds_teasers_v1_get](#odds_teasers_v1_get)   | Returns odds for specified teaser.                                                                                                                                                                                     |
| [odds_special_v1_get](#odds_special_v1_get)   | Returns odds for specials for all non-settled events.                                                                                                                                                                  |

## odds_straight_v1_get

Returns straight odds for all non-settled events. Please note that it is possible that the event is in Get Fixtures response but not in Get Odds. This happens when the odds are not currently available for wagering.

- HTTP Method: `GET`
- Endpoint: `/v1/odds`

**Parameters**

| Name             | Type                                                                    | Required | Description                                                                                                                                                                                                                                                                                                                                                                       |
| :--------------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sport_id         | int                                                                     | ✅       | The sportid for which to retrieve the odds.                                                                                                                                                                                                                                                                                                                                       |
| league_ids       | List[int]                                                               | ❌       | The leagueIds array may contain a list of comma separated league ids.                                                                                                                                                                                                                                                                                                             |
| odds_format      | [OddsStraightV1GetOddsFormat](../models/OddsStraightV1GetOddsFormat.md) | ❌       | Format in which we return the odds. Default is American. [American, Decimal, HongKong, Indonesian, Malay]                                                                                                                                                                                                                                                                         |
| since            | int                                                                     | ❌       | This is used to receive incremental updates. Use the value of last from previous odds response. When since parameter is not provided, the odds are delayed up to 1 min to encourage the use of the parameter. Please note that when using since parameter you will get in the response ONLY changed periods. If a period did not have any changes it will not be in the response. |
| is_live          | bool                                                                    | ❌       | To retrieve ONLY live odds set the value to 1 (isLive=1). Otherwise response will have all odds.                                                                                                                                                                                                                                                                                  |
| event_ids        | List[int]                                                               | ❌       | Filter by EventIds                                                                                                                                                                                                                                                                                                                                                                |
| to_currency_code | str                                                                     | ❌       | 3 letter currency code as in the [/currency](https://pinnacleapi.github.io/linesapi#operation/Currencies_V2_Get) response. Limits will be returned in the requested currency. Default is USD.                                                                                                                                                                                     |

**Return Type**

`OddsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import OddsStraightV1GetOddsFormat

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    9
]
event_ids=[
    1
]

result = sdk.odds.odds_straight_v1_get(
    sport_id=4,
    league_ids=league_ids,
    odds_format="American",
    since=9,
    is_live=True,
    event_ids=event_ids,
    to_currency_code="toCurrencyCode"
)

print(result)
```

## odds_teasers_v1_get

Returns odds for specified teaser.

- HTTP Method: `GET`
- Endpoint: `/v1/odds/teaser`

**Parameters**

| Name      | Type | Required | Description                                                                                  |
| :-------- | :--- | :------- | :------------------------------------------------------------------------------------------- |
| teaser_id | int  | ✅       | Unique identifier.Teaser details can be retrieved from a call to Get Teaser Groups endpoint. |

**Return Type**

`TeaserOddsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.odds.odds_teasers_v1_get(teaser_id=3)

print(result)
```

## odds_special_v1_get

Returns odds for specials for all non-settled events.

- HTTP Method: `GET`
- Endpoint: `/v1/odds/special`

**Parameters**

| Name        | Type                                                                  | Required | Description                                                                                                                                                                                                  |
| :---------- | :-------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sport_id    | int                                                                   | ✅       | Id of a sport for which to retrieve the specials.                                                                                                                                                            |
| odds_format | [OddsSpecialV1GetOddsFormat](../models/OddsSpecialV1GetOddsFormat.md) | ❌       | Format the odds are returned in. [American, Decimal, HongKong, Indonesian, Malay]                                                                                                                            |
| league_ids  | List[int]                                                             | ❌       | The leagueIds array may contain a list of comma separated league ids.                                                                                                                                        |
| since       | int                                                                   | ❌       | This is used to receive incremental updates. Use the value of last from previous response. When since parameter is not provided, the fixtures are delayed up to 1 min to encourage the use of the parameter. |
| special_id  | int                                                                   | ❌       | Id of the special. This is an optional argument.                                                                                                                                                             |

**Return Type**

`SpecialOddsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import OddsSpecialV1GetOddsFormat

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    2
]

result = sdk.odds.odds_special_v1_get(
    sport_id=1,
    odds_format="American",
    league_ids=league_ids,
    since=9,
    special_id=10
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
