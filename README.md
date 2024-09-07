# EDA for Telecom Data

This repository contains exploratory data analysis (EDA) for the telecom dataset. The analysis is performed using Jupyter notebooks and Python scripts to clean, analyze, and visualize the data. Below is a summary of the key steps and functions used in the analysis.

## Overview

1. **Data Loading**:
   - Connect to the PostgreSQL database and retrieve the data using the `get_data_from_postgres` function.
   - The dataset used for analysis is `xdr_data`.

2. **Data Cleaning**:
   - Clean the dataset using the `clean_data` function to handle missing values and outliers.

3. **Handset and Manufacturer Analysis**:
   - Identify the top 10 handsets using `get_top_handsets`.
   - Determine the top 3 manufacturers using `get_top_manufacturers`.
   - Identify the top 5 handsets for each of the top 3 manufacturers using `get_top_handsets_per_manufacturer`.

4. **User Segmentation**:
   - Segment users based on `Activity Duration DL (ms)` using the `segment_users` function.

5. **Exploratory Data Analysis**:
   - **Basic Metrics**: Compute basic metrics using `basic_metrics`.
   - **Univariate Analysis**: Plot univariate distributions using `plot_univariate`.
   - **Bivariate Analysis**: Plot bivariate relationships and analyze them using `plot_bivariate`.
   - **Correlation Analysis**: Compute and plot the correlation matrix using `compute_correlation_matrix` and `plot_correlation_matrix`.

6. **Dimensionality Reduction**:
   - Apply Principal Component Analysis (PCA) using `apply_pca` to reduce dimensions and interpret the results using `interpret_pca`.

## Files and Functions

### `notebooks/scripts/db_connection.py`

- **`get_data_from_postgres(query, db_config)`**:
  Connects to a PostgreSQL database, executes the SQL query provided, and returns the result as a pandas DataFrame.

### `notebooks/scripts/data_processing.py`

- **`load_data()`**: Loads the dataset.
- **`clean_data(df)`**: Cleans the data by handling missing values and outliers.
- **`segment_users(df, column)`**: Segments users based on the specified column.
- **`get_top_handsets(df)`**: Returns the top 10 handsets.
- **`get_top_manufacturers(df)`**: Returns the top 3 manufacturers.
- **`get_top_handsets_per_manufacturer(df, manufacturers)`**: Returns the top 5 handsets per specified manufacturers.

### `notebooks/scripts/eda_functions.py`

- **`basic_metrics(df)`**: Computes basic metrics for the dataset.
- **`compute_dispersion(df, column)`**: Computes dispersion metrics.
- **`bivariate_analysis(df, target, features)`**: Performs bivariate analysis between target variable and specified features.
- **`compute_correlation_matrix(df, features)`**: Computes the correlation matrix for specified features.

### `notebooks/scripts/visualizations.py`

- **`plot_univariate(df, column)`**: Plots the univariate distribution of the specified column.
- **`plot_bivariate(df, x, y)`**: Plots the bivariate relationship between the specified columns.
- **`plot_correlation_matrix(corr_matrix)`**: Plots the correlation matrix.

### `notebooks/scripts/pca_functions.py`

- **`apply_pca(df, features, n_components)`**: Applies PCA to the specified features and returns the results.
- **`interpret_pca(pca_results, explained_variance)`**: Interprets the PCA results and explained variance.

## Running the Analysis

1. **Set Up Environment**:
   Ensure you have the required libraries installed (e.g., pandas, psycopg2, matplotlib, sklearn).

2. **Execute Notebook**:
   Open `notebooks/eda_task_1.ipynb` and run the cells sequentially to perform the analysis.

3. **Review Results**:
   Check the outputs for the top handsets, manufacturers, and visualizations to gain insights from the data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of the libraries used in this analysis.
