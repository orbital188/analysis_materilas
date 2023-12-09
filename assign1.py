import csv

# Function to check if the space group is non-centrosymmetric
def is_non_centrosymmetric(code):
    return '/' in code or '-' in code

# Reading the data from the uploaded CSV file
input_file_path = './output.csv'  # replace with your input file path
output_file_path = './output1.csv'  # replace with your desired output file path

# Process the CSV and assign CS
with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Reading the header and writing a new header with 'CS' column
    header = next(reader)
    header.append('CS')
    writer.writerow(header)

    # Process each row
    for row in reader:
        code = row[1]
        cs = 'CS' if is_non_centrosymmetric(code) else ''
        row.append(cs)
        writer.writerow(row)

print("Processing complete. New file with CS column created.")

