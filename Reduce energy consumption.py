import numpy as np

# Simulated model prediction: energy consumption in kWh
predicted_energy = 180  # model output

# Simulated threshold
high_energy_threshold = 150

# Simulated context data
occupancy = 20          # people
temperature = 28        # degrees Celsius
co2_level = 850         # ppm
time_of_day = 14        # 2 PM

# Decision logic
actions = []

if predicted_energy > high_energy_threshold:
    actions.append("Reduce HVAC load by increasing setpoint temperature.")
    if occupancy < 10:
        actions.append("Turn off lighting in unoccupied zones.")
    if temperature > 26:
        actions.append("Close blinds to reduce solar heat gain.")
    if co2_level > 800:
        actions.append("Increase ventilation efficiency.")
    if time_of_day >= 13 and time_of_day <= 16:
        actions.append("Schedule high-load systems during off-peak hours if possible.")

# Output recommendations
print("Predicted energy consumption:", predicted_energy, "kWh")
print("Recommended Actions:")
for act in actions:
    print("-", act)