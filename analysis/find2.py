import pandas as pd
import ast

# Load the CSV file into a DataFrame
material1_df = pd.read_csv('./material1.csv')  # Replace with the path to your material1.csv file

# Convert the 'Elements' column from string representation of list to actual list
material1_df['Elements'] = material1_df['Elements'].apply(ast.literal_eval)

# Define the filtering criteria
contains_elements = ['O','F','Cl','Br']  # Add or remove elements as needed
excludes_elements = ['Fe', 'Co', 'Nd', 'Dy','Er','Cr','Mn','Ni','Yb']  # Add or remove elements as needed

# Filter the DataFrame
filtered_df = material1_df[material1_df['Elements'].apply(lambda x: any(elem in x for elem in contains_elements) and 
                                                          all(elem not in x for elem in excludes_elements))]

# Save the filtered DataFrame to a new CSV file
output_file = 'material2.csv'  # You can change the file name as needed
filtered_df.to_csv(output_file, index=False)

print(f"Filtered materials have been saved to {output_file}.")

