import pandas as pd

def extract_io3_compounds(input_file, output_file):
    try:
        # Load the CSV file
        data = pd.read_csv(input_file)

        # Filter rows where the Reduced Formula contains 'IO3'
        filtered_data = data[data['Reduced Formula'].str.contains('SeO3', na=False)]

        # Write the filtered data to a new CSV file
        filtered_data.to_csv(output_file, index=False)
        print(f"File '{output_file}' has been created with the filtered data.")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
input_file_path = './filtered_selenides.csv'  # Adjust this to the correct file path
output_file_path = './selenides_only.csv'
extract_io3_compounds(input_file_path, output_file_path)

