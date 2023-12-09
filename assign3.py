import pandas as pd

# Load the CSV file
file_path = './output1.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Replace 'polar' with 2 in the 'order' column
df['order'] = df['order'].replace('polar', 2)

# Iterate through the DataFrame and make the necessary updates
for index, row in df.iterrows():
    if row['CS'] == 'CS':
        # Insert 0 after 'CS'
        df.at[index, 'order'] = 0
    elif row['CS'] == 'NCS' and pd.isna(row['order']):
        # Insert 1 after 'NCS' if there's no value in the 'order' column
        df.at[index, 'order'] = 1

# Save the updated DataFrame to a new CSV file
output_file_path = 'output2.csv'  # You can change the output file name
df.to_csv(output_file_path, index=False)

print("CSV file has been updated and saved.")

