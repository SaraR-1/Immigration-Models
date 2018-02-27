# Immigration-Models

In this section, some attempts to replicate the model specified in the [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents) are performed.

As first the model introduced in the paper is replicated without including the spatial autocorrelation error model and the territory dependency in the parameters.

The model could be written as:

![](https://latex.codecogs.com/gif.latex?ln%28%5Cfrac%7Bn_%7Bi%2Ct%7D%7D%7Bn_%7BI%2Ct%7D%7D%29%20%3D%20%5Cbeta%20ln%28%5Cfrac%7Bn_%7Bi%2Ct-1%7D%7D%7Bn_%7BI%2Ct-1%7D%7D%29%20&plus;%20a%20&plus;%20v_%7Bi%2Ct%7D%2C%20%5Cforall%20i%20%5Cin%20%5B1%2C%20%5Cdots%2C%20I-1%5D%2C%20t%20%5Cin%20%5B1%2C%20%5Cdots%2C%20T%5D)

where:
- *I* is the reference territory
- ![](https://latex.codecogs.com/gif.latex?%5Cbeta) and *a* are the regression parameters, ![](https://latex.codecogs.com/gif.latex?%5Cbeta) can be interpreted as the network effect (is a local phenomenon that influences the immigrant choice, that is: foreign-born population tend to migrate to territories where a community of the same ethnic already exists)
- ![](https://latex.codecogs.com/gif.latex?%5Calpha_i%20%3D%20x%27_%7Bi%7D%20%5Ctheta%20&plus;%20%5Ceta) , ![](https://latex.codecogs.com/gif.latex?x%27_%7Bi%7D) is the vector of all the time invariant observable location factors, $\eta$ is an error random term
- ![](https://latex.codecogs.com/gif.latex?v_%7Bi%2Ct%7D%20%3D%20u_%7Bi%2Ct%7D%20-%20u_%7BI%2C%20t%7D), ![](https://latex.codecogs.com/gif.latex?u_%7Bi%2Ct%7D%20%5Csim%20N%280%2C%20%5Csigma%5E2%29) is an error random term

## Variable selection
On the [ISTAT website](http://dati.istat.it/#), it is possible to find some interesting features that could be included in the formulation of a model aim to explain the immigration flow to Italy.

To begin, an initial data filtering is performed. Only the data that are supposed to have a relation with the variable of interest are considered.

Some features can not be used, due to the availability of data:
- **Basic health care** only 2004-2013
- **Expenditure for intervections and social services** only 2013-2014
- **Expenditure for the house of families with foreign components** only at zones level in 2009
- **Aspect of dayli life - Interpersonal Trust** only from 2010
- **Hospitalizations** missing 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2016, 2017
- **Aspects of daily life - general life degree of satisfaction** missing 2003, 2004, 2005, 2006, 2007, 2008, 2009

Some others, due to statistical problems:
- **Economic situation opinions (Famigie per capacità di arrivare a fine mese)**: around 10.4% of data are not statistically significant and 4.6% do not reach the half of the minimun (ISTAT definition: Il dato si definisce poco significativo nel caso in cui corrisponda ad una numerosità campionaria compresa tra 20 e 49 unità.)
