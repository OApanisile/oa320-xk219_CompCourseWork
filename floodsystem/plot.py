
import matplotlib.pyplot as plt 






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

