def count_compounds(file_path):
    try:
        with open(file_path, 'r') as file:
            # Subtract 1 for the header row
            return sum(1 for line in file) - 1
    except FileNotFoundError:
        return "File not found."

# Prompt the user for the file name
file_name = input("Enter the file name: ")

# Assuming the file is in the current directory
file_path = f'./{file_name}'
number_of_compounds = count_compounds(file_path)
print(f"Number of compounds in the file: {number_of_compounds}")

