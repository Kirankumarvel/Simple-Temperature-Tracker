import matplotlib.pyplot as plt

def plot_temperatures():
    # Sample data (replace with your actual temperatures)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    temperatures = [22, 24, 21, 26, 23, 25, 27]  # in °C
    
    # Create figure with larger size
    plt.figure(figsize=(10, 6))
    
    # Plot the temperature data with styling
    plt.plot(
        days, 
        temperatures,
        marker='o',         # Circle markers
        markersize=8,       # Size of markers
        linestyle='-',      # Solid line
        linewidth=2,        # Thicker line
        color='#E74C3C'     # Red color
    )
    
    # Add labels and title
    plt.title('Weekly Temperature Variation', fontsize=16, pad=20)
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    
    # Customize grid and ticks
    plt.grid(
        True, 
        linestyle='--', 
        alpha=0.7, 
        which='both', 
        axis='y'
    )
    
    # Add value labels above points
    for i, temp in enumerate(temperatures):
        plt.text(
            i, 
            temp + 0.5, 
            f'{temp}°C', 
            ha='center', 
            va='bottom',
            fontsize=10
        )
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('weekly_temperatures.png', dpi=120)
    plt.show()

if __name__ == "__main__":
    plot_temperatures()