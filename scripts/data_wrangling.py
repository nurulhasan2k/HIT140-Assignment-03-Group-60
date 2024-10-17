import pandas as pd

# Load datasets
dataset1 = pd.read_csv('datasets/dataset1.csv')
dataset2 = pd.read_csv('datasets/dataset2.csv')
dataset3 = pd.read_csv('datasets/dataset3.csv')

# Merge datasets on 'ID'
merged_data = dataset1.merge(dataset2, on='ID').merge(dataset3, on='ID')

# Handle missing values
merged_data.fillna(merged_data.mean(), inplace=True)

# Save cleaned data
merged_data.to_csv('datasets/merged_data.csv', index=False)
