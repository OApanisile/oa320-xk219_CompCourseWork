import matplotlib
import numpy as np

# Task 2F Part 1
def polyfit(dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)

    t0 = x[0]
    dates = np.array([(t - t0) for t in x])

    # Fit polynomial of degree p to water levels
    coeffs = np.polyfit(x, levels, p)
    poly = np.poly1d(coeffs)

    # Return polynomial object and time shift
    return poly, t0
