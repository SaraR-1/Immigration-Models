import pandas as pd
import numpy as np
import build_data_functions as bdf
import plot_data_functions as pdf
import pycountry


# m:period of the moving average
def SMA_single(data_, m):
    res = []
    for c in range(0, len(data_)-m):
        res.append(np.mean(data_[c:m+c]))
    return(res)


def SMA(data_, country, times, territories, m):
    country = pycountry.countries.get(name=country).alpha_3
    idx = pd.MultiIndex.from_product(
        [times, territories], names=['Year', 'Province'])
    col = ['SMA %s years' % str(len(times)-m)]
    df = pd.DataFrame('-', idx, col)

    for t in territories:
        temp = SMA_single(data_.loc[(t, times), country].values, len(times)-m)
        est = list(data_.loc[(t, times), country].values[:len(times)-m])
        est.extend(temp)

        df.loc[(slice(None), t), 'SMA %s years' % str(len(times)-m)] = est
    return(df)


def exp_smoothing_single(data_, alpha):
    s = [data_[0]]
    for i, j in zip(data_[:-1], s):
        s.append(j + alpha*(i - j))
    return(s)


def exp_smoothing(data_, country, times, territories, alphas):
    country = pycountry.countries.get(name=country).alpha_3
    idx = pd.MultiIndex.from_product(
        [times, territories], names=['Year', 'Province'])
    col = ['Exp Smoothing %s alpha' % str(alpha) for alpha in alphas]
    df = pd.DataFrame('-', idx, col)

    for t in territories:
        for alpha in alphas:
            est = exp_smoothing_single(
                data_.loc[(t, times), country].values, alpha)

            df.loc[(slice(None), t), 'Exp Smoothing %s alpha' %
                   str(alpha)] = est
    return(df)
