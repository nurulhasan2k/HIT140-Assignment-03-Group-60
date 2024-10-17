import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
merged_data = pd.read_csv('datasets/merged_data.csv')

# Generate descriptive statistics
desc_stats = merged_data.describe()
desc_stats.to_csv('datasets/descriptive_statistics.csv')

# Box plot for screen time by gender
plt.figure(figsize=(8,6))
sns.boxplot(data=merged_data, x='gender', y='C_we')
plt.title('Computer Use on Weekends by Gender')
plt.savefig('visualizations/boxplot_gender_computer.png')
