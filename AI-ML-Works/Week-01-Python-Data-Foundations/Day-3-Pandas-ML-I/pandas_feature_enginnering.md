## In real Ml , data is never in one fil. you will have users table and a transactions table, we need to combine them to createa features for the model

# 1.Power of Merning 
 * In pandas , we use pd.merge it is same like sql join 
 left join > keep all the users even if they haven't bought anything
 inner join > Only keep users who mande a purchase

# 2. Groupby and aggreations 
once merged we need to summizer ht edata , for example what is the toal spend per county 
summary = df.groupby('country').agg({'spend':'sum','age'"mean'})

#today coing challenge in pandas
