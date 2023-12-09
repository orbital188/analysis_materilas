import pandas as pd

# Load the CSV files into DataFrames
sum_df = pd.read_csv('./sum.csv')  # Replace with the path to your sum.csv file
spacegroup_df = pd.read_csv('./spacegroup.csv')  # Replace with the path to your spacegroup.csv file

# Identify space group numbers corresponding to order 1 and 2 in spacegroup.csv
order_1_and_2_space_groups = spacegroup_df[spacegroup_df['order'].isin([1, 2])]['Number'].tolist()

# Find all materials in sum.csv that have these space group numbers
matching_materials = sum_df[sum_df['Space Group Number'].isin(order_1_and_2_space_groups)]

# Save the complete data lines of the matching materials to a new CSV file
matching_materials.to_csv('matching_materials_full_data.csv', index=False)

print("Full data lines of materials matching the criteria have been extracted and saved.")

