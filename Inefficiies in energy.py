import pandas as pd
import numpy as np

# Simulated smart building data
data = pd.DataFrame({
    'occupancy': [5, 10, 20, 30, 15, 25, 35, 40, 45, 50, 10],
    'temperature': [22, 23, 24, 25, 21, 22, 26, 27, 28, 29, 22],
    'humidity': [45, 50, 55, 60, 48, 52, 65, 63, 67, 70, 50],
    'energy_consumption': [30, 50, 65, 90, 45, 70, 95, 110, 120, 140, 200]
})

# Calculate Z-score for energy consumption
mean = np.mean(data['energy_consumption'])
std = np.std(data['energy_consumption'])

# Identify inefficiencies: Z-score > 2 or < -2
data['z_score'] = (data['energy_consumption'] - mean) / std
data['inefficient'] = data['z_score'].apply(lambda z: 'Yes' if abs(z) > 2 else 'No')

# Display results
print("Energy Inefficiency Detection (Z-Score Method):")
print(data[['occupancy', 'temperature', 'humidity', 'energy_consumption', 'inefficient']])