import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

# -------------------- CACHE DATA --------------------
@st.cache_data(ttl=3600)
def get_data(ticker, start_date='2010-01-01'):
    """
    Fetch historical close price data from yfinance and return the 'Close' column
    """
    stock_data = yf.download(ticker, start=start_date)
    if stock_data.empty:
        return pd.Series(dtype=float)
    return stock_data['Close']

# -------------------- STATIONARY CHECK --------------------
def stationary_check(close_price):
    """
    Perform ADF test to check stationarity
    """
    adf_test = adfuller(close_price)
    p_value = round(adf_test[1], 3)
    return p_value

# -------------------- ROLLING MEAN --------------------
def get_rolling_mean(close_price, window=7):
    """
    Returns rolling mean of the close price
    """
    return close_price.rolling(window=window).mean().dropna()

# -------------------- DIFFERENCING ORDER --------------------
def get_differencing_order(close_price, max_d=5):
    """
    Determine d (differencing order) for ARIMA to make series stationary
    """
    p_value = stationary_check(close_price)
    d = 0
    while p_value > 0.05 and d < max_d:
        d += 1
        close_price = close_price.diff().dropna()
        p_value = stationary_check(close_price)
    return d

# -------------------- FIT ARIMA MODEL --------------------
def fit_model(data, differencing_order, p=5, q=5, forecast_steps=30):
    """
    Fit ARIMA model on given data and return forecast for next 'forecast_steps' points
    """
    if len(data) < max(p, q) + 1:
        # Not enough data
        return pd.Series(dtype=float)
    
    model = ARIMA(data, order=(p, differencing_order, q))
    model_fit = model.fit()
    forecast = model_fit.get_forecast(steps=forecast_steps)
    predictions = forecast.predicted_mean
    return predictions

# -------------------- EVALUATE MODEL --------------------
def evaluate_model(original_price, differencing_order):
    """
    Evaluate ARIMA model using RMSE on last 30 points
    """
    if len(original_price) <= 30:
        return None  # Not enough data
    train_data, test_data = original_price[:-30], original_price[-30:]
    predictions = fit_model(train_data, differencing_order)
    if len(predictions) != len(test_data):
        return None
    rmse = np.sqrt(mean_squared_error(test_data, predictions))
    return round(rmse, 2)

# -------------------- SCALING --------------------
def scaling(close_price):
    """
    Standardize the close price
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(np.array(close_price).reshape(-1, 1))
    return scaled_data, scaler

def inverse_scaling(scaler, scaled_data):
    """
    Convert scaled data back to original values
    """
    return scaler.inverse_transform(np.array(scaled_data).reshape(-1, 1))

# -------------------- GET FORECAST --------------------
def get_forecast(original_price, differencing_order, forecast_steps=30):
    """
    Generate ARIMA forecast dataframe with future dates
    """
    predictions = fit_model(original_price, differencing_order, forecast_steps=forecast_steps)
    if predictions.empty:
        return pd.DataFrame(columns=['Close'])
    
    start_date = datetime.now()
    forecast_index = pd.date_range(start=start_date, periods=forecast_steps, freq='D')
    forecast_df = pd.DataFrame(predictions.values, index=forecast_index, columns=['Close'])
    return forecast_df

# -------------------- USAGE EXAMPLE --------------------
# You can use this in your Streamlit app like this:

# ticker = st.text_input("Enter Stock Ticker", "AAPL")
# close_price = get_data(ticker)
# if close_price.empty:
#     st.warning("No data available for this ticker!")
# else:
#     st.line_chart(close_price)
#     d = get_differencing_order(close_price)
#     forecast = get_forecast(close_price, d)
#     st.line_chart(forecast['Close'])
