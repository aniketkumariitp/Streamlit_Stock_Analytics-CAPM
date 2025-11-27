import plotly.graph_objects as go
import dateutil
import datetime
import numpy as np
import ta   # ✔ REPLACED pandas_ta

# ---------------------- TABLE ----------------------
def plotly_table_glassmorphism(dataframe, title=None, height=None):
    colors = {
        'header': 'rgba(255, 75, 75, 0.9)',
        'header_text': 'white',
        'row_odd': 'rgba(240, 242, 246, 0.6)',
        'row_even': 'rgba(255, 255, 255, 0.8)',
        'border': 'rgba(230, 234, 241, 0.5)',
        'text': "#FEFEFF"
    }

    row_colors = [colors['row_odd'] if i % 2 == 0 else colors['row_even']
                  for i in range(len(dataframe))]

    column_headers = ["<b>🎯 Index</b>"] + [f"<b>✨ {col}</b>" for col in dataframe.columns]

    cell_values = [[f"<b>{idx}</b>" for idx in dataframe.index]]
    for col in dataframe.columns:
        cell_values.append(dataframe[col].tolist())

    if height is None:
        height = 50 + len(dataframe) * 40 + (60 if title else 15) + 30

    fig = go.Figure(data=[
        go.Table(
            header=dict(
                values=column_headers,
                line_color='rgba(255, 255, 255, 0.3)',
                fill_color=colors['header'],
                align='center',
                font=dict(color=colors['header_text'], size=16),
                height=50
            ),
            cells=dict(
                values=cell_values,
                fill_color=[['rgba(0,0,0,0)'] + row_colors],
                align=['center'] + ['left'] * len(dataframe.columns),
                line_color=colors['border'],
                font=dict(color=colors['text'], size=14),
                height=40
            )
        )
    ])

    fig.update_layout(
        title=dict(text=title if title else "", font=dict(size=22), x=0.5),
        height=height,
        margin=dict(l=0, r=0, t=60 if title else 0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# ---------------------- FILTER ----------------------
def filter_data(dataframe, num_period):
    if num_period == '1mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-1)
    elif num_period == '5d':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(days=-5)
    elif num_period == '6mo':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(months=-6)
    elif num_period == '1y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-1)
    elif num_period == '5y':
        date = dataframe.index[-1] + dateutil.relativedelta.relativedelta(years=-5)
    elif num_period == 'ytd':
        date = datetime.datetime(dataframe.index[-1].year, 1, 1).strftime('%Y-%m-%d')
    else:
        date = dataframe.index[0]

    return dataframe.reset_index()[dataframe.reset_index()['Date'] > date]

# ---------------------- CHARTS ----------------------
def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open'))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High'))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low'))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500)
    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=dataframe['Date'], open=dataframe['Open'],
        high=dataframe['High'], low=dataframe['Low'],
        close=dataframe['Close']
    ))
    fig.update_layout(height=500)
    return fig

# ---------------------- RSI ----------------------
def RSI(dataframe, num_period):
    dataframe['RSI'] = ta.momentum.RSIIndicator(dataframe['Close']).rsi()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['RSI'], name='RSI'))

    fig.add_trace(go.Scatter(x=dataframe['Date'], y=[70]*len(dataframe),
                             name='Overbought', line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=[30]*len(dataframe),
                             name='Oversold', line=dict(dash='dash')))
    fig.update_layout(yaxis_range=[0,100], height=200)
    return fig

# ---------------------- SMA ----------------------
def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = ta.trend.SMAIndicator(dataframe['Close'], window=50).sma_indicator()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], name='Close'))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'], name='SMA 50'))
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(height=500)
    return fig

# ---------------------- MACD ----------------------
def MACD(dataframe, num_period):
    macd_indicator = ta.trend.MACD(dataframe['Close'])

    dataframe['MACD'] = macd_indicator.macd()
    dataframe['Signal'] = macd_indicator.macd_signal()
    dataframe['Hist'] = macd_indicator.macd_diff()

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['MACD'], name='MACD'))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Signal'], name='Signal'))
    fig.add_trace(go.Bar(x=dataframe['Date'], y=dataframe['Hist'], name='Histogram'))
    fig.update_layout(height=200)
    return fig

# ---------------------- FORECAST ----------------------
def Moving_average_forecast(forecast):
    import plotly.graph_objects as go
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=forecast.index[:-30], y=forecast['Close'].iloc[:-30], name='Historical'))
    fig.add_trace(go.Scatter(x=forecast.index[-31:], y=forecast['Close'].iloc[-31:], name='Forecast', line=dict(dash='dash')))
    
    fig.update_layout(height=500, xaxis_title='Date', yaxis_title='Price')
    fig.update_xaxes(rangeslider_visible=True)
    return fig
