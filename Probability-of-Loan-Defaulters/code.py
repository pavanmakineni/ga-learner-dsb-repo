# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path,sep=',')
print(df.columns)
print(df.head(2))

len_df = len(df)
print(len_df)
fico = df[df['fico'] > 700]
print(fico.head(2))
len_fico = len(fico)
print(len_fico)
p_a = len_fico/len_df
print(p_a)

df1 = df[df['purpose'] == "debt_consolidation"]
print(df1.head(2))
len_dc = len(df1)
print(len_dc)
p_b = len_dc/len_df
print(p_b)

'''
df2 = df[(df['purpose'] == "debt_consolidation") & (df['fico'] > 700)]
print(df2.head(2))
len_df2 = len(df2)
print(len_df2)

p_b_a = (len_df2/len_df)/p_a
print(p_b_a)

p_a_b = (len_df2/len_df)/p_b
print(p_a_b)
'''

df2 = df1[df1['fico'] > 700]
print(df2.head(2))

shappe = df2.shape
print(shappe)

p_a_b = df2.shape[0]/df1.shape[0]
print(p_a_b)

result = p_a_b == p_a 
print(result)




# code ends here


# --------------
# code starts here
print(df.columns)
print(df.head(1))

prob_lp = df[df["paid.back.loan"] == "Yes"].shape[0]/df.shape[0]
print(prob_lp)

prob_cs = df[df["credit.policy"] == "Yes"].shape[0]/df.shape[0]
print(prob_cs)

new_df = df[df["paid.back.loan"] == "Yes"]
print(new_df.head(2))

prob_pd_cs = new_df[new_df["credit.policy"] == "Yes"].shape[0]/new_df.shape[0]
print(prob_pd_cs)

bayes = (prob_pd_cs * prob_lp)/prob_cs
print(bayes)



# code ends here


# --------------
# code starts here
import matplotlib.pyplot as plt 

purpose = df.purpose.value_counts()
print(purpose)

purpose.plot(kind='bar')
plt.show()

df1 = df[df["paid.back.loan"] == "No"]
print(df1.head(2))

purpose_no = df1.purpose.value_counts()
print(purpose_no)

purpose_no.plot(kind='bar')
plt.show()


# code ends here


# --------------
# code starts here
import matplotlib.pyplot as plt 
inst_median = df.installment.median()
print(inst_median)

inst_mean = df.installment.mean()
print(inst_mean)

print(df.columns)

df.hist(column='installment',bins=8,figsize=(10,10))

df.hist(column='log.annual.inc',bins=8,figsize=(10,10))

plt.show()
# code ends here


