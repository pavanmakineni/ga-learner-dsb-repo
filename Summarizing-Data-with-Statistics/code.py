# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data =  pd.read_csv(path,sep=',')
print(data.columns)
print(data.head(5))

data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
print(gender_count)

gender_count.plot(kind='bar',figsize=(10,10))
plt.xlabel("Gender")
plt.ylabel("Distribution of Counts")
plt.title("Stats on SuperHero gender")
plt.show()
#Code starts here 




# --------------
#Code starts here
print(data.columns)
print(data.head(1))

alignment = data["Alignment"].value_counts()
print(alignment)

#alignment.plot(kind="pie",figsize=(10,10))
plt.pie(alignment,labels=alignment.index)
plt.title("Character Alignment")
plt.show()


# --------------
#Code starts here

sc_df = data[["Strength","Combat"]]
print(sc_df.head(1))

sc_covariance = sc_df.cov().iloc[0,1]
print(sc_covariance)

sc_strength = sc_df.Strength.std()
print(sc_strength)

sc_combat = sc_df.Combat.std()
print(sc_combat)

sc_pearson = sc_covariance / (sc_strength * sc_combat)
print(sc_pearson)

sc_pearson1 = sc_df.corr(method='pearson').iloc[0,1]
print(sc_pearson1)

ic_df = data[["Intelligence","Combat"]]
print(ic_df.head(5))

ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()

ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print(ic_pearson)

ic_pearson1 = ic_df.corr(method = "pearson").iloc[0,1]
print(ic_pearson1)


# --------------
#Code starts here

print(data.columns)

total_high = data.Total.quantile(0.99)
print(total_high)

super_best = data[data["Total"] > total_high]
print(super_best.head(10))

super_best_names = super_best.Name.tolist()
print(type(super_best_names))

print(super_best_names)


# --------------
#Code starts here

fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1,figsize=(25,25))
ax_1.boxplot(data.Intelligence)
ax_1.set(title = "Intelligence")

ax_2.boxplot(data.Speed)
ax_2.set(title = "Speed")

ax_3.boxplot(data.Power)
ax_3.set(title = "Power")


