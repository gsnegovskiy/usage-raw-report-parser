import pandas as pd
import os


def extract_and_redact_columns(input_csv_path):
    # Define the columns you want to extract
    columns_to_extract = [
        "Instance type",
        "Reservation ID",
        "Number of RIs",
        "On-Demand cost equivalent",
        "Effective reservation cost",
        "Net savings",
    ]

    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv(input_csv_path)

    # Create a new DataFrame with only the selected columns
    selected_columns_data = data[columns_to_extract]

    # Get the input file name without extension
    base_filename = os.path.splitext(os.path.basename(input_csv_path))[0]

    # Create the output CSV file name
    output_csv_path = f"/resulting-report/{base_filename}_redacted.csv"

    # Write the selected columns data to the output CSV file
    selected_columns_data.to_csv(output_csv_path, index=False)

    print(f"Selected columns extracted and saved to {output_csv_path}.")


# Example usage
input_csv_name = (
    "./../raw-data/input.csv"  # Replace with the actual input CSV file name
)
extract_and_redact_columns(input_csv_name)
