import numpy as np

# Sample data: [occupancy_count, temperature_C, humidity_%]
X = np.array([
    [20, 24, 50],
    [35, 22, 55],
    [10, 27, 45],
    [50, 20, 60],
    [40, 21, 58]
])

# Energy consumption in kWh (target)
y = np.array([120, 140, 90, 180, 160]).reshape(-1, 1)

# Add bias term
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Linear Regression: weights = (XᵀX)^(-1) Xᵀy
weights = np.linalg.inv(X.T @ X) @ X.T @ y

# Predict energy consumption
y_pred = X @ weights

# Output predictions
print("Predicted energy consumption (kWh):", y_pred.flatten())