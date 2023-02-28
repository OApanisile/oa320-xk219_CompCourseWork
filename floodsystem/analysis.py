import numpy as np

# Task 2F Part 1
def polyfit(dates, levels, p):
    # Compute time shift
    d0 = dates[0]
    dates = np.array([(t - d0).total_seconds() / 3600.0 for t in dates])

    # Fit polynomial of degree p to water levels
    coeffs = np.polyfit(dates, levels, p)
    poly = np.poly1d(coeffs)

    # Return polynomial object and time shift
    return poly, d0
