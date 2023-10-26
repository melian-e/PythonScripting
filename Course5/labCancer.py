import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

