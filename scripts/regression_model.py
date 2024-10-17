import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the cleaned dataset
merged_data = pd.read_csv('datasets/merged_data.csv')

# Define features and target
X = merged_data[['C_we', 'S_we', 'T_we']]  # Screen time features
y = merged_data['Optm']  # Target (optimism score)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate MAE, MSE, RMSE, R²
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}, MSE: {mse}, RMSE: {rmse}, R-squared: {r2}")

# Plot Actual vs Predicted Optimism Scores
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')  # Diagonal line
plt.title('Actual vs Predicted Optimism Scores')
plt.xlabel('Actual Optimism Score')
plt.ylabel('Predicted Optimism Score')
plt.savefig('visualizations/actual_vs_predicted.png')
