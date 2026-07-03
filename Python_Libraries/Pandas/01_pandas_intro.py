import pandas as pd

employees_dataset = {
    "employee_id": [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
        111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        121, 122, 123, 124, 125, 126, 127, 128, 129, 130
    ],

    "name": [
        "Ali Khan", "Abdul Majid", "Ahmed Raza", "Hassan Ali", "Hussain Shah",
        "Sara Ahmed", "Ayesha Khan", "Bilal Ahmed", "Danish Ali", "Farhan Raza",
        "Kashif Hussain", "Zain Malik", "Usman Tariq", "Hamza Noor", "Noman Ali",
        "Iqra Fatima", "Hira Khan", "Sana Malik", "Muneeb Ahmed", "Saad Raza",
        "Rehan Shah", "Taha Ali", "Asad Khan", "Laiba Noor", "Maham Tariq",
        "Nida Fatima", "Fahad Ali", "Arsalan Khan", "Komal Shah", "Rimsha Ahmed"
    ],

    "department": [
        "IT", "IT", "Finance", "HR", "Marketing",
        "Sales", "Finance", "IT", "HR", "Marketing",
        "Sales", "IT", "Finance", "HR", "Marketing",
        "Sales", "Finance", "IT", "HR", "Marketing",
        "Sales", "IT", "Finance", "HR", "Marketing",
        "Sales", "Finance", "IT", "HR", "Marketing"
    ],

    "designation": [
        "Software Engineer", "MERN Stack Developer", "Accountant", "HR Officer", "Marketing Executive",
        "Sales Officer", "Finance Manager", "Backend Developer", "Recruiter", "SEO Specialist",
        "Sales Manager", "Frontend Developer", "Audit Assistant", "HR Manager", "Content Writer",
        "Business Developer", "Tax Officer", "Data Analyst", "Office Assistant", "Social Media Manager",
        "Sales Executive", "Python Developer", "Finance Analyst", "HR Assistant", "Brand Manager",
        "Customer Support", "Accounts Officer", "Full Stack Developer", "Admin Officer", "Digital Marketer"
    ],

    "age": [
        23, 21, 26, 28, 25,
        24, 32, 27, 29, 26,
        31, 22, 25, 35, 24,
        27, 30, 26, 23, 28,
        29, 24, 27, 25, 33,
        26, 31, 25, 28, 24
    ],

    "city": [
        "Hyderabad", "Hyderabad", "Karachi", "Lahore", "Islamabad",
        "Karachi", "Hyderabad", "Lahore", "Karachi", "Islamabad",
        "Hyderabad", "Karachi", "Lahore", "Islamabad", "Hyderabad",
        "Karachi", "Lahore", "Hyderabad", "Islamabad", "Karachi",
        "Lahore", "Hyderabad", "Karachi", "Islamabad", "Lahore",
        "Hyderabad", "Karachi", "Hyderabad", "Lahore", "Islamabad"
    ],

    "salary": [
        55000, 45000, 60000, 65000, 50000,
        48000, 120000, 80000, 52000, 58000,
        95000, 50000, 47000, 130000, 42000,
        70000, 75000, 85000, 38000, 62000,
        68000, 60000, 72000, 40000, 110000,
        43000, 66000, 90000, 46000, 57000
    ],

    "experience_years": [
        2, 1, 4, 5, 3,
        2, 8, 4, 5, 3,
        7, 1, 2, 10, 2,
        4, 6, 3, 1, 5,
        6, 2, 4, 2, 9,
        3, 5, 4, 3, 2
    ],

    "joining_date": [
        "2022-01-15", "2024-03-10", "2021-06-20", "2020-09-01", "2022-11-12",
        "2023-02-05", "2018-07-18", "2021-12-01", "2020-05-22", "2022-08-30",
        "2019-04-14", "2024-01-10", "2023-06-25", "2016-03-19", "2023-09-08",
        "2021-10-11", "2020-01-27", "2022-04-09", "2024-05-01", "2021-07-15",
        "2020-11-23", "2023-01-12", "2021-09-18", "2023-04-20", "2017-12-10",
        "2022-06-05", "2020-08-28", "2021-03-17", "2022-10-25", "2023-11-02"
    ],

    "performance_score": [
        85, 90, 78, 82, 88,
        75, 91, 86, 80, 84,
        89, 92, 76, 95, 81,
        87, 83, 90, 74, 85,
        88, 86, 79, 77, 93,
        82, 84, 91, 78, 80
    ],

    "employment_status": [
        "Active", "Active", "Active", "Active", "Active",
        "Active", "Active", "Active", "Active", "Active",
        "Active", "Active", "Active", "Active", "Active",
        "Active", "Active", "Active", "Probation", "Active",
        "Active", "Active", "Active", "Probation", "Active",
        "Active", "Active", "Active", "Active", "Active"
    ]
}

df = pd.DataFrame(employees_dataset)

print(df)

# Save to CSV file
df.to_csv(
    r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas\employees_data.csv",
    index=False
)

print("Employees dataset has been written to CSV file successfully.")

# Save to Excel file
df.to_excel(
    r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas\employees_data.xlsx",
    index=False
)

print("Employees dataset has been written to Excel file successfully.")

#Save to JSON file
df.to_json(
    r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas\employees_data.json",
    orient='records' )
print("Employees dataset has been written to JSON file successfully.")

#small operations on dataframes
print("Performing small operations on the DataFrame:")

print(df.head())  # Display the first 5 rows of the DataFrame
print(df.tail())  # Display the last 5 rows of the DataFrame
print(df.info())  # Display information about the DataFrame
print(df.shape)  # Display the shape of the DataFrame (rows, columns)
print(df.describe())  # Display summary statistics of the DataFrame
print(df[df['age']>25]) # Display rows where age is greater than 25
print(df[(df['age']>25) & (df['salary']<50000) & (df['city']=='Lahore')]) # Display rows where age is greater than 25 and salary is less than 50000

print(df.sort_values(by='employee_id', ascending=False))  # Sort the DataFrame by employee_id in descending order