# Immigration-Models
The aim of this chapter is to model the immigrant flow across the Italian territory. Thus, working with *data panel* is necessary. Data panel, or longitudinal data, refers to a set of *n* units surveyed repeatedly over *T* times. The notation ![](https://latex.codecogs.com/gif.latex?Y_%7Bi%2Ct%7D) denotes the variable ![](https://latex.codecogs.com/gif.latex?Y) observed for the ![](https://latex.codecogs.com/gif.latex?i)-th unit at time ![](https://latex.codecogs.com/gif.latex?t).

## [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents)

In this section, some attempts to replicate the model specified in the [H. Jayet et al. paper](http://www.jstor.org/stable/41219121?casa_token=kWQZrm4oyF0AAAAA:KeWFnUzB0a35pI6h39ZjcK8jd4njelxV-w_oC98qZM2nro4pkyqIyrDON1KmTmVz7zfRrIvDY3xOU1ws2aQgkOANz_hYo-nkw0SGTtgDH2jGgG9k9g&seq=1#page_scan_tab_contents) are performed.

The initial model is defined as:

![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%28n_%7Bi%2C%20t%7D%29%20%3D%20%5Cbeta%20ln%20%28n_%7Bi%2C%20t-1%7D%29%20&plus;%20%5Calpha_i%20&plus;%20%5Cgamma_t%20&plus;%20u_%7Bi%2C%20t%7D%20%5C%20%5C%20i%20%3D%201%2C%20%5Cdots%2C%20I%20%5Ctext%7B%20and%20%7D%20t%20%3D%201%2C%20%5Cdots%2C%20T)

where:
- ![](https://latex.codecogs.com/gif.latex?%5Cbeta) is the parameters for the network effect (is a local phenomenon that influences the immigrant choice, that is: foreign-born population tend to migrate to territories where a community of the same ethnic already exists).
- ![](https://latex.codecogs.com/gif.latex?%5Calpha_i%20%3D%20x%27_i%20%5Ctheta%20&plus;%20%5Ceta_i) , ![](https://latex.codecogs.com/gif.latex?x%27_%7Bi%7D) is the vector of all the time invariant observable location factors (features vector), ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Ctheta) is the vector of coefficient and![](https://latex.codecogs.com/gif.latex?%5Ceta_i) is an error random term.
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cgamma_t) measures the fixed time effect.

![](https://latex.codecogs.com/gif.latex?u_%7Bi%2C%20t%7D) is the *error term*. It is modeled using a *Spatial Autoregressive Model*, ![](https://latex.codecogs.com/gif.latex?u_t%20%3D%20%28u_%7B1%2C%20t%7D%2C%20%5Cdots%2C%20u_%7BI%2C%20t%7D%29) follows:

![](https://latex.codecogs.com/gif.latex?u_t%20%3D%20%5Crho%20W%20u_t%20&plus;%20w_t),

where:
- ![](https://latex.codecogs.com/gif.latex?%5Crho) is the autoregressive parameter.
- ![](https://latex.codecogs.com/gif.latex?W) is the spatial weights matrix. It is symmetric and normalized with ![](https://latex.codecogs.com/gif.latex?w_%7Bij%7D%20%5Cge%200%2C%20%5C%20w_%7Bij%7D%20%3D%200%20%5Ctext%7B%20if%20%7D%20i%3Dj%2C%20%5C%20%5Csum_%7Bj%3D1%7D%5En%20w_%7Bij%7D%20%3D%201%20%5C%20%5C%20i%3D1%2C%20%5Cdots%2C%20n). (General form of a weights matrix, not necessary).
- ![](https://latex.codecogs.com/gif.latex?w_t%20%5Csim%20N%280%2C%20%5Csigma%5E2%20I%29) is an iid random term.

The model just defined cannot be estimated using both the time and the location fixed effects ![](https://latex.codecogs.com/gif.latex?%5Calpha_i) and ![](https://latex.codecogs.com/gif.latex?%5Cgamma_t). With an increasing sample size , maximum likelihood (ML) methods are asymptotically consistent, efficient and normally distributed. The ML estimates' consistency depends on the assumption that the number of parameters remains constant as the sample size increases.

Since the number of locations cannot increases, a larger sample in this model means a longer period. Thus, if the sample size increases, the number of fixed time effects increases. It is necessary to suppress them to consistently estimate the model.

In a general fixed effect model ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20%3D%20%5Cbeta%20x_%7Bi%2C%20t%7D%20&plus;%20%5Calpha_t%20&plus;%20%5Cepsilon_%7Bi%2C%20t%7D%2C%20%5C%20i%20%3D%201%2C%20%5Cdots%2C%20I%20%5C%20and%20%5C%20t%20%3D%201%2C%20%5Cdots%2C%20T), it is possible to eliminate the fixed effect ![](https://latex.codecogs.com/gif.latex?%5Cgamma_t) by:
1. fixed effects transformation: ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20-%20%5Cbar%7By%7D_t%20%3D%20%28x_%7Bi%2C%20t%7D%20-%20%5Cbar%7Bx%7D_t%29%5Cbeta%20&plus;%20%28%5Calpha_t%20-%20%5Cbar%7B%5Calpha%7D_t%29%20&plus;%20%28u_%7Bi%2C%20t%7D%20-%20%5Cbar%7Bu%7D_%7Bi%2Ct%7D%29).
2. differencing with respect to a fixed unit: ![](https://latex.codecogs.com/gif.latex?y_%7Bi%2C%20t%7D%20-%20y_%7BI%2C%20t%7D%20%3D%20%28x_%7Bi%2C%20t%7D%20-%20x_%7BI%2C%20t%7D%29%5Cbeta%20&plus;%20%28%5Calpha_t%20-%20%5Calpha_t%29%20&plus;%20%28u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D%29).

Here, the differentiating method with respect to a reference location, *I*, is used:

![](https://latex.codecogs.com/gif.latex?ln%28n_%7Bi%2C%20t%7D%29%20-%20ln%28n_%7BI%2C%20t%7D%29%20%3D%20%5Cbeta%28ln%28n_%7Bi%2C%20t-1%7D%29%20-%20ln%28n_%7BI%2C%20t-1%7D%29%29%20&plus;%20%5Calpha_i%20-%20%5Calpha_I%20&plus;%20%5Cgamma_t%20-%20%5Cgamma_t%20&plus;%20u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D)


![](https://latex.codecogs.com/gif.latex?%5Cinline%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2C%20t%7D%7D%7Bln%28n_%7BI%2C%20t%7D%29%7D%20%5Cright%20%29%20%3D%20%5Cbeta%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2C%20t-1%7D%7D%7Bln%28n_%7BI%2C%20t-1%7D%29%7D%20%5Cright%20%29%20&plus;%20a_i%20&plus;%20v_%7Bi%2C%20t%7D%2C)

with
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20i%20%3D%201%2C%20%5Cdots%2C%20I-1%20%5Ctext%7B%20and%20%7D%20t%20%3D%201%2C%20%5Cdots%2C%20T)
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20a_i%20%3D%20%5Calpha_i%20-%20%5Calpha_I)
- ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_%7Bi%2C%20t%7D%20%3D%20u_%7Bi%2C%20t%7D%20-%20u_%7BI%2C%20t%7D)

Thus, ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_t%20%3D%20Q%20u_t) with ![](https://latex.codecogs.com/gif.latex?%5Cinline%20v_t%20%3D%20%28v_%7B1%2C%20t%7D%2C%20v_%7BI-1%2C%20t%7D%29), ![](https://latex.codecogs.com/gif.latex?%5Cinline%20u_t%20%3D%20%28u_%7B1%2C%20t%7D%2C%20u_%7BI%2C%20t%7D%29) and ![](https://latex.codecogs.com/gif.latex?%5Cinline%20Q%20%3D%20%5Cleft%20%5B%20I_%7BI-1%7D%20%5C%20-1_%7BI-1%7D%20%5Cright%20%5D), being ![](https://latex.codecogs.com/gif.latex?%5Cinline%20I_%7BI-1%7D) and identity matrix of dimension ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%28I-1%20%5Ctext%7B%20x%20%7D%20I-1%20%29) and ![](https://latex.codecogs.com/gif.latex?%5Cinline%20-1_%7BI-1%7D) the column vector of dimension ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%28I-1%29) with all its element equal to -1.


Since the unobserved effect is correlated with the observed explanatory variable (i.e. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20Cov%20%5Cleft%20%28%20ln%20%5Cleft%20%28%20%5Cfrac%7Bn_%7Bi%2C%20t-1%7D%7D%7Bn_%7BI%2C%20t-1%7D%7D%20%5Cright%29%2C%20v_%7Bi%2C%20t%7D%20%5Cright%20%29%20%5Cne%200)), *ordinary squares estimates* are not consistent. To estimate the model is necessary to use the ML method.

In order to write the ML model, some computations are needed.
![](https://latex.codecogs.com/gif.latex?%5Cinline%20u_t%20%3D%20%5Cro%20W%20u_t%20&plus;%20w_t%20%5CRightarrow%20u_t%20%3D%20%5Cleft%20%28%20I%20-%20%5Crho%20W%20%5Cright%20%29%5E%7B-1%7D%20w_t%2C%20%5Ctext%7B%20where%20%7D%20w_t%20%5Csim%20N%280%2C%20%5Csigma%5E2I%29), so ![](https://latex.codecogs.com/gif.latex?%5Cinline%20u_t%20%5Csim%20N%280%2C%20%5Cleft%20%28%20I%20-%20%5Crho%20W%20%5Cright%20%29%5E%7B-1%7D%20%5Csigma%5E2%20%5Cleft%20%28%20I%20-%20%5Crho%20W%5ET%20%5Cright%20%29%5E%7B-1%7D%29)

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

It could be useful to use different methods to build the distance matrix between regions (zones):
- the distance between the two regions capitals
- the mean distance between all the province pairs belonging to the two regions (zones) considered

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

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_income_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_work_satisfaction1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_work_satisfaction2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_fertility_rate_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_reach_services_difficulty1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_reach_services_difficulty2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_internal_migration_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_live_births_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_housing_costs1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_housing_costs2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_hom_net_income_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_political_info1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_political_info2_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_social_act1_zones.png)

![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_social_act2_zones.png)

Let's see also the "Area" variable which is time invariant. Here as "Immigrant Stock" the mean over the years 2005-2015 is considered.
![](https://github.com/SaraR-1/Immigration-Models/blob/master/Plots/stock_vs_time_invariant_regions.png)

## Regression Model for Data Panel
