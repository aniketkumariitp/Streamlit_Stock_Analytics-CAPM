import streamlit as st
import pandas as pd 
import yfinance as yf
import datetime as datetime
import numpy as np 
import plotly.graph_objects as go
from pages.utils.plotly_figure import plotly_table_glassmorphism , filter_data , close_chart , candlestick ,RSI , Moving_average , MACD 

st.title("Stock Analysis")
col1 , col2 , col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker" , "AAPL")
# with col2:
#     start_date = st.date_input("Choose start Date" , datetime.date(today.year -1 , today.month , today.day))
# with col3:
#     end_date = st.date_input("Choose end Date " , datetime.date(today.year - 1 , today.month , today.day))


st.subheader(ticker)

stock = yf. Ticker(ticker)

st.write(stock.info['longBusinessSummary'] )
st.write("**Sector:**", stock. info['sector'])
st.write("**Full Time Employees:**" ,stock. info ['fullTimeEmployees' ])
st.write("**Website:**", stock. info [ 'website'])

col1 , col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index = ['Market Cap' , 'Beta' , 'EPS', 'PE Ratio'])
    df[''] = [stock.info["marketCap"] , stock.info["beta"] , stock.info["trailingEps"] , stock.info["trailingPE"]]
    fig_df = plotly_table_glassmorphism(df)
    st.plotly_chart(fig_df , use_container_width= True)
with col2:
    # Financial metrics
    metrics = {
        'Quick Ratio': stock.info.get('quickRatio', 'N/A'),
        'Revenue per Share': stock.info.get('revenuePerShare', 'N/A'),
        'Profit Margins': stock.info.get('profitMargins', 'N/A'),
        'Debt to Equity': stock.info.get('debtToEquity', 'N/A'),
        'Return on Equity': stock.info.get('returnOnEquity', 'N/A')
    }
    
    df = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
    
    fig_df = plotly_table_glassmorphism(df)
    st.plotly_chart(fig_df, width='stretch')

# data = yf.download(ticker , start = start_date , end = end_date )

# col1 , col2 , col3 = st.columns(3)
# daily_change = data ['Close'].iloc[-1] - data ['Close'].iloc[-2]
# col1.metric("Daily Change" , str(round(data['Close'].iloc[-1],2)) , str(round(daily_change , 2)))


ticker = "AAPL" 
start_date = st.date_input("Start Date", pd.to_datetime("today")) 
end_date = st.date_input("End Date", pd.to_datetime("today"))

data = yf.download(ticker, start=start_date, end=end_date, progress=False)

if len(data) < 2:
    data = yf.download(ticker, period="5d", progress=False)


col1, col2, col3 = st.columns(3)

if not data.empty and len(data) >= 2:
    
    current_price = data['Close'].iloc[-1]
    previous_price = data['Close'].iloc[-2]
    daily_change = current_price - previous_price
    current_val = float(current_price)
    change_val = float(daily_change)
    col1.metric(
        label="Daily Change", 
        value=f"{current_val:.2f}", 
        delta=f"{change_val:.2f}"
    )
    st.caption(f"Showing data for: {data.index[-1].date()}")

else:
    col1.error("Invalid Ticker Symbol")

last_Ten_df = data.tail(10).sort_index(ascending = False).round(3)
fig_df = plotly_table_glassmorphism(last_Ten_df)

st.write('##### Historical Data (Last 10 days)')
st.plotly_chart (fig_df , use_container_width = True )

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns([1,1,1,1,1,1,1,1,1,1,1,1])

num_period = " "  # Default value

with col1:
    if st.button('5D'):
        num_period = '5d'

with col2:
    if st.button('1M'):
        num_period = '1mo'

with col3:
    if st.button('6M'):
        num_period = '6mo'

with col4:
    if st.button('YTD'):
        num_period = 'ytd'

with col5:
    if st.button('1Y'):
        num_period = '1y'

with col6:
    if st.button('5Y'):
        num_period = '5y'

col1, col2, col3 = st.columns([1, 1, 4])

with col1:
    chart_type = st.selectbox("", ('Candle', 'Line'))

with col2:
    if chart_type == 'Candle':
        indicators = st.selectbox("", ('RSI', 'MACD'))
    else:
        indicators = st.selectbox("", ('RSI', 'Moving Average', 'MACD'))

ticker_ = yf.Ticker(ticker)
new_df1 = ticker_.history(period='max')
data1 = ticker_.history(period='max')

# Fetch historical data once
ticker_ = yf.Ticker(ticker)
df = ticker_.history(period='max')

# Set default period if empty
if num_period == '':
    num_period = '1y'

# Display charts based on chart type and indicator selection
if chart_type == 'Candle':
    # Using YOUR candlestick function here ✓
    st.plotly_chart(candlestick(df, num_period), use_container_width=True)
    
    # Display indicator
    if indicators == 'RSI':
        # Using YOUR RSI function here ✓
        st.plotly_chart(RSI(df, num_period), use_container_width=True)
    elif indicators == 'MACD':
        # Using YOUR MACD function here ✓
        st.plotly_chart(MACD(df, num_period), use_container_width=True)

elif chart_type == 'Line':
    # Display appropriate line chart based on indicator
    if indicators == 'Moving Average':
        # Using YOUR Moving_average function here ✓
        st.plotly_chart(Moving_average(df, num_period), use_container_width=True)
    else:
        # Using YOUR close_chart function here ✓
        st.plotly_chart(close_chart(df, num_period), use_container_width=True)
        
        # Display indicator
        if indicators == 'RSI':
            # Using YOUR RSI function here ✓
            st.plotly_chart(RSI(df, num_period), use_container_width=True)
        elif indicators == 'MACD':
            # Using YOUR MACD function here ✓
            st.plotly_chart(MACD(df, num_period), use_container_width=True)