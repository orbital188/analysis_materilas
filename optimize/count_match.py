def count_compounds(file_path):
    try:
        with open(file_path, 'r') as file:
            # Subtract 1 for the header row
            return sum(1 for line in file) - 1
    except FileNotFoundError:
        return "File not found."

# Replace 'path_to_file' with the actual path of your file.
file_path = './matching_materials_full_data.csv'
number_of_compounds = count_compounds(file_path)
print(f"Number of compounds in the file: {number_of_compounds}")

