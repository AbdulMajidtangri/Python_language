#pandas is python library used to used to clean and analyze data. It provides data structures and functions needed to manipulate structured data seamlessly.
import pandas as pd 


data  = pd.read_csv(r"C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas\fitness_dataset.csv")
# print(data)
# for the daTA CLEANING WE GAVE METHODS LIKE DROPNA, FILLNA, REPLACE, DROP DUPLICATES, RENAME COLUMNS, CHANGE DATA TYPES, REMOVE OUTLIERS, AND MANY MORE.
#DROPNA REMOVE THE ROMVE THE ROWS WITH NULL VALUES 
# data.dropna(inplace = True)
# print(data)
print(data)
#instead of droping entire row due to single value jsut fill cell with other value
# data.fillna({
#     "Date": "2020/12/22",
# }, inplace=True)
#replace using the using ther mean,mod,median values of the column
# mean_calories = data['Calories'].mean()
median_calories = data['Calories'].median()
mode_calories = data['Calories'].mode()[0]
data.fillna({
        "Calories": mode_calories,
        "Date": "20200823"
}, inplace=True)
print(data)
#change the wrong format dat of cell to correct method using to_datetime method 
data["Date"] = pd.to_datetime(data["Date"], format="mixed")
print(data)

#pandas fixex wrong data to correct data using the loc method and the index of the row and column name to fix the wrong data in the cell
data.loc[2, "Calories"] = 30000
#loc method is used to access a group of rows and columns by labels or a boolean array. It is primarily label based, but may also be used with a boolean array.

print(data)

#cleaning duplicate data using the drop_duplicates method which removes duplicate rows from the DataFrame based on specified columns or all columns.
print("Before removing duplicates:")
print(data.duplicated())  # return only true of false values for the duplicate rows
data.drop_duplicates(inplace=True)  # Remove duplicate rows 
print("After removing duplicates:")
print(data.duplicated().sum())  # Count the number of duplicate rows after removal
print(data)