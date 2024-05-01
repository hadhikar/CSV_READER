import pandas as pd


class FileBySubcategory:
    def __init__(self, file_location=None):
        # Initialize the class with the file location
        self._file_location = file_location

    def read_csv_file(self):
        try:
            # Read the csv file into a pandas DataFrame
            df = pd.read_csv(self._file_location, low_memory=False)
            print(f"Total number of rows in the csv file: {df.shape[0]}")
        except Exception as e:
            print(f"Error reading the csv file: {e}")
            return None
        return df

    def filter_subcategory(self, df, subcategory):
        try:
            # Filter the DataFrame to only include rows where the subcategory matches the provided subcategory or is NaN
            filtered_df = df[
                (df["subcategory"] == subcategory) | (pd.isnull(df["subcategory"]))
            ]
        except Exception as e:
            print(f"Error filtering the dataframe: {e}")
            return None
        return filtered_df

    def list_of_subcategories(self, df):
        try:
            # Get a list of unique subcategories from the DataFrame
            subcategories = df["subcategory"].unique()
            print(f"Total number of subcategories: {len(subcategories)}")
        except Exception as e:
            print(f"Error getting the unique subcategories: {e}")
            return None
        return subcategories

    def group_by_caller_id(self, df, subcategory):
        try:
            # Filter the DataFrame by the provided subcategory
            filtered_df = self.filter_subcategory(df, subcategory)

            # Group the filtered DataFrame by caller_id and aggregate the short_description and count
            grouped_df = filtered_df.groupby("caller_id").agg(
                {
                    "short_description": lambda x: " | ".join(x.astype(str)),
                    "caller_id": "count",
                }
            )

            # Rename the columns
            grouped_df.columns = ["short_description", "count"]

            # Reset the index
            grouped_df.reset_index(inplace=True)

            # Filter the DataFrame to only include rows where count is greater than or equal to 1
            grouped_df = grouped_df[grouped_df["count"] >= 1]

            # Sort the DataFrame by count in descending order
            grouped_df.sort_values(by="count", ascending=False, inplace=True)

            # Add the subcategory to the DataFrame and reorder the columns
            if isinstance(subcategory, float) and pd.isnull(subcategory):
                subcategory = "uncategorized"
            grouped_df["subcategory"] = subcategory
            grouped_df = grouped_df[
                ["caller_id", "count", "subcategory", "short_description"]
            ]
            file_name = f'output/{subcategory.replace("/", "_")}.csv'
        except Exception as e:
            print(f"Error grouping by caller_id: {e}")
            return None
        return grouped_df, file_name

    def process_csv_file(self):
        try:
            # Read the csv file into a DataFrame
            df = self.read_csv_file()
            # Get a list of unique subcategories from the DataFrame
            subcategories = self.list_of_subcategories(df)
            for subcategory in subcategories:
                # Group the DataFrame by caller_id for each subcategory and write the result to a csv file
                grouped_df, file_name = self.group_by_caller_id(df, subcategory)
                print(
                    f"Processing subcategory: {subcategory} - {grouped_df.shape[0]} rows"
                )
                grouped_df.to_csv(file_name, index=False)
        except Exception as e:
            print(f"Error processing the csv file: {e}")
            return None
