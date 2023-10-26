import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#create a dataframe from the iris_2 csv file
df = pd.read_csv('iris_2.csv')

#nb of colums and rows
print(df.shape)

#first 5 rows
print(df.head())

#keys of the dataframe
print(df.keys())

#any nan or missing values?
print(df.isnull().values.any())

#basic stats
print(df.describe())

# how are the three species of Iris distributed in the dataset? Do we have a balanced number of observations for all species?
print(df.groupby('Species').size())
#there are 50 of each species

# The first column does not give any insight concerning the data. Write the code that allows dropping this column.

df = df.drop('Unnamed: 0', axis=1)
print(df)


# Plot the frequency of the three species of Iris in the dataset by printing:
# a. A bar plot using seaborn

fig, axes = plt.subplots(1, 2)
sns.countplot(ax=axes[0], x='Species', data=df)
axes[0].set_title("bar plot")

# b. A pie plot using matplotlib.pyplot

df.groupby('Species').size().plot(kind='pie')
axes[1].set_title("pie plot")

# Is there any relationship between the sepal length and width of the three species? Answer by plotting:
# a. A scatter plot (each species is represented by a colour)

fig, axes = plt.subplots(1, 2)
sns.scatterplot(ax=axes[0], x='Sepal.Length', y='Sepal.Width', hue='Species', data=df)
axes[0].set_title("scatter plot")

# b. The correlation coefficients

sns.scatterplot(ax=axes[1], x='Petal.Length', y='Petal.Width', hue='Species', data=df)
axes[0].set_title("correlation coefficients")

# Use a histogram to plot the distribution of the length and width of sepal and petal in the dataset (use matplotlib).

df.hist()

# Create a joinplot (using seaborn) to describe individual distributions on the same plot between Sepal length and Sepal width.

sns.jointplot(x='Sepal.Length', y='Sepal.Width', data=df)

# Create a joinplot using "hexbin" to describe individual distributions on the same plot between Sepal length and Sepal width. The bivariate analogue of a histogram is known as a "hexbin" plot, because it shows the counts of observations that fall within hexagonal bins. This plot works best with relatively large datasets. It's available through the matplotlib plt.hexbin function and as a style in jointplot(). It looks best with a white background.

sns.jointplot(x='Sepal.Length', y='Sepal.Width', data=df, kind='hex')

# Create a joinplot using "kde" to describe individual distributions on the same plot between Sepal length and Sepal width. Note: The kernel density estimation (kde) procedure visualize the univariate and bivariate distributions. In seaborn, this kind of plot is shown with a contour plot and is available as a style in jointplot().

sns.jointplot(x='Sepal.Length', y='Sepal.Width', data=df, kind='kde')

# Draw a scatterplot, then add a joint density estimate to describe individual distributions on the same plot between Sepal length and Sepal width.

plt.figure(7)
sns.kdeplot(x='Sepal.Length', y='Sepal.Width', data=df)
sns.scatterplot(x='Sepal.Length', y='Sepal.Width', data=df)

# Create a pairplot of the iris data set and check which flower species seems to be the most separable.

sns.pairplot(df, hue='Species')

# Using seaborn, create a kde (Kernel Density Estimate) plot of sepal_length versus sepal width for setosa species of flower.

plt.figure(9)
sns.kdeplot(x='Sepal.Length', y='Sepal.Width', data=df, hue='Species', hue_order=['setosa'])

# Using seaborn, create a kde (Kernel Density Estimate ) plot of petal_length versus petal width for setosa species of flower.

plt.figure(10)
sns.kdeplot(x='Petal.Length', y='Petal.Width', data=df, hue='Species', hue_order=['setosa'])

# Using seaborn, create a kde (Kernel Density Estimate) plot of two shaded bivariate densities of Sepal Width and Sepal Length.

sns.kdeplot(x='Sepal.Length', y='Sepal.Width', data=df, shade=True)

# Find the correlation between variables of iris data. Also, create a heatmap using seaborn to present their relations.

plt.figure(11)
df = df.drop('Species', axis=1)
correlation = df.corr()
sns.heatmap(correlation, annot=True)

# Using seaborn, create a box plot (or box-and-whisker plot) which shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable of iris dataset.

plt.figure(12)
sns.boxplot(data=df)

plt.plot()
plt.show()