# TellCo User Engagement & Overview Analysis
## Week 2 Challenge - 10 Academy AI Mastery Program

### Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Data Description](#data-description)
- [Tasks Breakdown](#tasks-breakdown)
  - [Task 1: User Overview Analysis](#task-1-user-overview-analysis)
  - [Task 2: User Engagement Analysis](#task-2-user-engagement-analysis)
- [Setup and Installation](#setup-and-installation)
- [How to Run the Project](#how-to-run-the-project)
- [Results and Insights](#results-and-insights)
- [Next Steps](#next-steps)

---

## Project Overview
TellCo, a mobile service provider in the Republic of Pefkakia, has provided xDR (data session detail) records to perform an in-depth analysis of customer activity. The goal is to identify growth opportunities and make a recommendation for a potential business acquisition by a wealthy investor.

### Key Objectives
- **User Overview Analysis**: Explore and understand customer behaviors, including the most popular handsets and application usage.
- **User Engagement Analysis**: Analyze customer engagement based on session frequency, duration, and data usage. Segment customers using clustering techniques.

### Technologies Used
- **Python** (pandas, matplotlib, seaborn, scikit-learn)
- **PostgreSQL** (for database handling)
- **Jupyter Notebooks**
- **psycopg2** (for PostgreSQL connection)

---

## Project Structure
```plaintext
├── .github/               # CI/CD pipelines, testing workflows (optional)
├── .vscode/               # VSCode-specific settings
├── data/                  # Data source files and SQL schema
│   ├── schema.sql         # SQL schema for the xDR data
│   ├── week-2-data.csv    # Data used for the analysis
├── notebooks/
│   ├── eda_task_1.ipynb   # Notebook for Task 1 (User Overview Analysis)
│   ├── eda_task_2.ipynb   # Notebook for Task 2 (User Engagement Analysis)
│   ├── scripts/           # Directory containing Python scripts
│       ├── db_connection.py    # Script for database connection
|       ├── analysis_utils.py   # Script for analysis
|       ├── eda_fuctions.py     # Script for eda on task 1
|       ├── pca_fuctions.py     # Script for eda on task 1 (pca)
|       ├── user_engagement.py  # Script for task 2
|       ├── data_loader.py      # Script for loading data (only testing purpose)
│       ├── data_processing.py  # Functions for data processing and cleaning
│       ├── clustering.py       # Clustering logic and K-means algorithm
│       ├── visualizations.py   # Plotting and visualizing functions
├── requirements.txt       # Required Python libraries
├── README.md              # Project documentation (this file)

Data Description
The dataset consists of a month's worth of xDR (data session detail) records, capturing user activity across various applications like YouTube, Gaming, Netflix, and Social Media. Each record contains information on:

Bearer Id, IMSI, MSISDN/Number, IMEI: Identifiers for users and devices.
Session Details: Start/end timestamps, duration in milliseconds, and location.
Data Usage: Download/upload volume for applications like YouTube, Netflix, Google, etc.
RTT and TCP: Round-trip time and retransmission metrics for both download and upload.

Tasks Breakdown
Task 1: User Overview Analysis
Objective:
Understand customer behavior by exploring the following:

Top 10 handsets used by customers.
Top 3 handset manufacturers and their respective top 5 handsets.
Application Usage: Analyze data consumption for applications such as YouTube, Netflix, Gaming, and Social Media.
Steps:
EDA (Exploratory Data Analysis) to identify key patterns in handset usage.
Correlation Analysis to understand the relationship between application usage and total data consumption.
Segmentation: Segment users into deciles based on session duration and data usage.
Key Results:
Huawei and Apple dominate the handset market.
Applications such as Gaming and YouTube drive the majority of data usage.

Task 2: User Engagement Analysis
Objective:
Measure user engagement through session frequency, session duration, and data usage. Cluster users based on engagement metrics.

Steps:
Calculate Engagement Metrics for each customer.
K-Means Clustering: Classify customers into 3 engagement clusters.
Elbow Method: Determine the optimal number of clusters.
Plot Insights: Visualize the top 3 applications in terms of engagement.
Key Results:
Users fall into 3 distinct groups based on engagement metrics, with high-engagement users driving significant data consumption.
Gaming, YouTube, and Netflix are the most heavily used applications.

Setup and Installation
1. Clone the Repository

git clone git@github.com:SolomonZinabu/week-2.git
cd week-2


2. Install Dependencies
Install the necessary Python packages:

pip install -r requirements.txt

3. Set Up PostgreSQL Database
Install PostgreSQL on your local machine.
Create a database named telecom_data:
sql
CREATE DATABASE telecom_data;
Execute the schema.sql file to set up the table structure:
bash
psql -U postgres -d telecom_data -f data/schema.sql
Load the dataset:
sql
COPY xdr_data FROM 'C:/path_to_file/week-2-data.csv' DELIMITER ',' CSV HEADER;

4. Configure Database Connection
In the db_connection.py script, modify the db_config variable with your PostgreSQL credentials.

db_config = {
    'host': 'localhost',
    'database': 'telecom_data',
    'user': 'postgres',
    'password': 'your_password'
}

How to Run the Project
1. Run the Jupyter Notebooks
Launch the Jupyter notebook environment:

bash
jupyter notebook
Open the following notebooks:

eda_task_1.ipynb for User Overview Analysis
eda_task_2.ipynb for User Engagement Analysis
2. Analyze the Data
Use the notebooks to execute the analysis, generate visualizations, and explore insights.

Results and Insights

User Overview Analysis:
Top Handsets: Huawei B528S-23A and iPhone 6S are the most commonly used devices.
Top Manufacturers: Apple, Samsung, and Huawei dominate the customer base.
Application Usage: Gaming and YouTube are the most data-consuming applications.

User Engagement Analysis:
Engagement Clusters: Customers were grouped into 3 clusters based on their session frequency, session duration, and data usage.
Cluster 1: High-engagement users, contributing significantly to data usage.
Cluster 2: Moderate engagement.
Cluster 3: Low engagement.
Top Applications: Gaming, YouTube, and Netflix are the most engaged applications by data consumption.

Next Steps
Further Investigations:
Analyze low-engagement users to identify retention strategies.
Explore potential partnerships with popular handset manufacturers.
Dashboard Development:
Develop an interactive dashboard to communicate key insights.
Actionable Recommendations:
Focus marketing efforts on high-engagement users for premium services.
Allocate network resources to heavily used applications like Gaming, YouTube, and Netflix.