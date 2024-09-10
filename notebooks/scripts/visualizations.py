import matplotlib.pyplot as plt
import seaborn as sns

def plot_univariate(df, column, kde=True, bins=30):
    """
    Plot univariate distribution of a column.
    
    Args:
        df (DataFrame): The input data frame.
        column (str): Column name to plot.
        kde (bool): Whether to include kernel density estimate (default True).
        bins (int): Number of histogram bins (default 30).
    """
    if column not in df.columns:
        print(f"Error: Column '{column}' not found in DataFrame.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=kde, bins=bins)
    plt.title(f"Univariate Analysis of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()


def plot_correlation_matrix(df):
    """
    Plot correlation matrix for numeric columns of the data frame.

    Args:
        df (DataFrame): The input data frame.
    """
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    if numeric_df.empty:
        print("Error: No numeric columns found for correlation matrix.")
        return
    
    # Compute the correlation matrix
    corr_matrix = numeric_df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Matrix")
    plt.show()



def plot_bivariate(df, x, y):
    """
    Plot bivariate analysis of two columns.
    
    Args:
        df (DataFrame): The input data frame.
        x (str): Column name for x-axis.
        y (str): Column name for y-axis.
    """
    if x not in df.columns or y not in df.columns:
        print(f"Error: One of the columns '{x}' or '{y}' not found in DataFrame.")
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f"Bivariate Analysis: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()



def plot_distribution(df, category_col, value_col):
    """
    Plots the distribution of a numeric variable across different categories.

    Parameters:
    - df (pd.DataFrame): The input data frame.
    - category_col (str): The categorical column to group by (e.g., 'handset_type').
    - value_col (str): The numeric column to plot the distribution for (e.g., 'avg_throughput').
    """
    plt.figure(figsize=(12, 6))
    
    # Plotting the distribution of the numeric variable for each category
    sns.boxplot(x=category_col, y=value_col, data=df)
    
    # Adding titles and labels
    plt.title(f'Distribution of {value_col} per {category_col}', fontsize=16)
    plt.xlabel(category_col, fontsize=12)
    plt.ylabel(value_col, fontsize=12)
    
    # Rotate x-ticks for better readability
    plt.xticks(rotation=45)
    
    # Display the plot
    plt.tight_layout()
    plt.show()

