# Overview
This Python script is designed to process data files containing salary information located in a specific folder. The script reads data from multiple files, calculates gross salaries, finds the second highest salary, calculates the average salary, and writes the processed data along with footer information to a CSV file in another folder.

In this script 

# Directories and Variable Names
 - data_files: This directory contains input data files. Replace the files in this directory with your actual data files.
 - processed_data: This directory will contain the output CSV file with processed data. (result.csv)
 - data: This is a python list that stores the raw data read from input files.
 - header: This list stores the header information extracted from the first line of each input file.
 - salaries: This list stores the calculated gross salaries.
 - second_highest: This variable stores the second highest gross salary calculated from the data.
 - average: This variable stores the average gross salary calculated from the data.

# Functions
1. **`get_files(input_folder)`**
    - **Input**: `input_folder` - Path to the directory containing input data files.
    - **Output**: List of file names in the input folder.
    - **Detail**: Retrieves the list of files located in the input folder.

2. **`read_files(files)`**
    - **Input**: `files` - List of file names to be processed.
    - **Output**: None
    - **Detail**: Reads data from each file and extracts header information and raw data.

3. **`get_gross_salaries(data)`**
    - **Input**: `data` - List containing raw data read from input files.
    - **Output**: None
    - **Detail**: Calculates gross salaries for all entries in the data.

4. **`get_second_highest_salary(salaries)`**
    - **Input**: `salaries` - List containing gross salaries.
    - **Output**: Second highest salary.
    - **Detail**: Calculates and returns the second highest salary from the list of salaries.

5. **`get_average_salary(salaries)`**
    - **Input**: `salaries` - List containing gross salaries.
    - **Output**: Average salary.
    - **Detail**: Calculates and returns the average salary from the list of salaries.

6. **`write_to_csv(data)`**
    - **Input**: `data` - List containing raw data read from input files.
    - **Output**: None
    - **Detail**: Writes processed data along with footer information to a CSV file in the output folder.


# Execution
1. Replace the files in the data_files directory with your actual data files.
2. Execute the script. 
```
python main.py
```
3. The processed data will be written to the processed_data directory as result.csv. This CSV file will contain the processed data.

# Further Optimisations
1. **Class based**: Can be moved to a class based approach.
2. **Error Handling**: Implement error handling mechanisms to handle potential errors such as file not found errors, invalid data format, or insufficient data.
3. **Use Pandas Features**: Pandas library can be used to perform data manipulations more efficiently.
4. **Testing and Validation**: Developing test cases.






