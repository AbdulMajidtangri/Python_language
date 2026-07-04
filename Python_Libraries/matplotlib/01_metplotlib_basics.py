import matplotlib.pyplot as plt
#matplotlib is the python library that used to create graphs and charts from the data in python. It is used to create static, animated, and interactive visualizations in Python. It provides a wide range of plotting functions and customization options to create various types of plots, including line plots, scatter plots, bar plots, histograms, and more.


months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [10000, 15000, 1000, 18000, 22000]
#line chart is used to show the trend of data only over the time
plt.plot(sales,months)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
#bars chart is used to show the comparison of data over the time

employees= ["ali", "ahmed", "bilal", "umer", "hassan"]
salary = [10000, 15000, 1000, 18000, 22000]
plt.bar(employees,salary)
plt.title("Employee Salaries")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

#pie chart is used to show the percentage of data over the time
population = [90.00, 10.00,40.00,75.00]
areas= ["Asia", "Africa", "Europe", "America"]

plt.pie(population,labels=areas)
plt.title("Population Distribution")
plt.show()
# histogram is used to show the distribution of data over the time OR WE CAN USE HISTOGRAM TO SHOW THE FREQUENCY OF DATA OVER THE TIME  or salary distribution of employees
salary = [45000, 50000, 55000, 60000, 70000, 80000, 90000, 120000]

plt.hist(salary, bins=7, color='blue', edgecolor='black', linewidth=0.5)

plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Salary Distribution")

plt.show()
#scatter plot is used to show the relationship between two variables over the time
#it show the correclation between two variables over the time
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 6, 8, 10,4]
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()