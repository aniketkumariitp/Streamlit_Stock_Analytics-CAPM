# 📈 Stock Market Analysis & Prediction Dashboard

A comprehensive Streamlit-based web application for stock market analysis, technical indicators visualization, and price prediction using ARIMA models.


![App Preview](pages/app.webp)

## 🚀 Live Demo

**[Launch Application](https://stocksanalyticscapm.streamlit.app/)** 🔗

Try the live application deployed on Streamlit Cloud!

---

## 🌟 Features

### 1. **Real-Time Stock Data Analysis**
- Fetch live stock data using Yahoo Finance API
- Display current prices, daily changes, and percentage movements
- Historical data visualization for the last 10 days
- Interactive date range selection

### 2. **Technical Analysis & Charting**
- **Chart Types:**
  - Candlestick charts
  - Line charts (Open, High, Low, Close)
  
- **Technical Indicators:**
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - SMA (Simple Moving Average - 50 period)
  
- **Interactive Features:**
  - Multiple timeframe selection (5D, 1M, 6M, YTD, 1Y, 5Y)
  - Range slider for detailed analysis
  - Customizable chart styles

### 3. **Price Prediction**
- ARIMA-based time series forecasting
- 30-day future price predictions
- Model performance metrics (RMSE score)
- Visual representation of historical vs predicted prices

### 4. **Stock Comparison**
- Compare multiple stocks simultaneously
- Raw price comparison
- Normalized price comparison for better relative performance analysis
- Support for major stocks (TSLA, GOOGL, AMZN, AAPL) and S&P 500

### 5. **Capital Asset Pricing Model (CAPM)**
- Multi-stock selection and analysis
- Historical data visualization
- Customizable time periods
- Comprehensive dataframe views (head and tail)

## 📸 Screenshots

### Stock Analysis Dashboard
![Stock Analysis Dashboard](https://github.com/user-attachments/assets/23e3fd16-3644-4f92-8966-728e1caa89ab)
*Real-time stock data with historical performance and interactive controls*

### CAPM Analysis
![Price Prediction](https://github.com/user-attachments/assets/4d5d1c56-cd34-4b3a-8898-16fde74671ec)
*30-day forecast with ARIMA model and RMSE evaluation*

### Stock Analysis
![Stock Comparison](https://github.com/user-attachments/assets/e25a23e4-9914-4912-a8eb-690b8e254f3f)
*Side-by-side comparison of multiple stocks with normalization*

### Price Prediction
![CAPM Analysis](https://github.com/user-attachments/assets/d0b140ff-019b-4101-ab60-a403f8872d6d)
*Capital Asset Pricing Model with multi-stock selection*

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly, Plotly Graph Objects |
| **Technical Analysis** | pandas_ta |
| **Financial Data** | yfinance |
| **ML/Statistics** | statsmodels (ARIMA, ADF), scikit-learn |
| **Date Handling** | datetime, python-dateutil |

## 📋 Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/aniketkumariitp/stock-analysis-dashboard.git
cd stock-analysis-dashboard
```

### 2. Install required packages
```bash
pip install streamlit yfinance plotly pandas-ta python-dateutil statsmodels scikit-learn numpy pandas
```

### 3. Fix NumPy compatibility (if needed)
```bash
pip install "numpy<2.3"
```

## 📁 Project Structure
```
stock-analysis-dashboard/
│
├── app.py                          # Main Streamlit application
├── pages/
│   ├── stock_analysis.py          # Stock analysis page
│   ├── prediction.py              # Price prediction page
│   ├── comparison.py              # Stock comparison page
│   ├── capm.py                    # CAPM analysis page
│   └── utils/
│       ├── model_train.py         # ARIMA model training utilities
│       └── plotly_figure.py       # Plotly chart creation functions
│
├── functions/
│   ├── candlestick.py            # Candlestick chart function
│   ├── close_chart.py            # Line chart function
│   ├── RSI.py                    # RSI indicator function
│   ├── MACD.py                   # MACD indicator function
│   ├── Moving_average.py         # Moving average function
│   └── filter_data.py            # Data filtering utilities
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── screenshots/                   # Application screenshots
```

## 🎯 Usage

### 1. Run the application locally
```bash
streamlit run app.py
```

Or visit the **[Live Demo](https://stocksanalyticscapm.streamlit.app/)** 🌐

### 2. Navigate through pages
- Use the sidebar to switch between different analysis tools
- Select stock tickers and time periods
- Choose chart types and technical indicators

### 3. Stock Analysis
- Enter a stock ticker (e.g., AAPL, GOOGL, TSLA)
- Select chart type (Candlestick/Line)
- Choose technical indicator (RSI/MACD/Moving Average)
- Pick time period (5D, 1M, 6M, YTD, 1Y, 5Y)

### 4. Price Prediction
- Enter stock ticker
- View model RMSE score
- Analyze 30-day forecast data
- Compare historical vs predicted prices

### 5. Stock Comparison
- View raw price comparison across multiple stocks
- Analyze normalized performance for relative comparison

### 6. CAPM Analysis
- Select up to 4 stocks
- Set number of years for historical data
- View comprehensive data tables

## 📊 Key Functions

### Data Retrieval
```python
def get_data(ticker):
    """Fetches stock data from Yahoo Finance"""
    stock_data = yf.download(ticker, start='2024-01-01')
    return stock_data['Close']
```

### Technical Indicators
```python
def RSI(dataframe, num_period):
    """Calculates and plots RSI indicator"""
    
def MACD(dataframe, num_period):
    """Calculates and plots MACD indicator"""
    
def Moving_average(dataframe, num_period):
    """Calculates and plots SMA"""
```

### Charting
```python
def candlestick(dataframe, num_period):
    """Creates interactive candlestick chart"""
    
def close_chart(dataframe, num_period):
    """Creates line chart with OHLC data"""
```

### Prediction
```python
def fit_model(data, differencing_order):
    """Trains ARIMA model and generates predictions"""
    
def get_forecast(original_price, differencing_order):
    """Creates 30-day forecast dataframe"""
```

## 🔧 Configuration

### Supported Stock Tickers
| Ticker | Company |
|--------|---------|
| TSLA | Tesla |
| GOOGL | Google |
| AMZN | Amazon |
| AAPL | Apple |
| Custom | Any valid ticker |

### Time Periods
| Period | Description |
|--------|-------------|
| 5D | 5 days |
| 1M | 1 month |
| 6M | 6 months |
| YTD | Year to date |
| 1Y | 1 year |
| 5Y | 5 years |

## ☁️ Deployment

This application is deployed on **Streamlit Cloud**. 

**Live URL:** [https://stocksanalyticscapm.streamlit.app/](https://stocksanalyticscapm.streamlit.app/)

### Deploy Your Own

1. Fork this repository
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add `requirements.txt` with all dependencies
5. Click "Deploy"!

## ⚠️ Known Issues & Solutions

### NumPy Compatibility Error
**Issue:** 
```
ImportError: Numba needs NumPy 2.2 or less
```

**Solution:**
```bash
pip install numpy==2.1.3
```

### Missing Data
- Some stocks may have limited historical data
- Prediction accuracy depends on data quality and market volatility

## 🔮 Future Enhancements

- [ ] Add more technical indicators (Bollinger Bands, Stochastic Oscillator)
- [ ] Implement deep learning models (LSTM, GRU)
- [ ] Add portfolio optimization features
- [ ] Include sentiment analysis from news
- [ ] Real-time alert system
- [ ] Export reports as PDF
- [ ] Add cryptocurrency support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Yahoo Finance](https://finance.yahoo.com/) for providing free stock data API
- [Streamlit](https://streamlit.io/) team for the amazing framework
- [pandas_ta](https://github.com/twopirllc/pandas-ta) for technical analysis tools
- [Plotly](https://plotly.com/) for interactive visualizations

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/aniketkumariitp/stock-analysis-dashboard/issues) on GitHub.

---

## 👤 Author

**ANIKET KUMAR**  
*Data Analyst | Cricket Enthusiast | Focused on delivering clean & high-quality data*

- 🌐 **GitHub:** [aniketkumariitp](https://github.com/aniketkumariitp)  
- 💼 **LinkedIn:** [Aniket Kumar](https://www.linkedin.com/in/aniket-kumar-995424324/)  
- 📧 **Email:** aniketkumariitp@gmail.com

---

<div align="center">

### 🌐 [Try Live Demo](https://stocksanalyticscapm.streamlit.app/) 🌐

### ⭐ If you find this project helpful, please give it a star! ⭐

[![GitHub Stars](https://img.shields.io/github/stars/aniketkumariitp/stock-analysis-dashboard?style=social)](https://github.com/aniketkumariitp/stock-analysis-dashboard/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/aniketkumariitp/stock-analysis-dashboard?style=social)](https://github.com/aniketkumariitp/stock-analysis-dashboard/network/members)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stocksanalyticscapm.streamlit.app/)

Made with ❤️ by [Aniket Kumar](https://github.com/aniketkumariitp)

</div>
