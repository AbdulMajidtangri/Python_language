#correlation means the relationship between two variables. It is a statistical measure that describes the extent to which two variables are related to each other. In pandas, we can use the corr() function to calculate the correlation between two columns in a DataFrame.
import pandas as pd

data  = pd.read_csv(r'C:\Users\MS Compuuter\OneDrive\Desktop\python\start_from_basics\Python_Libraries\Pandas\data.csv')
correlation = data['Calories'].corr(data['Duration'])
#corr is method used to calculate the correlation between two columns in a DataFrame. It returns a value between -1 and 1, where:
# -1 indicates a perfect negative correlation (as one variable increases, the other decreases)
# 0 indicates no correlation
# 1 indicates a perfect positive correlation
print(f"Correlation between Calories and Duration: {correlation}")
correlation2 = data['Pulse'].corr(data['Maxpulse'])
print(f"Correlation between Pulse and Maxpulse: {correlation2}")