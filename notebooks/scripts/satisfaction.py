import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def calculate_engagement_scores(df):
    # Example to calculate engagement scores based on clustering
    return np.linalg.norm(df[['session_frequency', 'session_duration']] - least_engaged_cluster, axis=1)

def calculate_experience_scores(df):
    # Example to calculate experience scores based on clustering
    return np.linalg.norm(df[['tcp_retransmission', 'rtt']] - worst_experience_cluster, axis=1)

def build_regression_model(df, target):
    # Build a simple linear regression model
    X = df[['engagement_score', 'experience_score']]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    return model, mse
