# OthersService

A list of all methods in the `OthersService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                                |
| :---------------------------------------------------------- | :----------------------------------------------------------------------------------------- |
| [sports_v2_get](#sports_v2_get)                             | Returns all sports with the status whether they currently have lines or not.               |
| [leagues_v2_get](#leagues_v2_get)                           | Returns all sports leagues with the status whether they currently have lines or not.       |
| [periods_v1_get](#periods_v1_get)                           | Returns all periods for a given sport.                                                     |
| [in_running_v1_get](#in_running_v1_get)                     | Returns all live soccer events that have a status that indicates the event is in progress. |
| [teaser_groups_v1_get](#teaser_groups_v1_get)               | Returns all teaser groups.                                                                 |
| [cancellation_reasons_v1_get](#cancellation_reasons_v1_get) | Lookup for all the cancellation reasons                                                    |
| [currencies_v2_get](#currencies_v2_get)                     | Returns the list of supported currencies                                                   |

## sports_v2_get

Returns all sports with the status whether they currently have lines or not.

- HTTP Method: `GET`
- Endpoint: `/v2/sports`

**Return Type**

`SportsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.sports_v2_get()

print(result)
```

## leagues_v2_get

Returns all sports leagues with the status whether they currently have lines or not.

- HTTP Method: `GET`
- Endpoint: `/v2/leagues`

**Parameters**

| Name     | Type | Required | Description                                   |
| :------- | :--- | :------- | :-------------------------------------------- |
| sport_id | str  | ✅       | Sport id for which the leagues are requested. |

**Return Type**

`Leagues`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.leagues_v2_get(sport_id="sportId")

print(result)
```

## periods_v1_get

Returns all periods for a given sport.

- HTTP Method: `GET`
- Endpoint: `/v1/periods`

**Parameters**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| sport_id | str  | ✅       |             |

**Return Type**

`SportPeriod`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.periods_v1_get(sport_id="sportId")

print(result)
```

## in_running_v1_get

Returns all live soccer events that have a status that indicates the event is in progress.

- HTTP Method: `GET`
- Endpoint: `/v1/inrunning`

**Return Type**

`InRunningResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.in_running_v1_get()

print(result)
```

## teaser_groups_v1_get

Returns all teaser groups.

- HTTP Method: `GET`
- Endpoint: `/v1/teaser/groups`

**Parameters**

| Name        | Type                                                                    | Required | Description                                                                       |
| :---------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------- |
| odds_format | [TeaserGroupsV1GetOddsFormat](../models/TeaserGroupsV1GetOddsFormat.md) | ✅       | Format the odds are returned in. [American, Decimal, HongKong, Indonesian, Malay] |

**Return Type**

`TeaserGroupsResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment
from pinnacle_link.models import TeaserGroupsV1GetOddsFormat

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.teaser_groups_v1_get(odds_format="American")

print(result)
```

## cancellation_reasons_v1_get

Lookup for all the cancellation reasons

- HTTP Method: `GET`
- Endpoint: `/v1/cancellationreasons`

**Return Type**

`CancellationReasonResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.cancellation_reasons_v1_get()

print(result)
```

## currencies_v2_get

Returns the list of supported currencies

- HTTP Method: `GET`
- Endpoint: `/v2/currencies`

**Return Type**

`SuccessfulCurrenciesResponse`

**Example Usage Code Snippet**

```python
from pinnacle_link import PinnacleLink, Environment

sdk = PinnacleLink(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

result = sdk.others.currencies_v2_get()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
