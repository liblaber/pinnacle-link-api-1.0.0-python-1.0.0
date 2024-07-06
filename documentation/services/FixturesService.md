# FixturesService

A list of all methods in the `FixturesService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [fixtures_v1_get](#fixtures_v1_get)                                   | Returns all **non-settled** events for the given sport. Please note that it is possible that the event is in Get Fixtures response but not in Get Odds. This happens when the odds are not currently available for wagering. Please note that it is possible to receive the same exact response when using **since** parameter. This is rare and can be caused by internal updates of event properties. |
| [fixtures_special_v1_get](#fixtures_special_v1_get)                   | Returns all **non-settled** specials for the given sport.                                                                                                                                                                                                                                                                                                                                               |
| [fixtures_settled_v1_get](#fixtures_settled_v1_get)                   | Returns fixtures settled in the last 24 hours for the given sport.                                                                                                                                                                                                                                                                                                                                      |
| [fixtures_specials_settled_v1_get](#fixtures_specials_settled_v1_get) | Returns all specials which are settled in the last 24 hours for the given Sport.                                                                                                                                                                                                                                                                                                                        |

## fixtures_v1_get

Returns all **non-settled** events for the given sport. Please note that it is possible that the event is in Get Fixtures response but not in Get Odds. This happens when the odds are not currently available for wagering. Please note that it is possible to receive the same exact response when using **since** parameter. This is rare and can be caused by internal updates of event properties.

- HTTP Method: `GET`
- Endpoint: `/v1/fixtures`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                                                                              |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sport_id   | int       | ✅       | The sport id to retrieve the fixtures for.                                                                                                                                                                               |
| league_ids | List[int] | ❌       | The leagueIds array may contain a list of comma separated league ids.                                                                                                                                                    |
| is_live    | bool      | ❌       | To retrieve ONLY live events set the value to 1 (isLive=1). Missing or any other value will result in retrieval of events regardless of their Live status.                                                               |
| since      | int       | ❌       | This is used to receive incremental updates. Use the value of last from previous fixtures response. When since parameter is not provided, the fixtures are delayed up to 1 minute to encourage the use of the parameter. |
| event_ids  | List[int] | ❌       | Comma separated list of event ids to filter by                                                                                                                                                                           |

**Return Type**

`FixturesResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    3
]
event_ids=[
    3
]

result = sdk.fixtures.fixtures_v1_get(
    sport_id=6,
    league_ids=league_ids,
    is_live=True,
    since=9,
    event_ids=event_ids
)

print(result)
```

## fixtures_special_v1_get

Returns all **non-settled** specials for the given sport.

- HTTP Method: `GET`
- Endpoint: `/v1/fixtures/special`

**Parameters**

| Name       | Type      | Required | Description                                                                                                                                                                                                            |
| :--------- | :-------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sport_id   | int       | ✅       | Id of a sport for which to retrieve the specials.                                                                                                                                                                      |
| league_ids | List[int] | ❌       | The leagueIds array may contain a list of comma separated league ids.                                                                                                                                                  |
| since      | int       | ❌       | This is used to receive incremental updates. Use the value of last field from the previous response. When since parameter is not provided, the fixtures are delayed up to 1 min to encourage the use of the parameter. |
| category   | str       | ❌       | The category the special falls under.                                                                                                                                                                                  |
| event_id   | int       | ❌       | Id of an event associated with a special.                                                                                                                                                                              |
| special_id | int       | ❌       | Id of the special.                                                                                                                                                                                                     |

**Return Type**

`SpecialsFixturesResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    8
]

result = sdk.fixtures.fixtures_special_v1_get(
    sport_id=8,
    league_ids=league_ids,
    since=1,
    category="category",
    event_id=0,
    special_id=0
)

print(result)
```

## fixtures_settled_v1_get

Returns fixtures settled in the last 24 hours for the given sport.

- HTTP Method: `GET`
- Endpoint: `/v1/fixtures/settled`

**Parameters**

| Name       | Type      | Required | Description |
| :--------- | :-------- | :------- | :---------- |
| sport_id   | int       | ✅       |             |
| league_ids | List[int] | ❌       |             |
| since      | int       | ❌       |             |

**Return Type**

`SettledFixturesSport`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    1
]

result = sdk.fixtures.fixtures_settled_v1_get(
    sport_id=1,
    league_ids=league_ids,
    since=0
)

print(result)
```

## fixtures_specials_settled_v1_get

Returns all specials which are settled in the last 24 hours for the given Sport.

- HTTP Method: `GET`
- Endpoint: `/v1/fixtures/special/settled`

**Parameters**

| Name       | Type      | Required | Description                                                                                |
| :--------- | :-------- | :------- | :----------------------------------------------------------------------------------------- |
| sport_id   | int       | ✅       | Id of the sport for which to retrieve the settled specials.                                |
| league_ids | List[int] | ❌       | Array of leagueIds. This is optional parameter.                                            |
| since      | int       | ❌       | This is used to receive incremental updates. Use the value of last from previous response. |

**Return Type**

`SettledSpecialsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)
league_ids=[
    8
]

result = sdk.fixtures.fixtures_specials_settled_v1_get(
    sport_id=3,
    league_ids=league_ids,
    since=5
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
