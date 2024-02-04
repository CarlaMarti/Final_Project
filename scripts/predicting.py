"""
Predictive model code
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression


def normalization(column, name, df_predict):
    """
    Normalization function
    """
    min_value = column.min()
    max_value = column.max()

    df_predict[name] = (column - min_value) / (max_value - min_value)


def predictive_model(df):
    """
    Predictive model function
    """

    # Select only numeric features
    numeric_columns = df.select_dtypes(include=['number']).columns
    x = df[numeric_columns].drop(columns=['Avg_Utilization_Ratio'])
    y = df['Avg_Utilization_Ratio']

    # Create train and test sets
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.1, random_state=0)

    # Normalization
    scaler = MinMaxScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Model fitting
    regr = LinearRegression()
    regr.fit(x_train_scaled, y_train)

    # Predictions
    y_pred = regr.predict(x_test_scaled)

    # Mean Absolute Error
    mae = mean_absolute_error(y_test, y_pred)
    print(f"MAE: {mae:.2f}")
