import numpy as np

# Simulated AI predictions (in kWh)
predicted_demand = 200               # energy needed for the building
predicted_solar_generation = 150    # solar generation forecast
battery_storage = 40                # energy available in battery

# Net balance
net_energy = predicted_solar_generation + battery_storage - predicted_demand

# AI decision logic
actions = []

if net_energy >= 0:
    actions.append("Operate building as usual using solar and battery.")
    actions.append("Store surplus energy in battery or feed to grid.")
else:
    shortfall = abs(net_energy)
    actions.append(f"Energy shortfall: {shortfall} kWh.")
    actions.append("Reduce HVAC load intelligently (adjust setpoints).")
    actions.append("Delay non-essential equipment usage.")
    actions.append("Buy only green-certified energy for remaining demand.")

# Output AI decisions
print("AI Net-Zero Simulation")
print("-----------------------")
print("Predicted Demand:", predicted_demand, "kWh")
print("Predicted Solar:", predicted_solar_generation, "kWh")
print("Battery Storage:", battery_storage, "kWh")
print("Net Energy Balance:", net_energy, "kWh\n")

print("AI Recommended Actions:")
for act in actions:
    print("-", act)