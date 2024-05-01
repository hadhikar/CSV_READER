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
This project requires Python and pandas. You can install pandas with pip:

```bash
    pip install pandas
```

To download and install the project from GitHub, follow these steps:

1. Clone the repository to your local machine:
```
    git clone https://github.com/<yourusername>/CSV_READER.git
```

2. Navigate to the project directory:
```
    cd FileBySubcategory
```

3. Install the project:
```
    pip install .
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

## Testing
The test file for FileBySubcategory contains unit tests for each method in the class. It uses the pytest module to create and run the tests. Here is an excerpt from the test file:
```
    def test_read_csv_file(file_by_subcategory):
        """Test that read_csv_file method returns a DataFrame."""
        df, _ = file_by_subcategory
        assert isinstance(df, pd.DataFrame)
        assert not df.empty

    def test_filter_subcategory(file_by_subcategory):
        """Test that filter_subcategory method returns a filtered DataFrame."""
        df, file_by_subcategory = file_by_subcategory
        filtered_df = file_by_subcategory.filter_subcategory(df, 'Hardware')
        assert not filtered_df.empty
        assert all(filtered_df['subcategory'] == 'Hardware' or pd.isnull(filtered_df['subcategory']))
```
You can run the test file with the following command:
```
    
    pytest TestFileBySubcategory.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
