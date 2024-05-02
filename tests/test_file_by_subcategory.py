import pandas as pd
import pytest
from csv_reader.FileBySubcategory import FileBySubcategory


@pytest.fixture(scope="module")
def file_by_subcategory():
    """Fixture to initialize FileBySubcategory and read the CSV file."""
    file_by_subcategory = FileBySubcategory(file_location="2023_service_desk.csv")
    df = file_by_subcategory.read_csv_file()
    return df, file_by_subcategory


def test_read_csv_file(file_by_subcategory):
    """Test that read_csv_file method returns a DataFrame."""
    df, _ = file_by_subcategory
    assert isinstance(df, pd.DataFrame)
    assert not df.empty


def test_filter_subcategory(file_by_subcategory):
    """Test that filter_subcategory method returns a filtered DataFrame."""
    df, file_by_subcategory = file_by_subcategory
    filtered_df = file_by_subcategory.filter_subcategory(df, "Hardware")
    assert not filtered_df.empty
    assert all(
        filtered_df["subcategory"] == "Hardware"
        or pd.isnull(filtered_df["subcategory"])
    )
