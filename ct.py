import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\TRISHA MAITHRI\Documents\Dataset\Dataset\titanic.csv")
age_survived=data[data['survived']==1]['age']
age_not_survived=data[data['survived']==0]['age']
plt.hist(age_survived,alpha=0.6,label='survived')
plt.hist(age_not_survived,alpha=1,label='not survived')
plt.xlabel("age")
plt.ylabel("frequency")
plt.title("age distribution of suervived and not survived passengers")
plt.show()

