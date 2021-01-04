# Standard Deviation (symbol: sigma)
# a measure of how spread out numbers are 

# DISCLAIMER: Standard deviation and mean fall for the same outlier problem where just one
# astronomical value can skew the data significantly! So the interquartile range is a more robust alternative

# Standard deviation is the square root of the variance
# Variance is the average of the squared differences from the mean.

# For a Population:
# 1. Find the mean
# 2. For each number, subtract the mean, square it. 
# 3. Find the average of those squared differences for variance.
# 4. Square root of that is standard deviation. 

# We can expect about 68% of values to be within plus-or-minus 1 standard deviation.


# BUT if the DATA IS A SAMPLE (a selection taken from a bigger Population), then the calculation changes!

# when you have N data values...
# for population: divide by N when calculating variance step 3
# for sample: divide by N-1 instead of N for step 3. 
import math
from Quantile import quantile

def mean_deviations(a_list):
    ''' returns a list of the difference of each value from the mean. '''
    x_bar = mean(a_list)
    return [(x - x_bar)**2 for item in a_list]

def sum_of_squares(a_list):
    ''' returns the sum of the squared values in a list '''
    return sum([x*x for x in a_list])

def variance(a_list):
    ''' Almost the average squared deviation from the mean. '''
    assert len(a_list) >= 2 # variance requires atleast two elements

    n = len(a_list)
    deviations = mean_deviations(a_list)
    return sum_of_squares(deviation) / (n-1)

def standard_deviation(a_list):
    ''' square root of the variance '''
    return math.sqrt(variance(a_list))

def interquartile_range(a_list):
    ''' Returns the difference between the 75th percentile and the 25th percentile'''
    return quantile(a_list, 0.75) - quantile(a_list, 0.25)


if __name__ == "__main__":
    pass