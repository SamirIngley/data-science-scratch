
# Covariance - whereas variance measures how a single variable deviates from its mean, covariance measures how two variables
# vary in tandem from their means:
from Data_Manipulation.Linear_Algebra.Vectors import dot

def covariance(xs: List[float], ys: List[float]) -> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) -1)

# assert 22.42 < coavariance(num_friends, daily_minutes) < 22.43
# assert 22.42 / 60 < covariance(num_friends, daily_hours) < 22.43 / 60

def correlation(xs: List[float], ys: List[float]) -> float:
    ''' Measures how much xs and ys vary in tandem about their means ''' 
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs, ys) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

# ignore outliers, correlation can be sensitive

# Simpson's Paradox 
# correlations can be misleading when confounding variables are ignored.