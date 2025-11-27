import plotly.graph_objects as go 
import dateutil
import datetime
import numpy as np 
import pandas_ta as pta

def plotly_table_glassmorphism(dataframe, title=None, height=None):
    """
    Modern glassmorphism-inspired table design
    """
    
    colors = {
        'header': 'rgba(255, 75, 75, 0.9)',      # Semi-transparent red
        'header_text': 'white',
        'row_odd': 'rgba(240, 242, 246, 0.6)',   # Glass effect
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
    
    # Calculate height based on number of rows
    if height is None:
        header_height = 50
        cell_height = 40
        title_space = 60 if title else 15
        height = header_height + (len(dataframe) * cell_height) + title_space + 30
    
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=column_headers,
                    line_color='rgba(255, 255, 255, 0.3)',
                    fill_color=colors['header'],
                    align='center',
                    font=dict(
                        color=colors['header_text'],
                        size=16,
                        family='Source Sans Pro, sans-serif'
                    ),
                    height=50
                ),
                cells=dict(
                    values=cell_values,
                    fill_color=[['rgba(0,0,0,0)'] + row_colors],
                    align=['center'] + ['left'] * len(dataframe.columns),
                    line_color=colors['border'],
                    font=dict(
                        color=colors['text'],
                        size=14,
                        family='Source Sans Pro, sans-serif'
                    ),
                    height=40
                )
            )
        ]
    )
    
    fig.update_layout(
        title=dict(
            text=title if title else "",
            font=dict(size=22, color='#262730'),
            x=0.5,
            xanchor='center'
        ),
        height=height,
        margin=dict(l=0, r=0, t=60 if title else 0, b=0),
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent background
        plot_bgcolor='rgba(0, 0, 0, 0)'     # Transparent plot area
    )
    
    return fig

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

def close_chart(dataframe, num_period=False):
    if num_period:
        dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], 
        y=dataframe['Open'], 
        mode='lines', 
        name='Open', 
        line=dict(width=2, color='#5ab7ff')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], 
        y=dataframe['Close'], 
        mode='lines', 
        name='Close', 
        line=dict(width=2, color='black')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], 
        y=dataframe['High'], 
        mode='lines', 
        name='High', 
        line=dict(width=2, color='#0078ff')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'], 
        y=dataframe['Low'], 
        mode='lines', 
        name='Low', 
        line=dict(width=2, color='red')
    ))
    
    fig.update_xaxes(rangeslider_visible=True)
    
    fig.update_layout(
        height=500, 
        margin=dict(l=0, r=20, t=20, b=0), 
        plot_bgcolor='white', 
        paper_bgcolor='#e1efff', 
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
    )
    
    return fig

def candlestick(dataframe, num_period):
    dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Candlestick(
        x=dataframe['Date'],
        open=dataframe['Open'],
        high=dataframe['High'],
        low=dataframe['Low'],
        close=dataframe['Close']
    ))
    
    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff'
    )
    
    return fig

def RSI(dataframe, num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe.RSI,
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70]*len(dataframe),
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30]*len(dataframe),
        fill='tonexty',
        name='Oversold',
        marker_color='#79da84',
        line=dict(width=2, color='#79da84', dash='dash')
    ))
    
    fig.update_layout(
        yaxis_range=[0, 100],
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], 50)
    dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['Open'],
        mode='lines',
        name='Open',
        line=dict(width=2, color='#5ab7ff')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['Close'],
        mode='lines',
        name='Close',
        line=dict(width=2, color='black')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['High'],
        mode='lines',
        name='High',
        line=dict(width=2, color='#0078ff')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['Low'],
        mode='lines',
        name='Low',
        line=dict(width=2, color='red')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['SMA_50'],
        mode='lines',
        name='SMA 50',
        line=dict(width=2, color='purple')
    ))
    
    fig.update_xaxes(rangeslider_visible=True)
    
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
    )
    
    return fig

def MACD(dataframe, num_period):
    macd = pta.macd(dataframe['Close']).iloc[:, 0]
    macd_signal = pta.macd(dataframe['Close']).iloc[:, 1]
    macd_hist = pta.macd(dataframe['Close']).iloc[:, 2]
    
    dataframe['MACD'] = macd
    dataframe['MACD Signal'] = macd_signal
    dataframe['MACD Hist'] = macd_hist
    
    dataframe = filter_data(dataframe, num_period)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD'],
        name='MACD',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))
    
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD Signal'],
        name='Signal',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))
    
    fig.add_trace(go.Bar(
        x=dataframe['Date'],
        y=dataframe['MACD Hist'],
        name='Histogram',
        marker_color=['red' if val < 0 else 'green' for val in dataframe['MACD Hist']]
    ))
    
    fig.update_layout(
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#e1efff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="top", y=1.02, xanchor="right", x=1)
    )
    return fig

def Moving_average_forecast(forecast):
    import plotly.graph_objects as go
    
    fig = go.Figure()

    # Historical Close Price
    fig.add_trace(
        go.Scatter(
            x=forecast.index[:-30],
            y=forecast['Close'].iloc[:-30],
            mode='lines',
            name='Historical Close Price',
            line=dict(width=2)
        )
    )

    # Future Close Price
    fig.add_trace(
        go.Scatter(
            x=forecast.index[-31:],
            y=forecast['Close'].iloc[-31:],
            mode='lines',
            name='Predicted Future Price',
            line=dict(width=2, dash='dash')
        )
    )

    fig.update_layout(
        height=500,
        margin=dict(l=40, r=40, t=40, b=40),
        plot_bgcolor='white',
        paper_bgcolor='black',
        xaxis_title='Date',
        yaxis_title='Stock Price',
        legend=dict(
            title='Legend',
            yanchor="top",
            y=0.98,
            xanchor="right",
            x=0.98
        ),
        hovermode='x'
    )

    fig.update_xaxes(rangeslider_visible=True)
    return fig
