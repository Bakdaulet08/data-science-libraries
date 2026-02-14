import pandas as pd

df = pd.read_csv('platforms.csv')
# print("Data from file:")
# print(df.head())

df['Views'] = df['Views'].fillna(df['Views'].mean())
df['Revenue'] = df['Revenue'].fillna(0)

df['Views'] = df['Views'].astype(int)
df.drop_duplicates(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

# print("Description")
# print(df.describe())

filtered = df[df['Platform'] == 'YouTube']
# print(filtered)


grouped = filtered.groupby('Date').agg({'Views': 'sum', 'Revenue':'sum'}).reset_index()
# print(grouped)

mean_views = grouped['Views'].mean()
mean_revenue = grouped['Revenue'].mean()
print(f"Mean views: {mean_views}")
print(f"Mean revenue: {mean_revenue}")

grouped.to_csv('new_platforms.csv', index=False)