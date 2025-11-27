# 📈 Financial Insights Dashboard: S&P 500 Analysis & Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://[YOUR_APP_LINK_HERE])

Welcome to the **Financial Insights Dashboard**, a powerful, multi-page Streamlit application designed for in-depth stock market analysis, focusing specifically on S&P 500 components. This project integrates statistical models, historical analysis, and machine learning prediction capabilities into one interactive tool.

![App Preview](pages/app.webp)
*Replace the above link with a compelling screenshot of your running dashboard.*

---

## 🧭 Table of Contents
1.  [✨ Key Features](#-key-features)
2.  [📂 Project Structure](#-project-structure)
3.  [🚀 Getting Started](#-getting-started)
4.  [⚙️ Dependencies](#-dependencies)
5.  [🤝 Contribution](#-contribution)
6.  [📄 License](#-license)

---

## ✨ Key Features

The application is structured around four distinct, high-value pages, easily accessible via the Streamlit sidebar:

### 1. 📉 CAPM & Return Analysis (`CAPM_Return.py`)
This serves as the core financial model calculator and application home page.
* **CAPM Calculation:** Determine the required rate of return for a stock using the Capital Asset Pricing Model.
* **Risk Metrics:** Calculate Beta ($\beta$) and Alpha ($\alpha$) relative to a market benchmark.
* **Core Logic:** Functions sourced from the `CAPM_functions.py` file.

### 2. 💹 Trading App Page (`1_Trading_app.py`)
A dedicated dashboard for analyzing short-term dynamics and potential trading signals.

### 3. 📊 Stock Analysis Page (`Stock_analysis.py`)
The main tool for deep dives into individual stock performance.
* **Historical Data:** Visualize price movements over customizable time ranges.
* **Technical Indicators:** Calculate and plot essential indicators (e.g., Moving Averages, RSI, MACD).
* **Interactive Charts:** Dynamic visualizations powered by **Plotly** for zooming and interaction.

### 4. 🧠 Stock Prediction Page (`Stock_Prediction.py`)
Utilize machine learning models to forecast future closing prices.
* **Model Training:** Interface to train or load predictive models (logic contained in `utils/Model_train.py`).
* **Forecasting Visualization:** See projected price paths based on the model's output.

---

## 📂 Project Structure

The project uses the standard Streamlit multi-page layout. The main entry point is at the root, and helper scripts are organized under the `utils/` directory.

```text
S&P500_PROJECT/
├── CAPM_Return.py           # 🏠 Main Streamlit Entry Point (CAPM & Returns)
├── CAPM_functions.py        # 🧮 Core mathematical functions for CAPM/Beta/Alpha
├── SOURCES.txt              # 📚 Documentation of data sources and references
├── pages/                   # 📑 Streamlit Sidebar Pages
│   ├── 1_Trading_app.py     # Trading Simulation/Signals Dashboard
│   ├── Stock_analysis.py    # General Stock Analysis and Indicators
│   ├── Stock_Prediction.py  # Machine Learning Prediction Interface
│   └── utils/               # 🛠️ Helper scripts
│       ├── Model_train.py   # Code for training and persistence of ML models
│       └── plotly_figure.py # Centralized Plotly figure generation logic
├── requirements.txt         # 📦 Python dependencies list
└── README.md                # 📖 This file!
