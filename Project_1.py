import pandas as pd
import os
from datetime import datetime

# Read the Excel file without header
df = pd.read_excel('project1BSSCollctionSI.xlsx', header=None)

# Date format modification
date_column_name = 2  # Assuming column 'C' is the third column (0-based index)
df[date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce').dt.strftime('%d/%m')

# Get unique values in the 'Language' column
column_name = 3  # Assuming column 'D' is the fourth column (0-based index)
unique_values = df[column_name].unique()

# Create output directory
output_directory = 'Project_1'
os.makedirs(output_directory, exist_ok=True)  # Create output directory if it doesn't exist

# Get the current date in the desired format
current_date = datetime.now().strftime('%Y-%m-%d')

for unique_value in unique_values:
    df_output = df[df[column_name] == unique_value]  # Filter by unique value
    
    # Define the output file path with the current date
    output_path = os.path.join(output_directory, f'BFIL_Pro1_{unique_value}_{current_date}.xlsx')
    
    # Save the filtered DataFrame to an Excel file
    df_output.to_excel(output_path, sheet_name=str(unique_value), index=False, header=False)
