# InRunningEvent

**Properties**

| Name    | Type  | Required | Description                                                                                                                                                                                                                                                                                                                                               |
| :------ | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_    | int   | ❌       | Game Id                                                                                                                                                                                                                                                                                                                                                   |
| state   | State | ❌       | State of the game. 1 = First half in progress, 2 = Half time in progress, 3 = Second half in progress, 4 = End of regular time, 5 = First half extra time in progress, 6 = Extra time half time in progress, 7 = Second half extra time in progress, 8 = End of extra time, 9 = End of Game, 10 = Game is temporary suspended, 11 = Penalties in progress |
| elapsed | int   | ❌       | Elapsed minutes                                                                                                                                                                                                                                                                                                                                           |

# State

State of the game.

1 = First half in progress,
2 = Half time in progress,
3 = Second half in progress,
4 = End of regular time,
5 = First half extra time in progress,
6 = Extra time half time in progress,
7 = Second half extra time in progress,
8 = End of extra time,
9 = End of Game,
10 = Game is temporary suspended,
11 = Penalties in progress

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_1  | int  | ✅       | 1           |
| \_2  | int  | ✅       | 2           |
| \_3  | int  | ✅       | 3           |
| \_4  | int  | ✅       | 4           |
| \_5  | int  | ✅       | 5           |
| \_6  | int  | ✅       | 6           |
| \_7  | int  | ✅       | 7           |
| \_8  | int  | ✅       | 8           |
| \_9  | int  | ✅       | 9           |
| \_10 | int  | ✅       | 10          |
| \_11 | int  | ✅       | 11          |

<!-- This file was generated by liblab | https://liblab.com/ -->
