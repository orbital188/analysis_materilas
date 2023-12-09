import csv

# Function to process the text and write to a CSV file
def process_text_to_csv(input_file, output_file):
    # Read the input file
    with open(input_file, 'r') as file:
        text_data = file.read()

    # Split the text into words
    words = text_data.split()

    # Pair the words (number, code)
    pairs = [(words[i], words[i+1]) for i in range(0, len(words), 2)]

    # Write pairs to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number', 'Code'])  # Writing header
        for pair in pairs:
            writer.writerow(pair)

    print("CSV file created successfully.")

# Specify your input and output file names
input_file = 'input.txt'
output_file = 'output.csv'

# Process the file
process_text_to_csv(input_file, output_file)

