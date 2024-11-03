# Correlation Matrix Analysis

This project involves creating a correlation matrix between countries based on provided data. Two types of correlation matrices are generated:
1. A correlation matrix targeting all the values provided.
2. A correlation matrix targeting the top 4 voted reasons.

## Steps

### 1. Data Preparation
- Read the CSV file into a DataFrame.
- Remove '%' character from all entries.
- Convert the cleaned entries to numeric values.

### 2. Correlation Matrix for All Values
- Compute the correlation matrix for all values.
- Filter the correlation matrix to keep only values above 0.95.
- Plot the filtered correlation matrix using a heatmap.

### 3. Correlation Matrix for Top 4 Voted Reasons
- Identify the top 4 values per column.
- If there are more than 4 values due to ties, split the value among them.
- Compute the correlation matrix for the top 4 voted reasons.
- Filter the correlation matrix to keep only values above 0.95.
- Plot the filtered correlation matrix using a heatmap.

## Code
Find all code within the two files correlationAllValues.py and correlationTop4Values.py