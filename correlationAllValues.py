import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a DataFrame
data_df = pd.read_csv('temp3.csv')

data_df.set_index('Reason', inplace=True)

# Step 2: Remove '%' character from all entries
data_df = data_df.replace('%', '', regex=True)

# Step 3: Convert the cleaned entries to numeric values
data_df = data_df.apply(pd.to_numeric)

# Step 4: Compute the correlation matrix
correlation_matrix = data_df.corr()

# Step 5: Plot the correlation matrix using a heatmap
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix [All Values]')
plt.savefig('images/correlation_matrix.png')

plt.show()

# Step 6: Save the plot as an image
