# Portfolio Risk Analyzer

We developed a comprehensive **Portfolio Risk Analyzer** using **Streamlit** (frontend) and **Python** with financial libraries (backend).

• On the **backend**, we created modules for **data loading**, **risk calculations**, and **visualizations** with fields like stock symbols, weights, and returns, and built a modular architecture using **Yahoo Finance API** for real-time data fetching with **risk metrics calculations** and **PDF report generation**.

• We also integrated sample portfolio data into a **CSV format** and exposed various analysis features:
  - **Data Loading** from Yahoo Finance API
  - **Risk Metrics** calculation (VaR, Sharpe Ratio, Volatility)
  - **Visualization** generation (correlation matrix, efficient frontier)
  - **Report Export** to PDF and Excel formats

• On the **frontend**, we built a **Streamlit UI** that allows **uploading portfolios**, **analyzing risk metrics**, **visualizing data**, **generating reports**, **comparing portfolios**, and **backtesting**, styled with a **modern interface**, **interactive charts**, **real-time updates**, and **export functionality**.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![yfinance](https://img.shields.io/badge/Yahoo_Finance-6001D2?style=for-the-badge&logo=yahoo&logoColor=white)
![FPDF](https://img.shields.io/badge/FPDF-DC382D?style=for-the-badge&logo=adobe-acrobat-reader&logoColor=white)

![OpenPyXL](https://img.shields.io/badge/OpenPyXL-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white)

---

## 📁 Project Structure

```
portfolio-risk-analyzer/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
│
├── data/                       # Portfolio data storage
│    └── sample_portfolio.csv   # Sample portfolio data
│
├── modules/                    # Core analysis modules
│    ├── data_loader.py        # Stock data fetching (Yahoo Finance)
│    ├── risk_metrics.py       # Risk calculations (VaR, Sharpe, etc.)
│    └── visualizations.py     # Interactive charts and plots
│
└── reports/                    # Generated reports
     └── portfolio_report.pdf   # Exported analysis reports
```

---

## ✨ Features

• **Portfolio Analysis** with comprehensive risk metrics calculation

• **Real-time Data** fetching from Yahoo Finance API

• **Interactive Visualizations** with correlation matrices and efficient frontier

• **Risk Metrics** including VaR, Sharpe Ratio, Beta, and volatility analysis

• **Portfolio Optimization** using Modern Portfolio Theory

• **Backtesting** capabilities for historical performance analysis

• **Export Functionality** to PDF and Excel formats

• **Responsive Streamlit** interface with modern UI components

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
pip package manager
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/portfolio-risk-analyzer.git
   cd portfolio-risk-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   ```
   Open your browser and navigate to: http://localhost:8501
   ```

---

## 📊 Usage

1. **Upload Portfolio**: Import your portfolio via CSV or enter stock symbols manually
2. **Set Parameters**: Configure analysis period, risk-free rate, and confidence levels
3. **Analyze Risk**: View comprehensive risk metrics and visualizations
4. **Optimize Portfolio**: Find optimal asset allocation using efficient frontier
5. **Export Reports**: Generate PDF reports with all analysis results

---

## 🔧 API Endpoints

The application uses the following data sources:

- **Yahoo Finance API** - Real-time stock prices and historical data
- **Risk-free Rate** - Treasury bill rates for Sharpe ratio calculations
- **Market Index** - Benchmark data for beta calculations

---

## 📸 Application Screenshots

### Portfolio Analysis Dashboard
![Portfolio Dashboard](https://github.com/fyisubz/portfolio-risk-analyzer/blob/main/images/portfolio_dashboard.png)
*Main dashboard showing key portfolio metrics, cumulative returns chart, and portfolio input controls*

### Risk Analysis & Export Features
![Risk Analysis](https://github.com/fyisubz/portfolio-risk-analyzer/blob/main/images/export_buttons.png)
*Drawdown analysis visualization and export functionality for PDF/Excel reports*

### Portfolio Drawdown Analysis
![Portfolio Drawdown](https://github.com/fyisubz/portfolio-risk-analyzer/blob/main/images/drawdown_analysis.png)
*Detailed drawdown chart showing portfolio losses from peak values over time*

---

## 📈 Sample Analysis

The application provides analysis for various asset classes:
- **Stocks** (Individual equities)
- **ETFs** (Exchange-traded funds)
- **Indices** (Market benchmarks)
- **Cryptocurrencies** (Digital assets)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

Mail - [9subhodeep@gmail.com](mailto:9subhodeep@gmail.com)

Project Link: [https://github.com/fyisubz/portfolio-risk-analyzer](https://github.com/fyisubz/portfolio-risk-analyzer)
