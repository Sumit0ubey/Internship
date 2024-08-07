import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the dataset
data = pd.read_csv('V:/Coding/Internship/Data Analysis internship/householdtask3.csv')

# Summarizing the data set
print(data.head(10), '\n')
print(data.describe())


def Graph(graphName, x=None, y=None, topic=None, x_label=None, y_label=None, data=None):
    if graphName == 'bar':
        plt.bar(x, y)
    elif graphName == 'scatter':
        plt.scatter(x, y)
    elif graphName == 'line':
        plt.plot(x, y)
    elif graphName == 'hist':
        plt.hist(y, bins=10, edgecolor='black')
    elif graphName == 'box':
        sns.boxplot(x=x, y=y, data=data)
    elif graphName == 'violin':
        sns.violinplot(x=x, y=y, data=data)
    elif graphName == 'heatmap':
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    elif graphName == 'pairplot':
        sns.pairplot(data)
    else:
        raise ValueError("Graph type not supported")
    plt.title(topic)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


Graph(graphName='all_graph', data=data)

# Bar graph on year against eqv_exp, eqv_income, expenditure
Graph('bar', x=data['year'], y=data['eqv_exp'], x_label='Year', y_label='Average Expenses', topic='Average Expenses per year')
Graph('bar', x=data['year'], y=data['eqv_income'], x_label='Year', y_label='Average Income', topic='Average Income per year')
Graph('bar', x=data['year'], y=data['expenditure'], x_label='Year', y_label='Expenditure', topic='Year vs Expenditure')

# Scatter Plot on year against own, age, prop_hhs
Graph('scatter', x=data['year'], y=data['own'], x_label='Year', y_label='Own', topic='Own vs Year')
Graph('scatter', x=data['year'], y=data['age'], x_label='Year', y_label='Age', topic='Age vs Year')
Graph('scatter', x=data['year'], y=data['prop_hhs'], x_label='Year', y_label='Proportion of Households', topic='Proportion of Households vs Year')

# Line Plot on year against eqv_exp, eqv_income, expenditure
Graph('line', x=data['year'], y=data['eqv_exp'], x_label='Year', y_label='Average Expenses', topic='Average Expenses per year (Line)')
Graph('line', x=data['year'], y=data['eqv_income'], x_label='Year', y_label='Average Income', topic='Average Income per year (Line)')
Graph('line', x=data['year'], y=data['expenditure'], x_label='Year', y_label='Expenditure', topic='Year vs Expenditure (Line)')

# Histogram of eqv_exp, eqv_income, and expenditure
Graph('hist', x=None, y=data['eqv_exp'], x_label='Average Expenses', y_label='Frequency', topic='Histogram of Average Expenses')
Graph('hist', x=None, y=data['eqv_income'], x_label='Average Income', y_label='Frequency', topic='Histogram of Average Income')
Graph('hist', x=None, y=data['expenditure'], x_label='Expenditure', y_label='Frequency', topic='Histogram of Expenditure')

# Box Plot on eqv_exp, eqv_income, and expenditure
Graph('box', x='year', y='eqv_exp', x_label='Year', y_label='Average Expenses', topic='Box Plot of Average Expenses per Year', data=data)
Graph('box', x='year', y='eqv_income', x_label='Year', y_label='Average Income', topic='Box Plot of Average Income per Year', data=data)
Graph('box', x='year', y='expenditure', x_label='Year', y_label='Expenditure', topic='Box Plot of Expenditure per Year', data=data)

# Violin Plot on eqv_exp, eqv_income, and expenditure
Graph('violin', x='year', y='eqv_exp', x_label='Year', y_label='Average Expenses', topic='Violin Plot of Average Expenses per Year', data=data)
Graph('violin', x='year', y='eqv_income', x_label='Year', y_label='Average Income', topic='Violin Plot of Average Income per Year', data=data)
Graph('violin', x='year', y='expenditure', x_label='Year', y_label='Expenditure', topic='Violin Plot of Expenditure per Year', data=data)

# Heatmap of correlation matrix
Graph('heatmap', x=None, y=None, x_label='', y_label='', topic='Heatmap of Correlation Matrix', data=data)

# Pair Plot of the dataset
Graph('pairplot', x=None, y=None, x_label='', y_label='', topic='Pair Plot of the Dataset', data=data)

