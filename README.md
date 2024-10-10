# Portfolio Stress Testing Framework

This project is a Python-based framework that simulates and evaluates the impact of various economic stress scenarios on a portfolio of Indian stocks. The aim is to assess how financial shocks—like economic downturns or market crashes—affect portfolio performance, helping investors and risk managers make data-driven decisions.

## Features

- **Stress Scenarios Simulation:** Assesses portfolio performance under stress conditions like economic downturns, market crashes, and interest rate hikes.
- **Portfolio Composition:** The portfolio includes 9 Indian stocks, equally weighted for simplicity, with real historical price data.
- **Data Visualization:** Generates a summary dashboard and heatmaps to visually represent the impact of each stress scenario.
- **Automated Excel Reporting:** Results are saved to Excel for easy reporting and further analysis.

## Portfolio Composition

The portfolio used in this analysis consists of the following 9 Indian stocks:
- **RELIANCE** (Reliance Industries Ltd.)
- **TCS** (Tata Consultancy Services Ltd.)
- **HDFCBANK** (HDFC Bank Ltd.)
- **INFY** (Infosys Ltd.)
- **ICICIBANK** (ICICI Bank Ltd.)
- **KOTAKBANK** (Kotak Mahindra Bank Ltd.)
- **ITC** (ITC Ltd.)
- **BAJFINANCE** (Bajaj Finance Ltd.)
- **LT** (Larsen & Toubro Ltd.)

Each stock is assigned an equal portfolio weight of approximately **11.11%**.

## Scenarios Considered

1. **Economic Downturn:** Simulates a 20% portfolio return decline due to economic slowdown.
   - Stress-adjusted return: **4.96%**
   
2. **Market Crash:** Simulates a 30% portfolio return decline due to a sudden market shock.
   - Stress-adjusted return: **4.34%**
   
3. **Interest Rate Increase:** Simulates a 10% portfolio return decline driven by rising interest rates.
   - Stress-adjusted return: **5.58%**

## Methodology

1. **Data Loading:** Historical price data is loaded from a CSV file, and daily returns are calculated.
2. **Portfolio Weights:** Each of the 9 Indian stocks is equally weighted to simplify the analysis.
3. **Stress Simulation:** Stress factors are applied to the annualized portfolio return, simulating the impact of the defined stress scenarios.
4. **Results Visualization:** A summary dashboard and heatmap are generated to visually interpret how each scenario impacts the portfolio.

## Visualizations

- **Summary Dashboard:** Displays the stress-adjusted returns for each scenario (Economic Downturn, Market Crash, Interest Rate Increase).
- **Heatmap:** A visual representation of the portfolio's performance under stress, providing a clear understanding of the portfolio’s risk exposure.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio-stress-testing.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python stress_testing.py
   ```

4. Generate the dashboard and heatmap:
   ```bash
   python summary_dashboard.py
   ```

## File Structure

- `stress_testing.py` - Simulates portfolio stress tests for different scenarios.
- `summary_dashboard.py` - Generates the summary dashboard and heatmap for visual analysis.
- `historical_prices.csv` - Historical stock price data for the 9 stocks used in the analysis.
- `requirements.txt` - Python libraries required for the project.

## Learnings from the Project

- **Risk Assessment & Scenario Analysis:** I gained practical experience in simulating portfolio performance under stress conditions, enhancing my ability to assess and manage risk through data-driven methods.
  
- **Data Visualization & Insights:** I learned to turn complex financial data into intuitive visualizations such as dashboards and heatmaps, making risk data more accessible to stakeholders for decision-making.

## Contributing

Feel free to submit issues or contribute by submitting pull requests. Contributions are always welcome!
