import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"X": [78, 85, 96, 80, 86], "Y": [84, 94, 89, 83, 86], "Z": [86, 97, 96, 72, 83]}
)

# ex1 : Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.

exam_data = {
    "name": [
        "Anastasia",
        "Dima",
        "Katherine",
        "James",
        "Emily",
        "Michael",
        "Matthew",
        
        "Laura",
        "Kevin",
        "Jonas",
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(exam_data, index=labels)
print(df)
print("\n")

# ex2 : Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.

print(df.info())
print("\n")

# ex3 : Write a Pandas program to get the first 3 rows of a given DataFrame.

print(df.iloc[:3])
print("\n")

# ex4 : Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.

print(df[['name', 'score']])
print("\n")

# ex5 : Write a Pandas program to select the specified columns and rows from a given data frame.

print(df.iloc[[1, 3, 5, 6], [1, 3]])
print("\n")

# ex6 : Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.

print(df[df['attempts'] > 2])
print("\n")

# ex7 : Write a Pandas program to count the number of rows and columns of a DataFrame.

print(df.shape)
print("\n")

# ex8 : Write a Pandas program to select the rows where the score is missing, i.e. is NaN.

print(df[df['score'].isnull()])
print("\n")

# ex9 : Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

print(df[df['score'].between(15, 20)])
print("\n")

# ex10 : Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

print(df[(df['attempts'] < 2) & (df['score'] > 15)])
print("\n")

# ex11 : Write a Pandas program to calculate the sum of the examination attempts by the students.

print("sum of examinations : ", df['attempts'].sum())

# ex12 : Write a Pandas program to calculate the mean score for each different student in DataFrame.

print("mean score : ", df['score'].mean())

# ex13 : Write a Pandas program to sort the data frame first by 'name' in descending order, then by 'score' in ascending order.

print(df.sort_values(by=['name'], ascending=[False]))
print("\n")
print(df.sort_values(by=['score'], ascending=[True]))
print("\n")

# ex14 : Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.

df['qualify'] = df['qualify'].map({'yes': True, 'no': False})
print(df)
print("\n")

# ex15 : Write a Pandas program to insert a new column in existing DataFrame

def addNewColumn(df, column_data, column_name):
    df[column_name] = column_data
    return df

column_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
column_name = 'newColumn'
df = addNewColumn(df, column_data, column_name)

print(df)
print("\n")

# ex16 : Write a Pandas program to iterate over rows in a DataFrame.

for index, row in df.iterrows():
    print(row['name'], row['score'])
print("\n")

# ex17 : Write a Pandas program to get list from DataFrame column headers.

print(list(df.columns.values))
print("\n")

# ex18 : Write a Pandas program to rename columns of a given DataFrame.

df = pd.DataFrame(np.arange(1, 10).reshape(3, 3), columns=['col1', 'col2', 'col3'])
print(df)
print("\n")

df = df.rename(columns={'col1': 'column1', 'col2': 'column2', 'col3': 'column3'})
print(df)
print("\n")

# ex19 : Write a Pandas program to write a DataFrame to CSV file using tab separator.

df = pd.DataFrame([[1, 4, 7], [4, 5, 8], [3, 6, 9], [4, 7, 0], [5, 8, 1]], index=np.arange(0, 5), columns=['col1', 'col2', 'col3'])
print(df)

df.to_csv('data.csv', sep='\t')