import pandas as pd
from scipy.stats import ttest_ind

# Load the cleaned dataset
merged_data = pd.read_csv('datasets/merged_data.csv')


# Get male and female optimism scores after cleaning data
male_optimism = merged_data[merged_data['gender'] == 1]['Optm']
female_optimism = merged_data[merged_data['gender'] == 0]['Optm']

# Perform the t-test
t_stat, p_value = ttest_ind(male_optimism, female_optimism)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
