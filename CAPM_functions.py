import plotly.express as px
import numpy as np
#creating function

def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    
    fig.update_layout(
        width=800,
        height=500,
        margin=dict(l=20, r=20, t=80, b=20),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1
        ),
        title=dict(
            text="Stock Price Comparison",
            y=0.98,
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        hovermode='x unified',
        template='plotly_white'
    )
    
    return fig

#function to normalize the prices

def normalize (df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i]/df[i][0]
    return df 

# function to calculate daily return

def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns [1:]:
        for j in range (1,len(df)):
            df[i][j]= ((df[i][j] - df [i][j-1])/df[i][j-1])*100
    df_daily_return[i][0] = 0 
    return df_daily_return

#function to calculate beta

def calculate_beta(stocks_daily_return , stock):
    rm = stocks_daily_return ['sp500'].mean()*252

    b,a = np.polyfit(stocks_daily_return['sp500'] , stocks_daily_return[stock] , 1)
    return b ,a 
