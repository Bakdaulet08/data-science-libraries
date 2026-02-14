import pandas as pd

data = {'Age': [34, 37, 13, 64, 37, 47, 24, 38, 26, 41, 19, 51, 44]}

df = pd.DataFrame(data)

mean_age = df['Age'].mean()
print(f"Average: {mean_age}")

median_age = df['Age'].median()
print(f"Median: {median_age}")

mode_age = df['Age'].mode()[0]
print(f"Mode: {mode_age}")

variance_age = df['Age'].var()
print(f"Variance: {variance_age}")

std_age = df['Age'].std()
print(f"STD: {std_age}")

quantiles_age = df['Age'].quantile([0.25, 0.5, 0.75])
percentile_age = df['Age'].quantile(0.7)
print(f"Quantile of Age: {quantiles_age}")
print(f"Percentile of Age: {percentile_age}")
