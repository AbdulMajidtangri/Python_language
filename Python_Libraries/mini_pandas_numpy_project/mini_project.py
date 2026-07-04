import numpy as np
import pandas as pd

file_path = r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\mini_pandas_numpy_project\employee_performance_practice_dataset.csv"

data  = pd.read_csv(file_path)

# print(data)

#apply the normal analysis over the data 
print(data.head(30))
print(data.tail(20))
print(data.shape)
print(data.describe())
print(data.info())

#checking the missing values
print(data.isnull().sum())
#chekcing the duplicates values
print(data.duplicated().sum())

#there are two ways to halde the missing values
#dropna or fillna
# i usually do ont prefer the dropna i use fillna for better data manipulation

mean_OFsalary = data['salary'].mean()
mean_OFperformance = data['performance_score'].mean()
mean_OFtraining_hours = data['training_hours'].mean()
expreience = data['experience_years'].mean()
city = data['city'].mode()[0]
data.fillna({
"salary": mean_OFsalary,
"performance_score":mean_OFperformance,
"training_hours" : mean_OFtraining_hours,
"experience_years":expreience,
"city": city,

},inplace=True)

print(data.isnull().sum())
#Drop duplicates
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())
#find average salary and highest,and lower perfromance

sal_to_num = data['salary'].to_numpy()
average_salary = np.mean(sal_to_num)

print(f"The average salary is using numpy :  {average_salary}")
perfromance_to_num = data['performance_score'].to_numpy()
highest_performance = np.max(perfromance_to_num)
lowest_permance = np.min(perfromance_to_num)

print(f"the highest and lower perfromace are foun using numpy they are : high = {highest_performance}  lower : {lowest_permance}")

#group the salary by the department 

grouping_salary = data.groupby("department")['salary'].mean()
print(grouping_salary)
#group the emp with salary 

gruop_emp_with_salary = data.groupby('employee_id')['salary'].sum()

print(gruop_emp_with_salary)

#count employee city wise

print(data['city'].value_counts())

# filter the emp accoring to the salary

print(data[data['salary']>80000])