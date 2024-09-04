import pandas as pd
data=pd.read_csv(r"C:\Users\TRISHA MAITHRI\Documents\Dataset\Dataset\auto-mpg.csv")
df=pd.DataFrame(data)
print(df)
hp_mean=df['Horsepower'].mean()
print("\n mean of horsepower:\n",hp_mean)
acc_st=df['Acceleration'].std()
print("\n standard deviation of acceleration:\n",acc_st)
car_mode=data.groupby('Model Year')['Model Year'].count()
print("\n the number of cars manufactured in each year:\n",car_mode)