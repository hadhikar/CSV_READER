# CSV READER

## FileBySubcategory
FileBySubcategory is a Python project that provides functionality to read a CSV file, filter it by a specific subcategory, and perform various operations on the data. It is designed to be easy to use and efficient, using pandas for data manipulation.

## Features
- **CSV File Reading**: The class can read a CSV file into a pandas DataFrame.
- **Data Filtering**: The class can filter the DataFrame to only include rows where the subcategory matches the provided subcategory or is NaN.
- **Subcategory Listing**: The class can get a list of unique subcategories from the DataFrame.
- **Grouping by Caller ID**: The class can group the DataFrame by caller_id for each subcategory and write the result to a CSV file.
- **CSV File Processing**: The class can process the CSV file, performing all of the above operations.

## Installation

### Prerequisites

Ensure that you have Python 3.x installed on your machine. You can verify this by running the following command in your terminal:

```bash
    python --version
```

If you don't have Python installed, please visit the official Python website to download and install it.

## Steps
Follow these steps to download and install the project from GitHub:

1. Clone the repository to your local machine:
```
    git clone https://github.com/<yourusername>/CSV_READER.git
```
Replace <yourusername> with your actual GitHub username.

2. Initialize the project:

If you're using VSCode, it will automatically run the initialize.sh file. If this script fails to run, or if you're using a different IDE, you can manually run it with the following command:
```
    bash initialize.sh
```

Alternatively, you can install the required libraries manually with:
```
    pip3 install -r requirements.txt
```

3. Run the project:

You can start the project with the following command:
```
    make run
```

4. Run tests:

You can run the tests with:
```
    make test
```
To view the test coverage, use:
```
    make show_coverage
```

## Usage
First, initialize the class with the location of your CSV file:
```
    file = FileBySubcategory('your_file_location.csv')
```

Then, you can process the CSV file:
```
    file.process_csv_file()
```

This will read the CSV file into a DataFrame, get a list of unique subcategories, group the DataFrame by caller_id for each subcategory, and write the result to a CSV file.
