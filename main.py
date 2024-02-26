import os
import pandas as pd
import csv


input_folder = 'data_files'
output_folder = 'processed_data'
data = []
header = []
salaries = []
second_highest = 0
average = 0

def get_files(input_folder):
    # List files in the input folder
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    return files

# def read_files(files):
#     for file in files:
#         data = pd.read_csv(input_folder+ "/" + file)
#         import pdb; pdb.set_trace()
    
def read_files(files):
    # Read data from each file
    for file_name in files:
        with open(os.path.join(input_folder, file_name), 'r') as file:
            # Assuming each line in the file contains a single salary value
            for num, line in enumerate(file):
                if num == 0:
                    for col in line.split():
                        header.append(col)
                    # Adding Gross salary as a column
                    header.append("Gross Salary")
                else:
                    data.append(line.split())                    

def get_gross_salaries(data):
    """
    Calculate gross salaries for all the data
    """
    for dl in data:
        salaries.append(int(dl[-2]) + int(dl[-1]))

def get_second_highest_salary(salaries):
    """
    Calculate the second highest salary from all the data
    """
    second_highest = sorted(set(salaries))[-2] if len(set(salaries)) >= 2 else None
    return second_highest

def get_average_salary(salaries):
    """
    Calculate the average salary
    """
    average = sum(salaries) / len(salaries) if len(salaries) > 0 else None
    return average

def write_to_csv(data):
    """
    Write data to result csv
    """
    with open(os.path.join(output_folder, 'result.csv'), 'w', newline='') as csvfile:
        
        writer = csv.writer(csvfile)
        
        # Write header to CSV
        writer.writerow(header)

        # Write data to CSV
        for ind, data_line in enumerate(data):
            data_line.append(salaries[ind])
            writer.writerow(data_line)
        
        # Write salaries in Footer
        writer.writerow([])
        writer.writerow([f"Second highest salary = {get_second_highest_salary(salaries)} ", f"Average salary  = {get_average_salary(salaries)}"])


files = get_files(input_folder)
read_files(files)
get_gross_salaries(data)
write_to_csv(data)

