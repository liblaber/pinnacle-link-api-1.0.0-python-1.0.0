# RoundRobinOptionWithOddsV2

**Properties**

| Name                   | Type             | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :--------------------- | :--------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| round_robin_option     | RoundRobinOption | ✅       | RoundRobinOptions Parlay = Single parlay that include all wagers (No Round Robin), TwoLegRoundRobin = Multiple parlays having 2 wagers each (round robin style), ThreeLegRoundRobin = Multiple parlays having 3 wagers each (round robin style), FourLegRoundRobin = Multiple parlays having 4 wagers each (round robin style), FiveLegRoundRobin = Multiple parlays having 5 wagers each (round robin style), SixLegRoundRobin = Multiple parlays having 6 wagers each (round robin style), SevenLegRoundRobin = Multiple parlays having 7 wagers each (round robin style), EightLegRoundRobin = Multiple parlays having 8 wagers each (round robin style) |
| odds                   | float            | ✅       | Parlay odds for this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| unrounded_decimal_odds | float            | ✅       | Unrounded parlay odds in decimal format to be used for calculations only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| number_of_bets         | float            | ❌       | Number of bets in the roundRobinOption.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

# RoundRobinOption

RoundRobinOptions

Parlay = Single parlay that include all wagers (No Round Robin),  
 TwoLegRoundRobin = Multiple parlays having 2 wagers each (round robin style),  
 ThreeLegRoundRobin = Multiple parlays having 3 wagers each (round robin style),  
 FourLegRoundRobin = Multiple parlays having 4 wagers each (round robin style),  
 FiveLegRoundRobin = Multiple parlays having 5 wagers each (round robin style),  
 SixLegRoundRobin = Multiple parlays having 6 wagers each (round robin style),  
 SevenLegRoundRobin = Multiple parlays having 7 wagers each (round robin style),  
 EightLegRoundRobin = Multiple parlays having 8 wagers each (round robin style)

**Properties**

| Name               | Type | Required | Description          |
| :----------------- | :--- | :------- | :------------------- |
| PARLAY             | str  | ✅       | "Parlay"             |
| TWOLEGROUNDROBIN   | str  | ✅       | "TwoLegRoundRobin"   |
| THREELEGROUNDROBIN | str  | ✅       | "ThreeLegRoundRobin" |
| FOURLEGROUNDROBIN  | str  | ✅       | "FourLegRoundRobin"  |
| FIVELEGROUNDROBIN  | str  | ✅       | "FiveLegRoundRobin"  |
| SIXLEGROUNDROBIN   | str  | ✅       | "SixLegRoundRobin"   |
| SEVENLEGROUNDROBIN | str  | ✅       | "SevenLegRoundRobin" |
| EIGHTLEGROUNDROBIN | str  | ✅       | "EightLegRoundRobin" |

<!-- This file was generated by liblab | https://liblab.com/ -->
