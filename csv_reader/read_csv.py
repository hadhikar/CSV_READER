import pandas as pd

# Read the csv file
df = pd.read_csv("service_desk.csv", low_memory=False)


# Filter the dataframe where subcategory is "System Error"
filtered_df = df[df["subcategory"] == "System Error"]

# Group by caller_id and aggregate the short_description and count
grouped_df = filtered_df.groupby("caller_id").agg(
    {"short_description": lambda x: " | ".join(x.astype(str)), "caller_id": "count"}
)

# Rename the columns
grouped_df.columns = ["short_description", "count"]

# Reset the index
grouped_df.reset_index(inplace=True)

# Add the subcategory column
grouped_df["subcategory"] = "System Error"
grouped_df = grouped_df[grouped_df["count"] > 1]

# Sort the dataframe by count in descending order
grouped_df.sort_values(by="count", ascending=False, inplace=True)

# Reorder the columns
grouped_df = grouped_df[["caller_id", "count", "subcategory", "short_description"]]

# Write to a new CSV file with sorted count
grouped_df.to_csv("output.csv", index=False)

# Create a new csv file each for each subcategory
