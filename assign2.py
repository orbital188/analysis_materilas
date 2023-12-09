import csv

# Specify the space group numbers for which you want to assign 'CS'
cs_numbers = ['1', '2', '3']  # You can modify this list as needed

# Reading the data from the uploaded CSV file
input_file_path = './output1.csv'  # replace with your input file path
output_file_path = './output2.csv'  # replace with your desired output file path

# Function to check if the space group number is in the specified list
def assign_cs(number):
    return 'CS' if number in cs_numbers else ''

# Process the CSV and assign CS based on the specified numbers
with open(input_file_path, mode='r') as infile, open(output_file_path, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Reading the header and writing a new header with 'CS' column
    header = next(reader)
    header.append('CS')
    writer.writerow(header)

    # Process each row
    for row in reader:
        number = row[0]
        cs = assign_cs(number)
        row.append(cs)
        writer.writerow(row)

print("Processing complete. New file with CS column created.")

