# Immigration-Models

In this section, some attempts to replicate the model specified in the [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents) are performed.

As first the model introduced in the paper is replicated without including the spatial autocorrelation error model.

The model could be written as:
\begin{equation}
ln(\frac{n_{i,t}}{n_{I,t}}) = \beta_0ln(\frac{n_{i,t-1}}{n_{I,t-1}}) + \beta_1 + \epsilon, \forall i \in [1, \dots, I-1], t \in [1, \dots, T]
\end{equation}
where:
- $I$ is the reference territory
- $a_i = \alpha_i - \alpha_I$
- $\alpha_i = x'_{i} \theta + \eta$, $x'_i$ is the vector of all the time invariant observable location factors, $\eta$ is an error random term
- $v_{i,t} = u_{i,t} - u_{I, t}$, $u_{i,t} ~ N(0, \sigma^2)$ is an error random term 

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
