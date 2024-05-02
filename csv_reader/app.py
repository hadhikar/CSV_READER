from csv_reader.FileBySubcategory import FileBySubcategory


def cli():
    # Create an instance of FileBySubcategory with the specified CSV file location
    file_by_subcategory = FileBySubcategory(file_location="2023_service_desk.csv")

    # Process the CSV file: read it, filter by subcategory, group by caller_id, and write to separate CSV files
    file_by_subcategory.process_csv_file()


# If this script is run directly (not imported), call the cli() function
if __name__ == "__main__":
    cli()
