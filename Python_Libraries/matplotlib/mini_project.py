# 1. Create bar chart of average salary by department.
# 2. Create pie chart of employee count by city.
# 3. Create histogram of salary.
# 4. Create scatter plot of experience vs salary.
# 5. Create line chart of average performance by department.
# 6. Save one chart as PNG image.
import matplotlib.pyplot as plt
import pandas as pd 
file_path = r'C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\mini_pandas_numpy_project\employee_performance_practice_dataset.csv'

data = pd.read_csv(file_path)
print(data.info())

print(data.isnull().sum())
print(data.duplicated())
data.fillna({
   "city" : data['city'].mode()[0],
    "salary":data['salary'].mean(),
    "experience_years" : data['experience_years'].mean(),
    'performance_score' : data['performance_score'].mean(),
    'training_hours':data['training_hours'].mean()
},inplace=True)
data.drop_duplicates(inplace=True)

print(data.isnull().sum())
print(data.duplicated().sum())

# 1. Create bar chart of average salary by department.
avg_slary = data.groupby('department')['salary'].mean()
plt.bar(avg_slary.index,avg_slary.values)
plt.xlabel("Departement")
plt.ylabel('avg salary')
plt.show()

# 2. Create pie chart of employee count by city.
city_count= data['city'].value_counts()
plt.pie(city_count.values)
plt.title(" employee count by city")
plt.show()

# 3. Create histogram of salary.
plt.hist(data['salary'],bins=5,color='black',bottom='green')
plt.title("Histogram of salary")
plt.show()

# 4. Create scatter plot of experience vs salary.
plt.scatter(data['experience_years'],data['salary'])
plt.title("experience vs salary")
plt.show()

# 5. Create line chart of average performance by department.
# 6. Save one chart as PNG image.

avg_perfromance = data.groupby('department')['performance_score'].mean()
plt.plot(avg_perfromance.index,avg_perfromance.values)
plt.title("Average performance by department")
plt.xlabel("Department")
plt.ylabel('avg Perfromance')
plt.show()
plt.savefig(fname='tutu')