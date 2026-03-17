# This is the file_cleaner.py file that takes in a raw CSV file and returns a clean, reliable dataset
# ready for analysis.
import pandas as pd

# Load the CSV file into a pandas dataframe
# Ensure that the filename is correct
def load_csv_file(filename):
    result = {
        "Status": "Success",
    }
    try:
        df = pd.read_csv(filename)
        result["df"] = df

        if df.empty:
            result["Status"] = "Failure"
            result["Error"] = "No data found"

    except FileNotFoundError:
        result["Status"] = "Failure"
        result["Error"] = f"No such file: '{filename}' found."
    except ValueError:
        result["Status"] = "Failure"
        result["Error"] = f"Invalid file path: '{filename}'."

    return result

# Normalize Column names
def normalize_column_names(df):
    result = {
        "Status": "Success",
    }
    df.columns = df.columns.str.strip().str.lower()

    if not set(df.columns) == {"name", "score"}:
        result["Status"] = "Failure"
        result["Error"] = "Invalid column names."
    result["df"] = df
    return result

# Remove Rows with any empty record
def remove_empty_rows(df):
    result = {}
    total_rows_count = df.shape[0]

    # Remove any row that has nan values
    df = df.dropna(axis=0, how="any")

    # Remove whitespaces around the names
    df.loc[:, "name"] = df["name"].str.strip()

    # Remove empty names
    df = df[df["name"] != ""]
    resulting_row_count = df.shape[0]

    result["no_of_dropped_rows"] = total_rows_count - resulting_row_count
    result["df"] = df
    return result

# Ensure numeric scores only
# Convert all values to numeric and change to nan other dtypes.
def ensure_numeric_scores(df):
    result = {}
    total_rows_count = df.shape[0]

    # Check the scores column and remove any row that does not have a numeric value
    df["score"] = pd.to_numeric(df["score"], errors="coerce")

    df = df.dropna(subset=["score"])

    resulting_row_count = df.shape[0]

    result["no_of_dropped_rows"] = total_rows_count - resulting_row_count
    result["df"] = df

    return result

def clean_file(filename):
    no_of_dropped_rows = 0
    result = {
        "Status": "Success",
    }
    # Verify that the loaded file path is valid
    load_file = load_csv_file(filename)
    if load_file["Status"] == "Failure":
        result["Status"] = "Failure"
        result["Error"] = load_file["Error"]
    else:
        df = load_file["df"]
        total_rows_count = df.shape[0]
        result["rows_original"] = total_rows_count
        normalize_col = normalize_column_names(df)
        df = normalize_col["df"]
        if normalize_col["Status"] == "Failure":
            result["Error"] = normalize_col["Error"]
        else:
            # Remove every nan values and trim the whitespaces
            remove_na = remove_empty_rows(df)
            no_of_dropped_rows += int(remove_na["no_of_dropped_rows"])
            df = remove_na["df"]

            # Record the number of rows dropped so far
            result["rows_removed_missing"] = no_of_dropped_rows

            if df.empty:
                result["rows_after_cleaning"] = total_rows_count - no_of_dropped_rows
                result["df"] = pd.DataFrame()
                return result

            # Ensure all the scores value is numeric
            score_col = ensure_numeric_scores(df)
            rows_removed_invalid_scores = int(score_col["no_of_dropped_rows"])
            no_of_dropped_rows += rows_removed_invalid_scores
            df = score_col["df"]

            # Record the number of rows dropped so far
            result["rows_removed_invalid_scores"] = rows_removed_invalid_scores
            result["rows_after_cleaning"] = total_rows_count - no_of_dropped_rows

            if df.empty:
                result["df"] = pd.DataFrame()
                return result

            result["df"] = df

    return result