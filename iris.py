import pandas as pd#import pandas library - for loading data
import matplotlib.pyplot as plt#import matplot lib library for visualization
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head())

    # Dataset structure
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean dataset (no missing values in this dataset, but shown for practice)
    df.dropna(inplace=True)

except Exception as e:
    print(f"Error loading the dataset: {e}")

# Task 2: Basic Data Analysis
try:
    print("\nBasic Statistics:")
    print(df.describe())

    # Group by species and compute mean of numerical features
    print("\nMean values grouped by species:")
    print(df.groupby("target").mean())

except Exception as e:
    print(f"Error during data analysis: {e}")

# Task 3: Data Visualization

# Set Seaborn style
sns.set(style="whitegrid")

try:
    # 1. Line chart (not ideal for Iris, so let's create a pseudo time-series)
    df['index'] = df.index
    plt.figure(figsize=(10, 5))
    sns.lineplot(x='index', y='sepal length (cm)', data=df)
    plt.title('Sepal Length Trend Over Index')
    plt.xlabel('Index')
    plt.ylabel('Sepal Length (cm)')
    plt.show()

    # 2. Bar chart: average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x='target', y='petal length (cm)', data=df, estimator='mean', ci=None)
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Petal Length (cm)')
    plt.show()

    # 3. Histogram of sepal width
    plt.figure(figsize=(8, 5))
    sns.histplot(df['sepal width (cm)'], bins=20, kde=True)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Count')
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='target', palette='Set2')
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.show()

except Exception as e:
    print(f"Error during visualization: {e}")
