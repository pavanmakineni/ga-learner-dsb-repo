# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Code starts here

data = pd.read_csv(path,sep=',')
print(data.head(5))
print(data.columns)

loan_status = data['Loan_Status'].value_counts()
print(loan_status)
print(type(loan_status))

loan_status.plot(kind='bar')
plt.show()


# --------------
#Code starts here
import pandas as pd 
import matplotlib.pyplot as plt 

print(data.columns)
print(data.head(5))

property_and_loan = data.groupby(['Property_Area','Loan_Status'])
print(property_and_loan)

property_and_loan = property_and_loan.size().unstack()
print(property_and_loan)

property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.title("Loan Approval Distribution across the regions")
plt.xticks(rotation=45)

plt.show()


# --------------
#Code starts here
import pandas as pd 
import matplotlib.pyplot as plt 

print(data.head(1))
print(data.columns)

education_and_loan = data.groupby(['Education','Loan_Status'])
print(education_and_loan)

education_and_loan = education_and_loan.size().unstack()
print(education_and_loan)

education_and_loan.plot(kind='bar',stacked=True,figsize=(15,10))
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.title("Relating Higher Education in Issuing Loans")

plt.show()


# --------------
#Code starts here
import pandas as pd  
import matplotlib.pyplot as plt

print(data.head(1))
print(data.columns)

graduate = data[data["Education"] == "Graduate"]
#print(graduate)
print(type(graduate))

not_graduate = data[data["Education"] == "Not Graduate"]
#print(not_graduate)
print(type(not_graduate))

graduate["LoanAmount"].plot(kind='density',label='Graduate')

not_graduate["LoanAmount"].plot(kind='density',label='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import pandas as pd 
import matplotlib.pyplot as plt 

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
print(data.columns)
print(data.head(2))
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3, ncols=1, figsize=(20,8))

'''
plt.scatter(data["ApplicantIncome"],data["LoanAmount"])
plt.title("Applicant Income")

data.plot.scatter(x="ApplicantIncome",y="LoanAmount")
plt.ax_1.title("Applicant Income")

data.plot.scatter(x="CoapplicantIncome",y="LoanAmount")
plt.ax_2.title("Coapplicant Income")

data.plot.scatter(x='TotalIncome',y='LoanAmount')
plt.ax_3.title("Total Income")
'''
ax_1.scatter(data["ApplicantIncome"],data["LoanAmount"])
ax_1.set(title="Applicant Income")

ax_2.scatter(data["CoapplicantIncome"],data["LoanAmount"])
ax_2.set(title="Coapplicant Income")

ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set(title="Total Income")

plt.show()


