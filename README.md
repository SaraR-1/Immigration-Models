# Immigration-Models
The aim of this chapter is to model the immigrant flow across the Italian territory. Thus, working with *data panel* is necessary. Data panel, or longitudinal data, refers to a set of *I* units surveyed repeatedly over *T* times. The notation ![](https://latex.codecogs.com/gif.latex?Y_%7Bi%2Ct%7D) denotes the variable ![](https://latex.codecogs.com/gif.latex?Y) observed for the ![](https://latex.codecogs.com/gif.latex?i)-th unit at time ![](https://latex.codecogs.com/gif.latex?t).

## Variable selection
On the [ISTAT website](http://dati.istat.it/#), it is possible to find some interesting features that could be included in the formulation of a model aim to explain the immigration flow to Italy.

To begin, an initial data filtering is performed. Only the data that are supposed to have a relation with the variable of interest are considered.

Some features can not be used, due to the availability of data:
- **Basic health care** only 2004-2013
- **Expenditure for intervections and social services** only 2013-2014
- **Expenditure for the house of families with foreign components** only 2009
- **Aspect of dayli life - Interpersonal Trust** only from 2010
- **Hospitalizations** missing 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2016, 2017
- **Aspects of daily life - general life degree of satisfaction** missing 2003, 2004, 2005, 2006, 2007, 2008, 2009

Some others, due to statistical problems:
- **Economic situation opinions (Famigie per capacità di arrivare a fine mese)**: around 10.4% of data are not statistically significant and 4.6% do not reach the half of the minimum (ISTAT definition: Il dato si definisce poco significativo nel caso in cui corrisponda ad una numerosità campionaria compresa tra 20 e 49 unità.)

In order to see the relationship between the Immigrant flow and other additional features, let's plot them. The zone level is sufficient to understand the behaviour.

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_population_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_social_act1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_political_info1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_consumption_expend_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_fertility_rate_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_disp_income_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_housing_costs2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_live_births_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_unemployment_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_work_satisfaction2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_reach_services_difficulty2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_internal_migration_zones.png)

Let's see also the "Area" variable which is time-invariant. Here as "Immigrant Stock" the mean over the years 2005-2015 is considered.
![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_time_invariant_regions.png)


Some variables like:
- Native population
- Difficulty to reach services (e.g. pharmacy)
- Housing costs
- Net Income
- Social activities
- Unemployment
seems to effect, somehow, one or more location-specific immigrant flow.

The others may be included in a regression model to see if they improve or not the prediction.

## Regression Model for Data Panel

In this section regression models for data panel are performed. The model is given by:

![](https://latex.codecogs.com/gif.latex?y_%7Bi%2Ct%7D%20%3D%20%5Cbeta%5ET%20x_%7Bi%2C%20t-1%7D%20&plus;%20%5Cepsilon_%7Bi%2C%20t%7D)

where:
- ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2Ct%7D) is the stock of foreign-born in territory ![](https://latex.codecogs.com/gif.latex?i) at time ![](https://latex.codecogs.com/gif.latex?t).
- ![](https://latex.codecogs.com/gif.latex?%5Cbeta) is the parameters vector.
- ![](https://latex.codecogs.com/gif.latex?x_%7Bi%2C%20t%7D) is the independent variables vector.

No unit-specific effect is used in the model, since it is assumed the randomness depends both on the time and the unit.

For each origin country, multiples regression models are trained using different independent variables:
- only the previous time stock;
- the previous two times stock;
- a set of 3, 5, 7, 10, 15 variables selected through the Mutual information criterion;
- the previous two times stock plus a set of seven features. The selection of the additional variables is based on the plots.

Each model is then trained:
-  on the whole period 2005-2016;
- on the period 2005-2013 and tested on the period 2014-2016.

The countries object of the study are:
- Romania;
- Morocco;
- Albania;
- Tunisia;
- Egypt;
- Ecuador;
- Peru;
- China;
- Philippines.

Follows the results of the models performed at Italian zones level.

Romania, Training 2006-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.081200 |  1.334000 |  0.799000 |  1.165300 |  0.877000 |  0.745700 |  0.663900 | 0.675900 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.282300 |  0.069100 |  -0.196800 |  -0.006800 |  0.024700 |  -0.007700 | -0.160600 |
| native population - Total | - |  - |  0.002100 |  - |  - |  - |  - | - |
| Free activities in voluntary associations | - |  - |  15.580300 |  - |  - |  - |  -62.712300 | -76.538200 |
| Meetings in cultural, recreational or other associations | - |  - |  -72.535600 |  - |  - |  - |  - | - |
| Disposable Income | - |  - |  17.876800 |  - |  7.641100 |  13.414500 |  20.605900 | 37.216000 |
| Average monthly expenditure for housing | - |  - |  1678.173700 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -153.797400 |  - |  -88.203200 |  -99.841500 |  -127.868400 | -169.664800 |
| reach_difficulty - Emergency room | - |  - |  -18.316400 |  - |  - |  - |  - | - |
| Average age of fathers at birth | - |  - |  - |  520.428300 |  109.418200 |  7375.524800 |  -24692.321500 | -64195.415900 |
| Communications | - |  - |  - |  - |  - |  -89.699400 |  235.638800 | 71.595400 |
| Average age of mothers at birth | - |  - |  - |  - |  - |  -8329.268300 |  27101.712800 | 71975.967500 |
| internal_migration - Foreign country | - |  - |  - |  - |  - |  - |  0.699700 | 1.160900 |
| Clothing and footwear | - |  - |  - |  - |  - |  - |  -153.154900 | -126.613300 |
| reach_difficulty - Pharmacy | - |  - |  - |  - |  - |  - |  - | -11.684400 |
| Born alive | - |  - |  - |  - |  - |  - |  - | -0.631100 |
| Other goods and services | - |  - |  - |  - |  - |  - |  - | -33.326300 |
| Transport | - |  - |  - |  - |  - |  - |  - | 54.550500 |
| political_info - Every day | - |  - |  - |  - |  - |  - |  - | -13.385800 |
| **R2** | 0.996300 |  0.996700 |  0.972300 |  0.996500 |  0.984600 |  0.984900 |  0.976700 | 0.974900 |
| **R2_adj** | 0.996000 |  0.996200 |  0.944700 |  0.995500 |  0.976000 |  0.969800 |  0.918400 | 1.351400 |
| **MAE** | 12282.847700 |  11605.668200 |  36255.202900 |  11309.191200 |  26215.767400 |  24672.924900 |  36891.122400 | 37232.851400 |
| **MPE** | -0.572900 |  -0.446000 |  23.500300 |  -3.850400 |  15.451200 |  13.704800 |  21.948300 | 22.635600 |
| **MAPE** | 5.156300 |  4.864500 |  23.500300 |  7.201000 |  15.451200 |  14.297400 |  21.948300 | 22.635600 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_romania__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_romania_2zones.png)

Morocco, Training 2006-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.036300 |  1.235100 |  0.963200 |  1.166400 |  1.213900 |  1.320300 |  1.349400 | 0.839700 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.208600 |  0.102700 |  -0.192900 |  -0.286900 |  -0.440000 |  -0.604700 | -0.244700 |
| native population - Total | - |  - |  0.004300 |  - |  0.000400 |  0.000500 |  0.004600 | -0.006900 |
| Free activities in voluntary associations | - |  - |  -3.343500 |  5.024900 |  -7.893400 |  4.711700 |  17.020300 | -4.838800 |
| Meetings in cultural, recreational or other associations | - |  - |  -20.964300 |  - |  - |  -6.946500 |  0.488400 | 20.856200 |
| Disposable Income | - |  - |  -2.378400 |  - |  - |  - |  - | 7.024200 |
| Average monthly expenditure for housing | - |  - |  523.648900 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -26.432600 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -2.596900 |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  - |  - |  - |  0.252100 |  0.343200 |  0.152300 | 0.275900 |
| Pay money to an association | - |  - |  - |  - |  - |  -5.020000 |  -12.174800 | 12.772300 |
| internal_migration - Italy | - |  - |  - |  - |  - |  - |  0.088300 | 0.201400 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  -37.306800 | -17.365900 |
| Free activities in non voluntary associations | - |  - |  - |  - |  - |  - |  -23.399900 | -76.306900 |
| Other goods and services | - |  - |  - |  - |  - |  - |  - | 35.215200 |
| Transport | - |  - |  - |  - |  - |  - |  - | -26.370800 |
| Non food | - |  - |  - |  - |  - |  - |  - | 3.069400 |
| political_info - Every day | - |  - |  - |  - |  - |  - |  - | -2.985600 |
| **R2** | 0.996700 |  0.997300 |  0.996200 |  0.997500 |  0.998800 |  0.998000 |  0.995900 | 0.954800 |
| **R2_adj** | 0.996400 |  0.996900 |  0.992400 |  0.996800 |  0.998100 |  0.996000 |  0.985600 | 1.632400 |
| **MAE** | 4486.943300 |  4099.887500 |  6013.020800 |  4278.618800 |  3003.125200 |  3285.453000 |  5418.167600 | 19895.411300 |
| **MPE** | -1.221000 |  -1.141900 |  7.706900 |  -3.195600 |  -0.308600 |  -3.544600 |  -4.788800 | 32.710300 |
| **MAPE** | 4.653500 |  4.301600 |  10.232200 |  4.991400 |  3.962500 |  3.862200 |  6.638400 | 32.710300 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_morocco__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_morocco_2zones.png)


Albania, Training 2006-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.042100 |  1.457300 |  1.213800 |  1.439700 |  1.334800 |  1.441300 |  1.460700 | 1.206400 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.438300 |  -0.169300 |  -0.431200 |  -0.394000 |  -0.531800 |  -0.578500 | -0.321700 |
| native population - Total | - |  - |  0.004200 |  0.000100 |  0.000600 |  0.001300 |  0.003300 | -0.003000 |
| Free activities in voluntary associations | - |  - |  8.667900 |  - |  - |  -23.356300 |  -29.850600 | 6.279500 |
| Meetings in cultural, recreational or other associations | - |  - |  -28.259000 |  - |  - |  - |  - | -39.665400 |
| Disposable Income | - |  - |  -2.265500 |  - |  -0.651300 |  -0.331200 |  0.199100 | -5.547300 |
| Average monthly expenditure for housing | - |  - |  565.312800 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -18.361600 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -5.328200 |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  - |  - |  - |  0.128500 |  0.448200 |  0.446900 | 0.519100 |
| political_info - Every day | - |  - |  - |  - |  - |  -0.492400 |  -0.395700 | 3.419300 |
| reach_difficulty - Pharmacy | - |  - |  - |  - |  - |  - |  0.812900 | -19.066500 |
| reach_difficulty - Supermarket | - |  - |  - |  - |  - |  - |  -2.357400 | -37.300200 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  -12.910300 | 37.080200 |
| reach_difficulty - Police, carabinieri | - |  - |  - |  - |  - |  - |  - | -21.471100 |
| Born alive | - |  - |  - |  - |  - |  - |  - | 1.226300 |
| political_info - Some times in a week | - |  - |  - |  - |  - |  - |  - | 11.969900 |
| Pay money to an association | - |  - |  - |  - |  - |  - |  - | -3.420900 |
| **R2** | 0.995900 |  0.997100 |  0.997200 |  0.997200 |  0.998000 |  0.999100 |  0.999100 | 0.992800 |
| **R2_adj** | 0.995600 |  0.996600 |  0.994500 |  0.996400 |  0.996800 |  0.998100 |  0.996900 | 1.100200 |
| **MAE** | 5556.493300 |  5051.532400 |  5206.002000 |  5070.328200 |  4394.872200 |  2818.670500 |  2717.642000 | 7782.112200 |
| **MPE** | -2.940900 |  -2.143400 |  4.215400 |  -3.696500 |  -4.203800 |  1.500300 |  1.475300 | 10.831200 |
| **MAPE** | 5.211100 |  4.808800 |  8.541000 |  5.214700 |  5.853500 |  4.513500 |  5.359300 | 14.942900 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_albania__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_albania_2zones.png)


Tunisia, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.006200 |  1.043000 |  0.621200 |  1.017900 |  0.878500 |  1.039200 |  0.845200 | 0.418100 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.037600 |  0.148000 |  -0.057700 |  0.096400 |  -0.009600 |  0.197400 | 0.321800 |
| native population - Total | - |  - |  0.000500 |  - |  - |  0.000300 |  0.000700 | 0.001700 |
| Free activities in voluntary associations | - |  - |  5.089100 |  0.935100 |  -4.212600 |  -5.845500 |  -13.440700 | -4.234700 |
| Meetings in cultural, recreational or other associations | - |  - |  -3.071400 |  - |  - |  -4.706600 |  -2.666400 | 2.347200 |
| Disposable Income | - |  - |  -0.746700 |  - |  - |  - |  - | - |
| Average monthly expenditure for housing | - |  - |  588.866700 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -6.534400 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -0.906600 |  - |  - |  - |  - | 3.849500 |
| internal_migration - Foreign country | - |  - |  - |  - |  0.002000 |  0.058400 |  0.133900 | -0.017900 |
| Pay money to an association | - |  - |  - |  - |  2.705500 |  1.966100 |  6.611100 | -1.014100 |
| Accommodation and catering services | - |  - |  - |  - |  - |  - |  8.553200 | 33.028300 |
| political_info - Every day | - |  - |  - |  - |  - |  - |  -1.081500 | -4.982300 |
| Free activities in non voluntary associations | - |  - |  - |  - |  - |  - |  -28.596900 | -23.348800 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  - | -0.774800 |
| Born alive | - |  - |  - |  - |  - |  - |  - | 0.191400 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  - | -7.306800 |
| political_info - Never | - |  - |  - |  - |  - |  - |  - | -6.802100 |
| **R2** | 0.996600 |  0.996600 |  0.991900 |  0.996100 |  0.992200 |  0.995300 |  0.942500 | 0.947900 |
| **R2_adj** | 0.996300 |  0.996100 |  0.983800 |  0.995000 |  0.987900 |  0.990600 |  0.798800 | 1.729400 |
| **MAE** | 971.384100 |  956.531800 |  1667.222900 |  1084.081400 |  1398.343700 |  1118.430600 |  4751.340200 | 4586.364500 |
| **MPE** | 2.403300 |  2.295200 |  11.958500 |  0.869700 |  9.040700 |  5.935000 |  29.428000 | 10.781300 |
| **MAPE** | 4.798900 |  4.701300 |  12.079200 |  5.443400 |  9.076600 |  6.753200 |  29.428000 | 28.851500 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_tunisia__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_tunisia_2zones.png)


Egypt, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.027200 |  0.813900 |  0.669800 |  0.803800 |  0.778900 |  0.666500 |  0.749600 | 0.562100 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  0.224300 |  0.410600 |  0.223200 |  0.232400 |  0.391200 |  0.273400 | 0.390500 |
| native population - Total | - |  - |  0.003000 |  0.000000 |  -0.000000 |  0.000000 |  0.001400 | 0.000000 |
| Free activities in voluntary associations | - |  - |  -4.863500 |  - |  - |  -14.479600 |  -10.373600 | -13.147800 |
| Meetings in cultural, recreational or other associations | - |  - |  -5.860800 |  - |  - |  - |  - | - |
| Disposable Income | - |  - |  -1.347000 |  - |  - |  - |  - | - |
| Average monthly expenditure for housing | - |  - |  184.261600 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -9.403800 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -5.280200 |  - |  - |  - |  - | - |
| Non food | - |  - |  - |  - |  -0.059800 |  0.305700 |  -1.624900 | 6.874800 |
| Pay money to an association | - |  - |  - |  - |  0.790400 |  6.180000 |  3.554200 | 2.478400 |
| internal_migration - Foreign country | - |  - |  - |  - |  - |  0.023300 |  0.018900 | -0.267300 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  -10.575000 | -6.037100 |
| Communications | - |  - |  - |  - |  - |  - |  42.310600 | -3.017900 |
| Accommodation and catering services | - |  - |  - |  - |  - |  - |  2.560300 | -12.825900 |
| internal_migration - Italy | - |  - |  - |  - |  - |  - |  - | 0.153800 |
| reach_difficulty - Supermarket | - |  - |  - |  - |  - |  - |  - | -5.928400 |
| Other goods and services | - |  - |  - |  - |  - |  - |  - | 1.052400 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  - | -11.395500 |
| Transport | - |  - |  - |  - |  - |  - |  - | -25.039400 |
| **R2** | 0.990500 |  0.988000 |  0.976000 |  0.987800 |  0.986600 |  0.959500 |  0.980300 | 0.930200 |
| **R2_adj** | 0.989800 |  0.986000 |  0.952100 |  0.984500 |  0.979100 |  0.919100 |  0.931100 | 1.976800 |
| **MAE** | 1732.044500 |  2070.709000 |  4436.408300 |  2018.025200 |  2169.215700 |  6042.958000 |  4066.703900 | 7955.170700 |
| **MPE** | 13.209400 |  15.715400 |  113.222200 |  1.195800 |  8.814800 |  153.336700 |  132.840800 | 150.391700 |
| **MAPE** | 13.589200 |  15.946600 |  113.222200 |  9.688000 |  14.120600 |  153.336700 |  133.934600 | 150.391700 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_egypt__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_egypt_2zones.png)


Ecuador, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.041200 |  1.299500 |  1.144700 |  1.291300 |  1.239900 |  1.385800 |  1.330400 | 1.050400 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.277600 |  -0.096100 |  -0.274200 |  -0.221000 |  -0.372100 |  -0.306400 | -0.077400 |
| native population - Total | - |  - |  0.001800 |  0.000000 |  0.000000 |  0.001500 |  0.001600 | 0.000900 |
| Free activities in voluntary associations | - |  - |  -0.164800 |  - |  -2.252200 |  -7.295400 |  -7.394500 | -4.200300 |
| Meetings in cultural, recreational or other associations | - |  - |  -6.658400 |  - |  - |  - |  - | -11.271000 |
| Disposable Income | - |  - |  -0.794700 |  - |  - |  - |  - | - |
| Average monthly expenditure for housing | - |  - |  138.521100 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -5.388600 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -3.055100 |  - |  - |  - |  - | - |
| Pay money to an association | - |  - |  - |  - |  1.300900 |  -0.784900 |  -1.306400 | 2.585800 |
| internal_migration - Foreign country | - |  - |  - |  - |  - |  0.030900 |  0.044300 | -0.113800 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  -8.332600 |  -9.253500 | -4.651000 |
| Other goods and services | - |  - |  - |  - |  - |  - |  16.492400 | 3.656500 |
| Accommodation and catering services | - |  - |  - |  - |  - |  - |  -1.893400 | -3.549700 |
| Transport | - |  - |  - |  - |  - |  - |  -10.302000 | -12.809300 |
| internal_migration - Italy | - |  - |  - |  - |  - |  - |  - | 0.083100 |
| reach_difficulty - Supermarket | - |  - |  - |  - |  - |  - |  - | -6.145300 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  - | -5.237900 |
| Non food | - |  - |  - |  - |  - |  - |  - | 2.914400 |
| **R2** | 0.995300 |  0.995700 |  0.995600 |  0.995700 |  0.995800 |  0.996700 |  0.996200 | 0.991600 |
| **R2_adj** | 0.994900 |  0.995000 |  0.991200 |  0.994600 |  0.993500 |  0.993400 |  0.986700 | 1.116900 |
| **MAE** | 1189.175900 |  1167.202100 |  1625.563400 |  1243.933400 |  1226.351600 |  1284.498800 |  1381.270900 | 2458.264300 |
| **MPE** | -1.984500 |  -1.291700 |  77.821000 |  -11.623400 |  21.313600 |  28.868700 |  49.889900 | 124.061800 |
| **MAPE** | 5.947900 |  5.849400 |  81.084800 |  13.989500 |  24.025800 |  44.507500 |  63.702000 | 124.867200 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_ecuador__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_ecuador_2zones.png)


Peru, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.068500 |  1.133500 |  1.042100 |  1.119500 |  1.144900 |  0.784100 |  0.865900 | 0.633800 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  -0.070600 |  0.043400 |  -0.063400 |  -0.096700 |  0.307400 |  0.191200 | 0.220500 |
| native population - Total | - |  - |  0.001000 |  0.000000 |  0.000100 |  0.000100 |  0.000900 | -0.002500 |
| Free activities in voluntary associations | - |  - |  -2.395200 |  - |  -1.359400 |  -1.903200 |  0.149600 | -2.991600 |
| Meetings in cultural, recreational or other associations | - |  - |  -1.334800 |  - |  - |  - |  -7.946900 | 5.110500 |
| Disposable Income | - |  - |  -0.307000 |  - |  - |  -0.296500 |  -0.024800 | 2.618400 |
| Average monthly expenditure for housing | - |  - |  61.821200 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -3.402600 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -2.206900 |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  - |  - |  - |  0.019300 |  -0.053600 |  -0.061900 | -0.053000 |
| Pay money to an association | - |  - |  - |  - |  - |  3.367400 |  4.085300 | 7.444700 |
| reach_difficulty - Supermarket | - |  - |  - |  - |  - |  - |  -0.285000 | 4.690400 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  -5.354100 | -3.250100 |
| internal_migration - Italy | - |  - |  - |  - |  - |  - |  - | 0.057200 |
| Other goods and services | - |  - |  - |  - |  - |  - |  - | -5.659100 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  - | 1.904000 |
| Non food | - |  - |  - |  - |  - |  - |  - | -0.297800 |
| political_info - Every day | - |  - |  - |  - |  - |  - |  - | -3.590300 |
| **R2** | 0.992300 |  0.992700 |  0.993300 |  0.992800 |  0.993800 |  0.990700 |  0.991400 | 0.980700 |
| **R2_adj** | 0.991700 |  0.991500 |  0.986600 |  0.990900 |  0.990400 |  0.981400 |  0.970000 | 1.270800 |
| **MAE** | 1709.931000 |  1685.920300 |  1872.193800 |  1776.341600 |  1632.523000 |  2066.226300 |  2125.719700 | 3393.737000 |
| **MPE** | -5.787000 |  -5.521500 |  45.000300 |  -15.152600 |  -7.327300 |  26.023600 |  35.135000 | 76.670600 |
| **MAPE** | 7.860700 |  7.634000 |  51.646200 |  16.478000 |  12.249100 |  32.095700 |  45.832800 | 88.189800 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_peru__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_peru_2zones.png)


China, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.080300 |  0.895300 |  0.686100 |  0.826600 |  0.680500 |  0.714200 |  0.164100 | 0.223100 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  0.200300 |  0.406800 |  0.204300 |  0.322800 |  0.424100 |  0.837500 | 0.745000 |
| native population - Total | - |  - |  0.001200 |  - |  - |  - |  -0.000400 | -0.004900 |
| Free activities in voluntary associations | - |  - |  0.302300 |  - |  - |  - |  -13.692100 | -9.079200 |
| Meetings in cultural, recreational or other associations | - |  - |  -4.650300 |  - |  - |  - |  - | - |
| Disposable Income | - |  - |  -0.726100 |  - |  - |  -1.557900 |  0.902900 | -0.917900 |
| Average monthly expenditure for housing | - |  - |  172.910600 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -6.050100 |  - |  - |  - |  - | 12.453900 |
| reach_difficulty - Emergency room | - |  - |  -1.273200 |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  - |  - |  0.047500 |  0.076500 |  0.034900 |  0.040800 | 0.188400 |
| Born alive | - |  - |  - |  - |  0.077000 |  0.176400 |  0.049100 | 0.540400 |
| political_info - Some times in a week | - |  - |  - |  - |  -3.879400 |  -1.612200 |  -2.446600 | -0.046200 |
| political_info - Every day | - |  - |  - |  - |  - |  -1.474600 |  -2.112100 | -0.984500 |
| Pay money to an association | - |  - |  - |  - |  - |  - |  12.079500 | 10.565000 |
| reach_difficulty - Pharmacy | - |  - |  - |  - |  - |  - |  - | 2.604300 |
| reach_difficulty - Food stores, markets | - |  - |  - |  - |  - |  - |  - | -2.886100 |
| reach_difficulty - Supermarket | - |  - |  - |  - |  - |  - |  - | -14.994900 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  - | 11.851100 |
| **R2** | 0.995400 |  0.995100 |  0.994700 |  0.996100 |  0.994400 |  0.994300 |  0.977700 | 0.960700 |
| **R2_adj** | 0.995000 |  0.994300 |  0.989400 |  0.995000 |  0.991300 |  0.988500 |  0.921900 | 1.550600 |
| **MAE** | 3010.976100 |  3249.705300 |  3561.305700 |  2837.138600 |  3150.402600 |  3451.476300 |  7308.850900 | 10857.541100 |
| **MPE** | -1.061300 |  -0.759000 |  2.530900 |  1.358200 |  6.532400 |  6.169700 |  18.982200 | 23.728900 |
| **MAPE** | 5.381800 |  5.747600 |  6.934900 |  5.432900 |  6.981900 |  7.997900 |  18.982200 | 23.728900 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_china__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_china_2zones.png)


Philippines, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.058900 |  0.901800 |  0.742200 |  0.898800 |  0.749600 |  0.662700 |  0.389600 | 0.412800 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | - |  0.167200 |  0.361700 |  0.162900 |  -0.012300 |  0.110700 |  0.362700 | 0.149400 |
| native population - Total | - |  - |  0.001600 |  - |  0.000800 |  0.000700 |  0.000500 | -0.001600 |
| Free activities in voluntary associations | - |  - |  -2.063400 |  - |  - |  1.685600 |  0.574000 | 0.231100 |
| Meetings in cultural, recreational or other associations | - |  - |  -3.322800 |  - |  - |  - |  - | - |
| Disposable Income | - |  - |  -0.778000 |  - |  - |  - |  - | 1.099500 |
| Average monthly expenditure for housing | - |  - |  109.525200 |  - |  - |  - |  - | - |
| unemployment - Total | - |  - |  -3.403000 |  - |  - |  - |  - | - |
| reach_difficulty - Emergency room | - |  - |  -2.842100 |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  - |  - |  0.004000 |  0.132500 |  0.106600 |  0.080100 | 0.191600 |
| Other goods and services | - |  - |  - |  - |  -12.060500 |  1.015700 |  -5.629400 | 3.459500 |
| Non food | - |  - |  - |  - |  - |  -1.208300 |  -0.733700 | -2.603300 |
| Communications | - |  - |  - |  - |  - |  - |  9.523800 | -0.640600 |
| Accommodation and catering services | - |  - |  - |  - |  - |  - |  -4.614500 | -4.732000 |
| Pay money to an association | - |  - |  - |  - |  - |  - |  3.771300 | 3.677400 |
| reach_difficulty - Post offices | - |  - |  - |  - |  - |  - |  - | -0.095900 |
| Born alive | - |  - |  - |  - |  - |  - |  - | 0.164500 |
| Housing, water, electricity, gas and other fuels | - |  - |  - |  - |  - |  - |  - | 1.237900 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  - | 2.225100 |
| **R2** | 0.992200 |  0.992300 |  0.992200 |  0.992400 |  0.975800 |  0.976000 |  0.974300 | 0.968100 |
| **R2_adj** | 0.991600 |  0.991000 |  0.984300 |  0.990300 |  0.962400 |  0.951900 |  0.910000 | 1.446500 |
| **MAE** | 2387.559100 |  2369.865300 |  2300.218600 |  2340.493600 |  4964.063700 |  4983.678300 |  5309.690500 | 5989.886800 |
| **MPE** | -1.174100 |  -0.903600 |  3.469800 |  -0.907000 |  -25.182700 |  -25.052200 |  -17.053800 | -11.114900 |
| **MAPE** | 6.371200 |  6.366500 |  6.937800 |  6.308200 |  30.070000 |  29.815000 |  27.234700 | 28.000400 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_philippines__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_philippines_2zones.png)


## [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents)

In this section, some attempts to replicate the model specified in the [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents) are performed.

The initial model is defined as:

![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%28n_%7Bi%2C%20t%7D%29%20%3D%20%5Cbeta%20ln%20%28n_%7Bi%2C%20t-1%7D%29%20&plus;%20%5Calpha_i%20&plus;%20%5Cgamma_t%20&plus;%20u_%7Bi%2C%20t%7D%20%5C%20%5C%20i%20%3D%201%2C%20%5Cdots%2C%20I%20%5Ctext%7B%20and%20%7D%20t%20%3D%201%2C%20%5Cdots%2C%20T)

where:
- ![](https://latex.codecogs.com/gif.latex?n_%7Bi%2C%20t%7D) is the stock of foreign-born in territory ![](https://latex.codecogs.com/gif.latex?i) at time ![](https://latex.codecogs.com/gif.latex?t).
- ![](https://latex.codecogs.com/gif.latex?%5Cbeta) is the parameters for the network effect (is a local phenomenon that influences the immigrant choice, that is: foreign-born population tend to migrate to territories where a community of the same ethnic already exists).
- ![](https://latex.codecogs.com/gif.latex?%5Calpha_i%20%3D%20x%27_i%20%5Ctheta%20&plus;%20%5Ceta_i) , ![](https://latex.codecogs.com/gif.latex?x%27_%7Bi%7D) is the vector of all the time-invariant observable location factors (features vector), ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Ctheta) is the vector of coefficient and![](https://latex.codecogs.com/gif.latex?%5Ceta_i) is an error random term.
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cgamma_t) measures the fixed time effect.

![](https://latex.codecogs.com/gif.latex?u_%7Bi%2C%20t%7D) is the *error term*. It is modeled using a *Spatial Autoregressive Model*, ![](https://latex.codecogs.com/gif.latex?u_t%20%3D%20%28u_%7B1%2C%20t%7D%2C%20%5Cdots%2C%20u_%7BI%2C%20t%7D%29) follows:

![](https://latex.codecogs.com/gif.latex?u_t%20%3D%20%5Crho%20W%20u_t%20&plus;%20w_t),

where:
- ![](https://latex.codecogs.com/gif.latex?%5Crho) is the autoregressive parameter.
- ![](https://latex.codecogs.com/gif.latex?W) is a symmetric spatial weights matrix. For ease of interpretation, the weights matrix is often normalized so that the elements of each row sum up to one. This ensure all weights are between 0 and 1, moreover each row-normalized weight can be interpreted as the fraction of all spatial influence on unit *i* attributable to unit *j*. ![](https://latex.codecogs.com/gif.latex?w_%7Bij%7D%20%5Cge%200%2C%20%5C%20w_%7Bij%7D%20%3D%200%20%5Ctext%7B%20if%20%7D%20i%3Dj%2C%20%5C%20%5Csum_%7Bj%3D1%7D%5En%20w_%7Bij%7D%20%3D%201%20%5C%20%5C%20i%3D1%2C%20%5Cdots%2C%20n). (General form of a weights matrix, not necessary).
- ![](https://latex.codecogs.com/gif.latex?w_t%20%5Csim%20N%280%2C%20%5Csigma%5E2%20I%29) is an iid random term.

The model just defined cannot be estimated using both the time and the location fixed effects ![](https://latex.codecogs.com/gif.latex?%5Calpha_i) and ![](https://latex.codecogs.com/gif.latex?%5Cgamma_t). With an increasing sample size , maximum likelihood (ML) methods are asymptotically consistent, efficient and normally distributed. The ML estimates' consistency depends on the assumption that the number of parameters remains constant as the sample size increases.

Since the number of locations cannot increases, a larger sample in this model means a longer period. Thus, if the sample size increases, the number of fixed time effects increases. It is necessary to suppress them to consistently estimate the model.

In a general fixed effect model ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20%3D%20%5Cbeta%20x_%7Bi%2C%20t%7D%20&plus;%20%5Calpha_t%20&plus;%20%5Cepsilon_%7Bi%2C%20t%7D%2C%20%5C%20i%20%3D%201%2C%20%5Cdots%2C%20I%20%5C%20and%20%5C%20t%20%3D%201%2C%20%5Cdots%2C%20T), it is possible to eliminate the fixed effect ![](https://latex.codecogs.com/gif.latex?%5Cgamma_t) by:
1. fixed effects transformation: ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20-%20%5Cbar%7By%7D_t%20%3D%20%28x_%7Bi%2C%20t%7D%20-%20%5Cbar%7Bx%7D_t%29%5Cbeta%20&plus;%20%28%5Calpha_t%20-%20%5Cbar%7B%5Calpha%7D_t%29%20&plus;%20%28u_%7Bi%2C%20t%7D%20-%20%5Cbar%7Bu%7D_%7Bi%2Ct%7D%29).
2. differencing with respect to a fixed unit: ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20-%20y_%7BI%2C%20t%7D%20%3D%20%28x_%7Bi%2C%20t%7D%20-%20x_%7BI%2C%20t%7D%29%5Cbeta%20&plus;%20%28%5Calpha_t%20-%20%5Calpha_t%29%20&plus;%20%28u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D%29).

Here, the differentiating method with respect to a reference location, *I*, is used:

![](https://latex.codecogs.com/gif.latex?ln%28n_%7Bi%2C%20t%7D%29%20-%20ln%28n_%7BI%2C%20t%7D%29%20%3D%20%5Cbeta%28ln%28n_%7Bi%2C%20t-1%7D%29%20-%20ln%28n_%7BI%2C%20t-1%7D%29%29%20&plus;%20%5Calpha_i%20-%20%5Calpha_I%20&plus;%20%5Cgamma_t%20-%20%5Cgamma_t%20&plus;%20u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D)


![](https://latex.codecogs.com/gif.latex?ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2Ct%7D%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20%3D%20%5Cbeta%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2Ct-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%20%29%20&plus;%20a_i%20&plus;%20v_%7Bi%2Ct%7D)

with
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20i%20%3D%201%2C%20%5Cdots%2C%20I-1%20%5Ctext%7B%20and%20%7D%20t%20%3D%201%2C%20%5Cdots%2C%20T)
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20a_i%20%3D%20%5Calpha_i%20-%20%5Calpha_I)
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_%7Bi%2C%20t%7D%20%3D%20u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D)

Thus, ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_t%20%3D%20Q%20u_t) with ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_t%20%3D%20%28v_%7B1%2C%20t%7D%2C%20v_%7BI-1%2C%20t%7D%29), ![](https://latex.codecogs.com/gif.latex?%5Cinline%20u_t%20%3D%20%28u_%7B1%2C%20t%7D%2C%20u_%7BI%2C%20t%7D%29) and ![](https://latex.codecogs.com/gif.latex?%5Cinline%20Q%20%3D%20%5Cleft%20%5B%20I_%7BI-1%7D%20%5C%20-1_%7BI-1%7D%20%5Cright%20%5D), being ![](https://latex.codecogs.com/gif.latex?%5Cinline%20I_%7BI-1%7D) and identity matrix of dimension ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%28I-1%20%5Ctext%7B%20x%20%7D%20I-1%20%29) and ![](https://latex.codecogs.com/gif.latex?%5Cinline%20-1_%7BI-1%7D) the column vector of dimension ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%28I-1%29) with all its element equal to -1.


Since the unobserved effect is correlated with the observed explanatory variable (i.e. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20Cov%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2C%20t-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%29%2C%20v_%7Bi%2C%20t%7D%20%5Cright%20%29%20%5Cne%200)), *ordinary squares estimates* are not consistent. To estimate the model is necessary to use the ML method.

In order to write the ML model, some computations are needed.
![](https://latex.codecogs.com/gif.latex?u_t%20%3D%20%5Crho%20W%20u_t%20&plus;%20w_t%20%5CRightarrow%20u_t%20%3D%20%5Cleft%20%5C%28%20I%20-%20%5Crho%20W%20%5Cright%20%5C%29%5E%7B-1%7D%2C%20%5Ctext%7B%20where%20%7D%20w_t%20%5Csim%20N%280%2C%20%5Csigma%5E2%20I%29),
so ![](https://latex.codecogs.com/gif.latex?%5Cinline%20u_t%20%5Csim%20N%280%2C%20%5Cleft%20%28%20I%20-%20%5Crho%20W%20%5Cright%20%29%5E%7B-1%7D%20%5Csigma%5E2%20%5Cleft%20%28%20I%20-%20%5Crho%20W%5ET%20%5Cright%20%29%5E%7B-1%7D%29)

![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_t%20%3D%20Q%20u_t%20%5CRightarrow%20v_t%20%5Csim%20N%20%5Cleft%20%28%200%2C%20%5C%20Q%20%5Cleft%20%28%20I%20-%20%5Crho%20W%20%5Cright%20%29%5E%7B-1%7D%20%5Csigma%5E2%20%5Cleft%20%28%20I%20-%20%5Crho%20W%5ET%20%5Cright%20%29%5E%7B-1%7D%20Q%5ET%20%5Cright%20%29)

Let's call ![](https://latex.codecogs.com/gif.latex?%5Cinline%20n_t%20%3D%20%28n_%7B1%2C%20t%7D%2C%20%5Cdots%2C%20n_%7BI-1%2C%20t%7D%29%2C%20%5C%20n_%7Bt-1%7D%20%3D%20%28n_%7B1%2C%20t-1%7D%2C%20%5Cdots%2C%20n_%7BI-1%2C%20t-1%7D%29%20%5Ctext%7B%20and%20%7D%20a%20%3D%20%28a_1%2C%20%5Cdots%2C%20a_%7BI-1%7D%29),
then:

![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20%3D%20%5Cbeta%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%20%29%20&plus;%20a%20&plus;%20v_t%2C%20%5C%20%5C%20t%3D1%2C%20%5Cdots%2C%20T),

so:  ![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20%5Csim%20N%20%5Cleft%20%28%20%5Cbeta%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%20%29%20&plus;%20a%20%2C%20Q%20%28I-%5Crho%20W%29%5E%7B-1%7D%5Csigma%5E2%20%28I-%5Crho%20W%5ET%29%5E%7B-1%7D%20Q%5ET%20%5Cright%20%29)

Let's denote:
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cmu%20%3D%20%5Cbeta%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%20%29%20&plus;%20a)
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5CSigma%20%3D%20Q%20%28I-%5Crho%20W%29%5E%7B-1%7D%5Csigma%5E2%20%28I-%5Crho%20W%5ET%29%5E%7B-1%7D%20Q%5ET)


It is now possible to write the distribution of each vector ![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt%7D%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29):

![](https://latex.codecogs.com/gif.latex?%5Cinline%20f%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt%7D%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20%5Cright%20%29%20%3D%20%7C2%20%5Cpi%20%5CSigma%20%7C%20%5E%7B-1/2%7D%20exp%20%5Cleft%20%5C%7B%20-%5Cfrac%7B1%7D%7B2%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt%7D%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%5Cmu%20%5Cright%20%29%5ET%20%5CSigma%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bt%7D%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%5Cmu%20%5Cright%20%29%20%5Cright%20%5C%7D)

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5CRightarrow%20%7C2%20%5Cpi%20%5CSigma%20%7C%20%5E%7B-1/2%7D%20%3D%202%20%5Cpi%20%5E%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%20%7C%5CSigma%7C%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D)

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cbegin%7Balign*%7D%20%5CRightarrow%20%7C%5CSigma%7C%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%26%3D%20%7CQ%20%28I-%20%5Crho%20W%29%5E%7B-1%7D%20%5Csigma%5E2%20%28I-%20%5Crho%20W%5ET%29%5E%7B-1%7DQ%5ET%20%7C%20%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20%5C%5C%20%26%3D%20%7C%5Csigma%5E2%20Q%20%28I-%20%5Crho%20W%29%5E%7B-1%7D%20%28I-%20%5Crho%20W%5ET%29%5E%7B-1%7DQ%5ET%20%7C%20%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20%5C%5C%20%26%3D%20%28%5Csigma%5E2%29%5E%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%20%7CQ%20%28I-%20%5Crho%20W%29%5E%7B-1%7D%20%28I-%20%5Crho%20W%5ET%29%5E%7B-1%7DQ%5ET%20%7C%20%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20%5C%5C%20%26%3D%20%28%5Csigma%5E2%29%5E%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%20%7CL%7C%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20%5Cend%7Balign*%7D)

and ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5CSigma%5E%7B-1%7D%3D%20%5Cfrac%7B1%7D%7B%5Csigma%5E2%7D%20%5Cleft%20%5B%20Q%20%28I-%20%5Crho%20W%29%5E%7B-1%7D%20%28I-%20%5Crho%20W%5ET%29%5E%7B-1%7DQ%5ET%20%5Cright%20%5D%5E%7B-1%7D%20%3D%20%5Cfrac%7B1%7D%7B%5Csigma%5E2%7D%20L%5E%7B-1%7D).

Thus, the distribution can be written as:
![](https://latex.codecogs.com/gif.latex?%5Cinline%20f%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20%5Cright%20%29%20%3D%20%282%20%5Cpi%20%5Csigma%5E2%29%5E%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%20%7CL%7C%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20exp%20%5Cleft%5C%7B%20-%20%5Cfrac%7B1%7D%7B2%20%5Csigma%5E2%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5Cright%5C%7D)

Let ![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29) be a ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cleft%20%28%20T%20%5Ctext%7B%20x%20%7D%20I-1%20%5Cright%20%29) matrix whose ![](https://latex.codecogs.com/gif.latex?%5Cinline%20T) rows are ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_1%7D%7Bn_%7BI%2C%201%7D%7D%20%5Cright%20%29%2C%20%5Cdots%2C%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_T%7D%7Bn_%7BI%2C%20T%7D%7D%20%5Cright%20%29%20%5Cright%20%29). The matrix normal distribution of ![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29) is defined as follows (it can be computed since the row components are conditionally - to the previous one - independent):

![](https://latex.codecogs.com/gif.latex?%5Cinline%20f%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29%20%5Cright%20%29%20%3D%20%5Cprod_%7Bt%3D1%7D%5ET%20%282%20%5Cpi%20%5Csigma%5E2%29%5E%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%20%7CL%7C%5E%7B-%5Cfrac%7B1%7D%7B2%7D%7D%20exp%20%5Cleft%5C%7B%20-%20%5Cfrac%7B1%7D%7B2%20%5Csigma%5E2%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5Cright%5C%7D)

The log-likelihood is then:
![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cbegin%7Balign*%7D%20L%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29%2C%20%5Cbeta%2C%20a%2C%20%5Crho%20%5Cright%20%29%20%26%3D%20%7B-%5Cfrac%7BI-1%7D%7B2%7D%7D%5Ccdot%20T%20%5Ccdot%20ln%282%20%5Cpi%20%5Csigma%5E2%29%20-%20%5Cfrac%7BT%7D%7B2%7Dln%7CL%7C%20-%20%5Cfrac%7B1%7D%7B2%20%5Csigma%5E2%7D%20%5Csum_%7Bt%3D1%7D%5ET%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5C%5C%20%26%20%5Cpropto%20-%20T%5Ccdot%20ln%7CL%7C%20-%20%5Cfrac%7B1%7D%7B%5Csigma%5E2%7D%20%5Csum_%7Bt%3D1%7D%5ET%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5C%5C%20%5Cend%7Balign*%7D),

assuming a unitary variance, it can be written as:
![](https://latex.codecogs.com/gif.latex?%5Cinline%20L%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29%2C%20%5Cbeta%2C%20a%2C%20%5Crho%20%5Cright%20%29%20%3D%20-%20T%5Ccdot%20ln%7CL%7C%20-%20%5Csum_%7Bt%3D1%7D%5ET%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5C%5C),

maximize ![](https://latex.codecogs.com/gif.latex?%5Cinline%20L%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn%7D%7Bn_%7BI%7D%7D%20%5Cright%20%29%2C%20%5Cbeta%2C%20a%2C%20%5Crho%20%5Cright%20%29) is equivalent to:

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Ctext%7B%20min%20%7D%20%5C%20%5C%20T%5Ccdot%20ln%7CL%7C%20&plus;%5Csum_%7Bt%3D1%7D%5ET%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%5ET%20L%5E%7B-1%7D%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_t%7D%7Bn_%7BI%2C%20t%7D%7D%20%5Cright%20%29%20-%20%5Cmu%20%5Cright%20%29%20%5C%5C)

Once ![](https://latex.codecogs.com/gif.latex?%5Chat%7B%5Cbeta%7D) and ![](https://latex.codecogs.com/gif.latex?%5Chat%7Ba%7D) have been found, it is possible to estimate the coefficients of the time-invariant features through the formula:

![](https://latex.codecogs.com/gif.latex?%5Chat%7Ba%7D_i%20%3D%20a_i%20&plus;%20%5Cxi_i%20%3D%20%5Calpha_i%20-%20%5Calpha_I%20&plus;%20%5Cxi_i%20%3D%20%5Cleft%20%5C%28%20x%5ET_i%20-%20x%5ET_I%20%5Cright%20%5C%29%5Ctheta%20&plus;%20%5Cepsilon_i%20&plus;%20%5Cxi_i%2C)

where ![](https://latex.codecogs.com/gif.latex?%5Cepsilon_i%20%3D%20%5Ceta_i%20-%20%5Ceta_I)

![](https://latex.codecogs.com/gif.latex?%5Ctheta) is then estimated by ordinary least squares.

### Spatial weights matrix

In order to build the spatial weights matrix, useful information are available on the [ISTA website](http://www.istat.it/it/archivio/157423).

ISTAT releases the origin-destination matrices of distances in meters and travel times (in minutes) between all Italian municipalities. The matrices are grouped by Region. The files are provided in text format and all Italian municipalities.
The islands are treated separately. The matrices of Sicily and Sardinia contain only the between-region distances (the distances only of the municipalities of the regions).
In a separate excel file are available the distances for the main ports that connect the islands with respect to Peninsular Italy. This allows you to add the travel time by ship to the routes calculated from the main ports of connection to the islands.

There are some problems with the different tables:
- the column names are not always the same;
- column are index may be inverted: for all the regions but Lombardy the region-provinces are in the "Destination" column and the other provinces in the "Origin" column. In the Lombardy table the two data are inverted (thus, the need to transpose the matrix);
- I am not able to find the Sicily and Sardinia ports distances.

To compute the distances between Sicily-Sardinia and the other Italian regions, it is possible to manually detect (GoogleMaps) some useful distances between the main ports and compute the distances as the sum of multiple component.

In particular:
- from Sicily: ![](https://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20d_%7B%28origin%2C%20Trapani%29%7D%20&plus;%20d_%7B%28Trapani%2C%20Cagliari%29%7D%20&plus;%20d_%7B%28Cagliari%2C%20destination%29%7D%20%26%20%5Ctext%7Bif%20destination%20in%20Sardinia%7D%20%5C%5C%20d_%7B%28origin%2C%20Messina%29%7D%20&plus;%20d_%7B%28Messina%2C%20Villa%20San%20Giovanni%29%7D%20&plus;%20d_%7B%28Villa%20San%20Giovanni%2C%20destination%29%7D%20%26%20%5Ctext%7Botherwise%7D%20%5Cend%7Bmatrix%7D%5Cright.)
- from Sardinia:
![](https://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20d_%7B%28origin%2C%20Cagliari%29%7D%20&plus;%20d_%7B%28Cagliari%2C%20Trapani%29%7D%20&plus;%20d_%7B%28Trapani%2C%20destination%20%29%7D%20%26%20%5Ctext%7Bif%20destination%20in%20Sicily%7D%20%5C%5C%20min%5Cleft%20%28d_%7BMessina%7D%2C%20d_%7BLivorno%7D%2C%20d_%7BCivitavecchia%7D%20%5Cright%29%20%26%20%5Ctext%7Botherwise%7D%20%5Cend%7Bmatrix%7D%5Cright.),

where:
1. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20d_%7BMessina%7D%20%3D%20d_%7B%28origin%2C%20Cagliari%29%7D%20&plus;%20d_%7B%28Cagliari%2C%20Trapani%29%7D%20&plus;%20d_%7B%28Trapani%2C%20Messina%29%7D%20&plus;%20d_%7B%28Messina%2C%20Villa%20San%20Giovanni%29%7D%20&plus;%20d_%7B%28Villa%20San%20Giovanni%2C%20destination%29%7D)
2. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20d_%7BLivorno%7D%20%3D%20d_%7B%28origin%2C%20Olbia%29%7D%20&plus;%20d_%7B%28Olbia%2C%20Livorno%29%7D%20&plus;%20d_%7B%28Livorno%2C%20destination%29%7D)
3. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20d_%7BCivitavecchia%7D%20%3D%20d_%7B%28origin%2C%20Olbia%29%7D%20&plus;%20d_%7B%28Olbia%2C%20Civitavecchia%29%7D%20&plus;%20d_%7B%28Civitavecchia%2C%20destination%29%7D)

The regions distance matrix is computed as the mean distance between all the province pairs belonging to the two regions considered.

The zones distance matrix is obtained by taking the mean distance between all the regions pairs belonging to the two zones considered.

As spacial weights the inverse of the squared of the distances are used. The result matrix ![](https://latex.codecogs.com/gif.latex?W) is a symmetric, non-negative matrix with ![](https://latex.codecogs.com/gif.latex?w_%7Bij%7D%20%3E%3D%200) and ![](https://latex.codecogs.com/gif.latex?w_%7Bii%7D%20%3D%200).

The row-normalized ![](https://latex.codecogs.com/gif.latex?W) is used for ease of interpretation. It is defined as ![](https://latex.codecogs.com/gif.latex?%5Csum_%7Bj%3D1%7D%5En%20w_%7Bij%7D%20%3D%201%2C%20%5Cforall%20i%20%3D%201%2C%20%5Cdots%2C%20n). This ensure that all weights are between 0 and 1. Each row-normalized weight, ![](https://latex.codecogs.com/gif.latex?wij), can be interpreted as the fraction of all spatial influence on unit ![](https://latex.codecogs.com/gif.latex?i) attributable to unit ![](https://latex.codecogs.com/gif.latex?j).

### Estimation Results

The model specified is used to predict the immigrant stock at Italian zones level. Same features, times period and origin countries used it the previous section (Regression Model for Data Panel) are considered.

All the features are assumed to be time invariant, thus as reference period the 2013 is considered.

The model also requires a reference territory, the estimation of the "Italia" stock at the current time ![](https://latex.codecogs.com/gif.latex?t) is used.

The prediction of the overall Italian flow is obtained through regression models whose independent variables are chosen using an automatic feature selection based on mutual information. Follows the results and the plot of the prediction.

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/regression_model_italy.png)

For each origin country, just the models using 3, and 5 features are used. The models with an higher number of variables gave really bad estimations.

Romania, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.926300 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 6.865800 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.998400 |  0.998800 |  0.998900 |  0.998900 |  0.998800 |  0.998400 |  0.999000 | 0.998700 |
| **R2_adj** | 0.998400 |  0.998700 |  0.998800 |  0.998700 |  0.998400 |  0.997800 |  0.998400 | 0.997800 |
| **MAE** | 7351.814500 |  6731.112800 |  6313.440300 |  6193.532600 |  6651.446200 |  7351.814500 |  6136.917900 | 7674.905700 |
| **MPE** | -2.011200 |  -2.050300 |  -2.071400 |  -2.050200 |  -2.015500 |  -2.011200 |  -1.713400 | -2.274000 |
| **MAPE** | 4.347800 |  3.565000 |  3.503200 |  3.516300 |  3.963600 |  4.347800 |  3.306200 | 4.334900 |
| a Centro | -0.109700 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -0.110200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.136800 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.112800 |  - |  - |  - |  - |  - |  - | - |
| ![](https://latex.codecogs.com/gif.latex?a_%7BSud%7D) | -0.086300 |  - |  - |  - |  - |  - |  - | - |
| Free activity for a union | - |  0.000200 |  0.000500 |  0.000400 |  -0.000800 |  0.001800 |  0.000500 | 0.000800 |
| Free activities in voluntary associations | - |  - |  -0.000000 |  -0.000100 |  0.000100 |  -0.000300 |  0.000000 | -0.000100 |
| Meetings in cultural, recreational or other associations | - |  - |  - |  0.000000 |  -0.000300 |  0.002000 |  -0.000100 | 0.000000 |
| Meetings in ecological associations, for civil rights, for peace | - |  - |  - |  - |  0.002000 |  -0.004900 |  0.000400 | 0.000200 |
| Free activities in non voluntary associations | - |  - |  - |  - |  - |  -0.002600 |  0.000100 | -0.000100 |
| political_info - Some times in a year | - |  - |  - |  - |  - |  - |  -0.000000 | 0.000000 |
| Recreation, shows and culture | - |  - |  - |  - |  - |  - |  - | 0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_romania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_romania_.png)

Morocco, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.814100 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.041200 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.999200 |  0.990600 |  0.998600 |  0.998700 |  0.999200 |  0.999200 |  0.998600 | 0.999100 |
| **R2_adj** | 0.999200 |  0.990000 |  0.998400 |  0.998400 |  0.998900 |  0.998800 |  0.997800 | 0.998500 |
| **MAE** | 2643.818500 |  7931.735400 |  3190.173300 |  2777.037500 |  2681.001000 |  2643.818500 |  3478.986200 | 2813.939800 |
| **MPE** | 2.313400 |  3.607200 |  2.607200 |  2.541400 |  2.313900 |  2.313400 |  4.746400 | 7.577100 |
| **MAPE** | 3.999600 |  8.133400 |  6.263100 |  5.915300 |  4.013800 |  3.999600 |  4.746400 | 7.577100 |
| a Centro | -0.370600 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -0.614200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.211300 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.163000 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -0.447700 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  -0.000000 |  -0.000000 |  -0.000000 | 0.000000 |
| Free activity for a union | - |  - |  -0.001700 |  -0.001600 |  0.011300 |  0.015500 |  0.001800 | 0.001300 |
| Recreation, shows and culture | - |  - |  - |  -0.000000 |  0.000900 |  0.001100 |  0.000200 | 0.000300 |
| reach_difficulty - Municipal offices | - |  - |  - |  - |  -0.000600 |  -0.000900 |  -0.000100 | 0.000200 |
| work_satisfaction - Not | - |  - |  - |  - |  - |  0.004000 |  -0.007400 | -0.030800 |
| Pay money to an association | - |  - |  - |  - |  - |  - |  0.000100 | 0.000000 |
| Education | - |  - |  - |  - |  - |  - |  - | 0.001000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_morocco_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_morocco_.png)


Albania, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.725800 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.043800 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.999800 |  0.973600 |  0.994400 |  0.996300 |  0.996800 |  0.999800 |  0.997800 | 0.995400 |
| **R2_adj** | 0.999800 |  0.971900 |  0.993700 |  0.995500 |  0.995800 |  0.999800 |  0.996600 | 0.992100 |
| **MAE** | 1206.040100 |  15763.048900 |  6493.342800 |  5722.243200 |  5444.417000 |  1206.040100 |  4608.401200 | 6055.727800 |
| **MPE** | 1.628200 |  2.185800 |  1.014700 |  1.409800 |  1.333300 |  1.628200 |  9.215100 | 8.371100 |
| **MAPE** | 2.526500 |  19.713200 |  13.058800 |  11.458300 |  11.318400 |  2.526500 |  9.585100 | 8.371100 |
| a Centro | -0.368300 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -1.156500 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.342200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.292600 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -0.647900 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.001400 |  0.000100 | -0.000200 |
| internal_migration - Italy | - |  - |  -0.000000 |  -0.000000 |  -0.000000 |  0.000000 |  -0.000300 | -0.000000 |
| Free activity for a union | - |  - |  - |  0.002600 |  0.002500 |  0.475800 |  -0.092800 | 0.065400 |
| Free activities in voluntary associations | - |  - |  - |  - |  -0.000200 |  0.070700 |  0.116600 | 0.018800 |
| reach_difficulty - Municipal offices | - |  - |  - |  - |  - |  -0.037300 |  0.016600 | -0.007300 |
| Free activities in non voluntary associations | - |  - |  - |  - |  - |  - |  -0.242400 | -0.017600 |
| reach_difficulty - Food stores, markets | - |  - |  - |  - |  - |  - |  - | 0.008600 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_albania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_albania_.png)

Tunisia, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.734100 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.040500 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.997800 |  0.994600 |  0.994600 |  0.997800 |  0.998000 |  0.997800 |  0.997000 | 0.996500 |
| **R2_adj** | 0.997800 |  0.994200 |  0.993900 |  0.997300 |  0.997300 |  0.996900 |  0.995400 | 0.994100 |
| **MAE** | 823.375500 |  1398.620800 |  1375.318600 |  786.114700 |  816.386000 |  823.375500 |  989.676800 | 1054.537500 |
| **MPE** | 1.350600 |  0.987800 |  0.933500 |  1.969500 |  1.640500 |  1.350600 |  0.741000 | -0.440800 |
| **MAPE** | 4.302800 |  9.689300 |  9.653500 |  4.223500 |  3.909100 |  4.302800 |  5.014700 | 6.055200 |
| a Centro | -0.486500 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -0.487200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.297000 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.330400 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -0.732300 |  - |  - |  - |  - |  - |  - | - |
| Accommodation and catering services | - |  0.000300 |  0.000300 |  -0.000700 |  -0.001200 |  -0.001000 |  -0.000700 | -0.000200 |
| Free activity for a union | - |  - |  -0.000000 |  -0.010700 |  -0.012000 |  -0.007400 |  -0.008500 | -0.006200 |
| political_info - Every day | - |  - |  - |  0.000400 |  0.000800 |  -0.000700 |  0.000300 | 0.000300 |
| Meetings in ecological associations, for civil rights, for peace | - |  - |  - |  - |  -0.009000 |  0.014300 |  0.000200 | -0.001500 |
| Free activities in voluntary associations | - |  - |  - |  - |  - |  0.002000 |  0.000500 | 0.000100 |
| native population - Total | - |  - |  - |  - |  - |  - |  -0.000000 | -0.000000 |
| Housing, water, electricity, gas and other fuels | - |  - |  - |  - |  - |  - |  - | -0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_tunisia_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_tunisia_.png)

Egypt, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.665600 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 6.975600 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.999300 |  0.724400 |  0.997600 |  0.999000 |  0.999400 |  0.999300 |  0.992200 | 0.969600 |
| **R2_adj** | 0.999300 |  0.707200 |  0.997200 |  0.998800 |  0.999200 |  0.999100 |  0.988000 | 0.948300 |
| **MAE** | 685.123900 |  9766.861300 |  1248.244200 |  705.672900 |  695.841600 |  685.123900 |  1813.740800 | 3965.482900 |
| **MPE** | 11.248800 |  12.849800 |  10.812200 |  11.649900 |  11.239900 |  11.248800 |  -0.443200 | 27.715600 |
| **MAPE** | 13.287300 |  25.543000 |  15.898600 |  12.377200 |  13.312500 |  13.287300 |  10.854200 | 27.715600 |
| a Centro | -0.686400 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -1.867000 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.922200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.083200 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -1.621300 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.000000 | 0.000100 |
| Free activities in voluntary associations | - |  - |  -0.002000 |  -0.002300 |  -0.001400 |  -0.001600 |  0.000500 | 0.001300 |
| Free activity for a union | - |  - |  - |  0.002200 |  0.004100 |  0.002900 |  0.021500 | -0.031200 |
| work_satisfaction - Not | - |  - |  - |  - |  -0.019700 |  -0.019900 |  -0.011200 | -0.018100 |
| reach_difficulty - Municipal offices | - |  - |  - |  - |  - |  0.000100 |  -0.001500 | 0.004400 |
| native population - Total | - |  - |  - |  - |  - |  - |  0.000000 | -0.000000 |
| Meetings in cultural, recreational or other associations | - |  - |  - |  - |  - |  - |  - | -0.004900 |
![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_egypt_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_egypt_.png)

Ecuador, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.284300 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.024800 |

| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.996100 |  0.396900 |  0.983100 |  0.995300 |  0.997200 |  0.996100 |  0.997500 | 0.996700 |
| **R2_adj** | 0.996100 |  0.359200 |  0.980900 |  0.994300 |  0.996400 |  0.994500 |  0.996100 | 0.994400 |
| **MAE** | 1014.877800 |  13130.880600 |  2519.719600 |  1334.395600 |  946.285400 |  1014.877800 |  817.274000 | 1041.463100 |
| **MPE** | 5.144200 |  -23.632700 |  2.883500 |  4.662200 |  5.143000 |  5.144200 |  0.208400 | -10.271100 |
| **MAPE** | 6.262900 |  86.942000 |  18.208700 |  14.414200 |  6.166600 |  6.262900 |  3.943600 | 11.271500 |
| a Centro | -1.303000 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -3.697400 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -1.855900 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.222400 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -3.512400 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000100 |  0.000100 |  0.000100 |  0.000200 |  0.000100 | 0.000100 |
| Free activities in voluntary associations | - |  - |  -0.004200 |  -0.005400 |  -0.004500 |  -0.008900 |  -0.001800 | -0.003400 |
| Meetings in ecological associations, for civil rights, for peace | - |  - |  - |  0.005100 |  0.012400 |  0.023200 |  0.008900 | 0.027300 |
| Average monthly expenditure for housing | - |  - |  - |  - |  -0.086200 |  -2.111100 |  0.150400 | -0.296900 |
| work_satisfaction - Quite | - |  - |  - |  - |  - |  0.440000 |  -0.055700 | 0.044900 |
| Health services and health expenditure | - |  - |  - |  - |  - |  - |  -0.001200 | 0.000000 |
| political_info - Every day | - |  - |  - |  - |  - |  - |  - | -0.000900 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_ecuador_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_ecuador_.png)

Peru, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.513300 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.023900 |


| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.997400 |  0.676300 |  0.992200 |  0.994500 |  0.985700 |  0.997400 |  0.914900 | 0.931800 |
| **R2_adj** | 0.997400 |  0.656100 |  0.991200 |  0.993300 |  0.981400 |  0.996300 |  0.868500 | 0.884000 |
| **MAE** | 913.316600 |  11646.324700 |  2024.001700 |  1918.997200 |  2769.531300 |  913.316600 |  5189.721100 | 5388.658000 |
| **MPE** | -2.643100 |  -18.961600 |  -7.276500 |  -6.460300 |  -6.849700 |  -2.643100 |  -11.547800 | -4.360600 |
| **MAPE** | 4.878800 |  65.822700 |  32.231700 |  30.589800 |  31.718500 |  4.878800 |  27.689200 | 23.148600 |
| a Centro | -0.607700 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -2.679200 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -1.217100 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.242000 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -2.030300 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.000300 |  -0.000000 | 0.000000 |
| Furniture, articles and services for the house | - |  - |  -0.002600 |  -0.004500 |  -0.003600 |  0.107700 |  -0.002900 | -0.007900 |
| Communications | - |  - |  - |  0.002700 |  0.002000 |  -0.005200 |  0.008100 | 0.009300 |
| Free activities in non voluntary associations | - |  - |  - |  - |  -0.001200 |  0.065100 |  0.010300 | 0.007800 |
| Education | - |  - |  - |  - |  - |  -1.113900 |  -0.054700 | -0.022500 |
| work_satisfaction - Not | - |  - |  - |  - |  - |  - |  -0.036600 | 0.148400 |
| Average monthly expenditure for housing | - |  - |  - |  - |  - |  - |  - | -0.367200 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_peru_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_peru_.png)

China, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.724900 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.024900 |


| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.998500 |  0.985900 |  0.995000 |  0.995700 |  0.995300 |  0.998500 |  0.997900 | 0.997900 |
| **R2_adj** | 0.998500 |  0.985100 |  0.994300 |  0.994800 |  0.993800 |  0.997900 |  0.996800 | 0.996500 |
| **MAE** | 1908.844100 |  5668.396900 |  3792.519700 |  3414.192700 |  3372.068800 |  1908.844100 |  2093.374600 | 2004.988200 |
| **MPE** | -0.611700 |  -0.072200 |  -0.680700 |  -0.692700 |  -0.098700 |  -0.611700 |  -2.655000 | -4.596300 |
| **MAPE** | 3.707400 |  12.836500 |  11.028100 |  10.771400 |  8.018400 |  3.707400 |  4.245700 | 5.858000 |
| a Centro | -0.354500 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -0.862100 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.353600 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.326200 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -0.643100 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000100 | 0.000000 |
| Alcoholic beverages and tobacco | - |  - |  -0.000800 |  -0.004100 |  -0.069300 |  -0.102100 |  -0.060700 | -0.007800 |
| Communications | - |  - |  - |  0.002000 |  0.053100 |  0.080900 |  0.038700 | 0.006300 |
| Furniture, articles and services for the house | - |  - |  - |  - |  -0.008300 |  -0.013500 |  0.000300 | -0.001100 |
| reach_difficulty - Pharmacy | - |  - |  - |  - |  - |  -0.000200 |  0.001200 | 0.001200 |
| Free activities in voluntary associations | - |  - |  - |  - |  - |  - |  -0.005100 | 0.000200 |
| native population - Total | - |  - |  - |  - |  - |  - |  - | -0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_china_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_china_.png)

Philippines, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?%5Cbeta) | 0.580000 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 7.026200 |


| Var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| **R2** | 0.997200 |  0.913200 |  0.992700 |  0.992500 |  0.997100 |  0.997200 |  0.998100 | 0.981400 |
| **R2_adj** | 0.997200 |  0.907800 |  0.991700 |  0.990900 |  0.996200 |  0.996000 |  0.997100 | 0.968400 |
| **MAE** | 1430.389200 |  8816.779800 |  2669.732000 |  2550.870200 |  1426.221300 |  1430.389200 |  1187.710800 | 3975.159600 |
| **MPE** | -0.790000 |  -1.506600 |  -0.300500 |  -0.729500 |  -0.409400 |  -0.790000 |  0.695200 | 13.254200 |
| **MAPE** | 3.936500 |  25.240200 |  10.788200 |  10.430000 |  4.269200 |  3.936500 |  3.474000 | 13.254200 |
| a Centro | -0.448000 |  - |  - |  - |  - |  - |  - | - |
| a Isole | -1.310900 |  - |  - |  - |  - |  - |  - | - |
| a Nord-est | -0.813800 |  - |  - |  - |  - |  - |  - | - |
| a Nord-ovest | -0.373900 |  - |  - |  - |  - |  - |  - | - |
| a Sud | -1.221200 |  - |  - |  - |  - |  - |  - | - |
| internal_migration - Foreign country | - |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.000000 | 0.000000 |
| Recreation, shows and culture | - |  - |  -0.001000 |  -0.000500 |  0.017700 |  0.016400 |  0.006800 | 0.014800 |
| Clothing and footwear | - |  - |  - |  -0.000500 |  -0.006000 |  -0.005000 |  0.004300 | 0.001600 |
| Accommodation and catering services | - |  - |  - |  - |  -0.014200 |  -0.013600 |  -0.005000 | -0.009900 |
| Born alive | - |  - |  - |  - |  - |  -0.000000 |  0.000000 | 0.000000 |
| Food and non-alcoholic beverages | - |  - |  - |  - |  - |  - |  -0.002100 | -0.002300 |
| Pay money to an association | - |  - |  - |  - |  - |  - |  - | -0.000700 |
![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_philippines_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/R2_trend_spatial_autocorr_model_philippines_.png)


## Other Forecasting methods for time serie

In order to understand if it is possible to achieve similar results using simpler methods, two of the most used time-series methods for forecasting are implemented: Simple Moving Average (SMA) and Exponential Smoothing (ES). Follows the results.

### SMA

| Country | **MAE** | **MPE** | **MAPE** |
|---|---|---|---|
| Romania | 74943.044444 |  36.364396 |  36.364396 |
| Morocco | 9959.074074 |  14.868793 |  15.131271 |
| Albania | 10197.348148 |  11.223284 |  11.246509 |
| Tunisia | 1404.488889 |  4.815107 |  8.095811 |
| Egypt | 5508.059259 |  38.099369 |  38.099369 |
| Ecuador | 2189.970370 |  12.887097 |  12.938755 |
| Peru | 4672.696296 |  18.636773 |  18.636773 |
| China | 15906.792593 |  28.914539 |  28.914539 |
| Philippines | 8715.185185 |  25.634843 |  25.634843 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_romania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_morocco_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_albania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_tunisia_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_egypt_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_ecuador_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_peru_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_china_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/SMA_2005_2016/SMA_philippines_zones.png)



### ES

<table>
  <tr style="font-weight:bold">
    <td>Country</td>
    <td colspan="4">**MAE**</td>
    <td colspan="4">**MPE**</td>
    <td colspan="4">**MAPE**</td>
  </tr>
  <tr style="font-weight:bold">
    <td > Alpha </td>
    <td > .5 </td>
    <td > .65 </td>
    <td > .8 </td>
    <td > .95 </td>
    <td > .5 </td>
    <td > .65 </td>
    <td > .8 </td>
    <td > .95 </td>
    <td > .5 </td>
    <td > .65 </td>
    <td > .8 </td>
    <td > .95 </td>
  </tr>
  <tr>
    <td > Romania </td>
    <td > 32955.4013 </td>
    <td > 28003.7612 </td>
    <td > 24711.5463 </td>
    <td > 22213.5109 </td>
    <td > 23.45 </td>
    <td > 19.4462 </td>
    <td > 16.6643 </td>
    <td > 14.6081 </td>
    <td > 23.9909 </td>
    <td > 20.7964 </td>
    <td > 18.7528 </td>
    <td > 17.1427 </td>
 <tr>
 <tr>
    <td > Morocco </td>
    <td > 6682.7207 </td>
    <td > 5989.0264 </td>
    <td > 5545.7767 </td>
    <td > 5214.6405 </td>
    <td > 7.8055 </td>
    <td > 6.1918 </td>
    <td > 5.1051 </td>
    <td > 4.3271 </td>
    <td > 8.8426 </td>
    <td > 7.8167 </td>
    <td > 7.1769 </td>
    <td > 6.6941 </td>
 <tr>
 <tr>
    <td > Albania </td>
    <td > 6955.5154 </td>
    <td > 6150.2918 </td>
    <td > 5578.5362 </td>
    <td > 5182.3615 </td>
    <td > 6.2386 </td>
    <td > 4.8868 </td>
    <td > 3.9823 </td>
    <td > 3.3363 </td>
    <td > 7.1969 </td>
    <td > 6.437 </td>
    <td > 5.889 </td>
    <td > 5.4836 </td>
 <tr>
 <tr>
    <td > Tunisia </td>
    <td > 1645.0713 </td>
    <td > 1486.2055 </td>
    <td > 1378.05 </td>
    <td > 1326.8545 </td>
    <td > 3.0166 </td>
    <td > 2.3431 </td>
    <td > 1.9045 </td>
    <td > 1.5932 </td>
    <td > 8.211 </td>
    <td > 7.5533 </td>
    <td > 7.1339 </td>
    <td > 6.9416 </td>
 <tr>
 <tr>
    <td > Egypt </td>
    <td > 2395.4524 </td>
    <td > 2189.7131 </td>
    <td > 2040.1306 </td>
    <td > 1924.7865 </td>
    <td > 13.2605 </td>
    <td > 11.0599 </td>
    <td > 9.455 </td>
    <td > 8.2349 </td>
    <td > 16.8895 </td>
    <td > 15.6183 </td>
    <td > 14.6928 </td>
    <td > 13.9876 </td>
 <tr>
 <tr>
    <td > Ecuador </td>
    <td > 1587.0311 </td>
    <td > 1421.4098 </td>
    <td > 1296.1294 </td>
    <td > 1219.8557 </td>
    <td > 7.8424 </td>
    <td > 6.1588 </td>
    <td > 5.0338 </td>
    <td > 4.23 </td>
    <td > 9.4241 </td>
    <td > 8.4047 </td>
    <td > 7.7435 </td>
    <td > 7.3468 </td>
 <tr>
 <tr>
    <td > Peru </td>
    <td > 1991.1991 </td>
    <td > 1654.3821 </td>
    <td > 1473.3755 </td>
    <td > 1387.0943 </td>
    <td > 9.5488 </td>
    <td > 7.5221 </td>
    <td > 6.1543 </td>
    <td > 5.1834 </td>
    <td > 10.1769 </td>
    <td > 8.7867 </td>
    <td > 8.142 </td>
    <td > 7.7737 </td>
 <tr>
 <tr>
    <td > China </td>
    <td > 5543.2813 </td>
    <td > 4582.4997 </td>
    <td > 3920.3913 </td>
    <td > 3602.3217 </td>
    <td > 13.9338 </td>
    <td > 11.3141 </td>
    <td > 9.4868 </td>
    <td > 8.1446 </td>
    <td > 14.3419 </td>
    <td > 12.2095 </td>
    <td > 10.7486 </td>
    <td > 9.9299 </td>
 <tr>
 <tr>
    <td > Philippines </td>
    <td > 2896.8385 </td>
    <td > 2327.568 </td>
    <td > 2036.0115 </td>
    <td > 1898.881 </td>
    <td > 10.8173 </td>
    <td > 8.7033 </td>
    <td > 7.22 </td>
    <td > 6.1298 </td>
    <td > 10.8173 </td>
    <td > 8.7965 </td>
    <td > 7.7668 </td>
    <td > 7.1522 </td>
 <tr>
</table>


![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_romania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_morocco_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_albania_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_tunisia_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_egypt_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_ecuador_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_peru_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_china_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/ES_2005_2016/ES_philippines_zones.png)


## Conclusion (?)

From the previous section, it is possible to conclude that adding features or using more sophisticated models does not improve significantly the performance in terms of prediction nor in terms of interpretation.

#### Romania

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_romania.png)

#### Morocco

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_morocco.png)

#### Albania
![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_albania.png)

#### Tunisia

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_tunisia.png)

#### Egypt

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_egypt.png)

#### Ecuador

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_ecuador.png)

#### Peru

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_peru.png)

#### China

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_china.png)

#### Philippines

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Models_compar/models_mae_mape_philippines.png)