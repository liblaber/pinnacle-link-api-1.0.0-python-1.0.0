# SettledFixturesPeriod

**Properties**

| Name                | Type                        | Required | Description                                                                                                                                                                             |
| :------------------ | :-------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| number              | int                         | ❌       | This represents the period of the match.                                                                                                                                                |
| status              | SettledFixturesPeriodStatus | ❌       | Period settlement status. 1 = Event period is settled, 2 = Event period is re-settled, 3 = Event period is cancelled, 4 = Event period is re-settled as cancelled, 5 = Event is deleted |
| settlement_id       | int                         | ❌       | Unique id of the settlement. In case of a re-settlement, a new settlementId and settledAt will be generated.                                                                            |
| settled_at          | str                         | ❌       | Date and time in UTC when the period was settled.                                                                                                                                       |
| team1_score         | int                         | ❌       | Team1 score.                                                                                                                                                                            |
| team2_score         | int                         | ❌       | Team2 score.                                                                                                                                                                            |
| team1_score_sets    | int                         | ❌       | Team1 sets score. Supported for tennis only.                                                                                                                                            |
| team2_score_sets    | int                         | ❌       | Team2 sets score. Supported for tennis only.                                                                                                                                            |
| cancellation_reason | CancellationReasonType      | ❌       |                                                                                                                                                                                         |

# SettledFixturesPeriodStatus

Period settlement status.

1 = Event period is settled,
2 = Event period is re-settled,
3 = Event period is cancelled,
4 = Event period is re-settled as cancelled,
5 = Event is deleted

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_1  | int  | ✅       | 1           |
| \_2  | int  | ✅       | 2           |
| \_3  | int  | ✅       | 3           |
| \_4  | int  | ✅       | 4           |
| \_5  | int  | ✅       | 5           |

<!-- This file was generated by liblab | https://liblab.com/ -->