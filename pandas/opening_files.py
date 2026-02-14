import pandas as pd

df = pd.read_csv('sample.csv')
# print(df.head())

filtered_df = df[df['Product'] == 'Product A']
print(filtered_df)

# filtered_df.to_csv('new_info.csv', index=False)

df.fillna(0, inplace = True)

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

df['Age'] = df['Age'].astype(int)

grouped = df.groupby('Age').sum()

print(grouped)

