import pandas as pd

# Define the columns you want to extract
columns_to_extract = [
    "column_name1",
    "column_name2",
    "column_name3",
]  # Replace with actual column names

# Load the CSV file into a pandas DataFrame
input_csv_path = "input.csv"  # Replace with the path to your input CSV file
data = pd.read_csv(input_csv_path)

# Create a new DataFrame with only the selected columns
selected_columns_data = data[columns_to_extract]

# Define the output CSV file path
output_csv_path = "output.csv"  # Replace with the desired output CSV file path

# Write the selected columns data to the output CSV file
selected_columns_data.to_csv(output_csv_path, index=False)

print("Selected columns extracted and saved to the new CSV file.")
