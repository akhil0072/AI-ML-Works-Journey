import numpy as np
import pandas as pd
df = pd.DataFrame()
df.users = ['user_id','age','country']
df.sales = ['transaction_id','user_id','amount']
df.users = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'age': [25, 30, 22, 35],
    'country': ['US', 'UK', 'US', 'CA']
})
df.sales = pd.DataFrame({
    'transaction_id': [101, 102, 103, 104],
    'user_id': [1, 2, 2, 5],
    'amount': [250, 150, 200, 300]
})


#perform the left merge to join the sales to users
merged_df = pd.merge(df.sales, df.users, on='user_id', how='left')

#fill nulls if a users has no sales there amount will Nan or 0
merged_df['amount'].fillna(0, inplace=True)
merged_df['country'].fillna('Unknown', inplace=True)
#aggreate the total sales amount by country
merged_df = merged_df.groupby('country').agg({'amount': 'sum', 'user_id': 'count'}).reset_index()
merged_df.rename(columns={'amount': 'total_sales', 'user_id': 'num_transactions'}, inplace=True)

print(merged_df)