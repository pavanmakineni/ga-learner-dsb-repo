# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path,sep=',',header='infer')
#print(bank)

categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# code ends here


# --------------
# code starts here
import pandas as pd 


print(bank.columns)
banks = bank.drop(columns = 'Loan_ID')
print(banks.columns)

print(banks.isnull().sum())


bank_mode1 = banks.mode()
print(bank_mode1)

bank_mode = banks.mode().iloc[0]
print(bank_mode)

banks.fillna(bank_mode, inplace=True)


print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
import pandas as pd 




avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)
print(type(avg_loan_amount))

# code ends here



# --------------
# code starts here
import pandas as pd 

loan_status = 614


loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
#print(loan_approved_se)
print(type(loan_approved_se))

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
#print(loan_approved_nse)
print(type(loan_approved_nse))
print(loan_approved_se.count())
print(loan_approved_se.count().iloc[0])

percentage_se = (loan_approved_se.count().iloc[0]/loan_status) * 100
print(percentage_se)

percentage_nse = (loan_approved_nse.count().iloc[0]/loan_status) * 100
print(percentage_nse)
# code ends here


# --------------
# code starts here
import pandas as pd 

print(banks.columns)

def convert_to_year(months):
    return int(months)/12

loan_term = banks['Loan_Amount_Term'].apply(lambda x:convert_to_year(x))
#print(loan_term)
print(type(loan_term))
print(banks.columns)

big_loan_term1 = loan_term[loan_term >= 25].count()
print(big_loan_term1)
print(type(big_loan_term1))

big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)
print(type(big_loan_term))
# code ends here


# --------------
# code starts here
import pandas as pd 

loan_groupby = banks.groupby('Loan_Status')
print(loan_groupby)

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
print(loan_groupby)

mean_values = loan_groupby.apply(np.mean)
print(mean_values)
# code ends here


