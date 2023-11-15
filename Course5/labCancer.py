import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

#create a dataframe from the iris_2 csv file
df = pd.read_csv('Breast_cancer_data.csv')

# 1 Is the classification problem binary or multi-class?

print("It's binary because the values are either malignant or benign")

# 2 We propose to use the features Radius Worst and Compactness Worst to do the classification.
# a. Using Pearson correlation, find the correlation between the two features. What do the results reveal?

print(df[['radius_worst', 'compactness_worst']].corr(method='pearson'))
print("We can see that there is a strong positive correlation between the two features")

# b. Using seaborn, print their correlation heatmap.

sns.heatmap(df[['radius_worst', 'compactness_worst']].corr(method='pearson'))
plt.show()

# c. Find the correlation between each feature and the dependent variable. What do the results reveal? Look at the appendix to see the function that allows finding the correlation between a numerical variable and a categorical one.

df = df.drop(['id'], axis=1)
df['diagnosis']=df['diagnosis'].astype('category').cat.codes
print(df[['radius_worst', 'compactness_worst']].corrwith(df['diagnosis'],method='pearson'))

# d. Given all the correlation measures, is predicting the dependent variable given these two features a good idea? Justify.

print("It seems like a good idea because the is high and similar")

# 3 List the data preprocessing steps that should be made, by explaining and justifying each step.

print("Verify if there are any missing values")
print("Verify if there are any categorical variables")
print("Feature Scaling")
print("Allow for values to be easily comparable")

# 4 Write in python the code that performs data preprocessing.

print(df.isnull().values.any())
df = df.dropna()
df = df.drop(['Unnamed: 32'], axis=1)
df['diagnosis']=df['diagnosis'].astype('category').cat.codes
df.dropna("columns")

print(df.dtypes)
print(df.isnull().values.any())

# 5 Build the logistic regression model (using scikit-learn) and save it.