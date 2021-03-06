# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header=1)
print("\nData: \n\n",data)
print("\nType of data: \n\n",type(data))
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#new_record=np.array(new_record)
census = np.concatenate((data,new_record),axis=0)
print("\nCensus: \n\n",census)
print("\nType of data: \n\n",type(census))
#Code starts here



# --------------
#Code starts here
age = census[:,0]
print(age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race = census[:,2]
#print(race)
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
#print(race_0)
#print(race_1)
#print(race_2)
#print(race_3)
#print(race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0)
print(len_1)
print(len_2)
print(len_3)
print(len_4)

race_list = [len_0,len_1,len_2,len_3,len_4]
print(race_list)

minority_race = race_list.index(min(race_list))
print(minority_race)



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
#print(senior_citizens)

working_hours_sum = np.sum(senior_citizens[:,6],axis=0)
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

if(avg_working_hours > 25):
    print("Govt Policy Violated")
else:
    print("Average Working Hours are with in the Govt Policy")


# --------------
#Code starts here
high = census[census[:,1]>10]
low  = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)


if(avg_pay_high > avg_pay_low):
    print("Better Education leads to Better Pay")


