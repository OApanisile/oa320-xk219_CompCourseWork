import matplotlib.pyplot as plt 
import datetime
import numpy as np
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):

    
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.axhline(y=station[0].typical_range[0])
    plt.axhline(y=station[0].typical_range[1])
    plt.xticks(rotation=45);
    plt.title(station[0].name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

# Task 2F Part 2
def plot_water_level_with_fit(station, dates, levels, p):
    poly, t0 = polyfit(dates, levels, p)
    
    # Plot data and fit
    fig, ax = plt.subplots()
    ax.plot(dates, levels, label="Water level")
    ax.plot(dates, poly(t0), label=f"Polyfit (degree {p})")
    ax.set_title(f"Water Level at {station}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Water Level (m)")
    ax.legend()
    plt.show()








