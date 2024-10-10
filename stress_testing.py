import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

# Load historical price data
data = pd.read_csv('historical_prices.csv', parse_dates=['Date'], index_col='Date')

# Ensure all data in the DataFrame is numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values after conversion
data.dropna(inplace=True)

# Calculate daily returns
returns = data.pct_change(fill_method=None).dropna()  # Explicitly set fill_method to None

# Define portfolio weights based on the number of stocks in the returns DataFrame
num_stocks = returns.shape[1]
portfolio_weights = np.array([1 / num_stocks] * num_stocks)  # Equal weights for simplicity

def simulate_stress_test(returns, weights, scenario):
    if scenario == 'economic_downturn':
        stress_factor = -0.20  # 20% decline
    elif scenario == 'market_crash':
        stress_factor = -0.30  # 30% decline
    elif scenario == 'interest_rate_increase':
        stress_factor = -0.10  # 10% decline
    else:
        stress_factor = 0

    # Simulate portfolio return under stress
    portfolio_return = np.sum(returns.mean() * weights) * 252  # Annualized return
    stress_return = portfolio_return * (1 + stress_factor)

    return stress_return

# Define stress scenarios
scenarios = ['economic_downturn', 'market_crash', 'interest_rate_increase']
results = {}

# Run stress tests for each scenario
for scenario in scenarios:
    stress_return = simulate_stress_test(returns, portfolio_weights, scenario)
    results[scenario] = stress_return

# Save results to Excel
results_df = pd.DataFrame.from_dict(results, orient='index', columns=['Stress Return'])
results_df.to_excel('stress_test_results.xlsx')

print("Stress test results saved to stress_test_results.xlsx")

# Visualization of Stress Test Results
plt.figure(figsize=(8, 5))
plt.bar(results_df.index, results_df['Stress Return'], color=['blue', 'red', 'orange'])
plt.title('Stress Testing Results')
plt.xlabel('Stress Scenarios')
plt.ylabel('Stress Return (%)')
plt.axhline(0, color='black', linewidth=0.8)  # Line at y=0
plt.grid(axis='y')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('stress_testing_results.png')  # Save the figure
plt.show()
