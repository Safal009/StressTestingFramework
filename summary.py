import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the stress test results
data = {
    'Scenario': ['economic_downturn', 'market_crash', 'interest_rate_increase'],
    'Stress Return': [4.957730366, 4.33801407, 5.577446661]
}

results_df = pd.DataFrame(data)

# 1. Create a Summary Dashboard
# Display the summary statistics
print("Summary Dashboard:")
print(results_df)

# 2. Create a Heatmap
# Reshape the DataFrame to make it suitable for heatmap
heatmap_data = results_df.set_index('Scenario')

# Set up the matplotlib figure
plt.figure(figsize=(8, 4))

# Create the heatmap
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt='.2f', cbar_kws={'label': 'Stress Return (%)'})

# Set labels and title
plt.title('Stress Test Results Heatmap')
plt.xlabel('Stress Return')
plt.ylabel('Scenario')

# Show the heatmap
plt.tight_layout()
plt.show()
