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

![](https://latex.codecogs.com/gif.latex?y_%7Bi%2Ct%7D%20%3D%20%5Cbeta%5ET%20x_%7Bi%2C%20t%7D%20&plus;%20%5Cepsilon_%7Bi%2Ct%7D)

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

Romania, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.084| 1.359 | 1.186 | 1.068 | 0.974 | 0.799 | 0.687 | 0.838 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D)  | | -0.308 | -0.210 | -0.202 | -0.190 |  -0.171 | -0.032 | 0.006 |
| Average age of mothers at birth  | | | 524.506 | 55284.921 | 74630.324 | 32634.865 | 42023.009 | |
| Average age of fathers at birth | |  | | -49289.944 | -66271.533 | -30346.083 | -39339.754 | |
| Free activities in voluntary associations | | | | 19.771 | 44.505 | -0.775 | 18.446 | -15.847 |
| Communications | | | | | -100.724 | -869.426 | -163.744 | |
| Other goods and services | | | | | 16.786 | 299.458 | 247.428 | |
| Disposable Income | | | | | | 18.357 | 32.520 | 19.498 |
| Reach_difficulty - Pharmacy | | | | | | -56.561 | -39.905 | |
| Internal_migration - Foreign country | | | | |  | -0.840 | -1.165 | |
| Transport | | | | | | | -43.753 | |
| Reach_difficulty - Emergency room | | | | | | | 27.943 | 8.721 |
| Unemployment - Total | | | | | | | -109.413 | -60.310 |
| Born alive | | | | | | | -0.810 | |
| Clothing and footwear | | | | | | | -197.273 | |
| Native population - Total  | | | | | | | | -0.012 |
| Meetings in cultural, recreational or other associations  | | | | | | | | 43.804 |
| Average monthly expenditure for housing  | | | | | | | | -51-706 |
| **R-squared** | 0.982  |  0.984 | 0.986  | 0.987  |  0.987 |  0.985 |  0.990 | 0.986  |
| **Adj R-squared** | 0.982  |  0.984 | 0.986  | 0.986  | 0.987  | 0.985  |  0.990 |  0.986 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_romania__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_romania_2zones.png)

Morocco, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.043 | 1.346 | 1.188 | 0.941 | 0.946 | 0.624 | 0.541 | 0.685 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | | -0.320 | -0.237 | -0.099 | -0.116 | 0.390 | 0.483 | 0.250 |
| Free activities in voluntary associations | | | 7.301 | 40.489 | 45.084 | 9.580 | -8.331 | 10.240 |
| Internal_migration - Foreign country | | | | -0.170 | -0.156 | -0.666 | -0.498 | |
| Native population - Total | | | | -0.001 | -0.001 | 0.004 | -0.002 | 0.001 |
| Free activities in non voluntary associations | | | | | -31.145 | 33.851 | 15.454 | |
| Meetings in cultural, recreational or other associations | | | | | 9.237 | -12.697 | 15.807 | 5.075 |
| Internal_migration - Italy | | | | | | -0.011 | -0.111 | |
| Political_info - Some times in a week | | | | | | 19.406 | 24.884 | |
| Pay money to an association | | | | | | 23.873 | 19.558 | |
| Reach_difficulty - Supermarket | | | | | | | 24.042 | |
| Reach_difficulty - Post offices | | | | | | | -14.270 | |
| Born alive | | | | | | | -0.012 | |
| Disposable Income | | | | | | | -3.921 | -3.179 |
| Political_info - Every day | | | | | | | -1.001 | |
| Average monthly expenditure for housing  | | | | | | | | -126.261 |
| Unemployment - Total | | | | | | | | -20.336 |
| Reach_difficulty - Emergency room  | | | | | | | | 10.584 |
| **R-squared** | 0.996 |  0.996 | 0.997 | 0.996  |  0.996 |  0.996 |  0.997 | 0.997  |
| **Adj R-squared** | 0.996 |  0.996 | 0.997  | 0.996 | 0.996  | 0.996  |  0.997 |  0.997 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_morocco__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_morocco_2zones.png)


Albania, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.049 | 1.568 | 1.537 | 1.471 | 1.34 | 1.164 | 0.449 | 1.153 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | | -0.552 | -0.534 | -0.479 | -0.344 | -0.098 | 0.557 | -0.153 |
| Native population - Total | | | 0.001 | -0.001 | 0.001 | -0.001 | 0.002 | 0.002 |
| Internal_migration - Foreign country | | | | -0.111 | -0.229 | -0.301 | -0.440 | |
| Free activities in voluntary associations | | | | 12.233 | 7.609 | 23.119 | -4.664 | -0.336 |
| Disposable Income  | | | | | -3.684 | -7.379 | -4.214 | -1.713 |
| Political_info - Every day | | | | | 7.635 | 7.760 | -1.752 | |
| Reach_difficulty - Supermarket  | | | | | | -3.932 | -1.432 | |
| Born alive | | | | | | 0.473 | 0.100 | |
| Free activities in non voluntary associations | | | | | | -42.284 | -38.935 | |
| Reach_difficulty - Pharmacy | | | | | | | 0.452 | |
| Political_info - Never | | | | | | | -7.226 | |
| Political_info - Some times in a week | | | | | | | 11.357 | |
| Pay money to an association | | | | | | | 25.832 | |
| Meetings in cultural, recreational or other associations | | | | | | | 2.164 | -2.775 |
| Average monthly expenditure for housing | | | | | | | | 188.830 |
| Unemployment - Total | | | | | | | | -19.643 |
| Reach_difficulty - Emergency room | | | | | | | | 1.174 |
| **R-squared** | 0.996 |  0.998 | 0.998  | 0.997  |  0.998 |  0.998 |  0.998 | 0.998 |
| **Adj R-squared** | 0.996 |  0.998 | 0.998 | 0.997  | 0.998  | 0.998  |  0.998 |  0.998 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_albania__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_albania_2zones.png)


Tunisia, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.015 | 1.131 | 0.956 | 0.542 | 0.530 | 0.823 | 0.234 | 0.406 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D)  | | -0.119 | -0.044 | 0.415 | 0.396 |  0.069 | 0.623 | 0.298 |
| Pay money to an association | | | 1.204 | 6.724 | 5.956 | 4.273 | 6.650 |  |
| Internal_migration - Foreign country | | | | -0.129 | -0.146 | -0.209 | -0.152 | |
| Native population - Total  | | | | -0.001 | -0.001 | 0.001 | 0.001 | -0.001 |
| Free activities in voluntary associations | | | |  | 2.259 | 4.978 |  -0.837 | 2.873|
| Meetings in cultural, recreational or other associations  | | | | | 1.895 | -1.273 | 2.292 | 7.529 |
| Free activities in non voluntary associations  | | | | |  | -4.278 | -24.446 | |
| Reach_difficulty - Post offices | | | | | |   -4.160 | -0.495 | |
| Political_info - Never | | | | | |  -2.871 | -2.295 | |
| Internal_migration - Italy | | | | |  |  | 0.011 | |
| Reach_difficulty - Pharmacy | | | | |  | | 3.409 | |
| Born alive | | | | |  | | -0.050 | |
| Accommodation and catering services  | | | | |  | | 9.149 | |
| Political_info - Every day | | | | |  | | 1.491 | |
| Disposable Income | | | | |  | |  | -0.802 |    
| Average monthly expenditure for housing  | | | | | | | | 577.273 |
| Unemployment - Total  | | | | | | | | -4.704 |
| Reach_difficulty - Emergency room  | | | | | | | | 2.717 |
| **R-squared** | 0.991  |  0.991 | 0.992  | 0.993  |  0.993 |  0.993 |  0.983 | 0.994  |
| **Adj R-squared** | 0.991  |  0.991 | 0.991  | 0.993  | 0.993  | 0.993  |  0.983 |  0.994 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_tunisia__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_tunisia_2zones.png)


Egypt, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.039 | 0.893 | 0.876 | 0.783 | 0.595 | 0.374 | 0.321 | 0.591 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D)  | | 0.153 | 0.154 | 0.214 | 0.487 |  0.618 | 0.653 | 0.479 |
| Native population - Total | | | 0.001 | -0.001 | -0.001 | -0.002 | -0.002 | 0.001 |
| Pay money to an association| | | | 1.965 | 8.469 | 9.821 | 13.464 | |
| Non food | | | | -0.091 | 0.079 | 0.033 | 3.264 |  |
| Internal_migration - Foreign country | | | | | -0.203 | -0.238 | -0.222 |  |
| Free activities in voluntary associations  | | | | | 0.845 | 12.995 | 3.014 | -1.334 |
| Internal_migration - Italy  | | | | |  | 0.043 | 0.048 | |
| Reach_difficulty - Post offices | | | | |  | 5.431 | 9.096 | |
| Meetings in cultural, recreational or other associations| | | | |  | -11.948 | -15.948 | 0.078 |
| Other goods and services | | | | |  | | -24.446 | |
| Communications| | | | |  | | -35.374 | |
| Food and non-alcoholic beverages | | | | |  | | 3.052 | |
| Accommodation and catering services    | | | | |  | | 17.723 |  |    
| Transport | | | | |  | | -6.712 |  |
| Disposable Income | | | | |  | |  | -1.861 |    
| Average monthly expenditure for housing  | | | | | | | | 45.317 |
| Unemployment - Total  | | | | | | | | -10.960 |
| Reach_difficulty - Emergency room  | | | | | | | | 5.683 |
| **R-squared** | 0.984  |  0.983 | 0.983  | 0.984  |  0.983 |  0.983 |  0.966 | 0.979  |
| **Adj R-squared** | 0.983  |  0.983 | 0.983  | 0.983  | 0.983  | 0.983  |  0.966 |  0.979 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_egypt__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_egypt_2zones.png)


Ecuador, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.055 | 1.567 | 1.546 | 1.385 | 1.426 | 1.141 | 1.176 | 1.386 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D)  | | -0.557 | -0.545 | -0.359 | -0.398 |  -0.164 | -0.173 | -0.344 |
| Native population - Total | | | 0.001 | -0.001 | 0.001 | 0.001 | 0.002 | 0.001 |
| Internal_migration - Foreign country| | | | -0.085 | -0.102 | -0.130 | -0.064 | |
| Pay money to an association | | | | 3.849 | 3.787 | 8.274 | 3.038 |  |
| Reach_difficulty - Post offices | | | | | -2.999 | -2.086 | -3.835 |  |
| Free activities in voluntary associations  | | | | | -1.029 | 7.536 | 3.446 | -1.669 |
| Internal_migration - Italy  | | | | |  | 0.0153| -0.036 | |
| Accommodation and catering services | | | | |  | 1.455 | 14.394 | |
| Meetings in cultural, recreational or other associations| | | | |  | -18.261 | -5.907 | -2.456 |
| Other goods and services | | | | |  | | -8.600 | |
| Non food | | | | |  | | 1.664 | |
| Reach_difficulty - Supermarket  | | | | |  | | 7.971 | |    
| Transport | | | | |  | | -13.838 |  |
| Disposable Income | | | | |  | | -2.420 | -1.205 |    
| Average monthly expenditure for housing  | | | | | | | | 68.382 |
| Unemployment - Total  | | | | | | | | -5.074 |
| Reach_difficulty - Emergency room  | | | | | | | | -0.631 |
| **R-squared** | 0.990  |  0.993 | 0.993  | 0.993  |  0.993 |  0.994 |  0.994 | 0.994  |
| **Adj R-squared** | 0.989  |  0.993 | 0.993  | 0.993  | 0.993  | 0.994  |  0.994 |  0.993 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_ecuador__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_ecuador_2zones.png)


Peru, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.075 | 1.284 | 1.259 | 1.262 | 0.890 | 0.859 | 0.782 | 0.968 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D)  | | -0.228 | -0.212 | -0.182 | 0.246 |  0.279 | 0.305 | 0.130 |
| Native population - Total | | | 0.001 | -0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| Internal_migration - Foreign country| | | | -0.104 | -0.141| -0.112 | -0.167 | |
| Free activities in voluntary associations | | | | 7.768 | 2.849 | 5.315 | 1.910 | -2.678 |
| Pay money to an association | | | | | 4.168 | 4.791 | 6.407 |  |
| Disposable Income  | | | | | -0.699 | -0.779 | 0.237 | -0.834 |
| Internal_migration - Italy  | | | | |  | -0.012 | 0.001 | |
| Reach_difficulty - Post offices | | | | |  | 2.851 | -1.086 | |
| Meetings in cultural, recreational or other associations| | | | |  | -3.296 | -1.106 | 3.208 |
| Reach_difficulty - Supermarket  | | | | |  | | 6.476 | |
| Non food | | | | |  | | -0.074 | |
| Born alive  | | | | |  | | -0.195 | |    
| Political_info - Every day | | | | |  | | -0.148 |  |
| Free activities in non voluntary associations | | | | |  | | 2.6954   |    
| Average monthly expenditure for housing  | | | | | | | | -11.476 |
| Unemployment - Total  | | | | | | | | -3.698 |
| Reach_difficulty - Emergency room  | | | | | | | | 2.439 |
| **R-squared** | 0.994  |  0.995 | 0.995  | 0.994  |  0.993 |  0.994 |  0.986 | 0.995  |
| **Adj R-squared** | 0.984  |  0.994 | 0.995  | 0.993  | 0.993  | 0.994  |  0.985 |  0.995 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_peru__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_peru_2zones.png)


China, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.087 | 1.041 | 0.900 | 0.515 | 0.481 | 0.405 | 0.426 | 0.390 |
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | | 0.0500 | 0.152 | 0.488 | 0.512 | 0.463 | 0.539 | 0.690 |
| Born alive | | | 0.017 | 0.127 | 0.099 | 0.022 | -0.176 | |
| Internal_migration - Foreign country | | | | 0.094 | 0.101 | 0.060 | -0.178 | |
| Political_info - Some times in a week | | | | 6.394 | -6.785 | -5.820 | -4.261 | |
| Reach_difficulty - Pharmacy | | | | | 2.774 | 1.152 | 9.618 | |
| Free activities in voluntary associations | | | | | 1.093 | -4.378 | -0.315 | -2.807 |
| Reach_difficulty - Post offices  | | | | |  | -1.016 | -16.002 | |
| Political_info - Every day | | | | |  |  4.834 | 3.677 | |
| Meetings in cultural, recreational or other associations | | | | |  | 2.997 | -7.571 | 2.342 |
| Native population - Total | | | | |  | | 0.002 | 0.001 |
| Reach_difficulty - Emergency room | | | | |  | |  | |
| Disposable Income | | | | |  | | -0.058 | -0.975 |    
| Pay money to an association | | | | |  | | 8.923 |  |  
| Average age of fathers at birth | | | | |  | | -104.609 |  |  
| Average monthly expenditure for housing  | | | | | | | | 150.086 |
| Unemployment - Total  | | | | | | | | -13.276 |
| Reach_difficulty - Emergency room  | | | | | | | 6.368 | 3.281 |
| **R-squared** | 0.995  |  0.995 | 0.995 | 0.993 |  0.993 |  0.991 |  0.996 | 0.994 |
| **Adj R-squared** | 0.995 |  0.995 | 0.995  | 0.993  | 0.993  | 0.991  |  0.996 |  0.994 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_china__zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/regression_model_china_2zones.png)


Philippines, Training 2005-2013 models

| Indep. var.  | I | II | III | IV | V | VI | VII | VIII |
|---|---|---|---|---|---|---|---|---|
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-1%7D) | 1.063 | 0.955 | 0.918 | 0.699 | 0.761 | 0.610 | 0.762 | 0.633 |  
| ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t-2%7D) | | 0.142 | 0.137 | 0.202 | 0.221 | 0.347 | 0.284 | 0.473 |  
| Native population - Total | | | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 | 0.001 |
| Internal_migration - Foreign country | | | | 0.064 | 0.008 | -0.065 | -0.203 |  |
| Other goods and services  | | | | -6.116 | 10.469 | 12.515 | 10.231 |  |  
| Communications | | | | | -18.917 | -17.420 | -9.230 |  |  
| Non food | | | | | -0.679 | -0.141 | -1.418 |  |  
| Housing, water, electricity, gas and other fuels | | | | |  | -1.611 | 0.721 |  |  
| Accommodation and catering services | | | | |  | -8.049| 11.558 |  |  
| Free activities in voluntary associations| | | | |  | 11.167 | 5.669 | -3.116 |  
| Reach_difficulty - Post offices | | | | |  | | 1.075 |  |  
| Born alive | | | | |  | | -0.086 |  |  
| Pay money to an association  | | | | |  | | 2.375 |  |  
| Average age of fathers at birth | | | | |  | | -166.873 |  |
| Food and non-alcoholic beverages | | | | |  | | -2.390 |  |   
| Meetings in cultural, recreational or other associations | | | | |  |  |  | 1.444 |
| Disposable Income | | | | |  | |  | -0.913 |   
| Average monthly expenditure for housing  | | | | | | | | 43.382 |
| Unemployment - Total  | | | | | | | | -5.443 |
| Reach_difficulty - Emergency room  | | | | | | |  | -1.299 |
| **R-squared** | 0.995  |  0.995 | 0.995 | 0.992 |  0.994 |  0.988 |  0.990 | 0.995 |
| **Adj R-squared** | 0.995 |  0.995 | 0.995  | 0.992  | 0.994  | 0.988  |  0.990 |  0.994 |

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
| ![](https://latex.codecogs.com/gif.latex?a_%7BCentro%7D) | -0.109700 |
| ![](https://latex.codecogs.com/gif.latex?a_%7BIsole%7D) | -0.110200 |
| ![](https://latex.codecogs.com/gif.latex?a_%7BNord%20%5C%20est%7D)  | -0.136800 |
| ![](https://latex.codecogs.com/gif.latex?a_%7BNord%20%5C%20ovest%7D) | -0.112800 |
| ![](https://latex.codecogs.com/gif.latex?a_%7BSud%7D) | -0.086300 |
| ![](https://latex.codecogs.com/gif.latex?%5Crho) | 6.865800 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.998800 |  0.998900 |  0.998900 |  0.998800 |  0.998400 |  0.998400 |  0.998700 |
| **R2_adj** | 0.998700 |  0.998800 |  0.998700 |  0.998400 |  0.997800 |  0.997800 |  0.997800 |
| Free activity for a union | 0.000200 |  0.000500 |  0.000400 |  -0.000800 |  0.001800 |  0.001800 |  0.000800 |
| Free activities in voluntary associations | nan |  -0.000000 |  -0.000100 |  0.000100 |  -0.000300 |  -0.000300 |  -0.000100 |
| Meetings in cultural, recreational or other associations | nan |  nan |  0.000000 |  -0.000300 |  0.002000 |  0.002000 |  0.000000 |
| Meetings in ecological associations, for civil rights, for peace | nan |  nan |  nan |  0.002000 |  -0.004900 |  -0.004900 |  0.000200 |
| Free activities in non voluntary associations | nan |  nan |  nan |  nan |  -0.002600 |  -0.002600 |  -0.000100 |
| political_info - Some times in a year | nan |  nan |  nan |  nan |  nan |  nan |  0.000000 |
| Recreation, shows and culture | nan |  nan |  nan |  nan |  nan |  nan |  0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_romania_zones.png)


Morocco, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.814100 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.370600 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -0.614200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.211300 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.163000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -0.447700 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.041200 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.990600 |  0.998600 |  0.998700 |  0.999200 |  0.999200 |  0.999200 |  0.999100 |
| **R2_adj** | 0.990000 |  0.998400 |  0.998400 |  0.998900 |  0.998800 |  0.998800 |  0.998500 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  -0.000000 |  -0.000000 |  -0.000000 |  0.000000 |
| Free activity for a union | nan |  -0.001700 |  -0.001600 |  0.011300 |  0.015500 |  0.015500 |  0.001300 |
| Recreation, shows and culture | nan |  nan |  -0.000000 |  0.000900 |  0.001100 |  0.001100 |  0.000300 |
| reach_difficulty - Municipal offices | nan |  nan |  nan |  -0.000600 |  -0.000900 |  -0.000900 |  0.000200 |
| work_satisfaction - Not | nan |  nan |  nan |  nan |  0.004000 |  0.004000 |  -0.030800 |
| Pay money to an association | nan |  nan |  nan |  nan |  nan |  nan |  0.000000 |
| Education | nan |  nan |  nan |  nan |  nan |  nan |  0.001000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_Morocco_zones.png)


Albania, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.725800 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.368300 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -1.156500 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.342200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.292600 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -0.647900 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.043800 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.973600 |  0.994400 |  0.996300 |  0.996800 |  0.999800 |  0.999800 |  0.995400 |
| **R2_adj** | 0.971900 |  0.993700 |  0.995500 |  0.995800 |  0.999800 |  0.999800 |  0.992100 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.001400 |  -0.001400 |  -0.000200 |
| internal_migration - Italy | nan |  -0.000000 |  -0.000000 |  -0.000000 |  0.000000 |  0.000000 |  -0.000000 |
| Free activity for a union | nan |  nan |  0.002600 |  0.002500 |  0.475800 |  0.475800 |  0.065400 |
| Free activities in voluntary associations | nan |  nan |  nan |  -0.000200 |  0.070700 |  0.070700 |  0.018800 |
| reach_difficulty - Municipal offices | nan |  nan |  nan |  nan |  -0.037300 |  -0.037300 |  -0.007300 |
| Free activities in non voluntary associations | nan |  nan |  nan |  nan |  nan |  nan |  -0.017600 |
| reach_difficulty - Food stores, markets | nan |  nan |  nan |  nan |  nan |  nan |  0.008600 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_albania_zones.png)


Tunisia, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.734100 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.486500 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -0.487200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.297000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.330400 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -0.732300 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.040500 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.994600 |  0.994600 |  0.997800 |  0.998000 |  0.997800 |  0.997800 |  0.996500 |
| **R2_adj** | 0.994200 |  0.993900 |  0.997300 |  0.997300 |  0.996900 |  0.996900 |  0.994100 |
| Accommodation and catering services | 0.000300 |  0.000300 |  -0.000700 |  -0.001200 |  -0.001000 |  -0.001000 |  -0.000200 |
| Free activity for a union | nan |  -0.000000 |  -0.010700 |  -0.012000 |  -0.007400 |  -0.007400 |  -0.006200 |
| political_info - Every day | nan |  nan |  0.000400 |  0.000800 |  -0.000700 |  -0.000700 |  0.000300 |
| Meetings in ecological associations, for civil rights, for peace | nan |  nan |  nan |  -0.009000 |  0.014300 |  0.014300 |  -0.001500 |
| Free activities in voluntary associations | nan |  nan |  nan |  nan |  0.002000 |  0.002000 |  0.000100 |
| native population - Total | nan |  nan |  nan |  nan |  nan |  nan |  -0.000000 |
| Housing, water, electricity, gas and other fuels | nan |  nan |  nan |  nan |  nan |  nan |  -0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_tunisia_zones.png)


Egypt, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.665600 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.686400 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -1.867000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.922200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.083200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -1.621300 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 6.975600 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.724400 |  0.997600 |  0.999000 |  0.999400 |  0.999300 |  0.999300 |  0.969600 |
| **R2_adj** | 0.707200 |  0.997200 |  0.998800 |  0.999200 |  0.999100 |  0.999100 |  0.948300 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000100 |
| Free activities in voluntary associations | nan |  -0.002000 |  -0.002300 |  -0.001400 |  -0.001600 |  -0.001600 |  0.001300 |
| Free activity for a union | nan |  nan |  0.002200 |  0.004100 |  0.002900 |  0.002900 |  -0.031200 |
| work_satisfaction - Not | nan |  nan |  nan |  -0.019700 |  -0.019900 |  -0.019900 |  -0.018100 |
| reach_difficulty - Municipal offices | nan |  nan |  nan |  nan |  0.000100 |  0.000100 |  0.004400 |
| native population - Total | nan |  nan |  nan |  nan |  nan |  nan |  -0.000000 |
| Meetings in cultural, recreational or other associations | nan |  nan |  nan |  nan |  nan |  nan |  -0.004900 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_egypt_zones.png)


Ecuador, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.284300 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -1.303000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -3.697400 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -1.855900 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.222400 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -3.512400 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.024800 |

| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.396900 |  0.983100 |  0.995300 |  0.997200 |  0.996100 |  0.996100 |  0.996700 |
| **R2_adj** | 0.359200 |  0.980900 |  0.994300 |  0.996400 |  0.994500 |  0.994500 |  0.994400 |
| internal_migration - Foreign country | 0.000000 |  0.000100 |  0.000100 |  0.000100 |  0.000200 |  0.000200 |  0.000100 |
| Free activities in voluntary associations | nan |  -0.004200 |  -0.005400 |  -0.004500 |  -0.008900 |  -0.008900 |  -0.003400 |
| Meetings in ecological associations, for civil rights, for peace | nan |  nan |  0.005100 |  0.012400 |  0.023200 |  0.023200 |  0.027300 |
| Average monthly expenditure for housing | nan |  nan |  nan |  -0.086200 |  -2.111100 |  -2.111100 |  -0.296900 |
| work_satisfaction - Quite | nan |  nan |  nan |  nan |  0.440000 |  0.440000 |  0.044900 |
| Health services and health expenditure | nan |  nan |  nan |  nan |  nan |  nan |  0.000000 |
| political_info - Every day | nan |  nan |  nan |  nan |  nan |  nan |  -0.000900 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_ecuador_zones.png)


Peru, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.513300 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.607700 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -2.679200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -1.217100 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.242000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -2.030300 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.023900 |


| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.676300 |  0.992200 |  0.994500 |  0.985700 |  0.997400 |  0.997400 |  0.931800 |
| **R2_adj** | 0.656100 |  0.991200 |  0.993300 |  0.981400 |  0.996300 |  0.996300 |  0.884000 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  0.000000 |  -0.000300 |  -0.000300 |  0.000000 |
| Furniture, articles and services for the house | nan |  -0.002600 |  -0.004500 |  -0.003600 |  0.107700 |  0.107700 |  -0.007900 |
| Communications | nan |  nan |  0.002700 |  0.002000 |  -0.005200 |  -0.005200 |  0.009300 |
| Free activities in non voluntary associations | nan |  nan |  nan |  -0.001200 |  0.065100 |  0.065100 |  0.007800 |
| Education | nan |  nan |  nan |  nan |  -1.113900 |  -1.113900 |  -0.022500 |
| work_satisfaction - Not | nan |  nan |  nan |  nan |  nan |  nan |  0.148400 |
| Average monthly expenditure for housing | nan |  nan |  nan |  nan |  nan |  nan |  -0.367200 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_peru_zones.png)


China, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.724900 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.354500 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -0.862100 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.353600 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.326200 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -0.643100 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.024900 |


| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.985900 |  0.995000 |  0.995700 |  0.995300 |  0.998500 |  0.998500 |  0.997900 |
| **R2_adj** | 0.985100 |  0.994300 |  0.994800 |  0.993800 |  0.997900 |  0.997900 |  0.996500 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |
| Alcoholic beverages and tobacco | nan |  -0.000800 |  -0.004100 |  -0.069300 |  -0.102100 |  -0.102100 |  -0.007800 |
| Communications | nan |  nan |  0.002000 |  0.053100 |  0.080900 |  0.080900 |  0.006300 |
| Furniture, articles and services for the house | nan |  nan |  nan |  -0.008300 |  -0.013500 |  -0.013500 |  -0.001100 |
| reach_difficulty - Pharmacy | nan |  nan |  nan |  nan |  -0.000200 |  -0.000200 |  0.001200 |
| Free activities in voluntary associations | nan |  nan |  nan |  nan |  nan |  nan |  0.000200 |
| native population - Total | nan |  nan |  nan |  nan |  nan |  nan |  -0.000000 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_china_zones.png)


Philippines, Training 2005-2013 models

| Var.  | Value |
|---|---|
| ![](https://latex.codecogs.com/gif.latex?% 5Cbeta) | 0.580000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BCentro % 7D) | -0.448000 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BIsole % 7D) | -1.310900 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20est % 7D) | -0.813800 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BNord % 20 % 5C % 20ovest % 7D) | -0.373900 |
| ![](https://latex.codecogs.com/gif.latex?a_ % 7BSud % 7D) | -1.221200 |
| ![](https://latex.codecogs.com/gif.latex?% 5Crho) | 7.026200 |


| Var.  | I | II | III | IV | V | VI | VII |
|---|---|---|---|---|---|---|---|
| **R2** | 0.913200 |  0.992700 |  0.992500 |  0.997100 |  0.997200 |  0.997200 |  0.981400 |
| **R2_adj** | 0.907800 |  0.991700 |  0.990900 |  0.996200 |  0.996000 |  0.996000 |  0.968400 |
| internal_migration - Foreign country | 0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |  0.000000 |
| Recreation, shows and culture | nan |  -0.001000 |  -0.000500 |  0.017700 |  0.016400 |  0.016400 |  0.014800 |
| Clothing and footwear | nan |  nan |  -0.000500 |  -0.006000 |  -0.005000 |  -0.005000 |  0.001600 |
| Accommodation and catering services | nan |  nan |  nan |  -0.014200 |  -0.013600 |  -0.013600 |  -0.009900 |
| Born alive | nan |  nan |  nan |  nan |  -0.000000 |  -0.000000 |  0.000000 |
| Food and non-alcoholic beverages | nan |  nan |  nan |  nan |  nan |  nan |  -0.002300 |
| Pay money to an association | nan |  nan |  nan |  nan |  nan |  nan |  -0.000700 |

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Paper_2005_2016/spatial_autocorr_model_philippines_zones.png)
