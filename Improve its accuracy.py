
import numpy as np

# Features: [day_of_week (0=Sun, 6=Sat), solar_radiation (W/m²), hvac_setting (0=off, 1=on)]
X = np.array([
    [0, 300, 1],
    [1, 500, 1],
    [2, 200, 0],
    [3, 600, 1],
    [4, 100, 0]
])

# Energy consumption in kWh
y = np.array([110, 160, 80, 170, 60]).reshape(-1, 1)

# Add bias term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Linear Regression (Normal Equation)
w = np.linalg.inv(X.T @ X) @ X.T @ y
y_pred = X @ w

print("Predicted energy consumption (kWh):", y_pred.flatten())