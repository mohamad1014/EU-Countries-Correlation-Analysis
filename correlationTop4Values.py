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

# Take the the top 4 values per column, convert them to 1 and the rest to 0
# Function to assign top 4 values as 1, and split if there are ties
def assign_top_4(x):
    sorted_x = x.sort_values(ascending=False)
    top_3_values = sorted_x.head(3).values
    threshold_value = sorted_x.iloc[3]  # The 4th highest value
    count_at_threshold = (sorted_x == threshold_value).sum()
    
    result = []
    for value in x:
        if value in top_3_values:
            result.append(1)
        elif value == threshold_value:
            result.append(1 / count_at_threshold)
        else:
            result.append(0)
    return result

# Apply the function to each column
data_df = data_df.apply(assign_top_4)

# data_df = data_df.apply(lambda x: [1 if i in x.sort_values(ascending=False).head(4).values else 0 for i in x])

# Step 4: Compute the correlation matrix
correlation_matrix = data_df.corr()

# Step 5: Plot the correlation matrix using a heatmap
plt.figure(figsize=(20, 16))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix [Top 4+Ties]')

# Step 6: Save the plot as an image
plt.savefig('correlation_matrix2.png')

# Step 7: Show the plot
plt.show()
