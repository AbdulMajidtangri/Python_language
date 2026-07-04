# Pandas Employee Dataset Practice
# Pandas is a Python library used for data analysis and data manipulation.
# It is used to work with tabular data like CSV, Excel, JSON, and database tables.
import pandas as pd
from pathlib import Path


# 1. Create Employee Dataset
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
# 2. Convert Dictionary into DataFrame
df = pd.DataFrame(employees_dataset)

# Convert joining_date column into proper datetime format
df["joining_date"] = pd.to_datetime(df["joining_date"])

print("\nComplete Employee DataFrame:")
print(df)
# 3. Save DataFrame into CSV, Excel, and JSON

output_dir = Path(
    r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas"
)

output_dir.mkdir(parents=True, exist_ok=True)

csv_path = output_dir / "employees_data.csv"
excel_path = output_dir / "employees_data.xlsx"
json_path = output_dir / "employees_data.json"

df.to_csv(csv_path, index=False)
print("\nEmployees dataset has been written to CSV file successfully.")

df.to_excel(excel_path, index=False)
print("Employees dataset has been written to Excel file successfully.")

df.to_json(json_path, orient="records", indent=4)
print("Employees dataset has been written to JSON file successfully.")


# 4. Basic DataFrame Operations

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataFrame information:")
df.info()

print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nStatistical summary:")
print(df.describe())


# 5. Check Missing Values and Duplicate Rows

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal duplicate rows:")
print(df.duplicated().sum())


# 6. Select Specific Columns

print("\nSelecting name, department, and salary columns:")

selected_columns = df[["name", "department", "salary"]]
print(selected_columns)


# 7. Filter Data

print("\nEmployees whose age is greater than 25:")
print(df[df["age"] > 25])

print("\nEmployees whose age is greater than 25, salary less than 50000, and city is Lahore:")

filtered_employees = df[
    (df["age"] > 25) &
    (df["salary"] < 50000) &
    (df["city"] == "Lahore")
]

print(filtered_employees)

print("\nEmployees from IT department:")
print(df[df["department"] == "IT"])

print("\nEmployees with performance score greater than 90:")
print(df[df["performance_score"] > 90])

# 8. Sort Data

print("\nEmployees sorted by employee_id in descending order:")
print(df.sort_values(by="employee_id", ascending=False))

print("\nEmployees sorted by salary in descending order:")
print(df.sort_values(by="salary", ascending=False))


# 9. Add New Column

print("\nAdding bonus column:")

df["bonus"] = df["salary"] * 0.10

print(df[["name", "salary", "bonus"]])


# 10. Select Rows Using loc and iloc

print("\nFirst row using loc:")
print(df.loc[0])

print("\nRows from index 0 to 5 using loc:")
print(df.loc[0:5])

print("\nFirst row using iloc:")
print(df.iloc[0])

print("\nRows from position 0 to 5 using iloc:")
print(df.iloc[0:5])


# 11. loc vs iloc
# loc is label-based indexing.
# It uses row labels and column names.
#
# iloc is integer-position-based indexing.
# It uses only integer positions.

print("\nEmployee name from first row using loc:")
print(df.loc[0, "name"])

print("\nEmployee name from first row using iloc:")
print(df.iloc[0, 1])
# 12. GroupBy Analysis
#groupby() ka kaam hota hai data ko kisi column ke base par groups mein divide karna, phir har group par calculation perform karna.
print("\nAverage salary by department:")
print(df.groupby("department")["salary"].mean())

print("\nTotal salary by department:")
print(df.groupby("department")["salary"].sum())

print("\nAverage performance score by department:")
print(df.groupby("department")["performance_score"].mean())

print("\nNumber of employees in each city:")
print(df["city"].value_counts())

print("\nNumber of employees in each department:")
print(df["department"].value_counts())

# 13. Drop Column

print("\nDropping bonus column:")

df = df.drop(columns=["bonus"])

print(df.head())

# 14. Rename Columns

print("\nRenaming columns:")

df = df.rename(
    columns={
        "name": "employee_name",
        "department": "dept_name"
    }
)

print(df.head())

