import matplotlib
import numpy as np

# Task 2F Part 1
def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    
    # Compute time shift
    d0 = dates[0]
    dates_shift = np.array([(t - d0) for t in dates])

    # Fit polynomial of degree p to water levels
    coeffs = np.polyfit(x, levels, p)
    poly = np.poly1d(coeffs)

    # Return polynomial object and time shift
    return poly, d0
