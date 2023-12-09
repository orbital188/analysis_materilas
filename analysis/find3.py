import pandas as pd
import ast

# Load the CSV file into a DataFrame
material1_df = pd.read_csv('./material1.csv')  # Replace with the path to your material1.csv file

# Convert the 'Elements' column from string representation of list to actual list
material1_df['Elements'] = material1_df['Elements'].apply(ast.literal_eval)

# Define the filtering criteria
# Update these lists according to your new criteria
contains_elements = ['Zr','O']  # Add elements A and B
excludes_elements = ['Fe', 'Co', 'Nd', 'Dy','Er','Cr','Mn','Ni','Yb','Sm','Eu','Pr','Ho','Pa','U','Th','Tl']  # Add elements C and D

# Filter the DataFrame
filtered_df = material1_df[material1_df['Elements'].apply(lambda x: all(elem in x for elem in contains_elements) and 
                                                          all(elem not in x for elem in excludes_elements))]

# Save the filtered DataFrame to a new CSV file
output_file = 'filtered_zirconium.csv'  # You can change the file name as needed
filtered_df.to_csv(output_file, index=False)

print(f"Filtered materials have been saved to {output_file}.")

