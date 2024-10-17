import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
merged_data = pd.read_csv('datasets/merged_data.csv')

# Scatter Plot: Computer Use on Weekends vs Optimism
plt.figure(figsize=(8,6))
sns.scatterplot(data=merged_data, x='C_we', y='Optm')
plt.title('Computer Use on Weekends vs Optimism')
plt.xlabel('Computer Use (Weekends)')
plt.ylabel('Optimism Score')
plt.savefig('visualizations/scatter_computer_optimism.png')

# Correlation Heatmap
plt.figure(figsize=(10,8))
corr_matrix = merged_data[['C_we', 'S_we', 'T_we', 'Optm', 'Relx', 'Cheer']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Between Screen Time and Well-being Indicators')
plt.savefig('visualizations/correlation_heatmap.png')
