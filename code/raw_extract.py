import pandas as pd
import numpy as np
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

    # Calculate the sum of columns
    sum_row = selected_columns_data.select_dtypes(np.number).sum()
    sum_row["Instance type"] = "Total"
    sum_row["Reservation ID"] = "-"

    # Sort the data by the 'Instance type' column (excluding the Total row)
    sorted_data = selected_columns_data[
        selected_columns_data["Instance type"] != "Total"
    ].sort_values(by="Instance type")

    # Calculate the sum of positive and negative 'Net savings' separately
    positive_net_savings_sum = sorted_data[sorted_data["Net savings"] > 0][
        "Net savings"
    ].sum()
    negative_net_savings_sum = sorted_data[sorted_data["Net savings"] < 0][
        "Net savings"
    ].sum()

    # Append the Total Savings and Total Credits rows
    totals_row = pd.DataFrame(
        {
            "Instance type": ["Total Savings", "Total Credits"],
            "Reservation ID": ["-", "-"],
            "Number of RIs": ["-", "-"],
            "On-Demand cost equivalent": ["-", "-"],
            "Effective reservation cost": ["-", "-"],
            "Net savings": [positive_net_savings_sum, negative_net_savings_sum],
        }
    )

    # Append the Total row to the sorted data
    sorted_data = sorted_data._append(sum_row, ignore_index=True)

    # Append the Total Savings and Total Credits rows
    sorted_data = sorted_data._append(totals_row, ignore_index=True)

    # Get the input file name without extension
    base_filename = os.path.splitext(os.path.basename(input_csv_path))[0]

    # Create the output CSV file name
    output_csv_path = f"/resulting-report/{base_filename}_redacted.csv"

    # Write the selected columns data to the output CSV file
    sorted_data.to_csv(output_csv_path, index=False)

    print(
        f"Selected columns extracted with sums and added Total Savings/Total Credits. Sorted data saved to {output_csv_path}."
    )


# Example usage
input_csv_name = (
    "./../raw-data/input.csv"  # Replace with the actual input CSV file name
)
extract_and_redact_columns(input_csv_name)
